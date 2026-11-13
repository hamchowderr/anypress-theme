<?php
/**
 * Builds the Launch kit's demo: Tally, a whole website for an invoicing app for freelancers and small studios.
 *
 * It uses the kit's own words, so it has no copy.txt. Its photos are in photos/ with photos.json, and its features,
 * audience pages and blog posts in services.json, towns.json and posts.json. Run it inside WordPress with the
 * AnyPress theme active and the AnyPress Blocks and Fluent Forms plugins on, on an empty site only:
 *
 *     wp eval-file wp-content/themes/anypress/demo/launch/build.php
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'launch',
	'style'       => 'kit-launch',
	'home'        => 'kit-software',
	'name'        => 'Tally',
	'tagline'     => 'Invoicing for freelancers and small studios',
	'timezone'    => 'Europe/Lisbon',
	'quote'       => array(
		'slug'    => 'demo',
		'title'   => 'Book a demo',
		'pattern' => 'launch-page-join',
		'button'  => 'Book my demo',
		'labels'  => array(
			'service' => 'What would you like to see?',
			'choose'  => 'Choose one',
			'date'    => 'Best day for a call',
			'address' => 'Company or studio',
			'message' => 'Anything we should know?',
		),
	),
	'services'    => array( 'A full tour', 'Invoices and reminders', 'Payments', 'Tax', 'Bank matching', 'Moving from another tool', 'Team plan' ),
	'jobs'        => array( 'Senior product engineer', 'Customer support lead', 'Product designer' ),
	'apply'       => array( 'title' => 'Job application', 'label' => 'Which role?', 'choose' => 'Choose a role' ),
	'newsletter'  => array( 'button' => 'Subscribe', 'message' => "You're subscribed. The next issue arrives on the first Tuesday of the month." ),
	'area_title'  => '',
	'area_latlon' => 'no map on these pages',
	'sitemap'     => array(
		'services' => array( 'features', 'Features' ),
		'reviews'  => array( 'customers', 'Customer stories' ),
		'areas'    => array( 'for', "Who it's for" ),
		'offers'   => array( 'pricing', 'Pricing' ),
	),
	'pages'       => array(
		array( 'slug' => 'integrations', 'title' => 'Integrations', 'sections' => array( 'launch-page-integrations' ), 'order' => 11 ),
		array( 'slug' => 'changelog', 'title' => "What's new", 'sections' => array( 'launch-page-changelog' ), 'order' => 12 ),
	),
	'menu'        => array(
		array(
			'label'    => 'Features',
			'slug'     => 'features',
			'children' => array(
				array( 'label' => 'All features', 'slug' => 'features' ),
				array( 'label' => 'Invoices', 'slug' => 'invoices' ),
				array( 'label' => 'Reminders', 'slug' => 'reminders' ),
				array( 'label' => 'Payments', 'slug' => 'payments' ),
				array( 'label' => 'Tax', 'slug' => 'tax' ),
				array( 'label' => 'Bank matching', 'slug' => 'bank-matching' ),
				array( 'label' => 'For accountants', 'slug' => 'accountants' ),
				array( 'label' => 'Integrations', 'slug' => 'integrations' ),
			),
		),
		array(
			'label'    => "Who it's for",
			'slug'     => 'for',
			'children' => array(
				array( 'label' => 'Designers', 'slug' => 'designers' ),
				array( 'label' => 'Developers', 'slug' => 'developers' ),
				array( 'label' => 'Photographers', 'slug' => 'photographers' ),
				array( 'label' => 'Writers', 'slug' => 'writers' ),
				array( 'label' => 'Consultants', 'slug' => 'consultants' ),
				array( 'label' => 'Small studios', 'slug' => 'studios' ),
			),
		),
		array( 'label' => 'Pricing', 'slug' => 'pricing' ),
		array( 'label' => 'Customers', 'slug' => 'customers' ),
		array(
			'label'    => 'Company',
			'slug'     => 'about',
			'children' => array(
				array( 'label' => 'About', 'slug' => 'about' ),
				array( 'label' => "What's new", 'slug' => 'changelog' ),
				array( 'label' => 'Careers', 'slug' => 'careers' ),
				array( 'label' => 'Blog', 'slug' => 'blog' ),
				array( 'label' => 'Questions', 'slug' => 'faq' ),
				array( 'label' => 'Contact', 'slug' => 'contact' ),
			),
		),
	),
);
require dirname( __DIR__ ) . '/trades.php';
