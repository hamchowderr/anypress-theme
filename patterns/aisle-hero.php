<?php
/**
 * Title: Aisle hero: a full-width photo with two ways in
 * Slug: anypress/aisle-hero
 * Description: The first thing visitors see: a full-screen photo of the clothes being worn, the promise centred in a large serif and two buttons, one to what's new and one to the whole shop. Part of the Aisle kit; use a real photo of the shop's own clothes.
 * Categories: anypress/kit-store
 * Keywords: hero, banner, photo, new collection, shop, aisle
 * Viewport Width: 1400
 */
?>
<!-- wp:cover {"url":"<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-wide.svg' ) ); ?>","dimRatio":30,"overlayColor":"main","isUserOverlayColor":true,"minHeight":92,"minHeightUnit":"vh","contentPosition":"bottom center","align":"full","metadata":{"name":"Hero"},"style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large","left":"var:preset|spacing|medium","right":"var:preset|spacing|medium"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"60rem"}} -->
<div class="wp-block-cover alignfull has-custom-content-position is-position-bottom-center" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large);padding-left:var(--wp--preset--spacing--medium);padding-right:var(--wp--preset--spacing--medium);min-height:92vh"><img class="wp-block-cover__image-background" alt="" src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-wide.svg' ) ); ?>" data-object-fit="cover"/><span aria-hidden="true" class="wp-block-cover__background has-main-background-color has-background-dim-30 has-background-dim"></span><div class="wp-block-cover__inner-container"><!-- wp:paragraph {"align":"center","textColor":"base","fontSize":"x-small","style":{"typography":{"fontWeight":"600","letterSpacing":"0.14em","textTransform":"uppercase"}}} -->
<p class="has-text-align-center has-base-color has-text-color has-x-small-font-size" style="font-weight:600;letter-spacing:0.14em;text-transform:uppercase"><?php esc_html_e( 'The winter collection', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"textAlign":"center","level":1,"fontSize":"poster","style":{"typography":{"lineHeight":"0.95"}}} -->
<h1 class="wp-block-heading has-text-align-center has-poster-font-size" style="line-height:0.95"><?php esc_html_e( 'Everyday clothes, made to last.', 'anypress' ); ?></h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","fontSize":"medium"} -->
<p class="has-text-align-center has-medium-font-size"><?php esc_html_e( 'Hoodies, tees and jackets from two family mills, cut to fit and packed by hand.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/new-in/"><?php esc_html_e( 'Shop new in', 'anypress' ); ?></a></div>
<!-- /wp:button -->

<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/shop/"><?php esc_html_e( 'Shop everything', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div></div>
<!-- /wp:cover -->
