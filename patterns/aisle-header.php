<?php
/**
 * Title: Aisle header: shop menu, search, account and cart
 * Slug: anypress/aisle-header
 * Description: A site header for an online clothing shop that stays at the top while visitors scroll: a dark bar with free shipping and returns, then the shop's name and the menu (with dropdowns for the categories and help). Once the shop has a published product, FluentCart's product search, account link and mini cart appear beside the menu. Part of the Aisle kit; choose it for the header in the Site Editor.
 * Categories: header
 * Keywords: header, menu, navigation, sticky, shop, cart, search, account, ecommerce, aisle
 * Viewport Width: 1400
 * Block Types: core/template-part/header
 */
?>
<!-- wp:group {"metadata":{"name":"Header"},"align":"full","className":"is-style-sticky","style":{"spacing":{"blockGap":"0"}},"layout":{"type":"default"}} -->
<div class="wp-block-group alignfull is-style-sticky"><!-- wp:group {"metadata":{"name":"Top bar"},"align":"full","className":"is-style-section-dark","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-dark" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|large"}},"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Free shipping over $75', 'anypress' ); ?> · <?php esc_html_e( '60-day returns', 'anypress' ); ?> · <?php esc_html_e( 'Order by 2pm, sent today', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small","style":{"typography":{"fontWeight":"600"}}} -->
<p class="has-small-font-size" style="font-weight:600"><a href="/new-in/"><?php esc_html_e( 'New this week: the winter collection', 'anypress' ); ?> →</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->

<!-- wp:group {"backgroundColor":"base","metadata":{"name":"Main bar"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull has-base-background-color has-background" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|medium"}},"layout":{"type":"flex","justifyContent":"space-between","flexWrap":"nowrap","verticalAlignment":"center"}} -->
<div class="wp-block-group"><!-- wp:site-title {"level":0,"fontSize":"x-large","style":{"typography":{"lineHeight":"1"}}} /-->

<!-- wp:navigation {"overlayMenu":"mobile","layout":{"type":"flex","justifyContent":"right"}} /--></div>
<!-- /wp:group --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
