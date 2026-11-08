<?php
/**
 * Title: Market page: Hearth kit (one stall)
 * Slug: anypress/hearth-page-area
 * Description: A page for one market stall: a heading, when and where with a map, photos from the oven, reviews and the practical details. Hearth kit; make one per market.
 * Categories: anypress/pages
 * Keywords: market, stall, farmers market, location, hearth
 * Viewport Width: 1400
 * Block Types: core/post-content
 * Post Types: page
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Page hero"},"align":"full","className":"is-style-section-tint","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|x-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"72rem"}} -->
<section class="wp-block-group alignfull is-style-section-tint" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--x-large)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|medium"}},"layout":{"type":"constrained","contentSize":"46rem","justifyContent":"left"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"textColor":"secondary","fontSize":"small","style":{"typography":{"fontStyle":"italic"}}} -->
<p class="has-secondary-color has-text-color has-small-font-size" style="font-style:italic"><?php esc_html_e( 'Markets / Downtown', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1,"fontSize":"xxx-large"} -->
<h1 class="wp-block-heading has-xxx-large-font-size"><?php esc_html_e( 'Downtown Saturday market', 'anypress' ); ?></h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"large"} -->
<p class="has-secondary-color has-text-color has-large-font-size"><?php esc_html_e( 'Every loaf from the shop and the full pastry table, under the clock on Main Square.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/order/"><?php esc_html_e( 'Order for pickup', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></section>
<!-- /wp:group -->

<!-- wp:group {"tagName":"section","metadata":{"name":"Market"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:columns {"verticalAlignment":"top","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|x-large","left":"var:preset|spacing|x-large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-top"><!-- wp:column {"width":"42%"} -->
<div class="wp-block-column" style="flex-basis:42%"><!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'Under the clock on Main Square', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontFamily":"young-serif","fontSize":"large"} -->
<p class="has-young-serif-font-family has-large-font-size"><?php esc_html_e( 'Saturdays, 8am to 1pm, all year except the two weeks after Christmas.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"medium"} -->
<p class="has-medium-font-size"><?php esc_html_e( 'Look for the olive awning by the clock. Luca runs it with two of the bakers, and there\'s coffee from the van from 8.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:list {"fontSize":"medium"} -->
<ul class="wp-block-list has-medium-font-size"><!-- wp:list-item -->
<li><?php esc_html_e( 'Every loaf from the shop', 'anypress' ); ?></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><?php esc_html_e( 'The full pastry table', 'anypress' ); ?></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><?php esc_html_e( 'Whole cakes to order, picked up here', 'anypress' ); ?></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><?php esc_html_e( 'Cards and cash', 'anypress' ); ?></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/order/"><?php esc_html_e( 'Order for pickup here', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:anypress/map {"address":"Main Square, Springfield, IL","lat":39.8017,"lon":-89.6436,"zoom":16,"aspect":"4/3"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->

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

<!-- wp:group {"tagName":"section","metadata":{"name":"Reviews"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:group {"layout":{"type":"flex","justifyContent":"space-between","verticalAlignment":"bottom"}} -->
<div class="wp-block-group"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:heading {"fontSize":"xxx-large"} -->
<h2 class="wp-block-heading has-xxx-large-font-size"><?php esc_html_e( 'Kind words', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"medium","style":{"typography":{"fontStyle":"italic"}}} -->
<p class="has-secondary-color has-text-color has-medium-font-size" style="font-style:italic"><?php esc_html_e( 'From the people in the queue', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/reviews/"><?php esc_html_e( 'All reviews', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group -->

<!-- wp:anypress/carousel {"perView":3,"label":"Reviews"} -->
<!-- wp:group {"className":"is-style-section-card","style":{"spacing":{"padding":{"top":"var:preset|spacing|large","bottom":"var:preset|spacing|large","left":"var:preset|spacing|large","right":"var:preset|spacing|large"},"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-section-card" style="padding-top:var(--wp--preset--spacing--large);padding-bottom:var(--wp--preset--spacing--large);padding-left:var(--wp--preset--spacing--large);padding-right:var(--wp--preset--spacing--large)"><!-- wp:paragraph {"fontFamily":"young-serif","fontSize":"medium","style":{"typography":{"lineHeight":"1.4"}}} -->
<p class="has-young-serif-font-family has-medium-font-size" style="line-height:1.4"><?php esc_html_e( '“The rye is the best I\'ve had outside my grandmother\'s kitchen. We drive in every Saturday for it.”', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"small","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-secondary-color has-text-color has-small-font-size" style="font-weight:700"><?php esc_html_e( 'Anna K., Regular since 2004', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"className":"is-style-section-card","style":{"spacing":{"padding":{"top":"var:preset|spacing|large","bottom":"var:preset|spacing|large","left":"var:preset|spacing|large","right":"var:preset|spacing|large"},"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-section-card" style="padding-top:var(--wp--preset--spacing--large);padding-bottom:var(--wp--preset--spacing--large);padding-left:var(--wp--preset--spacing--large);padding-right:var(--wp--preset--spacing--large)"><!-- wp:paragraph {"fontFamily":"young-serif","fontSize":"medium","style":{"typography":{"lineHeight":"1.4"}}} -->
<p class="has-young-serif-font-family has-medium-font-size" style="line-height:1.4"><?php esc_html_e( '“They made our wedding cake in eight days and it was perfect. Three tiers, lemon and elderflower.”', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"small","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-secondary-color has-text-color has-small-font-size" style="font-weight:700"><?php esc_html_e( 'Jordan and Lee, Wedding cake', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"className":"is-style-section-card","style":{"spacing":{"padding":{"top":"var:preset|spacing|large","bottom":"var:preset|spacing|large","left":"var:preset|spacing|large","right":"var:preset|spacing|large"},"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-section-card" style="padding-top:var(--wp--preset--spacing--large);padding-bottom:var(--wp--preset--spacing--large);padding-left:var(--wp--preset--spacing--large);padding-right:var(--wp--preset--spacing--large)"><!-- wp:paragraph {"fontFamily":"young-serif","fontSize":"medium","style":{"typography":{"lineHeight":"1.4"}}} -->
<p class="has-young-serif-font-family has-medium-font-size" style="line-height:1.4"><?php esc_html_e( '“Get there before nine or the almond croissants are gone. Worth the alarm.”', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"small","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-secondary-color has-text-color has-small-font-size" style="font-weight:700"><?php esc_html_e( 'Sam R., Saturday regular', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"className":"is-style-section-card","style":{"spacing":{"padding":{"top":"var:preset|spacing|large","bottom":"var:preset|spacing|large","left":"var:preset|spacing|large","right":"var:preset|spacing|large"},"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-section-card" style="padding-top:var(--wp--preset--spacing--large);padding-bottom:var(--wp--preset--spacing--large);padding-left:var(--wp--preset--spacing--large);padding-right:var(--wp--preset--spacing--large)"><!-- wp:paragraph {"fontFamily":"young-serif","fontSize":"medium","style":{"typography":{"lineHeight":"1.4"}}} -->
<p class="has-young-serif-font-family has-medium-font-size" style="line-height:1.4"><?php esc_html_e( '“A proper lunch: soup, bread, a slab of tart and the nicest people behind the counter.”', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"small","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-secondary-color has-text-color has-small-font-size" style="font-weight:700"><?php esc_html_e( 'Priya N., Works on Market Street', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"className":"is-style-section-card","style":{"spacing":{"padding":{"top":"var:preset|spacing|large","bottom":"var:preset|spacing|large","left":"var:preset|spacing|large","right":"var:preset|spacing|large"},"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-section-card" style="padding-top:var(--wp--preset--spacing--large);padding-bottom:var(--wp--preset--spacing--large);padding-left:var(--wp--preset--spacing--large);padding-right:var(--wp--preset--spacing--large)"><!-- wp:paragraph {"fontFamily":"young-serif","fontSize":"medium","style":{"typography":{"lineHeight":"1.4"}}} -->
<p class="has-young-serif-font-family has-medium-font-size" style="line-height:1.4"><?php esc_html_e( '“They fed forty people at our office breakfast and remembered every allergy.”', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"small","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-secondary-color has-text-color has-small-font-size" style="font-weight:700"><?php esc_html_e( 'Marcus T., Catering order', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"className":"is-style-section-card","style":{"spacing":{"padding":{"top":"var:preset|spacing|large","bottom":"var:preset|spacing|large","left":"var:preset|spacing|large","right":"var:preset|spacing|large"},"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-section-card" style="padding-top:var(--wp--preset--spacing--large);padding-bottom:var(--wp--preset--spacing--large);padding-left:var(--wp--preset--spacing--large);padding-right:var(--wp--preset--spacing--large)"><!-- wp:paragraph {"fontFamily":"young-serif","fontSize":"medium","style":{"typography":{"lineHeight":"1.4"}}} -->
<p class="has-young-serif-font-family has-medium-font-size" style="line-height:1.4"><?php esc_html_e( '“Luca taught my son to shape a loaf on a quiet Tuesday. That\'s the kind of place it is.”', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"small","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-secondary-color has-text-color has-small-font-size" style="font-weight:700"><?php esc_html_e( 'Elena P., Neighbour', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->
<!-- /wp:anypress/carousel --></section>
<!-- /wp:group -->
