<?php
/**
 * Title: Frame top bar: when you're free and the phone number
 * Slug: anypress/frame-topbar
 * Description: A thin bar above the header with the date commissions open and a link to ask, and the studio's phone number. Part of the Frame kit; keep the date current.
 * Categories: anypress/kit-portfolio
 * Keywords: top bar, announcement, availability, phone, header, frame
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"metadata":{"name":"Top bar"},"align":"full","className":"is-style-section-brand","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-brand" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Taking commissions from March', 'anypress' ); ?> · <a href="/commission/"><?php esc_html_e( 'Ask about dates', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Call the studio', 'anypress' ); ?> <a href="tel:+351215550147"><?php esc_html_e( '+351 21 555 0147', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
