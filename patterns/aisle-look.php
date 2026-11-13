<?php
/**
 * Title: Aisle shop the look: one outfit, piece by piece
 * Slug: anypress/aisle-look
 * Description: A photo of an outfit filling half the screen beside the pieces in it, each linking to its product, with a button to the lookbook. Part of the Aisle kit; point each piece at the shop's own product.
 * Categories: anypress/kit-store
 * Keywords: shop the look, outfit, lookbook, styling, aisle
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Shop the look"},"align":"full","style":{"spacing":{"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"default"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0"><!-- wp:columns {"align":"full","style":{"spacing":{"blockGap":{"top":"0","left":"0"}}}} -->
<div class="wp-block-columns alignfull"><!-- wp:column {"width":"55%"} -->
<div class="wp-block-column" style="flex-basis:55%"><!-- wp:cover {"url":"<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-tall.svg' ) ); ?>","alt":"A man in a beanie drinking coffee by a tent","dimRatio":0,"overlayColor":"main","isUserOverlayColor":true,"minHeight":40,"minHeightUnit":"rem","layout":{"type":"constrained"}} -->
<div class="wp-block-cover" style="min-height:40rem"><img class="wp-block-cover__image-background" alt="A man in a beanie drinking coffee by a tent" src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-tall.svg' ) ); ?>" data-object-fit="cover"/><span aria-hidden="true" class="wp-block-cover__background has-main-background-color has-background-dim-0 has-background-dim"></span><div class="wp-block-cover__inner-container"></div></div>
<!-- /wp:cover --></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center","className":"is-style-section-tint","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large","left":"var:preset|spacing|xx-large","right":"var:preset|spacing|xx-large"}}}} -->
<div class="wp-block-column is-vertically-aligned-center is-style-section-tint" style="padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large);padding-left:var(--wp--preset--spacing--xx-large);padding-right:var(--wp--preset--spacing--xx-large)"><!-- wp:paragraph {"textColor":"secondary","fontSize":"x-small","style":{"typography":{"fontWeight":"600","letterSpacing":"0.14em","textTransform":"uppercase"}}} -->
<p class="has-secondary-color has-text-color has-x-small-font-size" style="font-weight:600;letter-spacing:0.14em;text-transform:uppercase"><?php esc_html_e( 'Shop the look', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xxx-large"} -->
<h2 class="wp-block-heading has-xxx-large-font-size"><?php esc_html_e( 'Weekend, sorted', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"medium"} -->
<p class="has-secondary-color has-text-color has-medium-font-size"><?php esc_html_e( 'Tess styled this one for a night out at Trillium Lake: a hoodie you can live in, jeans that soften with every wash and a cap for when it drizzles.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:list {"className":"is-style-no-bullets","fontSize":"large"} -->
<ul class="wp-block-list is-style-no-bullets has-large-font-size"><!-- wp:list-item -->
<li><a href="/item/classic-zipper-hoodie/"><?php esc_html_e( 'Classic zipper hoodie', 'anypress' ); ?></a> →</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/item/mens-slim-fit-jeans/"><?php esc_html_e( 'Slim fit jeans', 'anypress' ); ?></a> →</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/item/classic-cap/"><?php esc_html_e( 'Classic cap', 'anypress' ); ?></a> →</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/lookbook/"><?php esc_html_e( 'See the lookbook', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->
