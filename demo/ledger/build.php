<?php
/**
 * Builds the Ledger kit's demo: Hartley Shaw, a whole website for a small firm of accountants.
 *
 * It uses the kit's own words, so it has no copy.txt. Its photos are in photos/ with photos.json, and its services,
 * industries and insights posts in services.json, towns.json and posts.json. Run it inside WordPress with the AnyPress
 * theme active and the AnyPress Blocks and Fluent Forms plugins on, on an empty site only:
 *
 *     wp eval-file wp-content/themes/anypress/demo/ledger/build.php
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'ledger',
	'style'       => 'kit-ledger',
	'home'        => 'kit-professional',
	'name'        => 'Hartley Shaw',
	'tagline'     => 'Accounts, tax and payroll for small firms in Leeds',
	'timezone'    => 'Europe/London',
	'quote'       => array(
		'slug'    => 'book-a-call',
		'title'   => 'Book a free call',
		'pattern' => 'ledger-page-join',
		'button'  => 'Book my call',
		'labels'  => array(
			'service' => 'What do you need help with?',
			'choose'  => 'Choose one',
			'date'    => 'A good day for a call',
			'address' => 'Business name',
			'message' => 'Tell us about your business',
		),
	),
	'services'    => array( 'Year-end accounts', 'Bookkeeping and VAT', 'Payroll', 'A personal tax return', 'Business advice', 'Starting a business', 'All of it' ),
	'jobs'        => array( 'Trainee accountant', 'Payroll administrator', 'Senior accountant' ),
	'apply'       => array( 'title' => 'Job application', 'label' => 'Which role?', 'choose' => 'Choose a role' ),
	'newsletter'  => array( 'button' => 'Send me the dates', 'message' => "Thanks. You'll get the next email at the start of the month." ),
	'area_title'  => 'Accountants for ',
	'area_latlon' => 'no map on these pages',
	'sitemap'     => array(
		'reviews' => array( 'clients', 'Client stories' ),
		'areas'   => array( 'industries', 'Who we help' ),
		'offers'  => array( 'fees', 'Fees' ),
		'blog'    => array( 'insights', 'Insights' ),
	),
	'pages'       => array(
		array( 'slug' => 'team', 'title' => 'Our team', 'sections' => array( 'ledger-page-team' ), 'order' => 2 ),
	),
	'menu'        => array(
		array(
			'label'    => 'Services',
			'slug'     => 'services',
			'children' => array(
				array( 'label' => 'All services', 'slug' => 'services' ),
				array( 'label' => 'Year-end accounts', 'slug' => 'year-end-accounts' ),
				array( 'label' => 'Bookkeeping and VAT', 'slug' => 'bookkeeping-and-vat' ),
				array( 'label' => 'Payroll', 'slug' => 'payroll' ),
				array( 'label' => 'Personal tax returns', 'slug' => 'personal-tax' ),
				array( 'label' => 'Business advice', 'slug' => 'business-advice' ),
				array( 'label' => 'Starting a business', 'slug' => 'starting-a-business' ),
			),
		),
		array(
			'label'    => 'Who we help',
			'slug'     => 'industries',
			'children' => array(
				array( 'label' => 'Dentists', 'slug' => 'dentists' ),
				array( 'label' => 'Builders and trades', 'slug' => 'builders' ),
				array( 'label' => 'Restaurants and cafés', 'slug' => 'restaurants' ),
				array( 'label' => 'Creative agencies', 'slug' => 'creative-agencies' ),
			),
		),
		array( 'label' => 'Fees', 'slug' => 'fees' ),
		array(
			'label'    => 'About',
			'slug'     => 'about',
			'children' => array(
				array( 'label' => 'About the firm', 'slug' => 'about' ),
				array( 'label' => 'Our team', 'slug' => 'team' ),
				array( 'label' => 'Client stories', 'slug' => 'clients' ),
				array( 'label' => 'Careers', 'slug' => 'careers' ),
				array( 'label' => 'Questions', 'slug' => 'faq' ),
				array( 'label' => 'Insights', 'slug' => 'insights' ),
			),
		),
		array( 'label' => 'Contact', 'slug' => 'contact' ),
	),
);
require dirname( __DIR__ ) . '/trades.php';
