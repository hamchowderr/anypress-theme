<?php
/**
 * Builds a shop kit's demo website (Aisle): a whole online shop on FluentCart.
 *
 * A kit's demo/<kit>/build.php sets $anypress_kit and requires this file. Its folder holds photos/ with photos.json
 * (which photo replaces which placeholder), posts.json for the journal and shop.json for the catalogue: which of
 * FluentCart's own sample products to make, their prices and categories, the shop's own products (a gift card, a
 * subscription), coupons, reviews, shipping and tax.
 *
 * Everything a shopper buys with is FluentCart's: its own pages (shop, cart, checkout, receipt, account), its product
 * and category templates and its blocks. The demo adds the kit's pages around them, the forms, menus and the
 * journal. Run it inside WordPress with the AnyPress theme active and AnyPress Blocks, Fluent Forms and FluentCart on,
 * on an empty site only.
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;
require_once dirname( __FILE__ ) . '/lib.php';

use FluentCart\App\Models\ProductVariation;

anypress_demo_start( $anypress_kit );
$anypress_shop = json_decode( file_get_contents( $anypress_demo . '/shop.json' ), true );

/** A FluentCart REST call made inside WordPress, as its own admin screens make it. */
function anypress_demo_fc( $method, $route, $params = array() ) {
	$request = new WP_REST_Request( $method, '/fluent-cart/v2' . $route );
	if ( 'GET' === $method ) {
		$request->set_query_params( $params );
	} else {
		$request->set_header( 'content-type', 'application/json' );
		$request->set_body( (string) wp_json_encode( $params ) );
	}
	$response = rest_do_request( $request );
	if ( $response->get_status() >= 400 ) {
		throw new RuntimeException( "FluentCart $method $route: " . wp_json_encode( $response->get_data() ) );
	}
	return $response->get_data();
}

// ---------------------------------------------------------------------------------------------------------- the store
( new \FluentCart\Api\StoreSettings() )->set( 'store_name', $anypress_kit['name'] );
// FluentCart's own pages, as its onboarding makes them: shop, cart, checkout, receipt, order review and account. The
// Customer Rights add-on's page (withdrawal) is the kit's own Cancel an order page instead, made with the others below.
( new \FluentCart\App\CPT\Pages() )->createPages( array( 'withdrawal' ) );
flush_rewrite_rules();

/** Makes one of the demo's photos a product's picture and its gallery. */
function anypress_demo_product_photo( $pid, $file ) {
	global $anypress_media;
	$photo = $anypress_media[ $file ]['id'];
	set_post_thumbnail( $pid, $photo );
	update_post_meta( $pid, 'fluent-products-gallery-image', array( array( 'id' => $photo, 'url' => wp_get_attachment_url( $photo ), 'title' => get_post_field( 'post_title', $pid ) ) ) );
	// Each colour or size shows the same photo in its picker.
	foreach ( ProductVariation::where( 'post_id', $pid )->get() as $variation ) {
		\FluentCart\App\Services\Async\ImageAttachService::attachImageToVariant( $variation->id, array( wp_get_attachment_url( $photo ) ) );
	}
}

/** Every FluentCart product's id, oldest first. */
function anypress_demo_products() {
	return array_map( 'intval', \FluentCart\App\Models\Product::query()->orderBy( 'ID', 'ASC' )->pluck( 'ID' )->toArray() );
}

