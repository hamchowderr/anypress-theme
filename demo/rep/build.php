<?php
/**
 * Builds the Rep kit's demo: Ironside Gym, a whole website for a small coached gym with four coaches.
 *
 * It uses the kit's own words, so it has no copy.txt. Its photos are in photos/ with photos.json, and its classes,
 * coaches and blog posts in services.json, towns.json and posts.json. Run it inside WordPress with the AnyPress
 * theme active and the AnyPress Blocks and Fluent Forms plugins on, on an empty site only:
 *
 *     wp eval-file wp-content/themes/anypress/demo/rep/build.php
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'rep',
	'style'       => 'kit-rep',
	'home'        => 'kit-fitness',
	'name'        => 'Ironside',
	'tagline'     => 'Coached strength, conditioning and boxing in Portland',
	'timezone'    => 'America/Los_Angeles',
	'quote'       => array(
		'slug'    => 'trial',
		'title'   => 'Try a week free',
		'pattern' => 'rep-page-join',
		'button'  => 'Claim my free week',
		'labels'  => array(
			'service' => 'Which class would you like to try first?',
			'choose'  => 'Choose a class',
			'date'    => 'When would you like to start?',
			'address' => 'Any injuries we should know about?',
			'message' => 'Anything else? Your goals, what you have done before',
		),
	),
	'services'    => array( 'Strength', 'Conditioning', 'Boxing', 'Mobility', 'Personal training', 'Not sure yet' ),
	'jobs'        => array( 'Strength coach', "Kids' coach", 'Front desk' ),
	'apply'       => array( 'title' => 'Job application', 'label' => 'Which role?', 'choose' => 'Choose a role' ),
	'newsletter'  => array( 'button' => 'Send me the pass', 'message' => 'Thank you! Your free week pass is on its way by email.' ),
	'area_title'  => '',
	'area_latlon' => 'no map on these pages',
	'sitemap'     => array(
		'services' => array( 'classes', 'Classes' ),
		'areas'    => array( 'coaches', 'Coaches' ),
		'about'    => array( 'about', 'About the gym' ),
		'offers'   => array( 'memberships', 'Memberships' ),
		'faq'      => array( 'faq', 'Questions' ),
		'blog'     => array( 'blog', 'Blog' ),
	),
	'pages'       => array(
		array( 'slug' => 'timetable', 'title' => 'Timetable', 'sections' => array( 'rep-page-timetable' ), 'order' => 2 ),
	),
	'menu'        => array(
		array(
			'label'    => 'Classes',
			'slug'     => 'classes',
			'children' => array(
				array( 'label' => 'All classes', 'slug' => 'classes' ),
				array( 'label' => 'Strength', 'slug' => 'strength' ),
				array( 'label' => 'Conditioning', 'slug' => 'conditioning' ),
				array( 'label' => 'Boxing', 'slug' => 'boxing' ),
				array( 'label' => 'Mobility', 'slug' => 'mobility' ),
				array( 'label' => 'Personal training', 'slug' => 'personal-training' ),
			),
		),
		array( 'label' => 'Timetable', 'slug' => 'timetable' ),
		array( 'label' => 'Memberships', 'slug' => 'memberships' ),
		array(
			'label'    => 'Coaches',
			'slug'     => 'coaches',
			'children' => array(
				array( 'label' => 'All coaches', 'slug' => 'coaches' ),
				array( 'label' => 'Marcus', 'slug' => 'marcus' ),
				array( 'label' => 'Priya', 'slug' => 'priya' ),
				array( 'label' => 'Dee', 'slug' => 'dee' ),
				array( 'label' => 'Tom', 'slug' => 'tom' ),
			),
		),
		array(
			'label'    => 'About',
			'slug'     => 'about',
			'children' => array(
				array( 'label' => 'About the gym', 'slug' => 'about' ),
				array( 'label' => 'Reviews', 'slug' => 'reviews' ),
				array( 'label' => 'Careers', 'slug' => 'careers' ),
				array( 'label' => 'Questions', 'slug' => 'faq' ),
				array( 'label' => 'Blog', 'slug' => 'blog' ),
				array( 'label' => 'Contact', 'slug' => 'contact' ),
			),
		),
	),
);
require dirname( __DIR__ ) . '/trades.php';
