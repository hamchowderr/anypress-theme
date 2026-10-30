<?php
/**
 * Builds the Ridge kit's demo: Clearwater Plumbing & Heating, a whole website for a plumbing and heating firm.
 *
 * Run inside WordPress with the AnyPress theme active, and the AnyPress Blocks and Fluent Forms plugins on. The demo's
 * blueprint does this on WordPress Playground. On a site with WP-CLI:
 *
 *     wp eval-file wp-content/themes/anypress/demo/ridge/build.php
 *
 * It starts from the theme's Ridge starter pages and sections, so the demo shows exactly what an owner gets, then adds
 * the business's own words, photos, forms, menus and blog posts. It replaces the site's pages, posts, menus, header,
 * footer and global styles: run it on an empty site only.
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_demo = __DIR__;
wp_set_current_user( 1 );
require_once ABSPATH . 'wp-admin/includes/image.php';
require_once ABSPATH . 'wp-admin/includes/file.php';
require_once ABSPATH . 'wp-admin/includes/media.php';
require_once ABSPATH . 'wp-admin/includes/taxonomy.php';

/** The registered pattern's content, as WordPress hands it out. */
function anypress_demo_pattern( $name ) {
	$pattern = WP_Block_Patterns_Registry::get_instance()->get_registered( 'anypress/' . $name );
	if ( ! $pattern ) {
		throw new RuntimeException( "Pattern anypress/$name is missing: is the AnyPress theme active?" );
	}
	return $pattern['content'];
}

/** Replaces text in block markup. Keys and values are plain text; the markup holds them HTML-escaped. */
function anypress_demo_swap( $content, $pairs ) {
	$escaped = array();
	foreach ( $pairs as $from => $to ) {
		$escaped[ esc_html( $from ) ] = esc_html( $to );
		$escaped[ $from ]             = $to;
	}
	return strtr( $content, $escaped );
}

// Links in the patterns are written as /slug/; on a site in a subfolder (such as Playground's) they need the full path.
function anypress_demo_links( $content ) {
	// The kit's social icons point at # for the owner to fill in; the demo points them at each network.
	$content = strtr(
		$content,
		array(
			'{"url":"#","service":"facebook"}'  => '{"url":"https://www.facebook.com/","service":"facebook"}',
			'{"url":"#","service":"instagram"}' => '{"url":"https://www.instagram.com/","service":"instagram"}',
			'{"url":"#","service":"google"}'    => '{"url":"https://www.google.com/maps","service":"google"}',
		)
	);
	return preg_replace_callback(
		'#href="(/[a-z0-9/-]*)"#',
		fn( $m ) => 'href="' . esc_url( home_url( $m[1] ) ) . '"',
		$content
	);
}

// ---------------------------------------------------------------------------------------------------------- the site
update_option( 'blogname', 'Clearwater Plumbing & Heating' );
update_option( 'blogdescription', 'Plumbing and heating in Springfield since 2001' );
update_option( 'timezone_string', 'America/Chicago' );
update_option( 'default_comment_status', 'closed' );
$GLOBALS['wp_rewrite']->set_permalink_structure( '/%postname%/' );
flush_rewrite_rules();

// The Ridge style variation, as the site's own styles.
$anypress_variation = json_decode( file_get_contents( get_theme_file_path( 'styles/kit-ridge.json' ) ), true );
WP_Theme_JSON_Resolver::clean_cached_data();
$anypress_styles_id = WP_Theme_JSON_Resolver::get_user_global_styles_post_id();
wp_update_post(
	array(
		'ID'           => $anypress_styles_id,
		'post_content' => wp_json_encode(
			array(
				'version'                     => 3,
				'isGlobalStylesUserThemeJSON' => true,
				'settings'                    => array( 'color' => array( 'palette' => array( 'theme' => $anypress_variation['settings']['color']['palette'] ) ) ),
				'styles'                      => $anypress_variation['styles'],
			)
		),
	)
);
WP_Theme_JSON_Resolver::clean_cached_data();

// Start empty: the default post, page and comment go.
foreach ( get_posts( array( 'post_type' => array( 'post', 'page', 'wp_navigation' ), 'numberposts' => -1, 'post_status' => 'any' ) ) as $anypress_old ) {
	wp_delete_post( $anypress_old->ID, true );
}

