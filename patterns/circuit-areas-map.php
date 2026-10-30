<?php
/**
 * Title: Circuit areas: a map and the towns served
 * Slug: anypress/circuit-areas-map
 * Description: Where the electrician works: a map of the area beside every town served as a link to its own page, and a line on travel outside the area. Needs the AnyPress Blocks plugin for the map. Part of the Circuit kit.
 * Categories: anypress/kit-electrical
 * Keywords: service areas, map, towns, locations, coverage, electrician, circuit
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Areas served"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:columns {"verticalAlignment":"top","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|x-large","left":"var:preset|spacing|x-large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-top"><!-- wp:column {"width":"40%"} -->
<div class="wp-block-column" style="flex-basis:40%"><!-- wp:paragraph {"textColor":"primary","fontSize":"x-small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.12em","fontWeight":"700"}}} -->
<p class="has-primary-color has-text-color has-x-small-font-size" style="text-transform:uppercase;letter-spacing:0.12em;font-weight:700"><?php esc_html_e( 'Service areas', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'Across Columbus and the suburbs', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"medium"} -->
<p class="has-secondary-color has-text-color has-medium-font-size"><?php esc_html_e( 'No travel charge anywhere inside the I-270 loop and the towns around it. Further out? Call and ask.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:group {"align":"wide","style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"grid","columnCount":2,"minimumColumnWidth":"10rem"}} -->
<div class="wp-block-group alignwide"><!-- wp:paragraph {"fontSize":"medium","style":{"typography":{"fontWeight":"600"}}} -->
<p class="has-medium-font-size" style="font-weight:600"><a href="/service-areas/columbus/"><?php esc_html_e( 'Columbus', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"medium","style":{"typography":{"fontWeight":"600"}}} -->
<p class="has-medium-font-size" style="font-weight:600"><a href="/service-areas/westerville/"><?php esc_html_e( 'Westerville', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"medium","style":{"typography":{"fontWeight":"600"}}} -->
<p class="has-medium-font-size" style="font-weight:600"><a href="/service-areas/dublin/"><?php esc_html_e( 'Dublin', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"medium","style":{"typography":{"fontWeight":"600"}}} -->
<p class="has-medium-font-size" style="font-weight:600"><a href="/service-areas/worthington/"><?php esc_html_e( 'Worthington', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"medium","style":{"typography":{"fontWeight":"600"}}} -->
<p class="has-medium-font-size" style="font-weight:600"><a href="/service-areas/hilliard/"><?php esc_html_e( 'Hilliard', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"medium","style":{"typography":{"fontWeight":"600"}}} -->
<p class="has-medium-font-size" style="font-weight:600"><a href="/service-areas/grove-city/"><?php esc_html_e( 'Grove City', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"medium","style":{"typography":{"fontWeight":"600"}}} -->
<p class="has-medium-font-size" style="font-weight:600"><a href="/service-areas/gahanna/"><?php esc_html_e( 'Gahanna', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"medium","style":{"typography":{"fontWeight":"600"}}} -->
<p class="has-medium-font-size" style="font-weight:600"><a href="/service-areas/upper-arlington/"><?php esc_html_e( 'Upper Arlington', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:anypress/map {"address":"Columbus, Ohio","lat":39.9612,"lon":-82.9988,"zoom":10,"aspect":"4/3","style":{"border":{"radius":"var:preset|border-radius|lg"}}} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->
