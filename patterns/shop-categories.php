<?php
/**
 * Title: Shop: shop by category
 * Slug: anypress/shop-categories
 * Description: The shop's product categories as tiles with their names and how many products each has, each opening its category page, under a heading. For a home page.
 * Categories: anypress/blocks-shop
 * Keywords: shop, categories, collections, browse, home, fluentcart
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Shop by category"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|medium"}},"layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between","verticalAlignment":"bottom"}} -->
<div class="wp-block-group"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"constrained","contentSize":"40rem","justifyContent":"left"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"textColor":"secondary","fontSize":"small","style":{"typography":{"fontWeight":"600","letterSpacing":"0.08em","textTransform":"uppercase"}}} -->
<p class="has-secondary-color has-text-color has-small-font-size" style="font-weight:600;letter-spacing:0.08em;text-transform:uppercase"><?php esc_html_e( 'Browse', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'Shop by category', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'Find what you came for.', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="<?php echo esc_url( home_url( '/shop/' ) ); ?>"><?php esc_html_e( 'Shop everything', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group -->

<!-- wp:terms-query {"termQuery":{"perPage":8,"taxonomy":"product-categories","order":"desc","orderBy":"count","include":[],"hideEmpty":true,"showNested":false,"inherit":false}} -->
<div class="wp-block-terms-query"><!-- wp:term-template {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"grid","columnCount":4,"minimumColumnWidth":"9rem"}} -->
<!-- wp:group {"className":"is-style-section-tint anypress-category-tile","style":{"spacing":{"padding":{"top":"var:preset|spacing|medium","bottom":"var:preset|spacing|medium","left":"var:preset|spacing|medium","right":"var:preset|spacing|medium"},"blockGap":"var:preset|spacing|x-small"},"border":{"radius":"var:preset|border-radius|md"},"dimensions":{"minHeight":"7rem"}},"layout":{"type":"flex","orientation":"vertical","justifyContent":"left","verticalAlignment":"space-between"}} -->
<div class="wp-block-group is-style-section-tint anypress-category-tile" style="border-radius:var(--wp--preset--border-radius--md);min-height:7rem;padding-top:var(--wp--preset--spacing--medium);padding-right:var(--wp--preset--spacing--medium);padding-bottom:var(--wp--preset--spacing--medium);padding-left:var(--wp--preset--spacing--medium)"><!-- wp:term-name {"level":3,"isLink":true,"fontSize":"medium"} /-->

<!-- wp:term-count {"textColor":"secondary","fontSize":"small"} /--></div>
<!-- /wp:group -->
<!-- /wp:term-template --></div>
<!-- /wp:terms-query --></section>
<!-- /wp:group -->
