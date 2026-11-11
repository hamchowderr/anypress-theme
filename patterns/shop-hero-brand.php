<?php
/**
 * Title: Shop: brand heading
 * Slug: anypress/shop-hero-brand
 * Description: The top of a brand's page in the shop: a small label, the brand name and its description, on the tint section style. FluentCart's brand pages use it.
 * Categories: anypress/blocks-shop
 * Keywords: shop, brand, products, heading, fluentcart
 * Viewport Width: 1400
 * Inserter: no
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Page hero"},"align":"full","className":"is-style-section-tint","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|x-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull is-style-section-tint" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--x-large)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"constrained","contentSize":"48rem","justifyContent":"left"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"textColor":"secondary","fontSize":"small","style":{"typography":{"fontWeight":"600","letterSpacing":"0.08em","textTransform":"uppercase"}}} -->
<p class="has-secondary-color has-text-color has-small-font-size" style="font-weight:600;letter-spacing:0.08em;text-transform:uppercase"><?php esc_html_e( 'Brand', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:query-title {"type":"archive","showPrefix":false,"level":1,"fontSize":"xxx-large"} /-->

<!-- wp:term-description {"fontSize":"large"} /--></div>
<!-- /wp:group --></section>
<!-- /wp:group -->
