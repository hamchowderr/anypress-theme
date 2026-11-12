<?php
/**
 * Title: Aisle two photos: two collections side by side
 * Slug: anypress/aisle-spotlight-2
 * Description: Two collections side by side as tall photos, each with its name, a line and a link, so the home page changes shape between product rows. Part of the Aisle kit; point each at the shop's own category.
 * Categories: anypress/kit-store
 * Keywords: collections, categories, two photos, feature, promotion, aisle
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Two collections"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small","left":"var:preset|spacing|small","right":"var:preset|spacing|small"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"default"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small);padding-left:var(--wp--preset--spacing--small);padding-right:var(--wp--preset--spacing--small)"><!-- wp:group {"align":"wide","style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"grid","columnCount":2,"minimumColumnWidth":"20rem"}} -->
<div class="wp-block-group alignwide"><!-- wp:cover {"url":"<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-tall.svg' ) ); ?>","alt":"A stack of folded tees in grey, red and green","dimRatio":30,"overlayColor":"main","isUserOverlayColor":true,"minHeight":44,"minHeightUnit":"rem","contentPosition":"bottom left","align":"full","metadata":{"name":"The everyday tee"},"style":{"spacing":{"padding":{"top":"var:preset|spacing|large","bottom":"var:preset|spacing|large","left":"var:preset|spacing|large","right":"var:preset|spacing|large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"},"className":"aisle-tile"} -->
<div class="wp-block-cover alignfull has-custom-content-position is-position-bottom-left aisle-tile" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--large);padding-bottom:var(--wp--preset--spacing--large);padding-left:var(--wp--preset--spacing--large);padding-right:var(--wp--preset--spacing--large);min-height:44rem"><img class="wp-block-cover__image-background" alt="A stack of folded tees in grey, red and green" src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-tall.svg' ) ); ?>" data-object-fit="cover"/><span aria-hidden="true" class="wp-block-cover__background has-main-background-color has-background-dim-30 has-background-dim"></span><div class="wp-block-cover__inner-container"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:heading {"level":3,"fontSize":"xxx-large"} -->
<h3 class="wp-block-heading has-xxx-large-font-size"><a href="/product-categories/tops/"><?php esc_html_e( 'The everyday tee', 'anypress' ); ?></a></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Heavy cotton, five colours, made to be worn every day.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"x-small","style":{"typography":{"fontWeight":"600","letterSpacing":"0.14em","textTransform":"uppercase"}}} -->
<p class="has-x-small-font-size" style="font-weight:600;letter-spacing:0.14em;text-transform:uppercase"><a href="/product-categories/tops/"><?php esc_html_e( 'Shop tops', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div></div>
<!-- /wp:cover -->

<!-- wp:cover {"url":"<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-tall.svg' ) ); ?>","alt":"A woman in a checked scarf checking her watch","dimRatio":30,"overlayColor":"main","isUserOverlayColor":true,"minHeight":44,"minHeightUnit":"rem","contentPosition":"bottom left","align":"full","metadata":{"name":"Knits for cold mornings"},"style":{"spacing":{"padding":{"top":"var:preset|spacing|large","bottom":"var:preset|spacing|large","left":"var:preset|spacing|large","right":"var:preset|spacing|large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"},"className":"aisle-tile"} -->
<div class="wp-block-cover alignfull has-custom-content-position is-position-bottom-left aisle-tile" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--large);padding-bottom:var(--wp--preset--spacing--large);padding-left:var(--wp--preset--spacing--large);padding-right:var(--wp--preset--spacing--large);min-height:44rem"><img class="wp-block-cover__image-background" alt="A woman in a checked scarf checking her watch" src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-tall.svg' ) ); ?>" data-object-fit="cover"/><span aria-hidden="true" class="wp-block-cover__background has-main-background-color has-background-dim-30 has-background-dim"></span><div class="wp-block-cover__inner-container"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:heading {"level":3,"fontSize":"xxx-large"} -->
<h3 class="wp-block-heading has-xxx-large-font-size"><a href="/product-categories/accessories/"><?php esc_html_e( 'Knits for cold mornings', 'anypress' ); ?></a></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Scarves, caps and socks that keep their shape.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"x-small","style":{"typography":{"fontWeight":"600","letterSpacing":"0.14em","textTransform":"uppercase"}}} -->
<p class="has-x-small-font-size" style="font-weight:600;letter-spacing:0.14em;text-transform:uppercase"><a href="/product-categories/accessories/"><?php esc_html_e( 'Shop accessories', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div></div>
<!-- /wp:cover --></div>
<!-- /wp:group --></section>
<!-- /wp:group -->
