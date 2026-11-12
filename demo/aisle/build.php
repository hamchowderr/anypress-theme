<?php
/**
 * Builds the Aisle kit's demo: Thread & Co., a whole online clothing shop on FluentCart.
 *
 * It uses the kit's own words, so it has no copy.txt. Its photos are in photos/ with photos.json, its journal posts
 * in posts.json and its catalogue (products, prices, categories, reviews, coupons, shipping and tax) in shop.json.
 * Run it inside WordPress with the AnyPress theme active and the AnyPress Blocks, Fluent Forms and FluentCart plugins
 * on, on an empty site only:
 *
 *     wp eval-file wp-content/themes/anypress/demo/aisle/build.php
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'        => __DIR__,
	'prefix'     => 'aisle',
	'style'      => 'kit-aisle',
	'home'       => 'kit-store',
	'name'       => 'Thread & Co.',
	'tagline'    => 'Everyday clothes, made to last',
	'timezone'   => 'America/Los_Angeles',
	'newsletter' => array( 'button' => 'Get 10% off', 'message' => 'Thanks! Your 10% code is on its way by email.' ),
	'topics'     => array( 'An order I placed', 'A return or exchange', 'Sizing and fit', 'A repair', 'Gift cards', 'The Sock club', 'Something else' ),
	'blog'       => array( 'journal', 'Journal' ),
	'pages'      => array(
		array( 'new-in', 'New in', 'aisle-page-new-in' ),
		array( 'lookbook', 'Lookbook', 'aisle-page-lookbook' ),
		array( 'gift-cards', 'Gift cards', 'aisle-page-gift-cards' ),
		array( 'help', 'Help', 'aisle-page-help' ),
		array( 'shipping', 'Shipping', 'aisle-page-shipping', 'help' ),
		array( 'returns', 'Returns and exchanges', 'aisle-page-returns', 'help' ),
		array( 'size-guide', 'Size guide', 'aisle-page-size-guide', 'help' ),
		array( 'track-order', 'Track an order', 'aisle-page-track-order', 'help' ),
		array( 'faq', 'Questions', 'aisle-page-faq', 'help' ),
		array( 'contact', 'Contact us', 'aisle-page-contact', 'help' ),
		array( 'withdraw-from-contract', 'Cancel an order', 'aisle-page-cancel' ),
		array( 'our-story', 'Our story', 'aisle-page-about' ),
		array( 'reviews', 'Reviews', 'aisle-page-reviews' ),
	),
);

$anypress_cat = fn( $label, $slug ) => array( 'label' => $label, 'slug' => home_url( "/product-categories/$slug/" ) );

$anypress_kit['menu'] = array(
	array(
		'label'    => 'Shop',
		'slug'     => 'shop',
		'children' => array(
			array( 'label' => 'Everything', 'slug' => 'shop' ),
			$anypress_cat( 'Tops', 'tops' ),
			$anypress_cat( 'Bottoms', 'bottoms' ),
			$anypress_cat( 'Outerwear', 'outerwear' ),
			$anypress_cat( 'Accessories', 'accessories' ),
			$anypress_cat( 'Last few', 'last-few' ),
			array( 'label' => 'Gift cards', 'slug' => 'gift-cards' ),
		),
	),
	array( 'label' => 'New in', 'slug' => 'new-in' ),
	array( 'label' => 'Lookbook', 'slug' => 'lookbook' ),
	array(
		'label'    => 'About',
		'slug'     => 'our-story',
		'children' => array(
			array( 'label' => 'Our story', 'slug' => 'our-story' ),
			array( 'label' => 'Reviews', 'slug' => 'reviews' ),
			array( 'label' => 'Journal', 'slug' => 'journal' ),
		),
	),
	array(
		'label'    => 'Help',
		'slug'     => 'help',
		'children' => array(
			array( 'label' => 'Help centre', 'slug' => 'help' ),
			array( 'label' => 'Shipping', 'slug' => 'shipping' ),
			array( 'label' => 'Returns and exchanges', 'slug' => 'returns' ),
			array( 'label' => 'Size guide', 'slug' => 'size-guide' ),
			array( 'label' => 'Track an order', 'slug' => 'track-order' ),
			array( 'label' => 'Questions', 'slug' => 'faq' ),
			array( 'label' => 'Contact us', 'slug' => 'contact' ),
			array( 'label' => 'Cancel an order (EU)', 'slug' => 'withdraw-from-contract' ),
		),
	),
);
require dirname( __DIR__ ) . '/shop.php';
