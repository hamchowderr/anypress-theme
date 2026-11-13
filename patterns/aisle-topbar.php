<?php
/**
 * Title: Aisle top bar: free shipping, returns and what's new
 * Slug: anypress/aisle-topbar
 * Description: A thin bar above the header with the shop's three promises (free shipping over a set amount, easy returns, same-day dispatch) and a link to what's new. Part of the Aisle kit; keep the numbers true to the shop's settings.
 * Categories: anypress/kit-store
 * Keywords: top bar, announcement, free shipping, returns, header, aisle
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"metadata":{"name":"Top bar"},"align":"full","className":"is-style-section-dark","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-dark" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|large"}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Free shipping over $75', 'anypress' ); ?> · <?php esc_html_e( '60-day returns', 'anypress' ); ?> · <?php esc_html_e( 'Order by 2pm, sent today', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small","style":{"typography":{"fontWeight":"600"}}} -->
<p class="has-small-font-size" style="font-weight:600"><a href="/new-in/"><?php esc_html_e( 'New this week: the winter collection', 'anypress' ); ?> →</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
