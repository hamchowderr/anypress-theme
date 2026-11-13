<?php
/**
 * Title: Byline top bar: the new issue and the phone number
 * Slug: anypress/byline-topbar
 * Description: A thin bar above the header with the newest print issue and a link to subscribe, and the office phone number. Part of the Byline kit.
 * Categories: anypress/kit-magazine
 * Keywords: top bar, announcement, subscribe, phone, header, byline
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"metadata":{"name":"Top bar"},"align":"full","className":"is-style-section-dark","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-dark" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'The autumn issue is out now', 'anypress' ); ?> · <a href="/subscribe/"><?php esc_html_e( 'Subscribe', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Subscriptions and walks', 'anypress' ); ?> <a href="tel:4065550139"><?php esc_html_e( '(406) 555-0139', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
