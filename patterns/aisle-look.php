<?php
/**
 * Title: Aisle shop the look: one outfit, piece by piece
 * Slug: anypress/aisle-look
 * Description: A large photo of an outfit beside the pieces in it, each linking to its product, with a button to the lookbook. Part of the Aisle kit; point each piece at the shop's own product.
 * Categories: anypress/kit-store
 * Keywords: shop the look, outfit, lookbook, styling, aisle
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Shop the look"},"align":"full","className":"is-style-section-tint","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull is-style-section-tint" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:columns {"verticalAlignment":"center","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|xx-large","left":"var:preset|spacing|xx-large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-center"><!-- wp:column {"width":"52%"} -->
<div class="wp-block-column" style="flex-basis:52%"><!-- wp:image {"sizeSlug":"large","linkDestination":"none","aspectRatio":"4/5","scale":"cover"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-tall.svg' ) ); ?>" alt="<?php esc_attr_e( 'A man in a beanie drinking coffee by a tent', 'anypress' ); ?>" style="aspect-ratio:4/5;object-fit:cover"/></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center"} -->
<div class="wp-block-column is-vertically-aligned-center"><!-- wp:paragraph {"textColor":"secondary","fontSize":"small","style":{"typography":{"fontWeight":"700","letterSpacing":"0.1em","textTransform":"uppercase"}}} -->
<p class="has-secondary-color has-text-color has-small-font-size" style="font-weight:700;letter-spacing:0.1em;text-transform:uppercase"><?php esc_html_e( 'Shop the look', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'Weekend, sorted', 'anypress' ); ?></h2>
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
