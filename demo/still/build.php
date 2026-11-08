<?php
/**
 * Builds the Still kit's demo: Still Water, a whole website for a small massage practice with a quiet room, in an old
 * mill by a canal.
 *
 * It uses the kit's own words, so it has no copy.txt. Its photos are in photos/ with photos.json, and its treatments,
 * nearby towns and journal posts in services.json, towns.json and posts.json. Run it inside WordPress with the
 * AnyPress theme active and the AnyPress Blocks and Fluent Forms plugins on, on an empty site only:
 *
 *     wp eval-file wp-content/themes/anypress/demo/still/build.php
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'still',
	'style'       => 'kit-still',
	'home'        => 'kit-wellness',
	'name'        => 'Still Water',
	'tagline'     => 'Massage and quiet rooms in the old mill',
	'timezone'    => 'Europe/London',
	'quote'       => array(
		'slug'    => 'book',
		'title'   => 'Book a treatment',
		'pattern' => 'still-page-join',
		'button'  => 'Ask for a time',
		'labels'  => array(
			'service' => 'Which treatment?',
			'choose'  => 'Choose a treatment',
			'date'    => 'Which day suits you?',
			'address' => 'Best time of day',
			'message' => 'Anything we should know? Injuries, pregnancy, allergies',
		),
	),
	'services'    => array( 'Deep tissue massage', 'Hot stone massage', 'Pregnancy massage', 'Facial', 'Reflexology', 'The quiet room', 'A gift voucher', 'Not sure yet' ),
	'jobs'        => array( 'Massage therapist', 'Facialist', 'Front desk' ),
	'apply'       => array( 'title' => 'Job application', 'label' => 'Which role?', 'choose' => 'Choose a role' ),
	'newsletter'  => array( 'button' => 'Send me the letter', 'message' => 'Thank you. The next letter comes with the new season.' ),
	'area_title'  => 'Massage near ',
	'area_latlon' => '"lat":53.7424,"lon":-2.0137',
	'sitemap'     => array(
		'services' => array( 'treatments', 'Treatments' ),
		'reviews'  => array( 'reviews', 'Kind words' ),
		'areas'    => array( 'visiting', 'Coming from nearby' ),
		'offers'   => array( 'gifts', 'Gifts and offers' ),
		'careers'  => array( 'work-with-us', 'Work with us' ),
		'blog'     => array( 'journal', 'Journal' ),
	),
	'pages'       => array(
		array( 'slug' => 'rooms', 'title' => 'The rooms', 'sections' => array( 'still-page-rooms' ), 'order' => 2 ),
	),
	'menu'        => array(
		array(
			'label'    => 'Treatments',
			'slug'     => 'treatments',
			'children' => array(
				array( 'label' => 'All treatments', 'slug' => 'treatments' ),
				array( 'label' => 'Deep tissue massage', 'slug' => 'deep-tissue-massage' ),
				array( 'label' => 'Hot stone massage', 'slug' => 'hot-stone-massage' ),
				array( 'label' => 'Pregnancy massage', 'slug' => 'pregnancy-massage' ),
				array( 'label' => 'Facials', 'slug' => 'facials' ),
				array( 'label' => 'Reflexology', 'slug' => 'reflexology' ),
				array( 'label' => 'The quiet room', 'slug' => 'quiet-room' ),
			),
		),
		array( 'label' => 'The rooms', 'slug' => 'rooms' ),
		array( 'label' => 'Gifts', 'slug' => 'gifts' ),
		array(
			'label'    => 'About',
			'slug'     => 'about',
			'children' => array(
				array( 'label' => 'About us', 'slug' => 'about' ),
				array( 'label' => 'Kind words', 'slug' => 'reviews' ),
				array( 'label' => 'Coming from nearby', 'slug' => 'visiting' ),
				array( 'label' => 'Work with us', 'slug' => 'work-with-us' ),
				array( 'label' => 'Questions', 'slug' => 'faq' ),
				array( 'label' => 'Journal', 'slug' => 'journal' ),
			),
		),
		array( 'label' => 'Contact', 'slug' => 'contact' ),
	),
);
require dirname( __DIR__ ) . '/trades.php';
