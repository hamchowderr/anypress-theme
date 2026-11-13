<?php
/**
 * Title: Rep top bar: the free week and the phone number
 * Slug: anypress/rep-topbar
 * Description: A thin bar above the header with the free trial week and a link to it, and the gym's phone number. Part of the Rep kit; keep the offer current.
 * Categories: anypress/kit-fitness
 * Keywords: top bar, announcement, offer, trial, phone, header, rep
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"metadata":{"name":"Top bar"},"align":"full","className":"is-style-section-second-brand","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-second-brand" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'New here? Your first week is free', 'anypress' ); ?> · <a href="/trial/"><?php esc_html_e( 'Claim it', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Call the front desk', 'anypress' ); ?> <a href="tel:5035550162"><?php esc_html_e( '(503) 555-0162', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
