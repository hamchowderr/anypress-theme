<?php
/**
 * Title: Chapter top bar: the next start date and a phone number
 * Slug: anypress/chapter-topbar
 * Description: A thin dark bar above the header with the next start date and a link to join, and a number to call with questions. Part of the Chapter kit; keep the date current.
 * Categories: anypress/kit-courses
 * Keywords: top bar, announcement, start date, cohort, phone, header, chapter
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"metadata":{"name":"Top bar"},"align":"full","className":"is-style-section-dark","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-dark" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Next cohort starts 3 March', 'anypress' ); ?> · <a href="/join/"><?php esc_html_e( 'Save your place', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small","metadata":{"blockVisibility":{"viewport":{"mobile":false}}}} -->
<p class="has-small-font-size"><?php esc_html_e( 'Questions? Call or text', 'anypress' ); ?> <a href="tel:5550142"><?php esc_html_e( '555 0142', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
