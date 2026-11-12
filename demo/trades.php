<?php
/**
 * Builds a trades kit's demo website (Ridge, Circuit...): a whole website for a local trade business.
 *
 * A kit's demo/<kit>/build.php sets $anypress_kit (the business's name, the kit's style and pattern names, the form
 * choices) and requires this file. Its folder holds the business's words as JSON (services.json, towns.json,
 * posts.json), its photos and photos.json, which says which photo replaces which placeholder.
 *
 * It starts from the kit's starter pages and sections, so the demo shows exactly what an owner gets, then adds the
 * business's own words, photos, forms, menus and blog posts.
 *
 * A demo for another business on the same kit (demo/<kit>/<slug>/) also has swap.json, written by tools/demo/copy.py
 * from its copy: every piece of the kit's text and what it becomes, site-wide and per page, plus raw swaps for block
 * settings (map positions, phone links, counters). Its build.php can also set 'colors' and 'fonts' (a palette and a
 * font pairing from styles/colors and styles/typography), 'font_map' (the kit's display font => another),
 * 'pages' (more pages made from the kit's sections), 'menu', 'sitemap' (other slugs and titles for the main pages,
 * for a kit that isn't a trade), 'apply' (the application form's title and job label) and the quote form's 'labels'. It replaces the site's pages, posts, menus, header,
 * footer and global styles: run it on an empty site only.
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;
require_once dirname( __FILE__ ) . '/lib.php';

anypress_demo_start( $anypress_kit );

// ---------------------------------------------------------------------------------------------------------- pages
$anypress_pages = array();

// Where each of the site's main pages lives and what it's called. A kit for another kind of business can rename them
// in its build.php ('sitemap' => array( 'services' => array( 'programs', 'Programs' ) ...)).
$anypress_map = array_merge(
	array(
		'services' => array( 'services', 'Services' ),
		'about'    => array( 'about', 'About us' ),
		'reviews'  => array( 'reviews', 'Reviews' ),
		'areas'    => array( 'service-areas', 'Service areas' ),
		'offers'   => array( 'special-offers', 'Special offers' ),
		'faq'      => array( 'faq', 'Questions and answers' ),
		'careers'  => array( 'careers', 'Careers' ),
		'contact'  => array( 'contact', 'Contact' ),
		'blog'     => array( 'blog', 'Blog' ),
	),
	(array) ( $anypress_kit['sitemap'] ?? array() )
);

// The thank-you page first: the forms send visitors there.
anypress_demo_page( 'thank-you', 'Thank you', anypress_demo_pattern( $anypress_pre . '-page-thanks' ) );

$anypress_q     = $anypress_kit['quote'];
// The quote form's labels, which a kit for another kind of business can change ('date' => false leaves the date out).
$anypress_ql    = array_merge(
	array(
		'service' => 'What do you need?',
		'choose'  => 'Choose a service',
		'date'    => 'Best day for a visit',
		'address' => 'Address or town',
		'message' => "What's wrong?",
	),
	(array) ( $anypress_q['labels'] ?? array() )
);
$anypress_quote = anypress_demo_form(
	$anypress_q['title'],
	array(
		anypress_demo_field( 'input_name', 'names', 'Your name', true ),
		anypress_demo_field( 'input_email', 'email', 'Email', true ),
		anypress_demo_field( 'input_text', 'phone', 'Phone', true, array( 'attributes.type' => 'tel', 'attributes.autocomplete' => 'tel' ) ),
		anypress_demo_field( 'select', 'service', $anypress_ql['service'], true, array( 'settings.placeholder' => $anypress_ql['choose'], 'settings.advanced_options' => array_map( fn( $s ) => array( 'label' => $s, 'value' => $s, 'calc_value' => '' ), $anypress_kit['services'] ) ) ),
		$anypress_ql['date'] ? anypress_demo_field( 'input_date', 'preferred_date', $anypress_ql['date'], false, array( 'settings.date_format' => 'm/d/Y', 'settings.is_time_enabled' => false ) ) : null,
		anypress_demo_field( 'input_text', 'address', $anypress_ql['address'], false ),
		anypress_demo_field( 'textarea', 'message', $anypress_ql['message'], true, array( 'attributes.rows' => 4 ) ),
	),
	$anypress_q['button'],
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
	$anypress_kit['apply']['title'] ?? 'Job application',
	array(
		anypress_demo_field( 'input_name', 'names', 'Your name', true ),
		anypress_demo_field( 'input_email', 'email', 'Email', true ),
		anypress_demo_field( 'input_text', 'phone', 'Phone', true, array( 'attributes.type' => 'tel', 'attributes.autocomplete' => 'tel' ) ),
		anypress_demo_field( 'select', 'job', $anypress_kit['apply']['label'] ?? 'Which job?', true, array( 'settings.placeholder' => $anypress_kit['apply']['choose'] ?? 'Choose a job', 'settings.advanced_options' => array_map( fn( $s ) => array( 'label' => $s, 'value' => $s, 'calc_value' => '' ), $anypress_kit['jobs'] ) ) ),
		anypress_demo_field( 'textarea', 'message', 'A few lines about you', true, array( 'attributes.rows' => 5 ) ),
	),
	'Send my application',
	array( 'redirectTo' => 'customPage', 'customPage' => $anypress_pages['thank-you'], 'messageToShow' => '', 'samePageFormBehavior' => 'hide_form' )
);
$anypress_newsletter = anypress_demo_form(
	'Newsletter',
	array( anypress_demo_field( 'input_email', 'email', 'Email', true, array( 'attributes.placeholder' => 'you@example.com' ) ) ),
	$anypress_kit['newsletter']['button'],
	array( 'redirectTo' => 'samePage', 'messageToShow' => $anypress_kit['newsletter']['message'], 'samePageFormBehavior' => 'hide_form' )
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

$anypress_home = anypress_demo_page( 'home', 'Home', anypress_demo_forms( anypress_demo_pattern( $anypress_kit['home'] ) ) );
update_option( 'show_on_front', 'page' );
update_option( 'page_on_front', $anypress_home );

$anypress_services_page = anypress_demo_page( $anypress_map['services'][0], $anypress_map['services'][1], anypress_demo_pattern( $anypress_pre . '-page-services' ), 0, 1 );

// One page per service, from the service page pattern (written for one of them).
$anypress_service_text = json_decode( file_get_contents( $anypress_demo . '/services.json' ), true );
foreach ( $anypress_service_text as $anypress_i => $anypress_svc ) {
	$anypress_content = anypress_demo_swap( anypress_demo_pattern( $anypress_pre . '-page-service' ), $anypress_svc['swap'] ?? array() );
	anypress_demo_page( $anypress_svc['slug'], $anypress_svc['title'], $anypress_content, $anypress_services_page, $anypress_i );
}

anypress_demo_page( $anypress_map['about'][0], $anypress_map['about'][1], anypress_demo_pattern( $anypress_pre . '-page-about' ), 0, 2 );
anypress_demo_page( $anypress_map['reviews'][0], $anypress_map['reviews'][1], anypress_demo_pattern( $anypress_pre . '-page-reviews' ), 0, 3 );
$anypress_areas_page = anypress_demo_page( $anypress_map['areas'][0], $anypress_map['areas'][1], anypress_demo_pattern( $anypress_pre . '-page-areas' ), 0, 4 );

$anypress_towns = json_decode( file_get_contents( $anypress_demo . '/towns.json' ), true );
foreach ( $anypress_towns as $anypress_i => $anypress_town ) {
	$anypress_content = anypress_demo_swap( anypress_demo_pattern( $anypress_pre . '-page-area' ), $anypress_town['swap'] ?? array() );
	$anypress_content = str_replace( $anypress_kit['area_latlon'], '"lat":' . $anypress_town['lat'] . ',"lon":' . $anypress_town['lon'], $anypress_content );
	anypress_demo_page( $anypress_town['slug'], $anypress_kit['area_title'] . $anypress_town['name'], $anypress_content, $anypress_areas_page, $anypress_i );
}

anypress_demo_page( $anypress_map['offers'][0], $anypress_map['offers'][1], anypress_demo_forms( anypress_demo_pattern( $anypress_pre . '-page-offers' ) ), 0, 5 );
anypress_demo_page( $anypress_q['slug'], $anypress_q['title'], anypress_demo_forms( anypress_demo_pattern( $anypress_q['pattern'] ) ), 0, 6 );
anypress_demo_page( $anypress_map['faq'][0], $anypress_map['faq'][1], anypress_demo_pattern( $anypress_pre . '-page-faq' ), 0, 7 );
anypress_demo_page( $anypress_map['careers'][0], $anypress_map['careers'][1], anypress_demo_forms( str_replace( 'mailto:jobs@example.com', '#apply', anypress_demo_pattern( $anypress_pre . '-page-careers' ) ) ), 0, 8 );
anypress_demo_page( $anypress_map['contact'][0], $anypress_map['contact'][1], anypress_demo_forms( anypress_demo_pattern( $anypress_pre . '-page-contact' ) ), 0, 9 );
// More pages for this business, made from the kit's sections: array( slug, title, sections, parent slug, order ).
// A section is a pattern name, or "form:<kind>" for one of the site's forms.
foreach ( (array) ( $anypress_kit['pages'] ?? array() ) as $anypress_more ) {
	$anypress_content = implode(
		"\n\n",
		array_map(
			fn( $part ) => str_starts_with( $part, 'form:' ) ? "<!-- wp:shortcode -->\n[fluentform id=\"" . $GLOBALS[ 'anypress_' . substr( $part, 5 ) ] . "\"]\n<!-- /wp:shortcode -->" : anypress_demo_pattern( $part ),
			$anypress_more['sections']
		)
	);
	anypress_demo_page( $anypress_more['slug'], $anypress_more['title'], anypress_demo_forms( $anypress_content ), $anypress_pages[ $anypress_more['parent'] ?? '' ] ?? 0, $anypress_more['order'] ?? 11 );
}

anypress_demo_page(
	'privacy-policy',
	'Privacy policy',
	"<!-- wp:group {\"tagName\":\"section\",\"metadata\":{\"name\":\"Privacy\"},\"style\":{\"spacing\":{\"padding\":{\"top\":\"var:preset|spacing|xx-large\",\"bottom\":\"var:preset|spacing|xx-large\"}}},\"layout\":{\"type\":\"constrained\"}} -->\n<section class=\"wp-block-group\" style=\"padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)\"><!-- wp:heading {\"level\":1} -->\n<h1 class=\"wp-block-heading\">Privacy policy</h1>\n<!-- /wp:heading -->\n\n<!-- wp:paragraph -->\n<p>We use what you send us (your name, contact details and what you need) only to reply, book and carry out your job, and keep it for as long as the law asks us to keep job records. We never sell it. To see or delete what we hold about you, email hello@example.com.</p>\n<!-- /wp:paragraph -->" . anypress_demo_credits() . "</section>\n<!-- /wp:group -->",
	0,
	20
);
update_option( 'wp_page_for_privacy_policy', $anypress_pages['privacy-policy'] );

// The blog: a page for the posts, and posts with photos.
$anypress_blog = anypress_demo_page( $anypress_map['blog'][0], $anypress_map['blog'][1], '', 0, 10 );
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
$anypress_menu = array(
	array( 'label' => 'Services', 'slug' => $anypress_map['services'][0], 'children' => array_merge( array( array( 'label' => 'All services', 'slug' => $anypress_map['services'][0] ) ), array_map( fn( $s ) => array( 'label' => $s['title'], 'slug' => $s['slug'] ), $anypress_service_text ) ) ),
	array( 'label' => 'Areas', 'slug' => $anypress_map['areas'][0], 'children' => array_merge( array( array( 'label' => 'All areas', 'slug' => $anypress_map['areas'][0] ) ), array_map( fn( $t ) => array( 'label' => $t['name'], 'slug' => $t['slug'] ), $anypress_towns ) ) ),
	array( 'label' => 'About', 'slug' => $anypress_map['about'][0], 'children' => array( array( 'label' => 'About us', 'slug' => $anypress_map['about'][0] ), array( 'label' => 'Reviews', 'slug' => $anypress_map['reviews'][0] ), array( 'label' => 'Careers', 'slug' => $anypress_map['careers'][0] ), array( 'label' => 'Questions', 'slug' => $anypress_map['faq'][0] ) ) ),
	array( 'label' => 'Offers', 'slug' => $anypress_map['offers'][0] ),
	array( 'label' => 'Blog', 'slug' => $anypress_map['blog'][0] ),
	array( 'label' => 'Contact', 'slug' => $anypress_map['contact'][0] ),
);
if ( ! empty( $anypress_kit['menu'] ) ) {
	$anypress_menu = $anypress_kit['menu'];
}
$anypress_nav = wp_insert_post(
	array(
		'post_type'    => 'wp_navigation',
		'post_status'  => 'publish',
		'post_title'   => 'Main menu',
		'post_content' => implode( "\n", array_map( 'anypress_demo_menu_item', $anypress_menu ) ),
	)
);

$anypress_header = str_replace( '<!-- wp:navigation {', '<!-- wp:navigation {"ref":' . $anypress_nav . ',', anypress_demo_copy( anypress_demo_pattern( $anypress_pre . '-header' ) ) );
anypress_demo_part( 'header', 'header', anypress_demo_links( $anypress_header ) );
anypress_demo_part( 'footer', 'footer', anypress_demo_links( anypress_demo_photos( anypress_demo_forms( anypress_demo_copy( anypress_demo_pattern( $anypress_pre . '-footer' ) ) ) ) ) );

// Page links in every page.
foreach ( $anypress_pages as $anypress_id ) {
	$anypress_post = get_post( $anypress_id );
	wp_update_post( array( 'ID' => $anypress_id, 'post_content' => anypress_demo_links( $anypress_post->post_content ) ) );
}

// The site's logo, when the demo has one.
$anypress_logo = $anypress_media[ $anypress_photos['logo'] ]['id'] ?? 0;
if ( $anypress_logo ) {
	update_option( 'site_logo', $anypress_logo );
	update_option( 'site_icon', $anypress_logo );
}

echo wp_json_encode( array( 'pages' => count( $anypress_pages ), 'home' => get_permalink( $anypress_home ), 'quote' => '/' . $anypress_q['slug'] . '/', 'paths' => array_map( fn( $m ) => '/' . $m[0] . '/', $anypress_map ), 'leftover' => $anypress_kit['leftover'] ?? array(), 'forms' => array( $anypress_quote, $anypress_contact, $anypress_apply, $anypress_newsletter ) ) );