// FluentCart's sample products, at real prices, in the shop's categories, with a few on sale.
// Their photos belong to other shops, so they are not fetched; each product gets one of the demo's free photos.
$anypress_no_fetch = fn() => new WP_Error( 'anypress_demo', 'The demo uses its own photos.' );
add_filter( 'pre_http_request', $anypress_no_fetch );
$anypress_made = array();
foreach ( $anypress_shop['samples'] as $anypress_set ) {
	$anypress_before = anypress_demo_products();
	for ( $anypress_i = 0; $anypress_i < $anypress_set[1]; $anypress_i++ ) {
		$anypress_res = \FluentCart\App\Services\Async\DummyProductService::create( $anypress_set[0], $anypress_i );
		if ( is_wp_error( $anypress_res ) ) {
			throw new RuntimeException( "FluentCart's {$anypress_set[0]} sample $anypress_i: " . $anypress_res->get_error_message() );
		}
	}
	$anypress_made = array_merge( $anypress_made, array_values( array_diff( anypress_demo_products(), $anypress_before ) ) );
}
remove_filter( 'pre_http_request', $anypress_no_fetch );
$anypress_by_slug = array();
foreach ( array_values( $anypress_made ) as $anypress_n => $anypress_pid ) {
	$anypress_title = strtolower( get_post_field( 'post_title', $anypress_pid ) );
	if ( in_array( $anypress_title, array_map( 'strtolower', $anypress_shop['skip'] ?? array() ), true ) ) {
		wp_delete_post( $anypress_pid, true );
		continue;
	}
	$anypress_price = $anypress_shop['default_price'];
	foreach ( $anypress_shop['prices'] as $anypress_word => $anypress_cents ) {
		if ( str_contains( $anypress_title, $anypress_word ) ) {
			$anypress_price = $anypress_cents;
		}
	}
	$anypress_sale    = in_array( get_post_field( 'post_title', $anypress_pid ), $anypress_shop['sale'], true );
	$anypress_updates = array();
	foreach ( ProductVariation::where( 'post_id', $anypress_pid )->get() as $anypress_v => $anypress_variation ) {
		$anypress_full      = $anypress_price + ( $anypress_v % 2 ) * 200;
		$anypress_updates[] = array(
			'id'            => $anypress_variation->id,
			'item_price'    => $anypress_sale ? (int) round( $anypress_full * 0.7 / 100 ) * 100 : $anypress_full,
			'compare_price' => $anypress_sale ? $anypress_full : null,
		);
	}
	anypress_demo_fc( 'POST', '/products/variants/bulk-update', array( 'updates' => $anypress_updates ) );
	$anypress_terms = array();
	foreach ( $anypress_shop['categories'] as $anypress_cat => $anypress_words ) {
		foreach ( $anypress_words as $anypress_word ) {
			if ( str_contains( $anypress_title, $anypress_word ) ) {
				$anypress_terms[] = $anypress_cat;
				break 2;
			}
		}
	}
	if ( $anypress_sale ) {
		$anypress_terms[] = $anypress_shop['sale_category'];
	}
	wp_set_object_terms( $anypress_pid, $anypress_terms, 'product-categories', false );
	// Dates a few days apart, so "newest first" is a real order.
	wp_update_post( array( 'ID' => $anypress_pid, 'post_date' => gmdate( 'Y-m-d H:i:s', time() - DAY_IN_SECONDS * ( 3 + 2 * ( count( $anypress_made ) - $anypress_n ) ) ) ) );
	// FluentCart's samples end their address with the time they were made; give each a plain one.
	$anypress_slug = sanitize_title( str_replace( "'", '', get_post_field( 'post_title', $anypress_pid ) ) );
	wp_update_post( array( 'ID' => $anypress_pid, 'post_name' => $anypress_slug ) );
	$anypress_by_slug[ get_post_field( 'post_name', $anypress_pid ) ] = $anypress_pid;
	anypress_demo_product_photo( $anypress_pid, $anypress_shop['photos'][ $anypress_slug ] ?? $anypress_photos['fallback'] );
}

// FluentCart's own sample categories the shop doesn't use.
foreach ( $anypress_shop['drop_categories'] ?? array() as $anypress_cat ) {
	$anypress_term = get_term_by( 'name', $anypress_cat, 'product-categories' );
	if ( $anypress_term ) {
		wp_delete_term( $anypress_term->term_id, 'product-categories' );
	}
}

// Each category's words on its page, under its name.
foreach ( $anypress_shop['category_text'] as $anypress_cat => $anypress_text ) {
	$anypress_term = get_term_by( 'name', $anypress_cat, 'product-categories' ) ?: (object) wp_insert_term( $anypress_cat, 'product-categories' );
	$anypress_tid  = $anypress_term->term_id ?? 0;
	if ( $anypress_tid ) {
		wp_update_term( $anypress_tid, 'product-categories', array( 'description' => $anypress_text, 'slug' => sanitize_title( $anypress_cat ) ) );
	}
}

