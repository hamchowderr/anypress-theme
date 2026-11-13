<?php
/**
 * Title: Gloss numbers: four figures that count up
 * Slug: anypress/gloss-numbers
 * Description: Four numbers that count up as they scroll into view (years open, clients, star rating, consultation minutes), each with a short line. Needs the AnyPress Blocks plugin. Part of the Gloss kit; use real figures only.
 * Categories: anypress/kit-salon
 * Keywords: numbers, statistics, counter, reviews, salon, gloss
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Numbers"},"align":"full","className":"is-style-section-brand-soft","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull is-style-section-brand-soft" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:group {"align":"wide","style":{"spacing":{"blockGap":"var:preset|spacing|x-large"}},"layout":{"type":"grid","columnCount":4,"minimumColumnWidth":"13rem"}} -->
<div class="wp-block-group alignwide"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":14,"style":{"typography":{"fontWeight":"500","lineHeight":"0.9"}},"fontSize":"xxx-large","fontFamily":"bodoni-moda"} /-->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'years on Elm Street', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":3200,"style":{"typography":{"fontWeight":"500","lineHeight":"0.9"}},"fontSize":"xxx-large","fontFamily":"bodoni-moda"} /-->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'clients on our books', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":4.9,"decimals":1,"style":{"typography":{"fontWeight":"500","lineHeight":"0.9"}},"fontSize":"xxx-large","fontFamily":"bodoni-moda"} /-->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'stars from 640 reviews', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":30,"style":{"typography":{"fontWeight":"500","lineHeight":"0.9"}},"fontSize":"xxx-large","fontFamily":"bodoni-moda"} /-->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'free minutes for a first colour chat', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></section>
<!-- /wp:group -->
