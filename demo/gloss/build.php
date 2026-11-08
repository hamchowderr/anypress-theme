<?php
/**
 * Builds the Gloss kit's demo: Elm Studio, a whole website for a small hair salon with four stylists.
 *
 * It uses the kit's own words, so it has no copy.txt. Its photos are in photos/ with photos.json, and its services,
 * stylists and journal posts in services.json, towns.json and posts.json. Run it inside WordPress with the AnyPress
 * theme active and the AnyPress Blocks and Fluent Forms plugins on, on an empty site only:
 *
 *     wp eval-file wp-content/themes/anypress/demo/gloss/build.php
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'gloss',
	'style'       => 'kit-gloss',
	'home'        => 'kit-salon',
	'name'        => 'Elm Studio',
	'tagline'     => 'Hair, colour and brows on Elm Street',
	'timezone'    => 'America/Chicago',
	'quote'       => array(
		'slug'    => 'book',
		'title'   => 'Book an appointment',
		'pattern' => 'gloss-page-join',
		'button'  => 'Ask for a time',
		'labels'  => array(
			'service' => 'What would you like?',
			'choose'  => 'Choose a service',
			'date'    => 'Which day suits you?',
			'address' => 'Which stylist? (or anyone)',
			'message' => 'Anything we should know? Your hair now, what you would like',
		),
	),
	'services'    => array( 'Cut and style', 'Colour', 'Balayage', 'Blow-dry and styling', 'Brows and lashes', "Men's cut", 'A free colour consultation' ),
	'jobs'        => array( 'Stylist', 'Apprentice', 'Front desk' ),
	'apply'       => array( 'title' => 'Job application', 'label' => 'Which role?', 'choose' => 'Choose a role' ),
	'newsletter'  => array( 'button' => 'Tell me first', 'message' => 'Thank you! Your 20% code is on its way by email.' ),
	'area_title'  => '',
	'area_latlon' => 'no map on these pages',
	'sitemap'     => array(
		'about'   => array( 'about', 'About the salon' ),
		'areas'   => array( 'team', 'Our team' ),
		'offers'  => array( 'offers', 'Offers' ),
		'faq'     => array( 'faq', 'Questions' ),
		'blog'    => array( 'journal', 'Journal' ),
	),
	'pages'       => array(
		array( 'slug' => 'prices', 'title' => 'Prices', 'sections' => array( 'gloss-page-prices' ), 'order' => 2 ),
	),
	'menu'        => array(
		array(
			'label'    => 'Services',
			'slug'     => 'services',
			'children' => array(
				array( 'label' => 'All services', 'slug' => 'services' ),
				array( 'label' => 'Cut and style', 'slug' => 'cut-and-style' ),
				array( 'label' => 'Colour', 'slug' => 'colour' ),
				array( 'label' => 'Balayage', 'slug' => 'balayage' ),
				array( 'label' => 'Blow-dry and styling', 'slug' => 'blow-dry' ),
				array( 'label' => 'Brows and lashes', 'slug' => 'brows-and-lashes' ),
				array( 'label' => "Men's cuts", 'slug' => 'mens-cuts' ),
			),
		),
		array( 'label' => 'Prices', 'slug' => 'prices' ),
		array(
			'label'    => 'Our team',
			'slug'     => 'team',
			'children' => array(
				array( 'label' => 'The whole team', 'slug' => 'team' ),
				array( 'label' => 'Nadia', 'slug' => 'nadia' ),
				array( 'label' => 'Ollie', 'slug' => 'ollie' ),
				array( 'label' => 'Bea', 'slug' => 'bea' ),
				array( 'label' => 'Jess', 'slug' => 'jess' ),
			),
		),
		array(
			'label'    => 'About',
			'slug'     => 'about',
			'children' => array(
				array( 'label' => 'About the salon', 'slug' => 'about' ),
				array( 'label' => 'Reviews', 'slug' => 'reviews' ),
				array( 'label' => 'Offers', 'slug' => 'offers' ),
				array( 'label' => 'Careers', 'slug' => 'careers' ),
				array( 'label' => 'Questions', 'slug' => 'faq' ),
				array( 'label' => 'Journal', 'slug' => 'journal' ),
			),
		),
		array( 'label' => 'Contact', 'slug' => 'contact' ),
	),
);
require dirname( __DIR__ ) . '/trades.php';
