<?php
/**
 * Title: Shop: new arrivals
 * Slug: anypress/shop-new-arrivals
 * Description: The four newest products as cards with photo, name, price and button, under a heading, with a link to the whole shop. For a home page.
 * Categories: anypress/blocks-shop
 * Keywords: shop, products, new, latest, arrivals, home, fluentcart
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"New arrivals"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|medium"}},"layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between","verticalAlignment":"bottom"}} -->
<div class="wp-block-group"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"constrained","contentSize":"40rem","justifyContent":"left"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"textColor":"secondary","fontSize":"small","style":{"typography":{"fontWeight":"600","letterSpacing":"0.08em","textTransform":"uppercase"}}} -->
<p class="has-secondary-color has-text-color has-small-font-size" style="font-weight:600;letter-spacing:0.08em;text-transform:uppercase"><?php esc_html_e( 'Just in', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'New arrivals', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'The latest additions to the shop.', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="<?php echo esc_url( home_url( '/shop/' ) ); ?>"><?php esc_html_e( 'Shop everything', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group -->

<!-- wp:fluent-cart/products {"colors":{},"per_page":4,"order_by":"ID","order_type":"DESC","paginator":"numbers"} -->
<div class="wp-block-fluent-cart-products"><div class="fct-products-wrapper" data-fluent-cart-shop-app="true" data-fluent-cart-product-wrapper=""><!-- wp:fluent-cart/shopapp-product-container {"className":"fluent-product-container"} -->
<div class="wp-block-fluent-cart-shopapp-product-container fluent-product-container"><!-- wp:fluent-cart/shopapp-product-filter -->
<div class="fluent-cart-product-filter-wrapper"><!-- wp:fluent-cart/shopapp-product-filter-search-box /-->

<!-- wp:fluent-cart/shopapp-product-filter-filters /-->

<!-- wp:fluent-cart/shopapp-product-filter-button -->
<div class="fct-product-block-filter-item"><!-- wp:fluent-cart/shopapp-product-filter-apply-button /-->

<!-- wp:fluent-cart/shopapp-product-filter-reset-button /--></div>
<!-- /wp:fluent-cart/shopapp-product-filter-button --></div>
<!-- /wp:fluent-cart/shopapp-product-filter -->

<!-- wp:fluent-cart/shopapp-product-loop {"wp_client_id":"anypress-shop-new-arrivals","className":"fluent-product-loop","metadata":{"name":"Product Loop"}} -->
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