// The shop's own products: a gift card and a subscription, with a photo each.
foreach ( $anypress_shop['own'] as $anypress_item ) {
	$anypress_info = 'once' === $anypress_item['bills']
		? array( 'payment_type' => 'onetime' )
		: array( 'payment_type' => 'subscription', 'repeat_interval' => 'monthly' );
	$anypress_res = ( new \FluentCart\App\Services\BulkProductInsertService() )->insertChunk(
		array(
			array(
				'_cid'         => $anypress_item['slug'],
				'post_title'   => $anypress_item['title'],
				'post_excerpt' => $anypress_item['about'],
				'post_content' => $anypress_item['about'],
				'post_status'  => 'published',
				'detail'       => array( 'fulfillment_type' => $anypress_item['kind'], 'variation_type' => 'simple' ),
				'variants'     => array( array( 'item_price' => $anypress_item['cents'], 'other_info' => $anypress_info ) ),
			),
		)
	);
	$anypress_pid = (int) ( $anypress_res['created'][0]['id'] ?? 0 );
	if ( ! $anypress_pid ) {
		throw new RuntimeException( 'Could not make ' . $anypress_item['title'] );
	}
	wp_update_post( array( 'ID' => $anypress_pid, 'post_name' => $anypress_item['slug'] ) );
	wp_set_object_terms( $anypress_pid, array( $anypress_item['category'] ), 'product-categories', false );
	anypress_demo_product_photo( $anypress_pid, $anypress_item['photo'] );
	$anypress_by_slug[ $anypress_item['slug'] ] = $anypress_pid;
}

// Reviews on the product pages, from customers who bought them.
foreach ( $anypress_shop['reviews'] as $anypress_r ) {
	$anypress_pid = $anypress_by_slug[ $anypress_r[0] ] ?? 0;
	if ( $anypress_pid ) {
		anypress_demo_fc( 'POST', '/reviews', array( 'post_id' => $anypress_pid, 'rating' => $anypress_r[1], 'title' => $anypress_r[2], 'content' => $anypress_r[3], 'reviewer_name' => $anypress_r[4], 'reviewer_email' => sanitize_title( $anypress_r[4] ) . '@example.com', 'status' => 'approved', 'is_verified' => 1 ) );
	}
}

// Stock counted on two pieces: one nearly gone, one sold out.
$anypress_modules                     = \FluentCart\Api\ModuleSettings::getAllSettings( false );
$anypress_modules['stock_management'] = array( 'active' => 'yes' ) + (array) ( $anypress_modules['stock_management'] ?? array() );
anypress_demo_fc( 'POST', '/settings/modules', $anypress_modules );
\FluentCart\Api\ModuleSettings::getAllSettings( false );
foreach ( $anypress_shop['stock'] as $anypress_slug => $anypress_left ) {
	$anypress_pid = $anypress_by_slug[ $anypress_slug ] ?? 0;
	if ( ! $anypress_pid ) {
		continue;
	}
	anypress_demo_fc( 'PUT', "/products/$anypress_pid/update-manage-stock", array( 'manage_stock' => 1 ) );
	foreach ( ProductVariation::where( 'post_id', $anypress_pid )->get() as $anypress_v ) {
		anypress_demo_fc( 'PUT', "/products/$anypress_pid/update-inventory/{$anypress_v->id}", array( 'total_stock' => 20 + $anypress_left, 'available' => $anypress_left ) );
	}
}

foreach ( $anypress_shop['coupons'] as $anypress_c ) {
	anypress_demo_fc( 'POST', '/coupons', array( 'title' => $anypress_c[0], 'code' => $anypress_c[1], 'type' => $anypress_c[2], 'amount' => $anypress_c[3], 'status' => 'active', 'stackable' => 'no', 'show_on_checkout' => 'no', 'notes' => $anypress_c[4] ) );
}

