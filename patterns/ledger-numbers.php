<?php
/**
 * Title: Ledger numbers: four figures that count up
 * Slug: anypress/ledger-numbers
 * Description: Four big numbers that count up as they scroll into view (clients, years, returns filed late, average saving), each with a short line. Needs the AnyPress Blocks plugin. Part of the Ledger kit; use real figures only.
 * Categories: anypress/kit-professional
 * Keywords: numbers, statistics, counter, results, firm, ledger
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Numbers"},"align":"full","className":"is-style-section-tint","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull is-style-section-tint" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:group {"align":"wide","style":{"spacing":{"blockGap":"var:preset|spacing|x-large"}},"layout":{"type":"grid","columnCount":4,"minimumColumnWidth":"13rem"}} -->
<div class="wp-block-group alignwide"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":340,"style":{"typography":{"fontWeight":"700","lineHeight":"0.9"}},"fontSize":"xx-large","fontFamily":"libre-franklin"} /-->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'small businesses on our books', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":18,"style":{"typography":{"fontWeight":"700","lineHeight":"0.9"}},"fontSize":"xx-large","fontFamily":"libre-franklin"} /-->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'years at Park Square', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":0,"style":{"typography":{"fontWeight":"700","lineHeight":"0.9"}},"fontSize":"xx-large","fontFamily":"libre-franklin"} /-->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'returns filed late, ever', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":4200,"prefix":"$","style":{"typography":{"fontWeight":"700","lineHeight":"0.9"}},"fontSize":"xx-large","fontFamily":"libre-franklin"} /-->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'saved in tax per client, on average', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></section>
<!-- /wp:group -->
