<?php
/**
 * Title: Gloss visit: the salon's address and hours, with a map
 * Slug: anypress/gloss-visit
 * Description: Where the salon is, with the address, opening hours and parking beside a map. Needs the AnyPress Blocks plugin for the map. Part of the Gloss kit.
 * Categories: anypress/kit-salon
 * Keywords: visit, location, address, hours, map, salon, gloss
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Visit"},"anchor":"visit","align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section id="visit" class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:columns {"verticalAlignment":"center","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|xx-large","left":"var:preset|spacing|xx-large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-center"><!-- wp:column {"width":"40%"} -->
<div class="wp-block-column" style="flex-basis:40%"><!-- wp:paragraph {"textColor":"secondary","fontFamily":"jost","fontSize":"small","style":{"typography":{"fontWeight":"500","letterSpacing":"0.14em","textTransform":"uppercase"}}} -->
<p class="has-secondary-color has-text-color has-jost-font-family has-small-font-size" style="font-weight:500;letter-spacing:0.14em;text-transform:uppercase"><?php esc_html_e( 'Find us', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'On Elm Street, by the park', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"metadata":{"bindings":{"content":{"source":"anypress/site-details","args":{"key":"address"}}}},"fontSize":"large"} -->
<p class="has-large-font-size"><?php esc_html_e( '21 Elm Street, Springfield, IL 62701', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><?php esc_html_e( 'Tuesday to Friday, 9am to 8pm', 'anypress' ); ?></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><?php esc_html_e( 'Saturday, 9am to 5pm', 'anypress' ); ?></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><?php esc_html_e( 'Free parking behind the salon', 'anypress' ); ?></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><?php esc_html_e( 'Step-free, with a basin that tilts back gently', 'anypress' ); ?></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:anypress/map {"address":"21 Elm Street, Springfield, IL 62701","lat":39.8003,"lon":-89.6489,"zoom":16,"aspect":"4/3"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->
