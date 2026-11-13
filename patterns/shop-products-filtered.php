<?php
/**
 * Title: Shop: products with search and filters
 * Slug: anypress/shop-products-filtered
 * Description: The shop's products with a search box and filters for category and price beside them, then cards in pages. For a shop page with many products.
 * Categories: anypress/blocks-shop
 * Keywords: shop, products, filter, search, catalogue, store, fluentcart
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Products"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|medium","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--medium);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:fluent-cart/products {"colors":{},"enable_filter":true,"enable_wildcard_filter":true,"filters":{"product-categories":{"filter_type":"options","is_meta":true,"label":"Categories","enabled":true,"multiple":false},"price_range":{"filter_type":"range","is_meta":false,"label":"Price","enabled":true}}} -->
<div class="wp-block-fluent-cart-products"><div class="fct-products-wrapper" data-fluent-cart-shop-app="true" data-fluent-cart-product-wrapper=""><!-- wp:fluent-cart/shopapp-product-view-switcher {"className":"fluent-product-view-switcher","metadata":{"name":"View Switcher"}} /-->

<!-- wp:fluent-cart/shopapp-product-container {"className":"fluent-product-container"} -->
<div class="wp-block-fluent-cart-shopapp-product-container fluent-product-container"><!-- wp:fluent-cart/shopapp-product-filter -->
<div class="fluent-cart-product-filter-wrapper"><!-- wp:fluent-cart/shopapp-product-filter-search-box /-->

<!-- wp:fluent-cart/shopapp-product-filter-filters /-->

<!-- wp:fluent-cart/shopapp-product-filter-button -->
<div class="fct-product-block-filter-item"><!-- wp:fluent-cart/shopapp-product-filter-apply-button /-->

<!-- wp:fluent-cart/shopapp-product-filter-reset-button /--></div>
<!-- /wp:fluent-cart/shopapp-product-filter-button --></div>
<!-- /wp:fluent-cart/shopapp-product-filter -->

<!-- wp:fluent-cart/shopapp-product-loop {"wp_client_id":"anypress-shop-products-filtered","className":"fluent-product-loop","metadata":{"name":"Product Loop"}} -->
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

<!-- wp:fluent-cart/product-paginator {"className":"fluent-product-paginator","metadata":{"name":"Paginator"}} -->
<div class="fluent-cart-product-paginator"><!-- wp:fluent-cart/product-paginator-info /-->

<!-- wp:fluent-cart/product-paginator-number /--></div>
<!-- /wp:fluent-cart/product-paginator -->

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
