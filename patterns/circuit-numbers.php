<?php
/**
 * Title: Circuit numbers: four figures that count up
 * Slug: anypress/circuit-numbers
 * Description: Four numbers that count up as they scroll into view (years, jobs, rating, arrival time) on the brand colour. Needs the AnyPress Blocks plugin. Part of the Circuit kit; use the owner's real figures.
 * Categories: anypress/kit-electrical
 * Keywords: numbers, statistics, counter, proof, electrician, circuit
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Numbers"},"align":"full","className":"is-style-section-brand","style":{"spacing":{"padding":{"top":"var:preset|spacing|x-large","bottom":"var:preset|spacing|x-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull is-style-section-brand" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--x-large);padding-bottom:var(--wp--preset--spacing--x-large)"><!-- wp:group {"align":"wide","style":{"spacing":{"blockGap":"var:preset|spacing|large"}},"layout":{"type":"grid","columnCount":4,"minimumColumnWidth":"12rem"}} -->
<div class="wp-block-group alignwide"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":17,"suffix":" yrs","style":{"typography":{"fontWeight":"900","lineHeight":"0.9"}},"fontSize":"xx-large","fontFamily":"schibsted-grotesk"} /-->

<!-- wp:paragraph {"fontSize":"medium"} -->
<p class="has-medium-font-size"><?php esc_html_e( 'keeping Columbus switched on', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":9200,"suffix":"+","style":{"typography":{"fontWeight":"900","lineHeight":"0.9"}},"fontSize":"xx-large","fontFamily":"schibsted-grotesk"} /-->

<!-- wp:paragraph {"fontSize":"medium"} -->
<p class="has-medium-font-size"><?php esc_html_e( 'jobs finished', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":4.9,"decimals":1,"suffix":"\u2605","style":{"typography":{"fontWeight":"900","lineHeight":"0.9"}},"fontSize":"xx-large","fontFamily":"schibsted-grotesk"} /-->

<!-- wp:paragraph {"fontSize":"medium"} -->
<p class="has-medium-font-size"><?php esc_html_e( 'from 860 reviews', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":2,"suffix":" hrs","style":{"typography":{"fontWeight":"900","lineHeight":"0.9"}},"fontSize":"xx-large","fontFamily":"schibsted-grotesk"} /-->

<!-- wp:paragraph {"fontSize":"medium"} -->
<p class="has-medium-font-size"><?php esc_html_e( 'to an emergency, on average', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></section>
<!-- /wp:group -->
