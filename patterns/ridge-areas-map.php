<?php
/**
 * Title: Ridge areas: a map and the towns served
 * Slug: anypress/ridge-areas-map
 * Description: Where the business works: a map of the area and every town served as a link to its own page, with a line on travel outside the area. Needs the AnyPress Blocks plugin for the map. Part of the Ridge kit.
 * Categories: anypress/kit-home-services
 * Keywords: service areas, map, towns, locations, coverage, ridge
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Areas served"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:columns {"verticalAlignment":"top","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|x-large","left":"var:preset|spacing|x-large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-top"><!-- wp:column {"width":"36%"} -->
<div class="wp-block-column" style="flex-basis:36%"><!-- wp:heading {"fontSize":"xxx-large"} -->
<h2 class="wp-block-heading has-xxx-large-font-size"><?php esc_html_e( 'Where we work', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"medium"} -->
<p class="has-secondary-color has-text-color has-medium-font-size"><?php esc_html_e( 'Every town within 25 miles of Springfield, with no travel charge. Outside that, call and ask: we often say yes.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:list {"className":"is-style-no-bullets","fontFamily":"big-shoulders","fontSize":"x-large","style":{"typography":{"lineHeight":"1.15","textTransform":"uppercase","fontWeight":"800"}}} -->
<ul class="wp-block-list is-style-no-bullets has-big-shoulders-font-family has-x-large-font-size" style="line-height:1.15;text-transform:uppercase;font-weight:800"><!-- wp:list-item -->
<li><a href="/service-areas/springfield/"><?php esc_html_e( 'Springfield', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/service-areas/chatham/"><?php esc_html_e( 'Chatham', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/service-areas/rochester/"><?php esc_html_e( 'Rochester', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/service-areas/sherman/"><?php esc_html_e( 'Sherman', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/service-areas/riverton/"><?php esc_html_e( 'Riverton', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/service-areas/auburn/"><?php esc_html_e( 'Auburn', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/service-areas/petersburg/"><?php esc_html_e( 'Petersburg', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/service-areas/new-berlin/"><?php esc_html_e( 'New Berlin', 'anypress' ); ?></a></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:anypress/map {"address":"Springfield, Illinois","lat":39.7817,"lon":-89.6501,"zoom":10,"aspect":"4/3"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->
