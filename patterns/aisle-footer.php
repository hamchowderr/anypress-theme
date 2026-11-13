<?php
/**
 * Title: Aisle footer: newsletter, shop and help links
 * Slug: anypress/aisle-footer
 * Description: A site footer for an online clothing shop: a band for the newsletter, then the shop's categories, every help page and the brand's own pages on dark, and how people pay. The first-order popup sits on the home page, so it never gets in the way at checkout. Part of the Aisle kit; choose it for the footer in the Site Editor.
 * Categories: footer
 * Keywords: footer, links, shop, help, newsletter, ecommerce, aisle
 * Viewport Width: 1400
 * Block Types: core/template-part/footer
 */
?>
<!-- wp:group {"metadata":{"name":"Footer"},"align":"full","style":{"spacing":{"blockGap":"0"}},"layout":{"type":"default"}} -->
<div class="wp-block-group alignfull"><!-- wp:group {"tagName":"section","metadata":{"name":"Signup"},"anchor":"signup","align":"full","className":"is-style-section-tint","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"40rem"}} -->
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

<!-- wp:group {"metadata":{"name":"Footer columns"},"align":"full","className":"is-style-section-dark","style":{"spacing":{"padding":{"top":"var:preset|spacing|x-large","bottom":"var:preset|spacing|large"},"blockGap":"var:preset|spacing|large"}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-dark" style="padding-top:var(--wp--preset--spacing--x-large);padding-bottom:var(--wp--preset--spacing--large)"><!-- wp:columns {"verticalAlignment":"top","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|large","left":"var:preset|spacing|large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-top"><!-- wp:column {"width":"34%"} -->
<div class="wp-block-column" style="flex-basis:34%"><!-- wp:site-title {"level":0,"fontSize":"xx-large"} /-->

<!-- wp:paragraph {"textColor":"main-accent"} -->
<p class="has-main-accent-color has-text-color"><?php esc_html_e( 'Everyday clothes, made to last. Designed in Portland, made in two family mills, packed by hand.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"metadata":{"bindings":{"content":{"source":"anypress/site-details","args":{"key":"email_linked"}}}}} -->
<p><a href="mailto:hello@example.com">hello@example.com</a></p>
<!-- /wp:paragraph -->

<!-- wp:social-links {"layout":{"type":"flex"}} -->
<ul class="wp-block-social-links"><!-- wp:social-link {"url":"#","service":"instagram"} /-->

<!-- wp:social-link {"url":"#","service":"pinterest"} /-->

<!-- wp:social-link {"url":"#","service":"facebook"} /--></ul>
<!-- /wp:social-links --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":3,"fontSize":"medium"} -->
<h3 class="wp-block-heading has-medium-font-size"><?php esc_html_e( 'Shop', 'anypress' ); ?></h3>
<!-- /wp:heading -->

<!-- wp:list {"className":"is-style-no-bullets"} -->
<ul class="wp-block-list is-style-no-bullets"><!-- wp:list-item -->
<li><a href="/shop/"><?php esc_html_e( 'Everything', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/product-categories/tops/"><?php esc_html_e( 'Tops', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/product-categories/bottoms/"><?php esc_html_e( 'Bottoms', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/product-categories/outerwear/"><?php esc_html_e( 'Outerwear', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/product-categories/accessories/"><?php esc_html_e( 'Accessories', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/new-in/"><?php esc_html_e( 'New in', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/product-categories/last-few/"><?php esc_html_e( 'Last few', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/gift-cards/"><?php esc_html_e( 'Gift cards', 'anypress' ); ?></a></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":3,"fontSize":"medium"} -->
<h3 class="wp-block-heading has-medium-font-size"><?php esc_html_e( 'Help', 'anypress' ); ?></h3>
<!-- /wp:heading -->

<!-- wp:list {"className":"is-style-no-bullets"} -->
<ul class="wp-block-list is-style-no-bullets"><!-- wp:list-item -->
<li><a href="/help/"><?php esc_html_e( 'Help centre', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/help/shipping/"><?php esc_html_e( 'Shipping and delivery', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/help/returns/"><?php esc_html_e( 'Returns and exchanges', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/help/size-guide/"><?php esc_html_e( 'Size guide', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/help/track-order/"><?php esc_html_e( 'Track your order', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/help/faq/"><?php esc_html_e( 'Questions', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/help/contact/"><?php esc_html_e( 'Contact us', 'anypress' ); ?></a></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":3,"fontSize":"medium"} -->
<h3 class="wp-block-heading has-medium-font-size"><?php esc_html_e( 'Thread & Co.', 'anypress' ); ?></h3>
<!-- /wp:heading -->

<!-- wp:list {"className":"is-style-no-bullets"} -->
<ul class="wp-block-list is-style-no-bullets"><!-- wp:list-item -->
<li><a href="/our-story/"><?php esc_html_e( 'Our story', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/lookbook/"><?php esc_html_e( 'Lookbook', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/reviews/"><?php esc_html_e( 'Reviews', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/journal/"><?php esc_html_e( 'Journal', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/account/"><?php esc_html_e( 'Your account', 'anypress' ); ?></a></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:separator {"className":"is-style-wide"} -->
<hr class="wp-block-separator has-alpha-channel-opacity is-style-wide"/>
<!-- /wp:separator -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"textColor":"main-accent","fontSize":"small"} -->
<p class="has-main-accent-color has-text-color has-small-font-size"><?php esc_html_e( '© Thread & Co. Prices in US dollars. Secure checkout: cards, Apple Pay and Google Pay.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"main-accent","fontSize":"small"} -->
<p class="has-main-accent-color has-text-color has-small-font-size"><a href="/privacy-policy/"><?php esc_html_e( 'Privacy', 'anypress' ); ?></a> · <a href="/help/shipping/"><?php esc_html_e( 'Shipping', 'anypress' ); ?></a> · <a href="/help/returns/"><?php esc_html_e( 'Returns', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
