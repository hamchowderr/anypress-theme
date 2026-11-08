<?php
/**
 * Builds a Ridge demo for a handyman company: Fixwell Handyman in Orlando.
 *
 * Its words are in copy.txt (compiled to swap.json by tools/demo/copy.py), its photos in photos/ with photos.json, and
 * its services, towns and blog posts in the other JSON files. Run it on an empty site only:
 *
 *     wp eval-file wp-content/themes/anypress/demo/ridge/fixwell-handyman/build.php
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'ridge',
	'style'       => 'kit-ridge',
	'home'        => 'kit-home-services',
	'name'        => 'Fixwell Handyman',
	'tagline'     => 'Handyman repairs in Orlando since 2014',
	'timezone'    => 'America/New_York',
	'colors'      => 'ocean',
	'quote'       => array( 'slug' => 'get-a-quote', 'title' => 'Book a handyman', 'pattern' => 'ridge-page-quote', 'button' => 'Book my handyman' ),
	'services'    => array( 'Home repairs', 'Drywall', 'Carpentry', 'Painting', 'Mounting or assembly', 'Doors or windows', 'Something else' ),
	'jobs'        => array( 'Handyman', 'Carpenter', 'Office coordinator' ),
	'newsletter'  => array( 'button' => 'Send me the code', 'message' => "Thanks! Your code is FIXWELL25. We've emailed it to you too." ),
	'area_title'  => 'Handyman in ',
	'area_latlon' => '"lat":39.6761,"lon":-89.7043',
	'leftover'    => array( 'Clearwater', 'plumb', 'Springfield', 'Chatham', 'drain', 'boiler', 'water heater', 'Wabash', '48213', 'Alvarez', 'Rosa' ),
);
require dirname( __DIR__, 2 ) . '/trades.php';