// Pay later (FluentCart's offline payment), so anyone trying the demo can place an order without a card. A real shop
// connects Stripe or PayPal in FluentCart's Payment settings.
\FluentCart\App\Modules\PaymentMethods\Core\GatewayManager::getInstance( 'offline_payment' )->updateSettings( array( 'is_active' => 'yes', 'payment_mode' => 'live' ) );

// Free shipping over an amount: FluentCart's free version does it with a free-shipping coupon that shows at checkout
// (Pro's dynamic pricing can apply it on its own).
if ( ! empty( $anypress_shop['free_shipping'] ) ) {
	$anypress_free = $anypress_shop['free_shipping'];
	anypress_demo_fc( 'POST', '/coupons', array( 'title' => $anypress_free['title'], 'code' => $anypress_free['code'], 'type' => 'free_shipping', 'amount' => 0, 'status' => 'active', 'stackable' => 'yes', 'show_on_checkout' => 'yes', 'conditions' => array( 'min_purchase_amount' => $anypress_free['min'], 'min_amount_basis' => 'subtotal' ), 'notes' => 'Free standard shipping on orders over ' . $anypress_free['min'] . '.' ) );
}

// Shipping zones and methods, as the shop's Shipping page describes them.
foreach ( $anypress_shop['shipping'] as $anypress_zone ) {
	$anypress_where = array( 'name' => $anypress_zone['name'], 'region' => $anypress_zone['region'] );
	if ( 'EU' === $anypress_zone['region'] ) {
		// Every EU country in one zone, from FluentCart's own list.
		$anypress_where['region'] = 'selection';
		$anypress_where['meta']   = array( 'selection_type' => 'included', 'countries' => array_values( \FluentCart\App\Services\Localization\LocalizationManager::getInstance()->taxContinents( 'EU' )['countries'] ?? array() ) );
	}
	$anypress_z  = anypress_demo_fc( 'POST', '/shipping/zones', $anypress_where );
	$anypress_zid = (int) ( $anypress_z['shipping_zone']['id'] ?? 0 );
	foreach ( $anypress_zone['methods'] as $anypress_m ) {
		anypress_demo_fc( 'POST', '/shipping/methods', array( 'zone_id' => $anypress_zid, 'title' => $anypress_m[0], 'type' => $anypress_m[1], 'amount' => $anypress_m[2], 'settings' => array( 'configure_rate' => 'per_order' ), 'is_enabled' => 1 ) );
	}
}

// Tax from FluentCart's own rate tables: sales tax for each US state (none in Oregon), UK VAT, and EU VAT through the
// One Stop Shop, so EU shoppers see their own country's VAT at checkout.
$anypress_tax = $anypress_shop['tax'];
anypress_demo_fc( 'POST', '/onboarding/save-tax', array( 'enable_tax' => 'yes', 'tax_inclusion' => 'excluded', 'store_country' => $anypress_tax['country'] ) );
$anypress_taxed = $anypress_tax['countries'];
if ( ! empty( $anypress_tax['eu_oss'] ) ) {
	anypress_demo_fc( 'POST', '/tax/configuration/settings/eu-vat', array( 'action' => 'euCrossBorderSettings', 'eu_vat_settings' => array( 'method' => 'oss', 'oss_country' => $anypress_tax['eu_oss'][0], 'oss_vat' => $anypress_tax['eu_oss'][1] ) ) );
	$anypress_taxed = array_merge( $anypress_taxed, array_values( \FluentCart\App\Services\Localization\LocalizationManager::getInstance()->taxContinents( 'EU' )['countries'] ?? array() ) );
}
\FluentCart\App\Services\Tax\TaxManager::getInstance()->generateTaxClasses( $anypress_taxed );

// ---------------------------------------------------------------------------------------------------------- pages
$anypress_pages = array();
$anypress_fc    = array();
foreach ( get_posts( array( 'post_type' => 'page', 'numberposts' => -1, 'post_status' => 'any' ) ) as $anypress_p ) {
	$anypress_fc[ $anypress_p->post_name ] = $anypress_p->ID;
}
$anypress_pages = $anypress_fc;

