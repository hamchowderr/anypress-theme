<?php
/**
 * Title: Chapter workshops: in-person weekends and a map
 * Slug: anypress/chapter-workshops-map
 * Description: Where the teacher runs in-person workshops: every city as a link to its own page, beside a map of the home studio. Needs the AnyPress Blocks plugin for the map. Part of the Chapter kit.
 * Categories: anypress/kit-courses
 * Keywords: workshops, in person, cities, locations, map, studio, chapter
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Workshops"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:columns {"verticalAlignment":"top","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|x-large","left":"var:preset|spacing|x-large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-top"><!-- wp:column {"width":"38%"} -->
<div class="wp-block-column" style="flex-basis:38%"><!-- wp:paragraph {"textColor":"primary","fontFamily":"monospace","fontSize":"small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.08em"}}} -->
<p class="has-primary-color has-text-color has-monospace-font-family has-small-font-size" style="text-transform:uppercase;letter-spacing:0.08em"><?php esc_html_e( 'In person', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'Draw with us for a weekend', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"medium"} -->
<p class="has-secondary-color has-text-color has-medium-font-size"><?php esc_html_e( 'Twice a year Mara takes the course on the road: two days of drawing from life with twelve people, in a studio near you.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:list {"className":"is-style-no-bullets","fontSize":"large","style":{"typography":{"lineHeight":"1.6","fontWeight":"600"}}} -->
<ul class="wp-block-list is-style-no-bullets has-large-font-size" style="line-height:1.6;font-weight:600"><!-- wp:list-item -->
<li><a href="/workshops/portland/"><?php esc_html_e( 'Portland', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/workshops/seattle/"><?php esc_html_e( 'Seattle', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/workshops/san-francisco/"><?php esc_html_e( 'San Francisco', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/workshops/denver/"><?php esc_html_e( 'Denver', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/workshops/chicago/"><?php esc_html_e( 'Chicago', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/workshops/brooklyn/"><?php esc_html_e( 'Brooklyn', 'anypress' ); ?></a></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:anypress/map {"address":"214 SE Ash Street, Portland, Oregon","lat":45.5221,"lon":-122.661,"zoom":14,"aspect":"4/3"} /-->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"small"} -->
<p class="has-secondary-color has-text-color has-small-font-size"><?php esc_html_e( 'The home studio, 214 SE Ash Street, Portland. Open for drop-in drawing on Thursday evenings.', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->
