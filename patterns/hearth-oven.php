<?php
/**
 * Title: Hearth from the oven: photos that open full screen
 * Slug: anypress/hearth-oven
 * Description: Photos of the food in a carousel, each opening full screen when clicked, with a line saying what it is. Needs the AnyPress Blocks plugin. Part of the Hearth kit; use the owner's own photos.
 * Categories: anypress/kit-food
 * Keywords: gallery, photos, food, carousel, lightbox, bakery, hearth
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"From the oven"},"align":"full","className":"is-style-section-tint","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull is-style-section-tint" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:group {"layout":{"type":"flex","justifyContent":"space-between","verticalAlignment":"bottom"}} -->
<div class="wp-block-group"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:heading {"fontSize":"xxx-large"} -->
<h2 class="wp-block-heading has-xxx-large-font-size"><?php esc_html_e( 'From the oven', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"medium","style":{"typography":{"fontStyle":"italic"}}} -->
<p class="has-secondary-color has-text-color has-medium-font-size" style="font-style:italic"><?php esc_html_e( 'This morning\'s bake, more or less', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->

<!-- wp:anypress/carousel {"perView":3,"autoplay":6,"label":"Photos from the bakery"} -->
<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","aspectRatio":"1","scale":"cover"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-square.svg' ) ); ?>" alt="<?php esc_attr_e( 'From the oven: country loaves cooling on a rack', 'anypress' ); ?>" style="aspect-ratio:1;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"textColor":"secondary","style":{"typography":{"fontStyle":"italic"}}} -->
<p class="has-secondary-color has-text-color" style="font-style:italic"><?php esc_html_e( 'Country loaves, cooling', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","aspectRatio":"1","scale":"cover"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-square.svg' ) ); ?>" alt="<?php esc_attr_e( 'From the oven: a tray of croissants', 'anypress' ); ?>" style="aspect-ratio:1;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"textColor":"secondary","style":{"typography":{"fontStyle":"italic"}}} -->
<p class="has-secondary-color has-text-color" style="font-style:italic"><?php esc_html_e( 'Croissants, laminated by hand', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","aspectRatio":"1","scale":"cover"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-square.svg' ) ); ?>" alt="<?php esc_attr_e( 'From the oven: a baker shaping dough on a floured bench', 'anypress' ); ?>" style="aspect-ratio:1;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"textColor":"secondary","style":{"typography":{"fontStyle":"italic"}}} -->
<p class="has-secondary-color has-text-color" style="font-style:italic"><?php esc_html_e( 'Shaping the rye at 4am', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","aspectRatio":"1","scale":"cover"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-square.svg' ) ); ?>" alt="<?php esc_attr_e( 'From the oven: a slice of cake with berries', 'anypress' ); ?>" style="aspect-ratio:1;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"textColor":"secondary","style":{"typography":{"fontStyle":"italic"}}} -->
<p class="has-secondary-color has-text-color" style="font-style:italic"><?php esc_html_e( 'Cake of the day', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","aspectRatio":"1","scale":"cover"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-square.svg' ) ); ?>" alt="<?php esc_attr_e( 'From the oven: coffee being poured at the counter', 'anypress' ); ?>" style="aspect-ratio:1;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"textColor":"secondary","style":{"typography":{"fontStyle":"italic"}}} -->
<p class="has-secondary-color has-text-color" style="font-style:italic"><?php esc_html_e( 'The first coffee of the day', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->
<!-- /wp:anypress/carousel --></section>
<!-- /wp:group -->
