<?php
/**
 * Title: Assay where we treat: the states, with a map
 * Slug: anypress/assay-where
 * Description: Where the business can prescribe and ship: the states as a list of links beside a map, with a line on delivery times. Needs the AnyPress Blocks plugin for the map. Part of the Assay kit; list only states where providers are licensed.
 * Categories: anypress/kit-regulated
 * Keywords: states, where we treat, locations, licensed, map, assay
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Where we treat"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:columns {"verticalAlignment":"center","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|xx-large","left":"var:preset|spacing|xx-large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-center"><!-- wp:column {"width":"40%"} -->
<div class="wp-block-column" style="flex-basis:40%"><!-- wp:paragraph {"textColor":"primary","fontFamily":"monospace","fontSize":"small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.06em"}}} -->
<p class="has-primary-color has-text-color has-monospace-font-family has-small-font-size" style="text-transform:uppercase;letter-spacing:0.06em"><?php esc_html_e( 'Where we treat', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'Four states, two-day delivery', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"medium"} -->
<p class="has-medium-font-size"><?php esc_html_e( 'Our providers are licensed in these states, and the pharmacy ships cold-packed to every one of them in about two days.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|x-small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"large","style":{"typography":{"fontWeight":"500"}}} -->
<p class="has-large-font-size" style="font-weight:500"><a href="/states/arizona/"><?php esc_html_e( 'Arizona →', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"large","style":{"typography":{"fontWeight":"500"}}} -->
<p class="has-large-font-size" style="font-weight:500"><a href="/states/texas/"><?php esc_html_e( 'Texas →', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"large","style":{"typography":{"fontWeight":"500"}}} -->
<p class="has-large-font-size" style="font-weight:500"><a href="/states/florida/"><?php esc_html_e( 'Florida →', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"large","style":{"typography":{"fontWeight":"500"}}} -->
<p class="has-large-font-size" style="font-weight:500"><a href="/states/colorado/"><?php esc_html_e( 'Colorado →', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/states/"><?php esc_html_e( 'Where we treat', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:anypress/map {"address":"Phoenix, AZ","lat":33.4484,"lon":-112.074,"zoom":4,"aspect":"4/3"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->
