<?php
/**
 * Title: Aisle journal: the three latest posts
 * Slug: anypress/aisle-journal
 * Description: The three latest posts from the journal with a tall photo, title and date, under a centred title and a link to all posts. Part of the Aisle kit.
 * Categories: anypress/kit-store
 * Keywords: blog, journal, posts, style notes, care guides, aisle
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Journal"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"align":"center","textColor":"secondary","fontSize":"x-small","style":{"typography":{"fontWeight":"600","letterSpacing":"0.14em","textTransform":"uppercase"}}} -->
<p class="has-text-align-center has-secondary-color has-text-color has-x-small-font-size" style="font-weight:600;letter-spacing:0.14em;text-transform:uppercase"><?php esc_html_e( 'From the journal', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"textAlign":"center","fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-text-align-center has-xx-large-font-size"><?php esc_html_e( 'Style notes and care guides', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","fontSize":"x-small","style":{"typography":{"fontWeight":"600","letterSpacing":"0.14em","textTransform":"uppercase"}}} -->
<p class="has-text-align-center has-x-small-font-size" style="font-weight:600;letter-spacing:0.14em;text-transform:uppercase"><a href="/journal/"><?php esc_html_e( 'All posts', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:query {"queryId":31,"query":{"perPage":3,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false},"align":"wide","layout":{"type":"default"}} -->
<div class="wp-block-query alignwide"><!-- wp:post-template {"layout":{"type":"grid","columnCount":3}} -->
<!-- wp:post-featured-image {"isLink":true,"aspectRatio":"4/5"} /-->

<!-- wp:post-date {"fontSize":"x-small","textColor":"secondary"} /-->

<!-- wp:post-title {"isLink":true,"level":3,"fontSize":"large"} /-->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'New posts will appear here.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></section>
<!-- /wp:group -->
