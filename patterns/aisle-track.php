<?php
/**
 * Title: Aisle track your order: where to find it
 * Slug: anypress/aisle-track
 * Description: Where to see an order's progress (the customer's account, or the link in the shipping email), what each order status means and what to do if a parcel is late. Part of the Aisle kit.
 * Categories: anypress/kit-store
 * Keywords: track order, order status, delivery, account, aisle
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Track"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:columns {"verticalAlignment":"top","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|xx-large","left":"var:preset|spacing|xx-large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-top"><!-- wp:column {"width":"45%"} -->
<div class="wp-block-column" style="flex-basis:45%"><!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'Where\'s my order?', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"medium"} -->
<p class="has-medium-font-size"><?php esc_html_e( 'Every order, its status and its tracking link are in your account. Checked out as a guest? The tracking link is in your shipping email.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/account/"><?php esc_html_e( 'Go to your account', 'anypress' ); ?></a></div>
<!-- /wp:button -->

<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/help/contact/"><?php esc_html_e( 'Contact us', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":3,"fontSize":"large"} -->
<h3 class="wp-block-heading has-large-font-size"><?php esc_html_e( 'What the status means', 'anypress' ); ?></h3>
<!-- /wp:heading -->

<!-- wp:table {"hasFixedLayout":false,"className":"is-style-stripes"} -->
<figure class="wp-block-table is-style-stripes"><table><thead><tr><th><?php esc_html_e( 'Status', 'anypress' ); ?></th><th><?php esc_html_e( 'What\'s happening', 'anypress' ); ?></th></tr></thead><tbody><tr><td><?php esc_html_e( 'Processing', 'anypress' ); ?></td><td><?php esc_html_e( 'We\'ve got your order and we\'re packing it', 'anypress' ); ?></td></tr><tr><td><?php esc_html_e( 'Shipped', 'anypress' ); ?></td><td><?php esc_html_e( 'It\'s with the courier; the tracking link is in your email', 'anypress' ); ?></td></tr><tr><td><?php esc_html_e( 'Completed', 'anypress' ); ?></td><td><?php esc_html_e( 'It\'s been delivered', 'anypress' ); ?></td></tr><tr><td><?php esc_html_e( 'On hold', 'anypress' ); ?></td><td><?php esc_html_e( 'We need something from you, so check your email', 'anypress' ); ?></td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'Not arrived two days after the date in your tracking? Write to us with your order number and we\'ll chase it or send a new one.', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->