/** Puts the site's form in place of a pattern's "Form: <kind>" group. */
function anypress_demo_forms( $content ) {
	global $anypress_forms;
	foreach ( $anypress_forms as $kind => $id ) {
		$content = preg_replace(
			'#<!-- wp:group \{[^\n]*"metadata":\{"name":"Form: ' . $kind . '"\}.*?<!-- /wp:group -->#s',
			"<!-- wp:shortcode -->\n[fluentform id=\"$id\"]\n<!-- /wp:shortcode -->",
			$content
		);
	}
	return $content;
}

anypress_demo_page( 'thank-you', 'Thank you', anypress_demo_pattern( $anypress_pre . '-page-thanks' ) );
$anypress_done   = array( 'redirectTo' => 'customPage', 'customPage' => $anypress_pages['thank-you'], 'messageToShow' => '', 'samePageFormBehavior' => 'hide_form' );
$anypress_letter = anypress_demo_form( 'Newsletter', array( anypress_demo_field( 'input_email', 'email', 'Email', true, array( 'attributes.placeholder' => 'you@example.com' ) ) ), $anypress_kit['newsletter']['button'], array( 'redirectTo' => 'samePage', 'messageToShow' => $anypress_kit['newsletter']['message'], 'samePageFormBehavior' => 'hide_form' ) );
$anypress_forms  = array(
	'contact'    => anypress_demo_form(
		'Contact',
		array(
			anypress_demo_field( 'input_name', 'names', 'Your name', true ),
			anypress_demo_field( 'input_email', 'email', 'Email', true ),
			anypress_demo_field( 'input_text', 'order', 'Order number (if it is about an order)', false ),
			anypress_demo_field( 'select', 'topic', 'What is it about?', true, array( 'settings.placeholder' => 'Choose one', 'settings.advanced_options' => array_map( fn( $s ) => array( 'label' => $s, 'value' => $s, 'calc_value' => '' ), $anypress_kit['topics'] ) ) ),
			anypress_demo_field( 'textarea', 'message', 'Message', true, array( 'attributes.rows' => 4 ) ),
		),
		'Send message',
		$anypress_done
	),
	'newsletter' => $anypress_letter,
	'offer'      => $anypress_letter,
);

$anypress_home = anypress_demo_page( 'home', 'Home', anypress_demo_forms( anypress_demo_pattern( $anypress_kit['home'] ) ) );
update_option( 'show_on_front', 'page' );
update_option( 'page_on_front', $anypress_home );

// The kit's pages: array( slug, title, pattern, parent slug ).
foreach ( $anypress_kit['pages'] as $anypress_i => $anypress_more ) {
	anypress_demo_page( $anypress_more[0], $anypress_more[1], anypress_demo_forms( anypress_demo_pattern( $anypress_more[2] ) ), $anypress_pages[ $anypress_more[3] ?? '' ] ?? 0, $anypress_i + 1 );
}

// The EU cancellation form: FluentCart's free Customer Rights add-on shows it on the page set as its withdrawal page.
if ( class_exists( 'FluentCartCustomerRights' ) && ! empty( $anypress_pages['withdraw-from-contract'] ) ) {
	( new \FluentCart\Api\StoreSettings() )->set( 'withdrawal_page_id', $anypress_pages['withdraw-from-contract'] );
}

// The Shop page opens on its own photo (the theme's Shop template shows a page's featured image behind its title).
if ( ! empty( $anypress_shop['shop_photo'] ) && ! empty( $anypress_pages['shop'] ) ) {
	set_post_thumbnail( $anypress_pages['shop'], $anypress_media[ $anypress_shop['shop_photo'] ]['id'] );
}

