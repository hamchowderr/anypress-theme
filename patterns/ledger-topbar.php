<?php
/**
 * Title: Ledger top bar: the next deadline and the phone number
 * Slug: anypress/ledger-topbar
 * Description: A thin bar above the header with the next tax deadline and a link to book a call, and the phone number. Part of the Ledger kit; keep the deadline current.
 * Categories: anypress/kit-professional
 * Keywords: top bar, announcement, deadline, phone, header, ledger
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"metadata":{"name":"Top bar"},"align":"full","className":"is-style-section-dark","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-dark" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Next deadline: tax returns due 31 January', 'anypress' ); ?> · <a href="/book-a-call/"><?php esc_html_e( 'Get it done early', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small","metadata":{"blockVisibility":{"viewport":{"mobile":false}}}} -->
<p class="has-small-font-size"><?php esc_html_e( 'Call the office', 'anypress' ); ?> <a href="tel:01135550190"><?php esc_html_e( '0113 555 0190', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
