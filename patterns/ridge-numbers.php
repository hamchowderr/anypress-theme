<?php
/**
 * Title: Ridge numbers: four figures that count up
 * Slug: anypress/ridge-numbers
 * Description: Four big numbers that count up as they scroll into view (years, jobs, reviews, response time), each with a short label, on the dark style. Needs the AnyPress Blocks plugin. Part of the Ridge kit; use the owner's real figures.
 * Categories: anypress/kit-home-services
 * Keywords: numbers, statistics, counter, proof, years, jobs, ridge
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Numbers"},"align":"full","className":"is-style-section-dark","style":{"spacing":{"padding":{"top":"var:preset|spacing|x-large","bottom":"var:preset|spacing|x-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull is-style-section-dark" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--x-large);padding-bottom:var(--wp--preset--spacing--x-large)"><!-- wp:group {"align":"wide","style":{"spacing":{"blockGap":"var:preset|spacing|large"}},"layout":{"type":"grid","columnCount":4,"minimumColumnWidth":"12rem"}} -->
<div class="wp-block-group alignwide"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":25,"style":{"typography":{"fontWeight":"900","lineHeight":"0.9"}},"fontSize":"xxx-large","fontFamily":"big-shoulders"} /-->

<!-- wp:paragraph {"textColor":"main-accent","fontSize":"medium"} -->
<p class="has-main-accent-color has-text-color has-medium-font-size"><?php esc_html_e( 'years in the county', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":18400,"suffix":"+","style":{"typography":{"fontWeight":"900","lineHeight":"0.9"}},"fontSize":"xxx-large","fontFamily":"big-shoulders"} /-->

<!-- wp:paragraph {"textColor":"main-accent","fontSize":"medium"} -->
<p class="has-main-accent-color has-text-color has-medium-font-size"><?php esc_html_e( 'jobs done', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":4.9,"decimals":1,"suffix":"\u2605","style":{"typography":{"fontWeight":"900","lineHeight":"0.9"}},"fontSize":"xxx-large","fontFamily":"big-shoulders"} /-->

<!-- wp:paragraph {"textColor":"main-accent","fontSize":"medium"} -->
<p class="has-main-accent-color has-text-color has-medium-font-size"><?php esc_html_e( 'from 1,200 reviews', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":60,"suffix":" min","style":{"typography":{"fontWeight":"900","lineHeight":"0.9"}},"fontSize":"xxx-large","fontFamily":"big-shoulders"} /-->

<!-- wp:paragraph {"textColor":"main-accent","fontSize":"medium"} -->
<p class="has-main-accent-color has-text-color has-medium-font-size"><?php esc_html_e( 'average emergency arrival', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></section>
<!-- /wp:group -->
