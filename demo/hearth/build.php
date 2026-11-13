<?php
/**
 * Builds the Hearth kit's demo: Ferro Bakery, a whole website for a family bakery café with stalls at four markets.
 *
 * It uses the kit's own words, so it has no copy.txt. Its photos are in photos/ with photos.json, and the parts of its
 * menu, its market stalls and journal posts in services.json, towns.json and posts.json. Run it inside WordPress with
 * the AnyPress theme active and the AnyPress Blocks and Fluent Forms plugins on, on an empty site only:
 *
 *     wp eval-file wp-content/themes/anypress/demo/hearth/build.php
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'hearth',
	'style'       => 'kit-hearth',
	'home'        => 'kit-food',
	'name'        => 'Ferro Bakery',
	'tagline'     => 'Bread, coffee and a long lunch since 1989',
	'timezone'    => 'America/Chicago',
	'quote'       => array(
		'slug'    => 'order',
		'title'   => 'Order a cake',
		'pattern' => 'hearth-page-join',
		'button'  => 'Send my order',
		'labels'  => array(
			'service' => 'What would you like?',
			'choose'  => 'Choose one',
			'date'    => 'The day you need it',
			'address' => 'Delivery address (leave empty to pick up)',
			'message' => 'Size, flavour and any writing on top',
		),
	),
	'services'    => array( 'A birthday cake', 'A wedding cake', 'A box of pastries', 'A bread order', 'Office breakfast', 'Working lunch', 'Party table' ),
	'jobs'        => array( 'Early baker', 'Barista', 'Counter and café' ),
	'apply'       => array( 'title' => 'Job application', 'label' => 'Which role?', 'choose' => 'Choose a role' ),
	'newsletter'  => array( 'button' => 'Send me the bake list', 'message' => "Thanks! The weekend bake list arrives every Thursday." ),
	'area_title'  => '',
	'area_latlon' => '"lat":39.8017,"lon":-89.6436',
	'sitemap'     => array(
		'services' => array( 'menu', 'Menu' ),
		'about'    => array( 'about', 'Our story' ),
		'areas'    => array( 'markets', 'Markets' ),
		'offers'   => array( 'offers', 'Offers' ),
		'careers'  => array( 'jobs', 'Work with us' ),
		'contact'  => array( 'contact', 'Visit and contact' ),
		'blog'     => array( 'journal', 'Journal' ),
	),
	'pages'       => array(
		array( 'slug' => 'catering', 'title' => 'Catering', 'sections' => array( 'hearth-page-catering' ), 'order' => 2 ),
	),
	'menu'        => array(
		array(
			'label'    => 'Menu',
			'slug'     => 'menu',
			'children' => array(
				array( 'label' => 'Full menu', 'slug' => 'menu' ),
				array( 'label' => 'Bread', 'slug' => 'bread' ),
				array( 'label' => 'Pastries', 'slug' => 'pastries' ),
				array( 'label' => 'Cakes', 'slug' => 'cakes' ),
				array( 'label' => 'Breakfast', 'slug' => 'breakfast' ),
				array( 'label' => 'Lunch', 'slug' => 'lunch' ),
				array( 'label' => 'Coffee', 'slug' => 'coffee' ),
			),
		),
		array( 'label' => 'Order a cake', 'slug' => 'order' ),
		array( 'label' => 'Catering', 'slug' => 'catering' ),
		array(
			'label'    => 'Markets',
			'slug'     => 'markets',
			'children' => array(
				array( 'label' => 'All markets', 'slug' => 'markets' ),
				array( 'label' => 'Downtown, Saturdays', 'slug' => 'downtown' ),
				array( 'label' => 'Old Town, Sundays', 'slug' => 'old-town' ),
				array( 'label' => 'Westside, Wednesdays', 'slug' => 'westside' ),
				array( 'label' => 'University, Thursdays', 'slug' => 'university' ),
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
				array( 'label' => 'Questions', 'slug' => 'faq' ),
				array( 'label' => 'Journal', 'slug' => 'journal' ),
			),
		),
		array( 'label' => 'Visit', 'slug' => 'contact' ),
	),
);
require dirname( __DIR__ ) . '/trades.php';