// ---------------------------------------------------------------------------------------------------------- photos
// Each placeholder photo in the patterns has its own alt text; the demo puts a real photo in its place by that text.
$anypress_photos = json_decode( file_get_contents( $anypress_demo . '/photos.json' ), true );
$anypress_media  = array();
foreach ( $anypress_photos['files'] as $file => $alt ) {
	$path = $anypress_demo . '/photos/' . $file;
	$tmp  = wp_tempnam( $file );
	copy( $path, $tmp );
	$id = media_handle_sideload( array( 'name' => $file, 'tmp_name' => $tmp ), 0, $alt );
	if ( is_wp_error( $id ) ) {
		throw new RuntimeException( $file . ': ' . $id->get_error_message() );
	}
	update_post_meta( $id, '_wp_attachment_image_alt', $alt );
	$anypress_media[ $file ] = array( 'id' => $id, 'url' => wp_get_attachment_image_url( $id, 'large' ), 'full' => wp_get_attachment_image_url( $id, 'full' ) );
}

/** Swaps each placeholder image for the demo photo that matches its alt text. */
function anypress_demo_photos( $content ) {
	global $anypress_photos, $anypress_media;
	return preg_replace_callback(
		'#<!-- wp:(image|cover) (\{.*?\}) -->(.*?)<!-- /wp:\1 -->#s',
		function ( $m ) use ( $anypress_photos, $anypress_media ) {
			if ( ! preg_match( '#placeholder-[a-z]+\.svg#', $m[0] ) ) {
				return $m[0];
			}
			$alt = '';
			if ( preg_match( '#alt="([^"]*)"#', $m[3], $a ) ) {
				$alt = html_entity_decode( $a[1], ENT_QUOTES );
			}
			$file = $anypress_photos['by_alt'][ $alt ] ?? $anypress_photos['fallback'];
			$media = $anypress_media[ $file ];
			$attrs = json_decode( $m[2], true );
			$attrs['id'] = $media['id'];
			if ( 'cover' === $m[1] ) {
				$attrs['url'] = $media['full'];
			}
			$inner = preg_replace( '#alt="[^"]*"#', 'alt="' . esc_attr( 'cover' === $m[1] ? '' : $anypress_photos['files'][ $file ] ) . '"', $m[3], 1 );
			$inner = preg_replace( '#src="[^"]*placeholder-[a-z]+\.svg"#', 'src="' . esc_url( 'cover' === $m[1] ? $media['full'] : $media['url'] ) . '"', $inner );
			if ( 'image' === $m[1] ) {
				$inner = preg_replace( '#<img #', '<img class="wp-image-' . $media['id'] . '" ', $inner, 1 );
			} else {
				$inner = str_replace( 'class="wp-block-cover__image-background"', 'class="wp-block-cover__image-background wp-image-' . $media['id'] . '"', $inner );
			}
			return '<!-- wp:' . $m[1] . ' ' . wp_json_encode( $attrs, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . ' -->' . $inner . '<!-- /wp:' . $m[1] . ' -->';
		},
		$content
	);
}

// ---------------------------------------------------------------------------------------------------------- forms
$anypress_elements = ( static function () {
	return include WP_PLUGIN_DIR . '/fluentform/app/Services/FormBuilder/DefaultElements.php';
} )();

/** One Fluent Forms field, from Fluent Forms' own default for that kind of field. */
function anypress_demo_field( $kind, $name, $label, $required = false, $extra = array() ) {
	global $anypress_elements;
	$field = $anypress_elements['general'][ $kind ];
	$field['uniqElKey'] = 'el_' . $name;
	if ( 'input_name' === $kind ) {
		$field['fields']['first_name']['settings']['label']   = $label;
		$field['fields']['first_name']['attributes']['placeholder'] = '';
		$field['fields']['first_name']['settings']['validation_rules']['required']['value'] = $required;
		$field['fields']['middle_name']['settings']['visible'] = false;
		$field['fields']['last_name']['settings']['visible']   = false;
		return $field;
	}
	$field['attributes']['name']                                = $name;
	$field['settings']['label']                                 = $label;
	$field['settings']['validation_rules']['required']['value'] = $required;
	if ( isset( $field['attributes']['placeholder'] ) ) {
		$field['attributes']['placeholder'] = '';
	}
	foreach ( $extra as $path => $value ) {
		$ref  = &$field;
		$keys = explode( '.', $path );
		foreach ( $keys as $key ) {
			$ref = &$ref[ $key ];
		}
		$ref = $value;
		unset( $ref );
	}
	return $field;
}

function anypress_demo_form( $title, $fields, $button, $confirmation ) {
	$form = array(
		'fields'       => $fields,
		'submitButton' => array(
			'uniqElKey'      => 'el_submit',
			'element'        => 'button',
			'attributes'     => array( 'type' => 'submit', 'class' => 'wp-element-button' ),
			'settings'       => array( 'align' => 'left', 'button_style' => 'default', 'container_class' => '', 'help_message' => '', 'background_color' => '#1a7efb', 'button_size' => 'md', 'color' => 'var(--wp--preset--color--base)', 'button_ui' => array( 'type' => 'default', 'text' => $button, 'img_url' => '' ) ),
			'editor_options' => array( 'title' => 'Submit Button' ),
		),
	);
	$now = current_time( 'mysql' );
	$id  = wpFluent()->table( 'fluentform_forms' )->insertGetId( array( 'title' => $title, 'status' => 'published', 'type' => 'form', 'form_fields' => wp_json_encode( $form ), 'created_at' => $now, 'updated_at' => $now ) );
	wpFluent()->table( 'fluentform_form_meta' )->insert(
		array(
			'form_id'    => $id,
			'meta_key'   => 'formSettings', // phpcs:ignore WordPress.DB.SlowDBQuery.slow_db_query_meta_key
			'value'      => wp_json_encode(
				array(
					'confirmation' => $confirmation,
					'restrictions' => array(),
					'layout'       => array( 'labelPlacement' => 'top', 'helpMessagePlacement' => 'with_label', 'errorMessagePlacement' => 'inline', 'cssClassName' => '', 'asteriskPlacement' => 'asterisk-right' ),
				)
			),
		)
	);
	return $id;
}

// ---------------------------------------------------------------------------------------------------------- pages
$anypress_pages = array();
function anypress_demo_page( $slug, $title, $content, $parent = 0, $order = 0 ) {
	global $anypress_pages;
	$id = wp_insert_post(
		array(
			'post_type'    => 'page',
			'post_status'  => 'publish',
			'post_title'   => $title,
			'post_name'    => $slug,
			'post_parent'  => $parent,
			'menu_order'   => $order,
			'post_content' => anypress_demo_photos( $content ),
		)
	);
	update_post_meta( $id, '_wp_page_template', 'page-no-title' );
	$anypress_pages[ $slug ] = $id;
	return $id;
}

// The thank-you page first: the forms send visitors there.
anypress_demo_page( 'thank-you', 'Thank you', anypress_demo_pattern( 'ridge-page-thanks' ) );

$anypress_services = array(
	'Emergency plumbing',
	'Leaks and burst pipes',
	'Drain cleaning',
	'Water heaters',
	'Boilers and heating',
	'Bathrooms and kitchens',
	'Something else',
);
$anypress_quote = anypress_demo_form(
	'Get a quote',
	array(
		anypress_demo_field( 'input_name', 'names', 'Your name', true ),
		anypress_demo_field( 'input_email', 'email', 'Email', true ),
		anypress_demo_field( 'input_text', 'phone', 'Phone', true, array( 'attributes.type' => 'tel', 'attributes.autocomplete' => 'tel' ) ),
		anypress_demo_field( 'select', 'service', 'What do you need?', true, array( 'settings.placeholder' => 'Choose a service', 'settings.advanced_options' => array_map( fn( $s ) => array( 'label' => $s, 'value' => $s, 'calc_value' => '' ), $anypress_services ) ) ),
		anypress_demo_field( 'input_date', 'preferred_date', 'Best day for a visit', false, array( 'settings.date_format' => 'm/d/Y', 'settings.is_time_enabled' => false ) ),
		anypress_demo_field( 'input_text', 'address', 'Address or town', false ),
		anypress_demo_field( 'textarea', 'message', "What's wrong?", true, array( 'attributes.rows' => 4 ) ),
	),
	'Send my quote request',
	array( 'redirectTo' => 'customPage', 'customPage' => $anypress_pages['thank-you'], 'messageToShow' => '', 'samePageFormBehavior' => 'hide_form' )
);
$anypress_contact = anypress_demo_form(
	'Contact',
	array(
		anypress_demo_field( 'input_name', 'names', 'Your name', true ),
		anypress_demo_field( 'input_email', 'email', 'Email', true ),
		anypress_demo_field( 'input_text', 'phone', 'Phone', false, array( 'attributes.type' => 'tel', 'attributes.autocomplete' => 'tel' ) ),
		anypress_demo_field( 'textarea', 'message', 'Message', true, array( 'attributes.rows' => 4 ) ),
	),
	'Send message',
	array( 'redirectTo' => 'customPage', 'customPage' => $anypress_pages['thank-you'], 'messageToShow' => '', 'samePageFormBehavior' => 'hide_form' )
);
$anypress_apply = anypress_demo_form(
	'Job application',
	array(
		anypress_demo_field( 'input_name', 'names', 'Your name', true ),
		anypress_demo_field( 'input_email', 'email', 'Email', true ),
		anypress_demo_field( 'input_text', 'phone', 'Phone', true, array( 'attributes.type' => 'tel', 'attributes.autocomplete' => 'tel' ) ),
		anypress_demo_field( 'select', 'job', 'Which job?', true, array( 'settings.placeholder' => 'Choose a job', 'settings.advanced_options' => array_map( fn( $s ) => array( 'label' => $s, 'value' => $s, 'calc_value' => '' ), array( 'Service plumber', 'Heating engineer', 'Apprentice plumber' ) ) ) ),
		anypress_demo_field( 'textarea', 'message', 'A few lines about you', true, array( 'attributes.rows' => 5 ) ),
	),
	'Send my application',
	array( 'redirectTo' => 'customPage', 'customPage' => $anypress_pages['thank-you'], 'messageToShow' => '', 'samePageFormBehavior' => 'hide_form' )
);
$anypress_newsletter = anypress_demo_form(
	'Newsletter',
	array( anypress_demo_field( 'input_email', 'email', 'Email', true, array( 'attributes.placeholder' => 'you@example.com' ) ) ),
	'Send me the code',
	array( 'redirectTo' => 'samePage', 'messageToShow' => "Thanks! Your code is WELCOME50. We've emailed it to you too.", 'samePageFormBehavior' => 'hide_form' )
);

/** Puts the site's form in place of a pattern's "Form: <kind>" group. */
function anypress_demo_forms( $content ) {
	global $anypress_quote, $anypress_contact, $anypress_apply, $anypress_newsletter;
	$forms = array( 'quote' => $anypress_quote, 'contact' => $anypress_contact, 'apply' => $anypress_apply, 'newsletter' => $anypress_newsletter, 'offer' => $anypress_newsletter );
	foreach ( $forms as $kind => $id ) {
		$content = preg_replace(
			'#<!-- wp:group \{[^\n]*"metadata":\{"name":"Form: ' . $kind . '"\}.*?<!-- /wp:group -->#s',
			"<!-- wp:shortcode -->\n[fluentform id=\"$id\"]\n<!-- /wp:shortcode -->",
			$content
		);
	}
	return $content;
}

$anypress_home = anypress_demo_page( 'home', 'Home', anypress_demo_forms( anypress_demo_pattern( 'kit-home-services' ) ) );
update_option( 'show_on_front', 'page' );
update_option( 'page_on_front', $anypress_home );

$anypress_services_page = anypress_demo_page( 'services', 'Services', anypress_demo_pattern( 'ridge-page-services' ), 0, 1 );

// One page per service, from the service page pattern (written for drain cleaning).
$anypress_service_text = json_decode( file_get_contents( $anypress_demo . '/services.json' ), true );
foreach ( $anypress_service_text as $anypress_i => $anypress_svc ) {
	$anypress_content = anypress_demo_swap( anypress_demo_pattern( 'ridge-page-service' ), $anypress_svc['swap'] );
	anypress_demo_page( $anypress_svc['slug'], $anypress_svc['title'], $anypress_content, $anypress_services_page, $anypress_i );
}

anypress_demo_page( 'about', 'About us', anypress_demo_pattern( 'ridge-page-about' ), 0, 2 );
anypress_demo_page( 'reviews', 'Reviews', anypress_demo_pattern( 'ridge-page-reviews' ), 0, 3 );
$anypress_areas_page = anypress_demo_page( 'service-areas', 'Service areas', anypress_demo_pattern( 'ridge-page-areas' ), 0, 4 );

$anypress_towns = json_decode( file_get_contents( $anypress_demo . '/towns.json' ), true );
foreach ( $anypress_towns as $anypress_i => $anypress_town ) {
	$anypress_content = anypress_demo_swap( anypress_demo_pattern( 'ridge-page-area' ), $anypress_town['swap'] );
	$anypress_content = str_replace( '"lat":39.6761,"lon":-89.7043', '"lat":' . $anypress_town['lat'] . ',"lon":' . $anypress_town['lon'], $anypress_content );
	anypress_demo_page( $anypress_town['slug'], 'Plumber in ' . $anypress_town['name'], $anypress_content, $anypress_areas_page, $anypress_i );
}

anypress_demo_page( 'special-offers', 'Special offers', anypress_demo_forms( anypress_demo_pattern( 'ridge-page-offers' ) ), 0, 5 );
anypress_demo_page( 'get-a-quote', 'Get a quote', anypress_demo_forms( anypress_demo_pattern( 'ridge-page-quote' ) ), 0, 6 );
anypress_demo_page( 'faq', 'Questions and answers', anypress_demo_pattern( 'ridge-page-faq' ), 0, 7 );
anypress_demo_page( 'careers', 'Careers', anypress_demo_forms( str_replace( 'mailto:jobs@example.com', '#apply', anypress_demo_pattern( 'ridge-page-careers' ) ) ), 0, 8 );
anypress_demo_page( 'contact', 'Contact', anypress_demo_forms( anypress_demo_pattern( 'ridge-page-contact' ) ), 0, 9 );
anypress_demo_page(
	'privacy-policy',
	'Privacy policy',
	"<!-- wp:group {\"tagName\":\"section\",\"metadata\":{\"name\":\"Privacy\"},\"style\":{\"spacing\":{\"padding\":{\"top\":\"var:preset|spacing|xx-large\",\"bottom\":\"var:preset|spacing|xx-large\"}}},\"layout\":{\"type\":\"constrained\"}} -->\n<section class=\"wp-block-group\" style=\"padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)\"><!-- wp:heading {\"level\":1} -->\n<h1 class=\"wp-block-heading\">Privacy policy</h1>\n<!-- /wp:heading -->\n\n<!-- wp:paragraph -->\n<p>We use what you send us (your name, contact details and what you need) only to reply, book and carry out your job, and keep it for as long as the law asks us to keep job records. We never sell it. To see or delete what we hold about you, email hello@example.com.</p>\n<!-- /wp:paragraph --></section>\n<!-- /wp:group -->",
	0,
	20
);
update_option( 'wp_page_for_privacy_policy', $anypress_pages['privacy-policy'] );

// The blog: a page for the posts, and posts with photos.
$anypress_blog = anypress_demo_page( 'blog', 'Blog', '', 0, 10 );
update_option( 'page_for_posts', $anypress_blog );
wp_update_term( (int) get_option( 'default_category' ), 'category', array( 'name' => 'Tips', 'slug' => 'tips' ) );
$anypress_posts = json_decode( file_get_contents( $anypress_demo . '/posts.json' ), true );
foreach ( $anypress_posts as $anypress_i => $anypress_post ) {
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
function anypress_demo_link( $label, $slug_or_url ) {
	global $anypress_pages;
	$id  = $anypress_pages[ $slug_or_url ] ?? 0;
	$url = $id ? get_permalink( $id ) : $slug_or_url;
	$a   = array( 'label' => $label, 'url' => $url, 'kind' => $id ? 'post-type' : 'custom' );
	if ( $id ) {
		$a['type'] = 'page';
		$a['id']   = $id;
	}
	return $a;
}
function anypress_demo_menu_item( $item ) {
	if ( isset( $item['children'] ) ) {
		$a = anypress_demo_link( $item['label'], $item['slug'] );
		return '<!-- wp:navigation-submenu ' . wp_json_encode( $a, JSON_UNESCAPED_SLASHES ) . " -->\n" . implode( "\n", array_map( 'anypress_demo_menu_item', $item['children'] ) ) . "\n<!-- /wp:navigation-submenu -->";
	}
	return '<!-- wp:navigation-link ' . wp_json_encode( anypress_demo_link( $item['label'], $item['slug'] ), JSON_UNESCAPED_SLASHES ) . ' /-->';
}
$anypress_menu = array(
	array( 'label' => 'Services', 'slug' => 'services', 'children' => array_merge( array( array( 'label' => 'All services', 'slug' => 'services' ) ), array_map( fn( $s ) => array( 'label' => $s['title'], 'slug' => $s['slug'] ), $anypress_service_text ) ) ),
	array( 'label' => 'Areas', 'slug' => 'service-areas', 'children' => array_merge( array( array( 'label' => 'All areas', 'slug' => 'service-areas' ) ), array_map( fn( $t ) => array( 'label' => $t['name'], 'slug' => $t['slug'] ), $anypress_towns ) ) ),
	array( 'label' => 'About', 'slug' => 'about', 'children' => array( array( 'label' => 'About us', 'slug' => 'about' ), array( 'label' => 'Reviews', 'slug' => 'reviews' ), array( 'label' => 'Careers', 'slug' => 'careers' ), array( 'label' => 'Questions', 'slug' => 'faq' ) ) ),
	array( 'label' => 'Offers', 'slug' => 'special-offers' ),
	array( 'label' => 'Blog', 'slug' => 'blog' ),
	array( 'label' => 'Contact', 'slug' => 'contact' ),
);
$anypress_nav = wp_insert_post(
	array(
		'post_type'    => 'wp_navigation',
		'post_status'  => 'publish',
		'post_title'   => 'Main menu',
		'post_content' => implode( "\n", array_map( 'anypress_demo_menu_item', $anypress_menu ) ),
	)
);

function anypress_demo_part( $slug, $area, $content ) {
	foreach ( get_posts( array( 'post_type' => 'wp_template_part', 'name' => $slug, 'numberposts' => -1, 'post_status' => 'any' ) ) as $old ) {
		wp_delete_post( $old->ID, true );
	}
	$id = wp_insert_post(
		array(
			'post_type'    => 'wp_template_part',
			'post_status'  => 'publish',
			'post_name'    => $slug,
			'post_title'   => ucfirst( $slug ),
			'post_content' => $content,
			'tax_input'    => array( 'wp_theme' => array( get_stylesheet() ) ),
		)
	);
	wp_set_object_terms( $id, get_stylesheet(), 'wp_theme' );
	wp_set_object_terms( $id, $area, 'wp_template_part_area' );
	return $id;
}
$anypress_header = str_replace( '<!-- wp:navigation {', '<!-- wp:navigation {"ref":' . $anypress_nav . ',', anypress_demo_pattern( 'ridge-header' ) );
anypress_demo_part( 'header', 'header', anypress_demo_links( $anypress_header ) );
anypress_demo_part( 'footer', 'footer', anypress_demo_links( anypress_demo_photos( anypress_demo_forms( anypress_demo_pattern( 'ridge-footer' ) ) ) ) );

// Page links in every page.
foreach ( $anypress_pages as $anypress_id ) {
	$anypress_post = get_post( $anypress_id );
	wp_update_post( array( 'ID' => $anypress_id, 'post_content' => anypress_demo_links( $anypress_post->post_content ) ) );
}

// The site's logo: a drop of water on the brand colour.
$anypress_logo = $anypress_media[ $anypress_photos['logo'] ]['id'] ?? 0;
if ( $anypress_logo ) {
	update_option( 'site_logo', $anypress_logo );
	update_option( 'site_icon', $anypress_logo );
}

echo wp_json_encode( array( 'pages' => count( $anypress_pages ), 'home' => get_permalink( $anypress_home ), 'forms' => array( $anypress_quote, $anypress_contact, $anypress_apply, $anypress_newsletter ) ) );
