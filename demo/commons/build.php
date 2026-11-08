<?php
/**
 * Builds the Commons kit's demo: the Springfield Chamber of Commerce, a whole website for a chamber of commerce.
 *
 * It uses the kit's own words, so it has no copy.txt. Its photos are in photos/ with photos.json, and its programs,
 * directory categories and news posts in services.json, towns.json and posts.json. Run it inside WordPress with the
 * AnyPress theme active and the AnyPress Blocks and Fluent Forms plugins on, on an empty site only:
 *
 *     wp eval-file wp-content/themes/anypress/demo/commons/build.php
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'commons',
	'style'       => 'kit-commons',
	'home'        => 'kit-community',
	'name'        => 'Springfield Chamber of Commerce',
	'tagline'     => 'Speaking up for Springfield business since 1930',
	'timezone'    => 'America/Chicago',
	'quote'       => array(
		'slug'    => 'join',
		'title'   => 'Join the chamber',
		'pattern' => 'commons-page-join',
		'button'  => 'Send my application',
		'labels'  => array(
			'service' => 'Membership level',
			'choose'  => 'Choose a level',
			'date'    => false,
			'address' => 'Business name',
			'message' => 'Tell us about your business',
		),
	),
	'services'    => array( 'Individual ($60 a year)', 'Small business ($240 a year)', 'Corporate ($900 a year)', 'Not sure yet' ),
	'jobs'        => array( 'Event helper', 'Business mentor', 'Committee member' ),
	'apply'       => array( 'title' => 'Volunteer sign-up', 'label' => 'Which role?', 'choose' => 'Choose a role' ),
	'newsletter'  => array( 'button' => 'Sign me up', 'message' => "Thanks! You're on the list. The next email comes on Monday." ),
	'area_title'  => '',
	'area_latlon' => '"lat":39.8017,"lon":-89.6436',
	'sitemap'     => array(
		'services' => array( 'programs', 'Programs' ),
		'reviews'  => array( 'member-stories', 'Member stories' ),
		'areas'    => array( 'directory', 'Member directory' ),
		'offers'   => array( 'member-deals', 'Member deals' ),
		'careers'  => array( 'volunteer', 'Volunteer' ),
		'blog'     => array( 'news', 'News' ),
	),
	'pages'       => array(
		array( 'slug' => 'events', 'title' => 'Events', 'sections' => array( 'commons-page-events' ), 'order' => 1 ),
	),
	'menu'        => array(
		array( 'label' => 'Events', 'slug' => 'events' ),
		array(
			'label'    => 'Programs',
			'slug'     => 'programs',
			'children' => array(
				array( 'label' => 'All programs', 'slug' => 'programs' ),
				array( 'label' => 'Business breakfasts', 'slug' => 'business-breakfasts' ),
				array( 'label' => 'Mentoring', 'slug' => 'mentoring' ),
				array( 'label' => 'Leadership Springfield', 'slug' => 'leadership' ),
				array( 'label' => 'Workshops', 'slug' => 'workshops' ),
				array( 'label' => 'Speaking up for business', 'slug' => 'advocacy' ),
				array( 'label' => 'Young professionals', 'slug' => 'young-professionals' ),
			),
		),
		array( 'label' => 'Directory', 'slug' => 'directory' ),
		array(
			'label'    => 'About',
			'slug'     => 'about',
			'children' => array(
				array( 'label' => 'About us', 'slug' => 'about' ),
				array( 'label' => 'Member stories', 'slug' => 'member-stories' ),
				array( 'label' => 'Member deals', 'slug' => 'member-deals' ),
				array( 'label' => 'Volunteer', 'slug' => 'volunteer' ),
				array( 'label' => 'Questions', 'slug' => 'faq' ),
				array( 'label' => 'News', 'slug' => 'news' ),
			),
		),
		array( 'label' => 'Contact', 'slug' => 'contact' ),
	),
);
require dirname( __DIR__ ) . '/trades.php';
