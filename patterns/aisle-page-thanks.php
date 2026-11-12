<?php
/**
 * Title: Thank-you page: Aisle kit
 * Slug: anypress/aisle-page-thanks
 * Description: The page visitors see after sending a form: thanks, when to expect a reply and the newest products. Aisle kit; send every form here.
 * Categories: anypress/pages
 * Keywords: thank you, thanks, confirmation, form sent, aisle
 * Viewport Width: 1400
 * Block Types: core/post-content
 * Post Types: page
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Thanks"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xxx-large","bottom":"var:preset|spacing|x-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"56rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xxx-large);padding-bottom:var(--wp--preset--spacing--x-large)"><!-- wp:paragraph {"textColor":"secondary","fontSize":"small","style":{"typography":{"fontWeight":"700","letterSpacing":"0.1em","textTransform":"uppercase"}}} -->
<p class="has-secondary-color has-text-color has-small-font-size" style="font-weight:700;letter-spacing:0.1em;text-transform:uppercase"><?php esc_html_e( 'Message sent', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1,"fontSize":"xxx-large"} -->
<h1 class="wp-block-heading has-xxx-large-font-size"><?php esc_html_e( 'Thanks. We\'ll reply the same working day.', 'anypress' ); ?></h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"large"} -->
<p class="has-secondary-color has-text-color has-large-font-size"><?php esc_html_e( 'Check your email for a copy of what you sent. In the meantime, here\'s what just landed.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/"><?php esc_html_e( 'Back to the home page', 'anypress' ); ?></a></div>
<!-- /wp:button -->

<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/new-in/"><?php esc_html_e( 'Shop new in', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></section>
<!-- /wp:group -->

<!-- wp:group {"tagName":"section","metadata":{"name":"New in"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:group {"layout":{"type":"flex","justifyContent":"space-between","verticalAlignment":"bottom"}} -->
<div class="wp-block-group"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"textColor":"secondary","fontSize":"small","style":{"typography":{"fontWeight":"700","letterSpacing":"0.1em","textTransform":"uppercase"}}} -->
<p class="has-secondary-color has-text-color has-small-font-size" style="font-weight:700;letter-spacing:0.1em;text-transform:uppercase"><?php esc_html_e( 'Just landed', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'New in', 'anypress' ); ?></h2>
<!-- /wp:heading --></div>
<!-- /wp:group -->

<!-- wp:paragraph {"fontSize":"medium","style":{"typography":{"fontWeight":"600"}}} -->
<p class="has-medium-font-size" style="font-weight:600"><a href="/new-in/"><?php esc_html_e( 'See everything new', 'anypress' ); ?> →</a></p>
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
