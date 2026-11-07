<?php
/**
 * Builds a Ridge demo for a house cleaning company: Spotless Nest in Raleigh.
 *
 * Its words are in copy.txt (compiled to swap.json by tools/demo/copy.py), its photos in photos/ with photos.json, and
 * its services, towns and blog posts in the other JSON files. Run it on an empty site only:
 *
 *     wp eval-file wp-content/themes/anypress/demo/ridge/spotless-nest/build.php
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'ridge',
	'style'       => 'kit-ridge',
	'home'        => 'kit-home-services',
	'name'        => 'Spotless Nest',
	'tagline'     => 'House cleaning in Raleigh since 2014',
	'timezone'    => 'America/New_York',
	'colors'      => 'rose',
	'quote'       => array( 'slug' => 'get-a-quote', 'title' => 'Get a price', 'pattern' => 'ridge-page-quote', 'button' => 'Send my request' ),
	'services'    => array( 'Regular cleaning', 'Deep cleaning', 'Move-out cleaning', 'Rental turnovers', 'Office cleaning', 'Carpet and upholstery', 'Something else' ),
	'jobs'        => array( 'House cleaner', 'Team lead', 'Scheduler' ),
	'newsletter'  => array( 'button' => 'Send me the code', 'message' => "Thanks! Your code is NEST40. We've emailed it to you too." ),
	'area_title'  => 'House cleaning in ',
	'area_latlon' => '"lat":39.6761,"lon":-89.7043',
	'leftover'    => array( 'Clearwater', 'plumb', 'Springfield', 'Chatham', 'drain', 'boiler', 'water heater', 'Wabash', '48213', 'Alvarez', 'Rosa' ),
);
require dirname( __DIR__, 2 ) . '/trades.php';
