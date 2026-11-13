<?php
/**
 * Title: Commons directory: a map and every category
 * Slug: anypress/commons-directory-map
 * Description: Where to find members: every category of the member directory as a link to its own page, beside a map of the town. Needs the AnyPress Blocks plugin for the map. Part of the Commons kit.
 * Categories: anypress/kit-community
 * Keywords: directory, members, businesses, categories, map, find, commons
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Directory"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:columns {"verticalAlignment":"top","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|x-large","left":"var:preset|spacing|x-large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-top"><!-- wp:column {"width":"38%"} -->
<div class="wp-block-column" style="flex-basis:38%"><!-- wp:paragraph {"textColor":"primary-alt","fontSize":"x-small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.1em","fontWeight":"700"}}} -->
<p class="has-primary-alt-color has-text-color has-x-small-font-size" style="text-transform:uppercase;letter-spacing:0.1em;font-weight:700"><?php esc_html_e( 'Member directory', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'Find a member business', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"medium"} -->
<p class="has-secondary-color has-text-color has-medium-font-size"><?php esc_html_e( 'Shop local: 412 member businesses in Springfield and the villages around it.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:list {"className":"is-style-no-bullets","fontSize":"large","style":{"typography":{"lineHeight":"1.6","fontWeight":"600"}}} -->
<ul class="wp-block-list is-style-no-bullets has-large-font-size" style="line-height:1.6;font-weight:600"><!-- wp:list-item -->
<li><a href="/directory/food-and-drink/"><?php esc_html_e( 'Food and drink', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/directory/shops/"><?php esc_html_e( 'Shops', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/directory/trades-and-building/"><?php esc_html_e( 'Trades and building', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/directory/professional-services/"><?php esc_html_e( 'Professional services', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/directory/health-and-wellbeing/"><?php esc_html_e( 'Health and wellbeing', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/directory/arts-and-leisure/"><?php esc_html_e( 'Arts and leisure', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/directory/property/"><?php esc_html_e( 'Property', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/directory/nonprofits/"><?php esc_html_e( 'Nonprofits', 'anypress' ); ?></a></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:anypress/map {"address":"Springfield, Illinois","lat":39.799,"lon":-89.644,"zoom":13,"aspect":"4/3"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->
