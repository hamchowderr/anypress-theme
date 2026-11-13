<?php
/**
 * Title: Hearth top bar: today's bake and the phone number
 * Slug: anypress/hearth-topbar
 * Description: A thin bar above the header with a line about today's bake and a link to order, and the phone number. Part of the Hearth kit; keep the line current.
 * Categories: anypress/kit-food
 * Keywords: top bar, announcement, today, phone, header, hearth
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"metadata":{"name":"Top bar"},"align":"full","className":"is-style-section-brand","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-brand" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Fresh loaves from 7am, Tuesday to Sunday', 'anypress' ); ?> · <a href="/order/"><?php esc_html_e( 'Order a cake', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small","metadata":{"blockVisibility":{"viewport":{"mobile":false}}}} -->
<p class="has-small-font-size"><?php esc_html_e( 'Call the bakery', 'anypress' ); ?> <a href="tel:5550198"><?php esc_html_e( '555 0198', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
