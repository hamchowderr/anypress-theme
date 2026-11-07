<?php
/**
 * Builds a Ridge demo for a landscaping company: Greenline Landscaping in Nashville.
 *
 * Its words are in copy.txt (compiled to swap.json by tools/demo/copy.py), its photos in photos/ with photos.json, and
 * its services, towns and blog posts in the other JSON files. Run it on an empty site only:
 *
 *     wp eval-file wp-content/themes/anypress/demo/ridge/greenline-landscaping/build.php
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'ridge',
	'style'       => 'kit-ridge',
	'home'        => 'kit-home-services',
	'name'        => 'Greenline Landscaping',
	'tagline'     => 'Landscaping in Nashville since 2009',
	'timezone'    => 'America/Chicago',
	'colors'      => 'forest',
	'quote'       => array( 'slug' => 'get-a-quote', 'title' => 'Get a free estimate', 'pattern' => 'ridge-page-quote', 'button' => 'Book my free estimate' ),
	'services'    => array( 'Lawn care', 'Landscape design', 'Patio or walkway', 'Tree and shrub care', 'Irrigation', 'Seasonal cleanup', 'Something else' ),
	'jobs'        => array( 'Crew member', 'Crew lead', 'Hardscape installer' ),
	'newsletter'  => array( 'button' => 'Send me the code', 'message' => "Thanks! Your code is FIRSTMOW. We've emailed it to you too." ),
	'area_title'  => 'Landscaping in ',
	'area_latlon' => '"lat":39.6761,"lon":-89.7043',
	'leftover'    => array( 'Clearwater', 'plumb', 'Springfield', 'Chatham', 'drain', 'boiler', 'water heater', 'Wabash', '48213', 'Alvarez', 'Rosa' ),
);
require dirname( __DIR__, 2 ) . '/trades.php';
