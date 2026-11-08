<?php
/**
 * Title: Hearth market: one stall, when and where
 * Slug: anypress/hearth-market
 * Description: The body of a page for one market stall: when it runs, where to find it and what's on the table, beside a map. Needs the AnyPress Blocks plugin for the map. Part of the Hearth kit; make one per market.
 * Categories: anypress/kit-food
 * Keywords: market, stall, farmers market, location, map, hearth
 * Viewport Width: 1400
 */
?>
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
