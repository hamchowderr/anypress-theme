<?php
/**
 * Builds the Chapter kit's demo: Draw with Mara, a whole website for an online drawing school that also runs weekend
 * workshops in six cities.
 *
 * It uses the kit's own words, so it has no copy.txt. Its photos are in photos/ with photos.json, and its courses,
 * workshop cities and journal posts in services.json, towns.json and posts.json. Run it inside WordPress with the
 * AnyPress theme active and the AnyPress Blocks and Fluent Forms plugins on, on an empty site only:
 *
 *     wp eval-file wp-content/themes/anypress/demo/chapter/build.php
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'chapter',
	'style'       => 'kit-chapter',
	'home'        => 'kit-courses',
	'name'        => 'Draw with Mara',
	'tagline'     => 'Online drawing courses and weekend workshops',
	'timezone'    => 'America/Los_Angeles',
	'quote'       => array(
		'slug'    => 'join',
		'title'   => 'Join a course',
		'pattern' => 'chapter-page-join',
		'button'  => 'Send',
		'labels'  => array(
			'service' => 'Which course?',
			'choose'  => 'Choose a course',
			'date'    => false,
			'address' => 'Where do you draw from? (city)',
			'message' => 'What would you like to get better at?',
		),
	),
	'services'    => array( 'Draw people in 30 days', 'The sketchbook habit', 'Faces and portraits', 'Urban sketching', 'Watercolor for sketchers', 'Hands and feet', 'The community', 'A weekend workshop', 'Not sure yet' ),
	'jobs'        => array( 'Feedback assistant', 'Live session host', 'Workshop assistant' ),
	'apply'       => array( 'title' => 'Teaching application', 'label' => 'Which role?', 'choose' => 'Choose a role' ),
	'newsletter'  => array( 'button' => 'Send me the prompts', 'message' => "You're in! Your first drawing prompt arrives on Monday." ),
	'area_title'  => 'Workshops in ',
	'area_latlon' => '"lat":45.5221,"lon":-122.661',
	'sitemap'     => array(
		'services' => array( 'courses', 'Courses' ),
		'about'    => array( 'about', 'About Mara' ),
		'reviews'  => array( 'student-stories', 'Student stories' ),
		'areas'    => array( 'workshops', 'Workshops' ),
		'offers'   => array( 'offers', 'Offers and gifts' ),
		'careers'  => array( 'teach', 'Teach with us' ),
		'blog'     => array( 'journal', 'Journal' ),
	),
	'pages'       => array(
		array( 'slug' => 'community', 'title' => 'The community', 'sections' => array( 'chapter-page-community' ), 'order' => 1 ),
	),
	'menu'        => array(
		array(
			'label'    => 'Courses',
			'slug'     => 'courses',
			'children' => array(
				array( 'label' => 'All courses', 'slug' => 'courses' ),
				array( 'label' => 'Draw people in 30 days', 'slug' => 'draw-people-in-30-days' ),
				array( 'label' => 'The sketchbook habit', 'slug' => 'sketchbook-habit' ),
				array( 'label' => 'Faces and portraits', 'slug' => 'faces-and-portraits' ),
				array( 'label' => 'Urban sketching', 'slug' => 'urban-sketching' ),
				array( 'label' => 'Watercolor for sketchers', 'slug' => 'watercolor-for-sketchers' ),
				array( 'label' => 'Hands and feet', 'slug' => 'hands-and-feet' ),
			),
		),
		array( 'label' => 'Community', 'slug' => 'community' ),
		array( 'label' => 'Workshops', 'slug' => 'workshops' ),
		array(
			'label'    => 'About',
			'slug'     => 'about',
			'children' => array(
				array( 'label' => 'About Mara', 'slug' => 'about' ),
				array( 'label' => 'Student stories', 'slug' => 'student-stories' ),
				array( 'label' => 'Offers and gifts', 'slug' => 'offers' ),
				array( 'label' => 'Teach with us', 'slug' => 'teach' ),
				array( 'label' => 'Questions', 'slug' => 'faq' ),
				array( 'label' => 'Journal', 'slug' => 'journal' ),
			),
		),
		array( 'label' => 'Contact', 'slug' => 'contact' ),
	),
);
require dirname( __DIR__ ) . '/trades.php';
