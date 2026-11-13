<?php
/**
 * Title: Branch hero: one promise, six locations
 * Slug: anypress/branch-hero
 * Description: Opening section for a franchise: a big friendly headline, one sentence, a trial button and a find-a-location button, the number of locations, and a large photo. Part of the Branch kit; use the owner's own photo.
 * Categories: anypress/kit-franchise
 * Keywords: hero, franchise, locations, swim school, kids, booking, branch
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Hero"},"align":"full","className":"is-style-section-brand-soft","style":{"spacing":{"padding":{"top":"var:preset|spacing|x-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull is-style-section-brand-soft" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--x-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:columns {"verticalAlignment":"center","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|xx-large","left":"var:preset|spacing|xx-large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-center"><!-- wp:column {"verticalAlignment":"center","width":"50%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:50%"><!-- wp:paragraph {"textColor":"primary","fontSize":"small","style":{"typography":{"fontWeight":"700","letterSpacing":"0.04em","textTransform":"uppercase"}}} -->
<p class="has-primary-color has-text-color has-small-font-size" style="font-weight:700;letter-spacing:0.04em;text-transform:uppercase"><?php esc_html_e( 'Swim lessons for every age', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1,"fontSize":"xxx-large","style":{"typography":{"lineHeight":"0.98"}}} -->
<h1 class="wp-block-heading has-xxx-large-font-size" style="line-height:0.98"><?php esc_html_e( 'Happy, safe swimmers at six warm pools across Texas', 'anypress' ); ?></h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"large"} -->
<p class="has-large-font-size"><?php esc_html_e( 'Small classes of four, water at 90°F and instructors trained the same way at every pool. Your first lesson is free.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/book-a-trial/"><?php esc_html_e( 'Book a free trial', 'anypress' ); ?></a></div>
<!-- /wp:button -->

<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/locations/"><?php esc_html_e( 'Find a pool near you', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|medium"}},"layout":{"type":"flex","justifyContent":"left"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-small-font-size" style="font-weight:700"><?php esc_html_e( '★ 4.9 from 2,300 families', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-small-font-size" style="font-weight:700"><?php esc_html_e( '6 pools', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small","style":{"typography":{"fontWeight":"700"}}} -->
<p class="has-small-font-size" style="font-weight:700"><?php esc_html_e( 'Since 2012', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:image {"sizeSlug":"large","linkDestination":"none","aspectRatio":"4/5","scale":"cover","style":{"border":{"radius":"var:preset|border-radius|lg"}}} -->
<figure class="wp-block-image size-large has-custom-border"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-tall.svg' ) ); ?>" alt="<?php esc_attr_e( 'Two girls in goggles smiling at the side of the pool', 'anypress' ); ?>" style="border-radius:var(--wp--preset--border-radius--lg);aspect-ratio:4/5;object-fit:cover"/></figure>
<!-- /wp:image --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->
