<?php
/**
 * Title: Parcel top bar: free shipping and the next sale
 * Slug: anypress/parcel-topbar
 * Description: A thin bar above the header with the free shipping line, a link to the next sale and the studio's phone number. Part of the Parcel kit; keep the sale current.
 * Categories: anypress/kit-shop
 * Keywords: top bar, announcement, shipping, sale, phone, header, parcel
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"metadata":{"name":"Top bar"},"align":"full","className":"is-style-section-second-brand","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-second-brand" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Free shipping on orders over $60', 'anypress' ); ?> · <a href="/offers/"><?php esc_html_e( 'Seconds sale, first weekend of every month', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Questions? Call the studio', 'anypress' ); ?> <a href="tel:8285550147"><?php esc_html_e( '(828) 555-0147', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