anypress_demo_page(
	'privacy-policy',
	'Privacy policy',
	"<!-- wp:group {\"tagName\":\"section\",\"metadata\":{\"name\":\"Privacy\"},\"style\":{\"spacing\":{\"padding\":{\"top\":\"var:preset|spacing|xx-large\",\"bottom\":\"var:preset|spacing|xx-large\"}}},\"layout\":{\"type\":\"constrained\"}} -->\n<section class=\"wp-block-group\" style=\"padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)\"><!-- wp:heading {\"level\":1} -->\n<h1 class=\"wp-block-heading\">Privacy policy</h1>\n<!-- /wp:heading -->\n\n<!-- wp:paragraph -->\n<p>We use what you give us (your name, address, email and what you buy) to send your order, reply to you and, if you ask for it, send our newsletter. Card payments are handled by our payment provider; we never see or keep your card number. We keep order records for as long as tax law asks us to and never sell your details. To see, correct or delete what we hold about you, email hello@example.com.</p>\n<!-- /wp:paragraph -->" . anypress_demo_credits() . "</section>\n<!-- /wp:group -->",
	0,
	40
);
update_option( 'wp_page_for_privacy_policy', $anypress_pages['privacy-policy'] );

// The journal: a page for the posts, and posts with photos.
$anypress_blog = anypress_demo_page( $anypress_kit['blog'][0], $anypress_kit['blog'][1], '', 0, 30 );
update_option( 'page_for_posts', $anypress_blog );
wp_update_term( (int) get_option( 'default_category' ), 'category', array( 'name' => 'News', 'slug' => 'news' ) );
foreach ( json_decode( file_get_contents( $anypress_demo . '/posts.json' ), true ) as $anypress_i => $anypress_post ) {
	$anypress_cat = wp_create_category( $anypress_post['category'] );
	$anypress_pid = wp_insert_post(
		array(
			'post_status'   => 'publish',
			'post_title'    => $anypress_post['title'],
			'post_name'     => $anypress_post['slug'],
			'post_excerpt'  => $anypress_post['excerpt'],
			'post_content'  => anypress_demo_links( $anypress_post['content'] ),
			'post_category' => array( $anypress_cat ),
			'post_date'     => gmdate( 'Y-m-d H:i:s', time() - DAY_IN_SECONDS * ( 4 + 9 * $anypress_i ) ),
		)
	);
	set_post_thumbnail( $anypress_pid, $anypress_media[ $anypress_photos['posts'][ $anypress_post['key'] ] ]['id'] );
}

// ---------------------------------------------------------------------------------------------------------- menu, header, footer
$anypress_nav = wp_insert_post(
	array(
		'post_type'    => 'wp_navigation',
		'post_status'  => 'publish',
		'post_title'   => 'Main menu',
		'post_content' => implode( "\n", array_map( 'anypress_demo_menu_item', $anypress_kit['menu'] ) ),
	)
);
$anypress_header = str_replace( '<!-- wp:navigation {', '<!-- wp:navigation {"ref":' . $anypress_nav . ',', anypress_demo_pattern( $anypress_pre . '-header' ) );
anypress_demo_part( 'header', 'header', anypress_demo_links( $anypress_header ) );
anypress_demo_part( 'footer', 'footer', anypress_demo_links( anypress_demo_photos( anypress_demo_forms( anypress_demo_pattern( $anypress_pre . '-footer' ) ) ) ) );

// Links to one product point at its real page; then every page's links get the site's address.
$anypress_items = array();
foreach ( $anypress_by_slug as $anypress_slug => $anypress_pid ) {
	$anypress_items[ 'href="/item/' . $anypress_slug . '/"' ] = 'href="' . esc_url( get_permalink( $anypress_pid ) ) . '"';
}
foreach ( $anypress_pages as $anypress_id ) {
	$anypress_post = get_post( $anypress_id );
	wp_update_post( array( 'ID' => $anypress_id, 'post_content' => anypress_demo_links( strtr( $anypress_post->post_content, $anypress_items ) ) ) );
}

echo wp_json_encode(
	array(
		'pages'    => count( $anypress_pages ),
		'products' => count( $anypress_by_slug ),
		'home'     => get_permalink( $anypress_home ),
		'paths'    => array( 'contact' => '/help/contact/', 'blog' => '/' . $anypress_kit['blog'][0] . '/', 'shop' => '/shop/' ),
		'items'    => array_map( 'get_permalink', $anypress_by_slug ),
		'forms'    => array_values( $anypress_forms ),
	)
);
