<?php
/**
 * Builds a Circuit demo for a car repair shop: Main Street Auto Care in Boise.
 *
 * Its words are in copy.txt (compiled to swap.json by tools/demo/copy.py), its photos in photos/ with photos.json, and
 * its services, towns and blog posts in the other JSON files. Run it on an empty site only:
 *
 *     wp eval-file wp-content/themes/anypress/demo/circuit/main-street-auto/build.php
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

$anypress_kit = array(
	'dir'         => __DIR__,
	'prefix'      => 'circuit',
	'style'       => 'kit-circuit',
	'home'        => 'kit-home-electrical',
	'name'        => 'Main Street Auto Care',
	'tagline'     => 'Auto repair in Boise since 2006',
	'timezone'    => 'America/Boise',
	'colors'      => 'charcoal-gold',
	'quote'       => array( 'slug' => 'book-a-visit', 'title' => 'Book a service', 'pattern' => 'circuit-page-book', 'button' => 'Book my service' ),
	'services'    => array( 'Oil change or service', 'Brakes', 'Tires or alignment', 'Check engine light', 'AC or heating', 'Battery or starting', 'Something else' ),
	'jobs'        => array( 'Automotive technician', 'Tire and alignment tech', 'Apprentice technician' ),
	'newsletter'  => array( 'button' => 'Send it to me', 'message' => 'Thanks! The car care checklist and your code, MAINST30, are on their way to your inbox.' ),
	'area_title'  => 'Auto repair in ',
	'area_latlon' => '"lat":40.1262,"lon":-82.9291',
	'leftover'    => array( 'Brightline', 'Columbus', 'Westerville', 'Worthington', 'Gahanna', 'Hilliard', 'Upper Arlington', 'Grove City', 'King Avenue', '47215', 'BRIGHT40', 'Ana Ruiz', 'electrician', 'breaker', '555 0187', 'panel', 'EV charger', 'outlet', 'Ohio', 'solar' ),
);
require dirname( __DIR__, 2 ) . '/trades.php';
