<?php
/**
 * Builds the Circuit kit's demo: Brightline Electric, a whole website for an electrician in Columbus, Ohio.
 *
 * Run inside WordPress with the AnyPress theme active, and the AnyPress Blocks and Fluent Forms plugins on. The demo's
 * blueprint does this on WordPress Playground. On a site with WP-CLI:
 *
 *     wp eval-file wp-content/themes/anypress/demo/circuit/build.php
 *
 * It replaces the site's pages, posts, menus, header, footer and global styles: run it on an empty site only.
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'circuit',
	'style'       => 'kit-circuit',
	'home'        => 'kit-home-electrical',
	'name'        => 'Brightline Electric',
	'tagline'     => 'Electricians in Columbus since 2009',
	'timezone'    => 'America/New_York',
	'quote'       => array( 'slug' => 'book-a-visit', 'title' => 'Book a visit', 'pattern' => 'circuit-page-book', 'button' => 'Book my visit' ),
	'services'    => array( 'Repairs and fault finding', 'Panel upgrade', 'EV charger', 'Lighting', 'Rewiring', 'Generator or surge protection', 'Safety inspection', 'Something else' ),
	'jobs'        => array( 'Service electrician', 'EV and solar installer', 'Apprentice electrician' ),
	'newsletter'  => array( 'button' => 'Send it to me', 'message' => 'Thanks! The safety checklist and your code, BRIGHT40, are on their way to your inbox.' ),
	'area_title'  => 'Electrician in ',
	'area_latlon' => '"lat":40.1262,"lon":-82.9291',
);
require dirname( __DIR__ ) . '/trades.php';
