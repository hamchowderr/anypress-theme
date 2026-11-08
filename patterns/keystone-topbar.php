<?php
/**
 * Title: Keystone top bar: the free valuation and the phone number
 * Slug: anypress/keystone-topbar
 * Description: A thin bar above the header with the free valuation offer and a link to it, and the office phone number. Part of the Keystone kit.
 * Categories: anypress/kit-real-estate
 * Keywords: top bar, announcement, valuation, phone, header, keystone
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"metadata":{"name":"Top bar"},"align":"full","className":"is-style-section-brand","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-brand" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Thinking of selling? Free valuation in writing', 'anypress' ); ?> · <a href="/valuation/"><?php esc_html_e( 'Book one', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Call the office', 'anypress' ); ?> <a href="tel:8455550117"><?php esc_html_e( '(845) 555-0117', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
