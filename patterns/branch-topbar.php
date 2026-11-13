<?php
/**
 * Title: Branch top bar: the newest location and the franchise link
 * Slug: anypress/branch-topbar
 * Description: A thin bar above the header announcing the newest location and linking to the franchise page, with the main phone number. Part of the Branch kit (franchise and multi-location); keep it current.
 * Categories: anypress/kit-franchise
 * Keywords: top bar, announcement, new location, franchise, phone, header, branch
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"metadata":{"name":"Top bar"},"align":"full","className":"is-style-section-dark","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-dark" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Now open in Frisco', 'anypress' ); ?> · <a href="/own-a-franchise/"><?php esc_html_e( 'Own a Bluegill franchise', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Call any pool', 'anypress' ); ?> <a href="tel:5125550174"><?php esc_html_e( '(512) 555-0174', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
