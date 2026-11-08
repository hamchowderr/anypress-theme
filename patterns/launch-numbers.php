<?php
/**
 * Title: Launch numbers: four figures that count up
 * Slug: anypress/launch-numbers
 * Description: Four big numbers that count up as they scroll into view (customers, money handled, days faster, uptime), each with a short label. Needs the AnyPress Blocks plugin. Part of the Launch kit; use real figures only.
 * Categories: anypress/kit-software
 * Keywords: numbers, statistics, counter, metrics, results, launch
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Numbers"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:group {"align":"wide","style":{"spacing":{"blockGap":"var:preset|spacing|x-large"}},"layout":{"type":"grid","columnCount":4,"minimumColumnWidth":"14rem"}} -->
<div class="wp-block-group alignwide"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":3000,"suffix":"+","style":{"typography":{"fontWeight":"900","lineHeight":"0.9"}},"fontSize":"xx-large","fontFamily":"schibsted-grotesk"} /-->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"medium"} -->
<p class="has-secondary-color has-text-color has-medium-font-size"><?php esc_html_e( 'studios and freelancers', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":48,"prefix":"$","suffix":"M","style":{"typography":{"fontWeight":"900","lineHeight":"0.9"}},"fontSize":"xx-large","fontFamily":"schibsted-grotesk"} /-->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"medium"} -->
<p class="has-secondary-color has-text-color has-medium-font-size"><?php esc_html_e( 'invoiced through Tally last year', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":22,"suffix":" days","style":{"typography":{"fontWeight":"900","lineHeight":"0.9"}},"fontSize":"xx-large","fontFamily":"schibsted-grotesk"} /-->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"medium"} -->
<p class="has-secondary-color has-text-color has-medium-font-size"><?php esc_html_e( 'sooner paid, on average', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:anypress/counter {"number":99.98,"decimals":2,"suffix":"%","style":{"typography":{"fontWeight":"900","lineHeight":"0.9"}},"fontSize":"xx-large","fontFamily":"schibsted-grotesk"} /-->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"medium"} -->
<p class="has-secondary-color has-text-color has-medium-font-size"><?php esc_html_e( 'uptime over the last year', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></section>
<!-- /wp:group -->
