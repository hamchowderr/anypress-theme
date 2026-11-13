<?php
/**
 * Title: Gloss top bar: the new-client offer and the phone number
 * Slug: anypress/gloss-topbar
 * Description: A thin bar above the header with the new-client offer and a link to it, and the salon's phone number. Part of the Gloss kit; keep the offer current.
 * Categories: anypress/kit-salon
 * Keywords: top bar, announcement, offer, phone, header, gloss
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"metadata":{"name":"Top bar"},"align":"full","className":"is-style-section-dark","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-dark" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'New clients: 20% off your first colour', 'anypress' ); ?> · <a href="/offers/"><?php esc_html_e( 'See offers', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Call the salon', 'anypress' ); ?> <a href="tel:2175550133"><?php esc_html_e( '(217) 555-0133', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
