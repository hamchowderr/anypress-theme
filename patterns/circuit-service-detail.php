<?php
/**
 * Title: Circuit service: what's included and the price
 * Slug: anypress/circuit-service-detail
 * Description: The body of one service page: what the service covers in plain words, a list of what's included, a photo, and a rounded price card with the starting price and buttons to book or call. Part of the Circuit kit.
 * Categories: anypress/kit-electrical
 * Keywords: service, details, included, price, book, electrician, circuit
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Service details"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:columns {"verticalAlignment":"top","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|x-large","left":"var:preset|spacing|x-large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-top"><!-- wp:column {"width":"60%"} -->
<div class="wp-block-column" style="flex-basis:60%"><!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'What\'s included', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><?php esc_html_e( 'A home charger needs its own circuit, the right breaker and a panel that can take the load. We check all three before we quote, so the price is the price.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:list {"fontSize":"medium"} -->
<ul class="wp-block-list has-medium-font-size"><!-- wp:list-item -->
<li><?php esc_html_e( 'A load check of your panel and supply', 'anypress' ); ?></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><?php esc_html_e( 'A dedicated 240-volt circuit and breaker', 'anypress' ); ?></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><?php esc_html_e( 'Fitting and testing your charger, any brand', 'anypress' ); ?></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><?php esc_html_e( 'The permit and inspection', 'anypress' ); ?></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><?php esc_html_e( 'Help with your utility\'s rebate paperwork', 'anypress' ); ?></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none","aspectRatio":"16/9","scale":"cover","style":{"border":{"radius":"var:preset|border-radius|lg"}}} -->
<figure class="wp-block-image size-large has-custom-border"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-wide.svg' ) ); ?>" alt="<?php esc_attr_e( 'Photo of the service: rows of breakers in an electrical distribution board', 'anypress' ); ?>" style="border-radius:var(--wp--preset--border-radius--lg);aspect-ratio:16/9;object-fit:cover"/></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {"className":"is-style-section-tint","style":{"spacing":{"padding":{"top":"var:preset|spacing|large","bottom":"var:preset|spacing|large","left":"var:preset|spacing|large","right":"var:preset|spacing|large"},"blockGap":"var:preset|spacing|small"},"border":{"radius":"var:preset|border-radius|lg"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-section-tint" style="padding-top:var(--wp--preset--spacing--large);padding-bottom:var(--wp--preset--spacing--large);padding-left:var(--wp--preset--spacing--large);padding-right:var(--wp--preset--spacing--large);border-radius:var(--wp--preset--border-radius--lg)"><!-- wp:paragraph {"textColor":"primary","fontSize":"x-small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.12em","fontWeight":"700"}}} -->
<p class="has-primary-color has-text-color has-x-small-font-size" style="text-transform:uppercase;letter-spacing:0.12em;font-weight:700"><?php esc_html_e( 'EV chargers', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontFamily":"schibsted-grotesk","fontSize":"xxx-large","style":{"typography":{"fontWeight":"800","lineHeight":"1"}}} -->
<p class="has-schibsted-grotesk-font-family has-xxx-large-font-size" style="font-weight:800;line-height:1"><?php esc_html_e( 'From $950', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><?php esc_html_e( 'Most garage installs, with the charger supplied by you. Long cable runs or a panel upgrade are quoted first.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/book-a-visit/"><?php esc_html_e( 'Book a visit', 'anypress' ); ?></a></div>
<!-- /wp:button -->

<!-- wp:button {"metadata":{"bindings":{"url":{"source":"anypress/site-details","args":{"key":"phone_link"}},"text":{"source":"anypress/site-details","args":{"key":"phone"}}}},"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="tel:5550187"><?php esc_html_e( 'Call 555 0187', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->
