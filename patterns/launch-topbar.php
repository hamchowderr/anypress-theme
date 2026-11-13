<?php
/**
 * Title: Launch top bar: what's new and the sales number
 * Slug: anypress/launch-topbar
 * Description: A thin dark bar above the header with the latest product news and a link to the changelog, and a number for sales. Part of the Launch kit; keep the news current.
 * Categories: anypress/kit-software
 * Keywords: top bar, announcement, news, changelog, phone, header, launch
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"metadata":{"name":"Top bar"},"align":"full","className":"is-style-section-dark","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-dark" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'New: bank matching now works with 2,400 banks', 'anypress' ); ?> · <a href="/changelog/"><?php esc_html_e( 'What\'s new', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small","metadata":{"blockVisibility":{"viewport":{"mobile":false}}}} -->
<p class="has-small-font-size"><?php esc_html_e( 'Talk to sales', 'anypress' ); ?> <a href="tel:5550119"><?php esc_html_e( '555 0119', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
