<?php
/**
 * Builds the Keystone kit's demo: Hollis & Co, a whole website for a small real estate agency in the Hudson Valley.
 *
 * It uses the kit's own words, so it has no copy.txt. Its photos are in photos/ with photos.json, and its homes for
 * sale, towns and market notes in services.json, towns.json and posts.json. Run it inside WordPress with the AnyPress
 * theme active and the AnyPress Blocks and Fluent Forms plugins on, on an empty site only:
 *
 *     wp eval-file wp-content/themes/anypress/demo/keystone/build.php
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'keystone',
	'style'       => 'kit-keystone',
	'home'        => 'kit-real-estate',
	'name'        => 'Hollis & Co',
	'tagline'     => 'Homes bought, sold and rented in the Hudson Valley',
	'timezone'    => 'America/New_York',
	'quote'       => array(
		'slug'    => 'valuation',
		'title'   => 'Free valuation',
		'pattern' => 'keystone-page-join',
		'button'  => 'Book my valuation',
		'labels'  => array(
			'service' => 'What can we help with?',
			'choose'  => 'Choose one',
			'date'    => 'When would suit you for a visit?',
			'address' => 'Address of the home',
			'message' => 'Tell us about the home',
		),
	),
	'services'    => array( 'Selling a home', 'Buying a home', 'Renting a home', 'Letting out a home', 'Something else' ),
	'jobs'        => array( 'Licensed agent', 'Office manager' ),
	'apply'       => array( 'title' => 'Job application', 'label' => 'Which role?', 'choose' => 'Choose a role' ),
	'newsletter'  => array( 'button' => 'Send me new homes', 'message' => 'Thank you! New homes will reach you by email, a day early.' ),
	'area_title'  => '',
	'area_latlon' => 'no map on these pages',
	'sitemap'     => array(
		'services' => array( 'homes', 'Homes for sale' ),
		'areas'    => array( 'towns', 'Towns' ),
		'offers'   => array( 'selling', 'Selling' ),
		'faq'      => array( 'faq', 'Questions' ),
		'careers'  => array( 'join-us', 'Join us' ),
		'blog'     => array( 'market-notes', 'Market notes' ),
	),
	'pages'       => array(
		array(
			'slug'     => 'rentals',
			'title'    => 'Rentals',
			'sections' => array( 'keystone-page-rentals' ),
			'order'    => 5,
		),
	),
	'menu'        => array(
		array(
			'label'    => 'Homes',
			'slug'     => 'homes',
			'children' => array(
				array( 'label' => 'All homes for sale', 'slug' => 'homes' ),
				array( 'label' => '12 Orchard Lane', 'slug' => '12-orchard-lane' ),
				array( 'label' => '4 Mill Road', 'slug' => '4-mill-road' ),
				array( 'label' => 'The Old Rectory', 'slug' => 'the-old-rectory' ),
				array( 'label' => '27 Tinker Street', 'slug' => '27-tinker-street' ),
				array( 'label' => '9 River View Drive', 'slug' => '9-river-view-drive' ),
				array( 'label' => '2 Church Street', 'slug' => '2-church-street' ),
			),
		),
		array(
			'label'    => 'Towns',
			'slug'     => 'towns',
			'children' => array(
				array( 'label' => 'All towns', 'slug' => 'towns' ),
				array( 'label' => 'Rhinebeck', 'slug' => 'rhinebeck' ),
				array( 'label' => 'Kingston', 'slug' => 'kingston' ),
				array( 'label' => 'Hudson', 'slug' => 'hudson' ),
				array( 'label' => 'Woodstock', 'slug' => 'woodstock' ),
			),
		),
		array( 'label' => 'Rentals', 'slug' => 'rentals' ),
		array( 'label' => 'Selling', 'slug' => 'selling' ),
		array(
			'label'    => 'About',
			'slug'     => 'about',
			'children' => array(
				array( 'label' => 'About us', 'slug' => 'about' ),
				array( 'label' => 'Reviews', 'slug' => 'reviews' ),
				array( 'label' => 'Join us', 'slug' => 'join-us' ),
				array( 'label' => 'Questions', 'slug' => 'faq' ),
				array( 'label' => 'Market notes', 'slug' => 'market-notes' ),
			),
		),
		array( 'label' => 'Contact', 'slug' => 'contact' ),
	),
);
require dirname( __DIR__ ) . '/trades.php';
