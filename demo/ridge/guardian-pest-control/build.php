<?php
/**
 * Builds a Ridge demo for a pest control company: Guardian Pest Control in Houston.
 *
 * Its words are in copy.txt (compiled to swap.json by tools/demo/copy.py), its photos in photos/ with photos.json, and
 * its services, towns and blog posts in the other JSON files. Run it on an empty site only:
 *
 *     wp eval-file wp-content/themes/anypress/demo/ridge/guardian-pest-control/build.php
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'ridge',
	'style'       => 'kit-ridge',
	'home'        => 'kit-home-services',
	'name'        => 'Guardian Pest Control',
	'tagline'     => 'Pest control in Houston since 2011',
	'timezone'    => 'America/Chicago',
	'colors'      => 'night',
	'quote'       => array( 'slug' => 'get-a-quote', 'title' => 'Book an inspection', 'pattern' => 'ridge-page-quote', 'button' => 'Book my inspection' ),
	'services'    => array( 'General pest control', 'Termites', 'Mice or rats', 'Mosquitoes', 'Bed bugs', 'Wasps or bees', 'Something else' ),
	'jobs'        => array( 'Pest technician', 'Termite technician', 'Customer care rep' ),
	'newsletter'  => array( 'button' => 'Send me the code', 'message' => "Thanks! Your code is GUARDIAN50. We've emailed it to you too." ),
	'area_title'  => 'Pest control in ',
	'area_latlon' => '"lat":39.6761,"lon":-89.7043',
	'leftover'    => array( 'Clearwater', 'plumb', 'Springfield', 'Chatham', 'drain', 'boiler', 'water heater', 'Wabash', '48213', 'Alvarez', 'Rosa' ),
);
require dirname( __DIR__, 2 ) . '/trades.php';
