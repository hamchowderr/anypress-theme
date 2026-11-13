<?php
/**
 * Builds the Assay kit's demo: Tessel Health, a whole website for a doctor-led peptide therapy shop in Scottsdale,
 * Arizona, with its treatments, lab results, the states it treats in and its pricing.
 *
 * It uses the kit's own words, so it has no copy.txt. Its photos are in photos/ with photos.json, and its treatments,
 * states and articles in services.json, towns.json and posts.json. Run it inside WordPress with the AnyPress theme
 * active and the AnyPress Blocks and Fluent Forms plugins on, on an empty site only:
 *
 *     wp eval-file wp-content/themes/anypress/demo/assay/build.php
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'assay',
	'style'       => 'kit-assay',
	'home'        => 'kit-regulated',
	'name'        => 'Tessel Health',
	'tagline'     => 'Peptides prescribed by a doctor and tested by a lab',
	'timezone'    => 'America/Phoenix',
	'quote'       => array(
		'slug'    => 'get-started',
		'title'   => 'Start your consultation',
		'pattern' => 'assay-page-join',
		'button'  => 'Request my consultation',
		'labels'  => array(
			'service' => 'Which treatment are you curious about?',
			'choose'  => 'Choose one',
			'date'    => 'When would suit you for a video visit?',
			'address' => 'Which state do you live in?',
			'message' => 'Anything we should know? (No health details yet, please)',
		),
	),
	'services'    => array( 'NAD+', 'Sermorelin', 'Glutathione', 'Copper peptide serum', 'Not sure yet' ),
	'jobs'        => array( 'Nurse practitioner', 'Registered nurse, care team', 'Patient support' ),
	'apply'       => array( 'title' => 'Job application', 'label' => 'Which role?', 'choose' => 'Choose a role' ),
	'newsletter'  => array( 'button' => 'Send me the code', 'message' => 'Thank you! Your $50 code is on its way by email.' ),
	'area_title'  => 'Peptide therapy in ',
	'area_latlon' => '"lat":33.4484,"lon":-112.074',
	'sitemap'     => array(
		'services' => array( 'treatments', 'Treatments' ),
		'about'    => array( 'about', 'About us' ),
		'areas'    => array( 'states', 'Where we treat' ),
		'offers'   => array( 'pricing', 'Pricing' ),
		'faq'      => array( 'faq', 'Questions' ),
		'careers'  => array( 'careers', 'Careers' ),
		'blog'     => array( 'learn', 'Learn' ),
	),
	'pages'       => array(
		array( 'slug' => 'lab-results', 'title' => 'Lab results', 'sections' => array( 'assay-page-results' ), 'order' => 11 ),
		array( 'slug' => 'how-it-works', 'title' => 'How it works', 'sections' => array( 'assay-page-how' ), 'order' => 12 ),
	),
	'menu'        => array(
		array(
			'label'    => 'Treatments',
			'slug'     => 'treatments',
			'children' => array(
				array( 'label' => 'All treatments', 'slug' => 'treatments' ),
				array( 'label' => 'NAD+', 'slug' => 'nad-plus' ),
				array( 'label' => 'Sermorelin', 'slug' => 'sermorelin' ),
				array( 'label' => 'Glutathione', 'slug' => 'glutathione' ),
				array( 'label' => 'Copper peptide serum', 'slug' => 'copper-peptide-serum' ),
			),
		),
		array( 'label' => 'How it works', 'slug' => 'how-it-works' ),
		array( 'label' => 'Lab results', 'slug' => 'lab-results' ),
		array( 'label' => 'Pricing', 'slug' => 'pricing' ),
		array(
			'label'    => 'About',
			'slug'     => 'about',
			'children' => array(
				array( 'label' => 'About us', 'slug' => 'about' ),
				array( 'label' => 'Reviews', 'slug' => 'reviews' ),
				array( 'label' => 'Where we treat', 'slug' => 'states' ),
				array( 'label' => 'Questions', 'slug' => 'faq' ),
				array( 'label' => 'Learn', 'slug' => 'learn' ),
				array( 'label' => 'Careers', 'slug' => 'careers' ),
			),
		),
		array( 'label' => 'Contact', 'slug' => 'contact' ),
	),
);
require dirname( __DIR__ ) . '/trades.php';
