<?php
/**
 * Title: Ridge footer: signup band, links, phone and the offer popup
 * Slug: anypress/ridge-footer
 * Description: A site footer for a trade: a band for joining the email list, then the phone number, services, company pages, address and hours on dark, and the new-customer offer popup (needs the AnyPress Blocks plugin). Part of the Ridge kit; choose it for the footer in the Site Editor.
 * Categories: footer
 * Keywords: footer, links, newsletter, signup, phone, address, hours, popup, ridge
 * Viewport Width: 1400
 * Block Types: core/template-part/footer
 */
?>
<!-- wp:group {"metadata":{"name":"Footer"},"align":"full","style":{"spacing":{"blockGap":"0"}},"layout":{"type":"default"}} -->
<div class="wp-block-group alignfull"><!-- wp:group {"tagName":"section","metadata":{"name":"Signup"},"anchor":"signup","align":"full","className":"is-style-section-second-brand","style":{"spacing":{"padding":{"top":"var:preset|spacing|x-large","bottom":"var:preset|spacing|x-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section id="signup" class="wp-block-group alignfull is-style-section-second-brand" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--x-large);padding-bottom:var(--wp--preset--spacing--x-large)"><!-- wp:columns {"verticalAlignment":"center","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|large","left":"var:preset|spacing|large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-center"><!-- wp:column {"verticalAlignment":"center","width":"55%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:55%"><!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'Get $50 off your next job', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"medium"} -->
<p class="has-medium-font-size"><?php esc_html_e( 'Join the list for seasonal checks, offers and the odd useful tip. Two emails a month at most.', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center"} -->
<div class="wp-block-column is-vertically-aligned-center"><!-- wp:group {"metadata":{"name":"Form: newsletter"},"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/special-offers/"><?php esc_html_e( 'Join the list', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"Footer columns"},"align":"full","className":"is-style-section-dark","style":{"spacing":{"padding":{"top":"var:preset|spacing|x-large","bottom":"var:preset|spacing|large"},"blockGap":"var:preset|spacing|large"}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-dark" style="padding-top:var(--wp--preset--spacing--x-large);padding-bottom:var(--wp--preset--spacing--large)"><!-- wp:columns {"verticalAlignment":"top","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|large","left":"var:preset|spacing|large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-top"><!-- wp:column {"width":"34%"} -->
<div class="wp-block-column" style="flex-basis:34%"><!-- wp:site-title {"level":0,"fontSize":"x-large"} /-->

<!-- wp:paragraph {"textColor":"main-accent"} -->
<p class="has-main-accent-color has-text-color"><?php esc_html_e( 'Plumbing and heating for homes and small businesses across the county since 2001. Licensed, insured, and on call day and night.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontFamily":"big-shoulders","fontSize":"xx-large","style":{"typography":{"fontWeight":"900","lineHeight":"1"}}} -->
<p class="has-big-shoulders-font-family has-xx-large-font-size" style="font-weight:900;line-height:1"><a href="tel:5550142"><?php esc_html_e( '555 0142', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:social-links {"layout":{"type":"flex"}} -->
<ul class="wp-block-social-links"><!-- wp:social-link {"url":"#","service":"facebook"} /-->

<!-- wp:social-link {"url":"#","service":"instagram"} /-->

<!-- wp:social-link {"url":"#","service":"google"} /--></ul>
<!-- /wp:social-links --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":3,"fontSize":"medium"} -->
<h3 class="wp-block-heading has-medium-font-size"><?php esc_html_e( 'Services', 'anypress' ); ?></h3>
<!-- /wp:heading -->

<!-- wp:list {"className":"is-style-no-bullets"} -->
<ul class="wp-block-list is-style-no-bullets"><!-- wp:list-item -->
<li><a href="/services/emergency-plumbing/"><?php esc_html_e( 'Emergency plumbing', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/services/leak-repair/"><?php esc_html_e( 'Leaks and burst pipes', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/services/drain-cleaning/"><?php esc_html_e( 'Drain cleaning', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/services/water-heaters/"><?php esc_html_e( 'Water heaters', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/services/heating/"><?php esc_html_e( 'Boilers and heating', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/services/bathrooms-and-kitchens/"><?php esc_html_e( 'Bathrooms and kitchens', 'anypress' ); ?></a></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":3,"fontSize":"medium"} -->
<h3 class="wp-block-heading has-medium-font-size"><?php esc_html_e( 'Company', 'anypress' ); ?></h3>
<!-- /wp:heading -->

<!-- wp:list {"className":"is-style-no-bullets"} -->
<ul class="wp-block-list is-style-no-bullets"><!-- wp:list-item -->
<li><a href="/about/"><?php esc_html_e( 'About us', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/reviews/"><?php esc_html_e( 'Reviews', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/service-areas/"><?php esc_html_e( 'Service areas', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/special-offers/"><?php esc_html_e( 'Special offers', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/careers/"><?php esc_html_e( 'Careers', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/blog/"><?php esc_html_e( 'Blog', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/faq/"><?php esc_html_e( 'FAQ', 'anypress' ); ?></a></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":3,"fontSize":"medium"} -->
<h3 class="wp-block-heading has-medium-font-size"><?php esc_html_e( 'Visit or call', 'anypress' ); ?></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"main-accent"} -->
<p class="has-main-accent-color has-text-color"><?php esc_html_e( '2140 Wabash Avenue, Springfield', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"main-accent"} -->
<p class="has-main-accent-color has-text-color"><?php esc_html_e( 'Office: 7am to 7pm, seven days', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"main-accent"} -->
<p class="has-main-accent-color has-text-color"><?php esc_html_e( 'Emergencies: day and night', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/get-a-quote/"><?php esc_html_e( 'Get a free quote', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:separator {"className":"is-style-wide"} -->
<hr class="wp-block-separator has-alpha-channel-opacity is-style-wide"/>
<!-- /wp:separator -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"textColor":"main-accent","fontSize":"small"} -->
<p class="has-main-accent-color has-text-color has-small-font-size"><?php esc_html_e( '© Clearwater Plumbing & Heating. Master plumber licence 48213.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"main-accent","fontSize":"small"} -->
<p class="has-main-accent-color has-text-color has-small-font-size"><a href="/privacy-policy/"><?php esc_html_e( 'Privacy', 'anypress' ); ?></a> · <a href="/contact/"><?php esc_html_e( 'Contact', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->

<!-- wp:anypress/popup {"popupId":"offer","trigger":"delay","delay":5,"showAgainDays":14,"size":"medium","label":"Offer for new customers","style":{"spacing":{"padding":{"top":"0","bottom":"var:preset|spacing|large","left":"0","right":"0"}}}} -->
<!-- wp:image {"sizeSlug":"large","linkDestination":"none","aspectRatio":"16/9","scale":"cover"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-wide.svg' ) ); ?>" alt="<?php esc_attr_e( 'A plumber\'s hands tightening a pipe fitting with a wrench', 'anypress' ); ?>" style="aspect-ratio:16/9;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:group {"style":{"spacing":{"padding":{"left":"var:preset|spacing|large","right":"var:preset|spacing|large"},"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group" style="padding-left:var(--wp--preset--spacing--large);padding-right:var(--wp--preset--spacing--large)"><!-- wp:paragraph {"textColor":"primary","fontFamily":"big-shoulders","fontSize":"small","style":{"typography":{"textTransform":"uppercase","fontWeight":"800","letterSpacing":"0.02em"}}} -->
<p class="has-primary-color has-text-color has-big-shoulders-font-family has-small-font-size" style="text-transform:uppercase;font-weight:800;letter-spacing:0.02em"><?php esc_html_e( 'New customers', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( '$50 off your first job', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><?php esc_html_e( 'Leave your email and we\'ll send the code. One email, no calls.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:group {"metadata":{"name":"Form: offer"},"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/special-offers/"><?php esc_html_e( 'See this month\'s offers', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
<!-- /wp:anypress/popup --></div>
<!-- /wp:group -->
