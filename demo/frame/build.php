<?php
/**
 * Builds the Frame kit's demo: Ines Duarte, a whole website for an architectural photographer in Lisbon.
 *
 * It uses the kit's own words, so it has no copy.txt. Its photos are in photos/ with photos.json, and its services,
 * projects and journal posts in services.json, towns.json and posts.json. Run it inside WordPress with the AnyPress
 * theme active and the AnyPress Blocks and Fluent Forms plugins on, on an empty site only:
 *
 *     wp eval-file wp-content/themes/anypress/demo/frame/build.php
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'frame',
	'style'       => 'kit-frame',
	'home'        => 'kit-portfolio',
	'name'        => 'Ines Duarte',
	'tagline'     => 'Architecture and interiors photographed in Lisbon',
	'timezone'    => 'Europe/Lisbon',
	'quote'       => array(
		'slug'    => 'commission',
		'title'   => 'Commission',
		'pattern' => 'frame-page-join',
		'button'  => 'Send',
		'labels'  => array(
			'service' => 'What kind of shoot?',
			'choose'  => 'Choose a service',
			'date'    => 'When do you need the photos?',
			'address' => 'Where is the building?',
			'message' => 'Tell me about the project',
		),
	),
	'services'    => array( 'Architecture', 'Interiors', 'People and places', 'Editorial', 'A print', 'Something else' ),
	'jobs'        => array( 'Shoot assistant', 'Studio intern' ),
	'apply'       => array( 'title' => 'Assistant application', 'label' => 'Which role?', 'choose' => 'Choose a role' ),
	'newsletter'  => array( 'button' => 'Send me the code', 'message' => 'Thank you! Your 10% code is on its way by email.' ),
	'area_title'  => '',
	'area_latlon' => 'no map on these pages',
	'sitemap'     => array(
		'areas'   => array( 'work', 'Work' ),
		'reviews' => array( 'kind-words', 'Kind words' ),
		'offers'  => array( 'prints', 'Prints' ),
		'faq'     => array( 'faq', 'Questions' ),
		'careers' => array( 'assisting', 'Assisting' ),
		'blog'    => array( 'journal', 'Journal' ),
	),
	'menu'        => array(
		array(
			'label'    => 'Work',
			'slug'     => 'work',
			'children' => array(
				array( 'label' => 'All work', 'slug' => 'work' ),
				array( 'label' => 'Casa Moreira', 'slug' => 'casa-moreira' ),
				array( 'label' => 'Azul', 'slug' => 'azul' ),
				array( 'label' => 'Marvila studios', 'slug' => 'marvila-studios' ),
				array( 'label' => 'Tower One', 'slug' => 'tower-one' ),
				array( 'label' => 'Mercado Novo', 'slug' => 'mercado-novo' ),
			),
		),
		array(
			'label'    => 'Services',
			'slug'     => 'services',
			'children' => array(
				array( 'label' => 'All services', 'slug' => 'services' ),
				array( 'label' => 'Architecture', 'slug' => 'architecture' ),
				array( 'label' => 'Interiors', 'slug' => 'interiors' ),
				array( 'label' => 'People and places', 'slug' => 'people-and-places' ),
				array( 'label' => 'Editorial', 'slug' => 'editorial' ),
			),
		),
		array( 'label' => 'Prints', 'slug' => 'prints' ),
		array(
			'label'    => 'About',
			'slug'     => 'about',
			'children' => array(
				array( 'label' => 'About me', 'slug' => 'about' ),
				array( 'label' => 'Kind words', 'slug' => 'kind-words' ),
				array( 'label' => 'Assisting', 'slug' => 'assisting' ),
				array( 'label' => 'Questions', 'slug' => 'faq' ),
				array( 'label' => 'Journal', 'slug' => 'journal' ),
			),
		),
		array( 'label' => 'Contact', 'slug' => 'contact' ),
	),
);
require dirname( __DIR__ ) . '/trades.php';
