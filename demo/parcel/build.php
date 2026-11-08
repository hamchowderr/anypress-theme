<?php
/**
 * Builds the Parcel kit's demo: Park Clay, a whole website for a small pottery studio that sells online and in shops.
 *
 * It uses the kit's own words, so it has no copy.txt. Its photos are in photos/ with photos.json, and its
 * collections, stockists and journal posts in services.json, towns.json and posts.json. Run it inside WordPress with
 * the AnyPress theme active and the AnyPress Blocks and Fluent Forms plugins on, on an empty site only:
 *
 *     wp eval-file wp-content/themes/anypress/demo/parcel/build.php
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'parcel',
	'style'       => 'kit-parcel',
	'home'        => 'kit-shop',
	'name'        => 'Park Clay',
	'tagline'     => 'Stoneware thrown by hand in Asheville',
	'timezone'    => 'America/New_York',
	'quote'       => array(
		'slug'    => 'order',
		'title'   => 'Order a piece or a set',
		'pattern' => 'parcel-page-join',
		'button'  => 'Send my order',
		'labels'  => array(
			'service' => 'What would you like?',
			'choose'  => 'Choose one',
			'date'    => 'When you need it',
			'address' => 'Where it goes (town or ZIP code)',
			'message' => 'Which pieces, how many and which glaze',
		),
	),
	'services'    => array( 'Cups and mugs', 'Bowls', 'Plates', 'Vases', 'Bottles', 'A matching set', 'A gift card' ),
	'jobs'        => array( 'Studio assistant', 'Packing and shipping', 'Saturday shop' ),
	'apply'       => array( 'title' => 'Job application', 'label' => 'Which role?', 'choose' => 'Choose a role' ),
	'newsletter'  => array( 'button' => 'Tell me first', 'message' => 'Thanks! Your 10% code is on its way by email.' ),
	'area_title'  => 'Where to buy in ',
	'area_latlon' => '"lat":35.5868,"lon":-82.5671',
	'sitemap'     => array(
		'services' => array( 'shop', 'Shop' ),
		'about'    => array( 'about', 'Our story' ),
		'areas'    => array( 'stockists', 'Stockists' ),
		'offers'   => array( 'offers', 'Offers' ),
		'faq'      => array( 'help', 'Shipping and returns' ),
		'careers'  => array( 'jobs', 'Work with us' ),
		'blog'     => array( 'journal', 'Journal' ),
	),
	'menu'        => array(
		array(
			'label'    => 'Shop',
			'slug'     => 'shop',
			'children' => array(
				array( 'label' => 'Everything', 'slug' => 'shop' ),
				array( 'label' => 'Cups and mugs', 'slug' => 'cups-and-mugs' ),
				array( 'label' => 'Bowls', 'slug' => 'bowls' ),
				array( 'label' => 'Plates', 'slug' => 'plates' ),
				array( 'label' => 'Vases', 'slug' => 'vases' ),
				array( 'label' => 'Bottles', 'slug' => 'bottles' ),
			),
		),
		array( 'label' => 'Order a set', 'slug' => 'order' ),
		array(
			'label'    => 'Stockists',
			'slug'     => 'stockists',
			'children' => array(
				array( 'label' => 'All stockists', 'slug' => 'stockists' ),
				array( 'label' => 'Asheville studio', 'slug' => 'asheville' ),
				array( 'label' => 'Durham', 'slug' => 'durham' ),
				array( 'label' => 'Charleston', 'slug' => 'charleston' ),
				array( 'label' => 'Atlanta market', 'slug' => 'atlanta' ),
			),
		),
		array(
			'label'    => 'About',
			'slug'     => 'about',
			'children' => array(
				array( 'label' => 'Our story', 'slug' => 'about' ),
				array( 'label' => 'Reviews', 'slug' => 'reviews' ),
				array( 'label' => 'Offers', 'slug' => 'offers' ),
				array( 'label' => 'Work with us', 'slug' => 'jobs' ),
				array( 'label' => 'Shipping and returns', 'slug' => 'help' ),
				array( 'label' => 'Journal', 'slug' => 'journal' ),
			),
		),
		array( 'label' => 'Contact', 'slug' => 'contact' ),
	),
);
require dirname( __DIR__ ) . '/trades.php';
