<?php
/**
 * Builds the Byline kit's demo: Field Notes, a whole website for an independent outdoor magazine in Bozeman, Montana,
 * with its stories, route guides, guided walks and print subscription.
 *
 * It uses the kit's own words, so it has no copy.txt. Its photos are in photos/ with photos.json, and its walks, route
 * guides and stories in services.json, towns.json and posts.json. Run it inside WordPress with the AnyPress theme
 * active and the AnyPress Blocks and Fluent Forms plugins on, on an empty site only:
 *
 *     wp eval-file wp-content/themes/anypress/demo/byline/build.php
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'byline',
	'style'       => 'kit-byline',
	'home'        => 'kit-magazine',
	'name'        => 'Field Notes',
	'tagline'     => 'Walking, eating and sleeping outdoors',
	'timezone'    => 'America/Denver',
	'quote'       => array(
		'slug'    => 'book-a-walk',
		'title'   => 'Book a walk',
		'pattern' => 'byline-page-join',
		'button'  => 'Book my place',
		'labels'  => array(
			'service' => 'Which walk?',
			'choose'  => 'Choose a walk',
			'date'    => 'Which date would you like?',
			'address' => 'Where are you travelling from?',
			'message' => 'Anything we should know?',
		),
	),
	'services'    => array( 'Sunrise ridge walk', 'Cabin weekend', 'Cook on the trail', 'Map and compass day', 'A private walk' ),
	'jobs'        => array( 'Contributing writer', 'Walk leader', 'A story idea' ),
	'apply'       => array( 'title' => 'Pitch or application', 'label' => 'What are you sending?', 'choose' => 'Choose one' ),
	'newsletter'  => array( 'button' => 'Send me the stories', 'message' => 'Thank you! Your first story arrives on Thursday.' ),
	'area_title'  => '',
	'area_latlon' => '"lat":45.4383,"lon":-110.9603',
	'sitemap'     => array(
		'services' => array( 'walks', 'Walks' ),
		'areas'    => array( 'routes', 'Routes' ),
		'reviews'  => array( 'readers', 'Letters' ),
		'offers'   => array( 'subscribe', 'Subscribe' ),
		'faq'      => array( 'faq', 'Questions' ),
		'careers'  => array( 'write-for-us', 'Write for us' ),
		'blog'     => array( 'stories', 'Stories' ),
	),
	'menu'        => array(
		array( 'label' => 'Stories', 'slug' => 'stories' ),
		array(
			'label'    => 'Routes',
			'slug'     => 'routes',
			'children' => array(
				array( 'label' => 'All routes', 'slug' => 'routes' ),
				array( 'label' => 'Hyalite Lake', 'slug' => 'hyalite-lake' ),
				array( 'label' => 'Lava Lake', 'slug' => 'lava-lake' ),
				array( 'label' => 'Bridger Ridge', 'slug' => 'bridger-ridge' ),
				array( 'label' => 'Sypes Canyon', 'slug' => 'sypes-canyon' ),
			),
		),
		array(
			'label'    => 'Walks',
			'slug'     => 'walks',
			'children' => array(
				array( 'label' => 'All walks', 'slug' => 'walks' ),
				array( 'label' => 'Sunrise ridge walk', 'slug' => 'sunrise-ridge-walk' ),
				array( 'label' => 'Cabin weekend', 'slug' => 'cabin-weekend' ),
				array( 'label' => 'Cook on the trail', 'slug' => 'cook-on-the-trail' ),
				array( 'label' => 'Map and compass day', 'slug' => 'map-and-compass' ),
				array( 'label' => 'Book a walk', 'slug' => 'book-a-walk' ),
			),
		),
		array(
			'label'    => 'About',
			'slug'     => 'about',
			'children' => array(
				array( 'label' => 'About Field Notes', 'slug' => 'about' ),
				array( 'label' => 'Letters', 'slug' => 'readers' ),
				array( 'label' => 'Write for us', 'slug' => 'write-for-us' ),
				array( 'label' => 'Questions', 'slug' => 'faq' ),
			),
		),
		array( 'label' => 'Contact', 'slug' => 'contact' ),
	),
);
require dirname( __DIR__ ) . '/trades.php';
