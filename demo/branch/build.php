<?php
/**
 * Builds the Branch kit's demo: Bluegill Swim School, a whole website for a swim school with six pools across Texas
 * that also sells franchises, with its programmes, locations, free trial booking and franchise enquiry.
 *
 * It uses the kit's own words, so it has no copy.txt. Its photos are in photos/ with photos.json, and its programmes,
 * locations and news in services.json, towns.json and posts.json. Run it inside WordPress with the AnyPress theme
 * active and the AnyPress Blocks and Fluent Forms plugins on, on an empty site only:
 *
 *     wp eval-file wp-content/themes/anypress/demo/branch/build.php
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'branch',
	'style'       => 'kit-branch',
	'home'        => 'kit-franchise',
	'name'        => 'Bluegill Swim School',
	'tagline'     => 'Swim lessons for every age at six pools across Texas',
	'timezone'    => 'America/Chicago',
	'quote'       => array(
		'slug'    => 'book-a-trial',
		'title'   => 'Book a free trial',
		'pattern' => 'branch-page-join',
		'button'  => 'Book my free trial',
		'labels'  => array(
			'service' => 'Which class?',
			'choose'  => 'Choose a class',
			'date'    => 'Which day suits you best?',
			'address' => 'Which pool? (or your ZIP code)',
			'message' => "Your swimmer's age and anything we should know",
		),
	),
	'services'    => array( 'Little splashers', 'Preschool', 'Learn to swim', 'Swim team prep', 'Not sure yet' ),
	'jobs'        => array( 'Swim instructor', 'Front desk', 'Pool manager', 'Owning a franchise' ),
	'apply'       => array( 'title' => 'Job or franchise enquiry', 'label' => 'What are you applying for?', 'choose' => 'Choose one' ),
	'newsletter'  => array( 'button' => 'Send me the news', 'message' => 'Thank you! Your free trial code is on its way by email.' ),
	'area_title'  => 'Bluegill ',
	'area_latlon' => '"lat":30.2493,"lon":-97.781',
	'sitemap'     => array(
		'services' => array( 'programs', 'Programmes' ),
		'about'    => array( 'about', 'About us' ),
		'areas'    => array( 'locations', 'Locations' ),
		'offers'   => array( 'offers', 'Offers' ),
		'faq'      => array( 'faq', 'Questions' ),
		'careers'  => array( 'careers', 'Careers' ),
		'blog'     => array( 'news', 'News' ),
	),
	'pages'       => array(
		array( 'slug' => 'own-a-franchise', 'title' => 'Own a franchise', 'sections' => array( 'branch-page-franchise' ), 'order' => 11 ),
	),
	'menu'        => array(
		array(
			'label'    => 'Programmes',
			'slug'     => 'programs',
			'children' => array(
				array( 'label' => 'All programmes', 'slug' => 'programs' ),
				array( 'label' => 'Little splashers', 'slug' => 'little-splashers' ),
				array( 'label' => 'Preschool', 'slug' => 'preschool' ),
				array( 'label' => 'Learn to swim', 'slug' => 'learn-to-swim' ),
				array( 'label' => 'Swim team prep', 'slug' => 'swim-team-prep' ),
			),
		),
		array(
			'label'    => 'Locations',
			'slug'     => 'locations',
			'children' => array(
				array( 'label' => 'All locations', 'slug' => 'locations' ),
				array( 'label' => 'Austin, South Lamar', 'slug' => 'austin' ),
				array( 'label' => 'Round Rock', 'slug' => 'round-rock' ),
				array( 'label' => 'San Antonio', 'slug' => 'san-antonio' ),
				array( 'label' => 'Houston', 'slug' => 'houston' ),
				array( 'label' => 'Frisco', 'slug' => 'frisco' ),
				array( 'label' => 'Fort Worth', 'slug' => 'fort-worth' ),
			),
		),
		array( 'label' => 'Own a franchise', 'slug' => 'own-a-franchise' ),
		array(
			'label'    => 'About',
			'slug'     => 'about',
			'children' => array(
				array( 'label' => 'About us', 'slug' => 'about' ),
				array( 'label' => 'Reviews', 'slug' => 'reviews' ),
				array( 'label' => 'Offers', 'slug' => 'offers' ),
				array( 'label' => 'Questions', 'slug' => 'faq' ),
				array( 'label' => 'Careers', 'slug' => 'careers' ),
				array( 'label' => 'News', 'slug' => 'news' ),
			),
		),
		array( 'label' => 'Contact', 'slug' => 'contact' ),
	),
);
require dirname( __DIR__ ) . '/trades.php';
