<?php
/**
 * Builds the Ridge kit's demo: Clearwater Plumbing & Heating, a whole website for a plumbing and heating firm.
 *
 * Run inside WordPress with the AnyPress theme active, and the AnyPress Blocks and Fluent Forms plugins on. The demo's
 * blueprint does this on WordPress Playground. On a site with WP-CLI:
 *
 *     wp eval-file wp-content/themes/anypress/demo/ridge/build.php
 *
 * It replaces the site's pages, posts, menus, header, footer and global styles: run it on an empty site only.
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'ridge',
	'style'       => 'kit-ridge',
	'home'        => 'kit-home-services',
	'name'        => 'Clearwater Plumbing & Heating',
	'tagline'     => 'Plumbing and heating in Springfield since 2001',
	'timezone'    => 'America/Chicago',
	'quote'       => array( 'slug' => 'get-a-quote', 'title' => 'Get a quote', 'pattern' => 'ridge-page-quote', 'button' => 'Send my quote request' ),
	'services'    => array( 'Emergency plumbing', 'Leaks and burst pipes', 'Drain cleaning', 'Water heaters', 'Boilers and heating', 'Bathrooms and kitchens', 'Something else' ),
	'jobs'        => array( 'Service plumber', 'Heating engineer', 'Apprentice plumber' ),
	'newsletter'  => array( 'button' => 'Send me the code', 'message' => "Thanks! Your code is WELCOME50. We've emailed it to you too." ),
	'area_title'  => 'Plumber in ',
	'area_latlon' => '"lat":39.6761,"lon":-89.7043',
);
require dirname( __DIR__ ) . '/trades.php';
