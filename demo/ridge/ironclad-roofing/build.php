<?php
/**
 * Builds a Ridge demo for a roofing company: Ironclad Roofing in Oklahoma City.
 *
 * Its words are in copy.txt (compiled to swap.json by tools/demo/copy.py), its photos in photos/ with photos.json, and
 * its services, towns and blog posts in the other JSON files. Run it on an empty site only:
 *
 *     wp eval-file wp-content/themes/anypress/demo/ridge/ironclad-roofing/build.php
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'ridge',
	'style'       => 'kit-ridge',
	'home'        => 'kit-home-services',
	'name'        => 'Ironclad Roofing',
	'tagline'     => 'Roofers in Oklahoma City since 2006',
	'timezone'    => 'America/Chicago',
	'colors'      => 'charcoal-gold',
	'quote'       => array( 'slug' => 'get-a-quote', 'title' => 'Book a free inspection', 'pattern' => 'ridge-page-quote', 'button' => 'Book my free inspection' ),
	'services'    => array( 'Storm or hail damage', 'Roof replacement', 'Roof repair or leak', 'Metal roof', 'Emergency tarping', 'Gutters and downspouts', 'Insurance claim help', 'Something else' ),
	'jobs'        => array( 'Roofer', 'Crew lead', 'Claims assistant' ),
	'newsletter'  => array( 'button' => 'Send me the code', 'message' => "Thanks! Your code is IRONCLAD500. We've emailed it to you too." ),
	'area_title'  => 'Roofer in ',
	'area_latlon' => '"lat":39.6761,"lon":-89.7043',
	'leftover'    => array( 'Clearwater', 'plumb', 'Springfield', 'Chatham', 'drain', 'boiler', 'water heater', 'Wabash', '48213', 'Alvarez', 'Rosa' ),
);
require dirname( __DIR__, 2 ) . '/trades.php';
