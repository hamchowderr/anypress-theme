<?php
/**
 * Title: Workshop city page: Chapter kit (one city)
 * Slug: anypress/chapter-page-area
 * Description: A page for the workshops in one city, such as Portland: a heading, the weekend in a few lines with a map, the next dates, students' drawings and a closing band. Chapter kit; make one per city under Workshops.
 * Categories: anypress/pages
 * Keywords: workshop, city, in person, location, dates, chapter
 * Viewport Width: 1400
 * Block Types: core/post-content
 * Post Types: page
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Page hero"},"align":"full","className":"is-style-section-second-brand","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|x-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull is-style-section-second-brand" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--x-large)"><!-- wp:paragraph {"textColor":"primary-alt-accent","fontFamily":"monospace","fontSize":"small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.08em"}}} -->
<p class="has-primary-alt-accent-color has-text-color has-monospace-font-family has-small-font-size" style="text-transform:uppercase;letter-spacing:0.08em"><?php esc_html_e( 'Workshops / Portland', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1,"fontSize":"xxx-large"} -->
<h1 class="wp-block-heading has-xxx-large-font-size"><?php esc_html_e( 'Portland', 'anypress' ); ?></h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"medium"} -->
<p class="has-medium-font-size"><?php esc_html_e( 'Drawing weekends at the home studio, with a model, good coffee and twelve people at most.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/join/"><?php esc_html_e( 'Save a place', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></section>
<!-- /wp:group -->

<!-- wp:group {"tagName":"section","metadata":{"name":"Weekend"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:columns {"verticalAlignment":"top","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|x-large","left":"var:preset|spacing|x-large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-top"><!-- wp:column {"width":"50%"} -->
<div class="wp-block-column" style="flex-basis:50%"><!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'A weekend at the studio', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><?php esc_html_e( 'Two days, ten till four, in the studio where the courses are filmed. Saturday is gesture and proportion with a model; Sunday we draw faces in the morning and go out to sketch the neighbourhood after lunch.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:list {"fontSize":"medium"} -->
<ul class="wp-block-list has-medium-font-size"><!-- wp:list-item -->
<li><?php esc_html_e( 'Twelve places, so everyone gets time with Mara', 'anypress' ); ?></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><?php esc_html_e( 'Paper, boards and lunch included', 'anypress' ); ?></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><?php esc_html_e( '$290 for the weekend, $240 for members', 'anypress' ); ?></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:anypress/map {"address":"Portland, Oregon","lat":45.5221,"lon":-122.661,"zoom":14,"aspect":"4/3"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->

<!-- wp:group {"tagName":"section","metadata":{"name":"Dates"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"64rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:group {"layout":{"type":"flex","justifyContent":"space-between","verticalAlignment":"bottom"}} -->
<div class="wp-block-group"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"textColor":"primary","fontFamily":"monospace","fontSize":"small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.08em"}}} -->
<p class="has-primary-color has-text-color has-monospace-font-family has-small-font-size" style="text-transform:uppercase;letter-spacing:0.08em"><?php esc_html_e( 'Dates', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'The next weekends', 'anypress' ); ?></h2>
<!-- /wp:heading --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|medium"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:columns {"verticalAlignment":"center","isStackedOnMobile":false,"style":{"spacing":{"blockGap":{"top":"var:preset|spacing|large","left":"var:preset|spacing|large"}}}} -->
<div class="wp-block-columns are-vertically-aligned-center is-not-stacked-on-mobile"><!-- wp:column {"width":"5.5rem"} -->
<div class="wp-block-column" style="flex-basis:5.5rem"><!-- wp:group {"className":"is-style-section-brand","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small","left":"var:preset|spacing|small","right":"var:preset|spacing|small"},"blockGap":"var:preset|spacing|x-small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-section-brand" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small);padding-left:var(--wp--preset--spacing--small);padding-right:var(--wp--preset--spacing--small)"><!-- wp:paragraph {"align":"center","fontFamily":"fraunces","fontSize":"x-large","style":{"typography":{"lineHeight":"1","fontWeight":"700"}}} -->
<p class="has-text-align-center has-fraunces-font-family has-x-large-font-size" style="line-height:1;font-weight:700"><?php esc_html_e( '14', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"center","fontSize":"small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.08em"}}} -->
<p class="has-text-align-center has-small-font-size" style="text-transform:uppercase;letter-spacing:0.08em"><?php esc_html_e( 'Mar', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center"} -->
<div class="wp-block-column is-vertically-aligned-center"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|x-small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:heading {"level":3,"fontSize":"large"} -->
<h3 class="wp-block-heading has-large-font-size"><?php esc_html_e( 'Portland: drawing people from life', 'anypress' ); ?></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'Sat and Sun, 10am to 4pm · The home studio', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="/join/"><?php esc_html_e( 'Save a place', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:columns {"verticalAlignment":"center","isStackedOnMobile":false,"style":{"spacing":{"blockGap":{"top":"var:preset|spacing|large","left":"var:preset|spacing|large"}}}} -->
<div class="wp-block-columns are-vertically-aligned-center is-not-stacked-on-mobile"><!-- wp:column {"width":"5.5rem"} -->
<div class="wp-block-column" style="flex-basis:5.5rem"><!-- wp:group {"className":"is-style-section-brand","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small","left":"var:preset|spacing|small","right":"var:preset|spacing|small"},"blockGap":"var:preset|spacing|x-small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-section-brand" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small);padding-left:var(--wp--preset--spacing--small);padding-right:var(--wp--preset--spacing--small)"><!-- wp:paragraph {"align":"center","fontFamily":"fraunces","fontSize":"x-large","style":{"typography":{"lineHeight":"1","fontWeight":"700"}}} -->
<p class="has-text-align-center has-fraunces-font-family has-x-large-font-size" style="line-height:1;font-weight:700"><?php esc_html_e( '11', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"center","fontSize":"small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.08em"}}} -->
<p class="has-text-align-center has-small-font-size" style="text-transform:uppercase;letter-spacing:0.08em"><?php esc_html_e( 'Apr', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center"} -->
<div class="wp-block-column is-vertically-aligned-center"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|x-small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:heading {"level":3,"fontSize":"large"} -->
<h3 class="wp-block-heading has-large-font-size"><?php esc_html_e( 'Seattle: faces and portraits', 'anypress' ); ?></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'Sat and Sun, 10am to 4pm · Pike Street Studios', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="/join/"><?php esc_html_e( 'Save a place', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:columns {"verticalAlignment":"center","isStackedOnMobile":false,"style":{"spacing":{"blockGap":{"top":"var:preset|spacing|large","left":"var:preset|spacing|large"}}}} -->
<div class="wp-block-columns are-vertically-aligned-center is-not-stacked-on-mobile"><!-- wp:column {"width":"5.5rem"} -->
<div class="wp-block-column" style="flex-basis:5.5rem"><!-- wp:group {"className":"is-style-section-brand","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small","left":"var:preset|spacing|small","right":"var:preset|spacing|small"},"blockGap":"var:preset|spacing|x-small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-section-brand" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small);padding-left:var(--wp--preset--spacing--small);padding-right:var(--wp--preset--spacing--small)"><!-- wp:paragraph {"align":"center","fontFamily":"fraunces","fontSize":"x-large","style":{"typography":{"lineHeight":"1","fontWeight":"700"}}} -->
<p class="has-text-align-center has-fraunces-font-family has-x-large-font-size" style="line-height:1;font-weight:700"><?php esc_html_e( '09', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"center","fontSize":"small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.08em"}}} -->
<p class="has-text-align-center has-small-font-size" style="text-transform:uppercase;letter-spacing:0.08em"><?php esc_html_e( 'May', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center"} -->
<div class="wp-block-column is-vertically-aligned-center"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|x-small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:heading {"level":3,"fontSize":"large"} -->
<h3 class="wp-block-heading has-large-font-size"><?php esc_html_e( 'San Francisco: urban sketching', 'anypress' ); ?></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'Sat and Sun, 9am to 3pm · Meet at the Ferry Building', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="/join/"><?php esc_html_e( 'Save a place', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:columns {"verticalAlignment":"center","isStackedOnMobile":false,"style":{"spacing":{"blockGap":{"top":"var:preset|spacing|large","left":"var:preset|spacing|large"}}}} -->
<div class="wp-block-columns are-vertically-aligned-center is-not-stacked-on-mobile"><!-- wp:column {"width":"5.5rem"} -->
<div class="wp-block-column" style="flex-basis:5.5rem"><!-- wp:group {"className":"is-style-section-brand","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small","left":"var:preset|spacing|small","right":"var:preset|spacing|small"},"blockGap":"var:preset|spacing|x-small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-section-brand" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small);padding-left:var(--wp--preset--spacing--small);padding-right:var(--wp--preset--spacing--small)"><!-- wp:paragraph {"align":"center","fontFamily":"fraunces","fontSize":"x-large","style":{"typography":{"lineHeight":"1","fontWeight":"700"}}} -->
<p class="has-text-align-center has-fraunces-font-family has-x-large-font-size" style="line-height:1;font-weight:700"><?php esc_html_e( '13', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"center","fontSize":"small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.08em"}}} -->
<p class="has-text-align-center has-small-font-size" style="text-transform:uppercase;letter-spacing:0.08em"><?php esc_html_e( 'Jun', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center"} -->
<div class="wp-block-column is-vertically-aligned-center"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|x-small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:heading {"level":3,"fontSize":"large"} -->
<h3 class="wp-block-heading has-large-font-size"><?php esc_html_e( 'Denver: drawing people from life', 'anypress' ); ?></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'Sat and Sun, 10am to 4pm · RiNo Art Hall', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="/join/"><?php esc_html_e( 'Save a place', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:columns {"verticalAlignment":"center","isStackedOnMobile":false,"style":{"spacing":{"blockGap":{"top":"var:preset|spacing|large","left":"var:preset|spacing|large"}}}} -->
<div class="wp-block-columns are-vertically-aligned-center is-not-stacked-on-mobile"><!-- wp:column {"width":"5.5rem"} -->
<div class="wp-block-column" style="flex-basis:5.5rem"><!-- wp:group {"className":"is-style-section-brand","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small","left":"var:preset|spacing|small","right":"var:preset|spacing|small"},"blockGap":"var:preset|spacing|x-small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-section-brand" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small);padding-left:var(--wp--preset--spacing--small);padding-right:var(--wp--preset--spacing--small)"><!-- wp:paragraph {"align":"center","fontFamily":"fraunces","fontSize":"x-large","style":{"typography":{"lineHeight":"1","fontWeight":"700"}}} -->
<p class="has-text-align-center has-fraunces-font-family has-x-large-font-size" style="line-height:1;font-weight:700"><?php esc_html_e( '12', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"center","fontSize":"small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.08em"}}} -->
<p class="has-text-align-center has-small-font-size" style="text-transform:uppercase;letter-spacing:0.08em"><?php esc_html_e( 'Sep', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center"} -->
<div class="wp-block-column is-vertically-aligned-center"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|x-small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:heading {"level":3,"fontSize":"large"} -->
<h3 class="wp-block-heading has-large-font-size"><?php esc_html_e( 'Chicago: urban sketching', 'anypress' ); ?></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'Sat and Sun, 9am to 3pm · Meet at the Cultural Center', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="/join/"><?php esc_html_e( 'Save a place', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:columns {"verticalAlignment":"center","isStackedOnMobile":false,"style":{"spacing":{"blockGap":{"top":"var:preset|spacing|large","left":"var:preset|spacing|large"}}}} -->
<div class="wp-block-columns are-vertically-aligned-center is-not-stacked-on-mobile"><!-- wp:column {"width":"5.5rem"} -->
<div class="wp-block-column" style="flex-basis:5.5rem"><!-- wp:group {"className":"is-style-section-brand","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small","left":"var:preset|spacing|small","right":"var:preset|spacing|small"},"blockGap":"var:preset|spacing|x-small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-section-brand" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small);padding-left:var(--wp--preset--spacing--small);padding-right:var(--wp--preset--spacing--small)"><!-- wp:paragraph {"align":"center","fontFamily":"fraunces","fontSize":"x-large","style":{"typography":{"lineHeight":"1","fontWeight":"700"}}} -->
<p class="has-text-align-center has-fraunces-font-family has-x-large-font-size" style="line-height:1;font-weight:700"><?php esc_html_e( '10', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"center","fontSize":"small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.08em"}}} -->
<p class="has-text-align-center has-small-font-size" style="text-transform:uppercase;letter-spacing:0.08em"><?php esc_html_e( 'Oct', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center"} -->
<div class="wp-block-column is-vertically-aligned-center"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|x-small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:heading {"level":3,"fontSize":"large"} -->
<h3 class="wp-block-heading has-large-font-size"><?php esc_html_e( 'Brooklyn: faces and portraits', 'anypress' ); ?></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'Sat and Sun, 10am to 4pm · Dumbo Drawing Room', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="/join/"><?php esc_html_e( 'Save a place', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group --></section>
<!-- /wp:group -->

<!-- wp:group {"tagName":"section","metadata":{"name":"Gallery"},"align":"full","className":"is-style-section-tint","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull is-style-section-tint" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:group {"layout":{"type":"flex","justifyContent":"space-between","verticalAlignment":"bottom"}} -->
<div class="wp-block-group"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"textColor":"primary","fontFamily":"monospace","fontSize":"small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.08em"}}} -->
<p class="has-primary-color has-text-color has-monospace-font-family has-small-font-size" style="text-transform:uppercase;letter-spacing:0.08em"><?php esc_html_e( 'Student work', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'Drawn in the first month', 'anypress' ); ?></h2>
<!-- /wp:heading --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->

<!-- wp:anypress/carousel {"perView":3,"autoplay":6,"label":"Drawings by students"} -->
<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","aspectRatio":"4/5","scale":"cover"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-tall.svg' ) ); ?>" alt="<?php esc_attr_e( 'A sketchbook open on a table with pencil drawings of people', 'anypress' ); ?>" style="aspect-ratio:4/5;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'Tom B., day 30 of Draw people in 30 days', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","aspectRatio":"4/5","scale":"cover"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-tall.svg' ) ); ?>" alt="<?php esc_attr_e( 'A pencil portrait of a woman\'s face on paper', 'anypress' ); ?>" style="aspect-ratio:4/5;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'Ana M., Faces and portraits', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","aspectRatio":"4/5","scale":"cover"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-tall.svg' ) ); ?>" alt="<?php esc_attr_e( 'Someone sketching a city street from a café table', 'anypress' ); ?>" style="aspect-ratio:4/5;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'Leo R., Urban sketching in Lisbon', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","aspectRatio":"4/5","scale":"cover"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-tall.svg' ) ); ?>" alt="<?php esc_attr_e( 'Pencil studies of hands on a sheet of paper', 'anypress' ); ?>" style="aspect-ratio:4/5;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'Daniel K., Hands and feet', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","aspectRatio":"4/5","scale":"cover"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-tall.svg' ) ); ?>" alt="<?php esc_attr_e( 'Watercolor paints and brushes beside a painted sketch', 'anypress' ); ?>" style="aspect-ratio:4/5;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'Hannah W., Watercolor for sketchers', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->
<!-- /wp:anypress/carousel --></section>
<!-- /wp:group -->

<!-- wp:group {"tagName":"section","metadata":{"name":"Join us"},"align":"full","className":"is-style-section-second-brand","style":{"spacing":{"padding":{"top":"var:preset|spacing|x-large","bottom":"var:preset|spacing|x-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull is-style-section-second-brand" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--x-large);padding-bottom:var(--wp--preset--spacing--x-large)"><!-- wp:columns {"verticalAlignment":"center","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|x-large","left":"var:preset|spacing|x-large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-center"><!-- wp:column {"verticalAlignment":"center","width":"60%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:60%"><!-- wp:heading {"fontSize":"xxx-large"} -->
<h2 class="wp-block-heading has-xxx-large-font-size"><?php esc_html_e( 'Start drawing this week', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"large"} -->
<p class="has-large-font-size"><?php esc_html_e( 'Courses from $49. Thirty days to change your mind.', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center"} -->
<div class="wp-block-column is-vertically-aligned-center"><!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/join/"><?php esc_html_e( 'Join a course', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons -->

<!-- wp:paragraph -->
<p><?php esc_html_e( 'Questions? Call or text', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"metadata":{"bindings":{"content":{"source":"anypress/site-details","args":{"key":"phone_linked"}}}},"fontFamily":"fraunces","fontSize":"xx-large","style":{"typography":{"lineHeight":"1","fontWeight":"600"}}} -->
<p class="has-fraunces-font-family has-xx-large-font-size" style="line-height:1;font-weight:600"><a href="tel:5550142"><?php esc_html_e( '555 0142', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->
