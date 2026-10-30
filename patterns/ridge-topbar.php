<?php
/**
 * Title: Ridge top bar: emergency line and hours
 * Slug: anypress/ridge-topbar
 * Description: A thin dark bar above the header with the emergency phone number, the opening hours and a link to the quote page. Part of the Ridge kit; use the owner's real number.
 * Categories: anypress/kit-home-services
 * Keywords: top bar, emergency, phone, hours, announcement, header, ridge
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"metadata":{"name":"Top bar"},"align":"full","className":"is-style-section-dark","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-dark" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><strong><?php esc_html_e( '24/7 emergency line:', 'anypress' ); ?></strong> <a href="tel:5550142"><?php esc_html_e( '555 0142', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small","metadata":{"blockVisibility":{"viewport":{"mobile":false}}}} -->
<p class="has-small-font-size"><?php esc_html_e( 'Office: 7am to 7pm, seven days', 'anypress' ); ?> · <a href="/get-a-quote/"><?php esc_html_e( 'Free quotes', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
