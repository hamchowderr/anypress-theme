<?php
/**
 * Title: Keystone numbers: the agency's record
 * Slug: anypress/keystone-numbers
 * Description: Four numbers that count up as they scroll into view, showing the agency's record (homes sold, days on the market, asking price achieved, reviews). Needs the AnyPress Blocks plugin. Part of the Keystone kit; use real, current figures.
 * Categories: anypress/kit-real-estate
 * Keywords: numbers, statistics, record, proof, results, counter, keystone
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Record"},"align":"full","className":"is-style-section-tint","style":{"spacing":{"padding":{"top":"var:preset|spacing|x-large","bottom":"var:preset|spacing|x-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull is-style-section-tint" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--x-large);padding-bottom:var(--wp--preset--spacing--x-large)"><!-- wp:group {"align":"wide","style":{"spacing":{"blockGap":"var:preset|spacing|large"}},"layout":{"type":"grid","columnCount":4,"minimumColumnWidth":"12rem"}} -->
<div class="wp-block-group alignwide"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|x-small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":340,"style":{"typography":{"fontWeight":"400","lineHeight":"0.9"}},"fontSize":"xxx-large","fontFamily":"gloock"} /-->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'homes sold since 2019', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|x-small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":21,"suffix":" days","style":{"typography":{"fontWeight":"400","lineHeight":"0.9"}},"fontSize":"xxx-large","fontFamily":"gloock"} /-->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'on the market, on average', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|x-small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":98,"suffix":"%","style":{"typography":{"fontWeight":"400","lineHeight":"0.9"}},"fontSize":"xxx-large","fontFamily":"gloock"} /-->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'of asking price achieved', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|x-small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":4.9,"decimals":1,"suffix":" / 5","style":{"typography":{"fontWeight":"400","lineHeight":"0.9"}},"fontSize":"xxx-large","fontFamily":"gloock"} /-->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'from 210 reviews', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></section>
<!-- /wp:group -->
