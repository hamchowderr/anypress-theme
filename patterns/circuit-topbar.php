<?php
/**
 * Title: Circuit top bar: same-day service and the phone number
 * Slug: anypress/circuit-topbar
 * Description: A thin dark bar above the header with the business's promise, the opening hours and the phone number. Part of the Circuit kit (electricians); use the owner's real number.
 * Categories: anypress/kit-electrical
 * Keywords: top bar, phone, hours, announcement, header, electrician, circuit
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"metadata":{"name":"Top bar"},"align":"full","className":"is-style-section-dark","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-dark" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Same-day service across Columbus', 'anypress' ); ?> · <?php esc_html_e( 'Licensed and insured', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small","metadata":{"blockVisibility":{"viewport":{"mobile":false}}}} -->
<p class="has-small-font-size"><?php esc_html_e( 'Mon to Sat, 7am to 7pm · Emergencies 24/7:', 'anypress' ); ?> <a href="tel:5550187"><?php esc_html_e( '555 0187', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
