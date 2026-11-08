<?php
/**
 * Title: Branch map: where the locations are
 * Slug: anypress/branch-map
 * Description: The locations as a list of links beside a map of the area they cover, with a line on what's the same at every one. Needs the AnyPress Blocks plugin for the map. Part of the Branch kit.
 * Categories: anypress/kit-franchise
 * Keywords: locations, map, find a location, branches, franchise, branch
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Map"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:columns {"verticalAlignment":"center","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|xx-large","left":"var:preset|spacing|xx-large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-center"><!-- wp:column {"width":"40%"} -->
<div class="wp-block-column" style="flex-basis:40%"><!-- wp:paragraph {"textColor":"primary","fontSize":"small","style":{"typography":{"fontWeight":"700","letterSpacing":"0.04em","textTransform":"uppercase"}}} -->
<p class="has-primary-color has-text-color has-small-font-size" style="font-weight:700;letter-spacing:0.04em;text-transform:uppercase"><?php esc_html_e( 'Locations', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'A pool near you', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"medium"} -->
<p class="has-medium-font-size"><?php esc_html_e( 'Book at any pool and swim at all of them: your level, your lessons and your make-ups go with you.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|x-small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"large","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-large-font-size" style="font-weight:700"><a href="/locations/austin/"><?php esc_html_e( 'Austin, South Lamar →', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"large","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-large-font-size" style="font-weight:700"><a href="/locations/round-rock/"><?php esc_html_e( 'Round Rock →', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"large","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-large-font-size" style="font-weight:700"><a href="/locations/san-antonio/"><?php esc_html_e( 'San Antonio, Stone Oak →', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"large","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-large-font-size" style="font-weight:700"><a href="/locations/houston/"><?php esc_html_e( 'Houston, the Heights →', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"large","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-large-font-size" style="font-weight:700"><a href="/locations/frisco/"><?php esc_html_e( 'Frisco →', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"large","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-large-font-size" style="font-weight:700"><a href="/locations/fort-worth/"><?php esc_html_e( 'Fort Worth →', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:anypress/map {"address":"Austin, TX","lat":30.9,"lon":-97.3,"zoom":6,"aspect":"4/3"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->
