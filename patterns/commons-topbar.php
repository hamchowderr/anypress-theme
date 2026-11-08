<?php
/**
 * Title: Commons top bar: the next event and the phone number
 * Slug: anypress/commons-topbar
 * Description: A thin dark bar above the header with the next event and a link to the calendar, the office hours and the phone number. Part of the Commons kit; keep the event current.
 * Categories: anypress/kit-community
 * Keywords: top bar, announcement, next event, phone, hours, header, commons
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"metadata":{"name":"Top bar"},"align":"full","className":"is-style-section-dark","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-dark" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Next breakfast: Thursday 14 March, The Grand Hotel', 'anypress' ); ?> · <a href="/events/"><?php esc_html_e( 'All events', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small","metadata":{"blockVisibility":{"viewport":{"mobile":false}}}} -->
<p class="has-small-font-size"><?php esc_html_e( 'Office: Mon to Fri, 9am to 5pm', 'anypress' ); ?> · <a href="tel:5550164"><?php esc_html_e( '555 0164', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
