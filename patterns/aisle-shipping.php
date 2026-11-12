<?php
/**
 * Title: Aisle shipping: what it costs and how long it takes
 * Slug: anypress/aisle-shipping
 * Description: The shop's delivery options in a table (cost and time for each), then sending abroad, with prices and VAT for the EU and UK, and when orders leave. Part of the Aisle kit; keep it the same as the shipping set up in FluentCart.
 * Categories: anypress/kit-store
 * Keywords: shipping, delivery, costs, international, vat, eu, aisle
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Shipping"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"56rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'Delivery in the US', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:table {"hasFixedLayout":false,"className":"is-style-stripes"} -->
<figure class="wp-block-table is-style-stripes"><table><thead><tr><th><?php esc_html_e( 'Option', 'anypress' ); ?></th><th><?php esc_html_e( 'Cost', 'anypress' ); ?></th><th><?php esc_html_e( 'Arrives', 'anypress' ); ?></th></tr></thead><tbody><tr><td><?php esc_html_e( 'Standard', 'anypress' ); ?></td><td><?php esc_html_e( '$8, free over $75', 'anypress' ); ?></td><td><?php esc_html_e( '3 to 5 working days', 'anypress' ); ?></td></tr><tr><td><?php esc_html_e( 'Express', 'anypress' ); ?></td><td><?php esc_html_e( '$18', 'anypress' ); ?></td><td><?php esc_html_e( '1 to 2 working days', 'anypress' ); ?></td></tr><tr><td><?php esc_html_e( 'Pick up in Portland', 'anypress' ); ?></td><td><?php esc_html_e( 'Free', 'anypress' ); ?></td><td><?php esc_html_e( 'Ready the next working day', 'anypress' ); ?></td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'Orders placed by 2pm Pacific, Monday to Friday, leave the same day. You\'ll get an email with tracking as soon as yours is on its way.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'Sending abroad', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:table {"hasFixedLayout":false,"className":"is-style-stripes"} -->
<figure class="wp-block-table is-style-stripes"><table><thead><tr><th><?php esc_html_e( 'Where', 'anypress' ); ?></th><th><?php esc_html_e( 'Cost', 'anypress' ); ?></th><th><?php esc_html_e( 'Arrives', 'anypress' ); ?></th><th><?php esc_html_e( 'Tax and duties', 'anypress' ); ?></th></tr></thead><tbody><tr><td><?php esc_html_e( 'Canada', 'anypress' ); ?></td><td><?php esc_html_e( '$18', 'anypress' ); ?></td><td><?php esc_html_e( '5 to 8 working days', 'anypress' ); ?></td><td><?php esc_html_e( 'Paid on delivery', 'anypress' ); ?></td></tr><tr><td><?php esc_html_e( 'United Kingdom', 'anypress' ); ?></td><td><?php esc_html_e( '$22', 'anypress' ); ?></td><td><?php esc_html_e( '5 to 8 working days', 'anypress' ); ?></td><td><?php esc_html_e( 'UK VAT added at checkout', 'anypress' ); ?></td></tr><tr><td><?php esc_html_e( 'European Union', 'anypress' ); ?></td><td><?php esc_html_e( '$22', 'anypress' ); ?></td><td><?php esc_html_e( '5 to 10 working days', 'anypress' ); ?></td><td><?php esc_html_e( 'Your country\'s VAT added at checkout, no surprise fees', 'anypress' ); ?></td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'For the EU and the UK the VAT is worked out for your country at checkout, so there\'s nothing more to pay at the door. Buying for a business? Add your VAT number at checkout and the VAT comes off.', 'anypress' ); ?></p>
<!-- /wp:paragraph --></section>
<!-- /wp:group -->
