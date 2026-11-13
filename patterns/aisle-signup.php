<?php
/**
 * Title: Aisle signup: the newsletter, with 10% off
 * Slug: anypress/aisle-signup
 * Description: A quiet centred band asking visitors to join the shop's monthly letter for new colours first and 10% off the first order, with the signup form under it. Part of the Aisle kit; sits above the footer on every page.
 * Categories: anypress/kit-store
 * Keywords: newsletter, signup, email, discount, first order, aisle
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Signup"},"anchor":"signup","align":"full","className":"is-style-section-tint","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"40rem"}} -->
<section id="signup" class="wp-block-group alignfull is-style-section-tint" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:paragraph {"align":"center","textColor":"secondary","fontSize":"x-small","style":{"typography":{"fontWeight":"600","letterSpacing":"0.14em","textTransform":"uppercase"}}} -->
<p class="has-text-align-center has-secondary-color has-text-color has-x-small-font-size" style="font-weight:600;letter-spacing:0.14em;text-transform:uppercase"><?php esc_html_e( 'The Thread', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"textAlign":"center","fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-text-align-center has-xx-large-font-size"><?php esc_html_e( 'New colours first, and 10% off', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","textColor":"secondary"} -->
<p class="has-text-align-center has-secondary-color has-text-color"><?php esc_html_e( 'Once a month: what\'s new, care tips and a look behind the seams. Join and we\'ll send a code for 10% off your first order.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:group {"layout":{"type":"constrained","contentSize":"30rem"}} -->
<div class="wp-block-group"><!-- wp:group {"metadata":{"name":"Form: newsletter"},"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/new-in/"><?php esc_html_e( 'See what\'s new', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></section>
<!-- /wp:group -->
