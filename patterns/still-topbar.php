<?php
/**
 * Title: Still top bar: opening hours and the phone number
 * Slug: anypress/still-topbar
 * Description: A thin quiet bar above the header with the opening hours and a link to gift vouchers, and the phone number. Part of the Still kit.
 * Categories: anypress/kit-wellness
 * Keywords: top bar, announcement, hours, phone, header, still
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"metadata":{"name":"Top bar"},"align":"full","className":"is-style-section-tint","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-tint" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Open Tuesday to Sunday', 'anypress' ); ?> · <a href="/gifts/"><?php esc_html_e( 'Gift vouchers', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small","metadata":{"blockVisibility":{"viewport":{"mobile":false}}}} -->
<p class="has-small-font-size"><?php esc_html_e( 'Call', 'anypress' ); ?> <a href="tel:5550170"><?php esc_html_e( '555 0170', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
