<?php
/**
 * Title: Aisle new in: the eight newest products
 * Slug: anypress/aisle-new-in
 * Description: The eight newest products as FluentCart product cards (a tall photo, the name, the price, sale and sold-out badges, and quick add on the photo), under a centred title with a link to everything new. Part of the Aisle kit; it fills itself from the shop.
 * Categories: anypress/kit-store
 * Keywords: new in, new arrivals, latest, products, fluentcart, aisle
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"New in"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large","left":"var:preset|spacing|small","right":"var:preset|spacing|small"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"90rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large);padding-left:var(--wp--preset--spacing--small);padding-right:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"align":"center","textColor":"secondary","fontSize":"x-small","style":{"typography":{"fontWeight":"600","letterSpacing":"0.14em","textTransform":"uppercase"}}} -->
<p class="has-text-align-center has-secondary-color has-text-color has-x-small-font-size" style="font-weight:600;letter-spacing:0.14em;text-transform:uppercase"><?php esc_html_e( 'Just landed', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"textAlign":"center","fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-text-align-center has-xx-large-font-size"><?php esc_html_e( 'New in', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","fontSize":"x-small","style":{"typography":{"fontWeight":"600","letterSpacing":"0.14em","textTransform":"uppercase"}}} -->
<p class="has-text-align-center has-x-small-font-size" style="font-weight:600;letter-spacing:0.14em;text-transform:uppercase"><a href="/new-in/"><?php esc_html_e( 'Shop everything new', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:fluent-cart/products {"colors":{},"per_page":8,"order_by":"ID","order_type":"DESC","paginator":"numbers"} -->
<div class="wp-block-fluent-cart-products"><div class="fct-products-wrapper" data-fluent-cart-shop-app="true" data-fluent-cart-product-wrapper=""><!-- wp:fluent-cart/shopapp-product-container {"className":"fluent-product-container"} -->
<div class="wp-block-fluent-cart-shopapp-product-container fluent-product-container"><!-- wp:fluent-cart/shopapp-product-filter -->
<div class="fluent-cart-product-filter-wrapper"><!-- wp:fluent-cart/shopapp-product-filter-search-box /-->

<!-- wp:fluent-cart/shopapp-product-filter-filters /-->

<!-- wp:fluent-cart/shopapp-product-filter-button -->
<div class="fct-product-block-filter-item"><!-- wp:fluent-cart/shopapp-product-filter-apply-button /-->

<!-- wp:fluent-cart/shopapp-product-filter-reset-button /--></div>
<!-- /wp:fluent-cart/shopapp-product-filter-button --></div>
<!-- /wp:fluent-cart/shopapp-product-filter -->

<!-- wp:fluent-cart/shopapp-product-loop {"wp_client_id":"aisle-new-in","className":"fluent-product-loop","metadata":{"name":"Product Loop"}} -->
<div class="fluent-cart-product-loop fct-product-block-editor-product-card"><!-- wp:fluent-cart/shopapp-product-image -->
<div class="fluent-cart-product-image"></div>
<!-- /wp:fluent-cart/shopapp-product-image -->

<!-- wp:fluent-cart/sale-badge {"show_percentage":true} /-->

<!-- wp:fluent-cart/sold-out-badge /-->

<!-- wp:fluent-cart/shopapp-product-title /-->

<!-- wp:fluent-cart/shopapp-product-price /-->

<!-- wp:fluent-cart/shopapp-product-buttons /--></div>
<!-- /wp:fluent-cart/shopapp-product-loop --></div>
<!-- /wp:fluent-cart/shopapp-product-container -->

<!-- wp:fluent-cart/shopapp-product-no-result {"className":"fluent-product-no-result","metadata":{"name":"No Result"}} -->
<div class="fluent-cart-shop-no-result-wrap"><!-- wp:paragraph {"align":"center","fontSize":"large"} -->
<p class="has-text-align-center has-large-font-size"><?php esc_html_e( 'Nothing here yet', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"center","textColor":"secondary"} -->
<p class="has-text-align-center has-secondary-color has-text-color"><?php esc_html_e( 'Try clearing the filters, or look through everything in the shop.', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:fluent-cart/shopapp-product-no-result --></div></div>
<!-- /wp:fluent-cart/products --></section>
<!-- /wp:group -->
