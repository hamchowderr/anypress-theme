<?php
/**
 * Title: Circuit header: menu, phone and a Book a visit button
 * Slug: anypress/circuit-header
 * Description: A site header for an electrician that stays at the top while visitors scroll: a dark bar with the promise and hours, then the logo, the menu (with dropdowns for services and areas), the phone number and a Book a visit button. Part of the Circuit kit; choose it for the header in the Site Editor.
 * Categories: header
 * Keywords: header, menu, navigation, sticky, phone, book, electrician, circuit
 * Viewport Width: 1400
 * Block Types: core/template-part/header
 */
?>
<!-- wp:group {"metadata":{"name":"Header"},"align":"full","className":"is-style-sticky","style":{"spacing":{"blockGap":"0"}},"layout":{"type":"default"}} -->
<div class="wp-block-group alignfull is-style-sticky"><!-- wp:group {"metadata":{"name":"Top bar"},"align":"full","className":"is-style-section-dark","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-dark" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Same-day service across Columbus', 'anypress' ); ?> · <?php esc_html_e( 'Licensed and insured', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small","metadata":{"blockVisibility":{"viewport":{"mobile":false}}}} -->
<p class="has-small-font-size"><?php esc_html_e( 'Mon to Sat, 7am to 7pm · Emergencies 24/7:', 'anypress' ); ?> <a href="tel:5550187"><?php esc_html_e( '555 0187', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->

<!-- wp:group {"backgroundColor":"base","metadata":{"name":"Main bar"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull has-base-background-color has-background" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|medium"}},"layout":{"type":"flex","justifyContent":"space-between","flexWrap":"nowrap","verticalAlignment":"center"}} -->
<div class="wp-block-group"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"left","flexWrap":"nowrap","verticalAlignment":"center"}} -->
<div class="wp-block-group"><!-- wp:site-logo {"width":44,"shouldSyncIcon":true} /-->

<!-- wp:site-title {"level":0,"fontSize":"medium","style":{"typography":{"lineHeight":"1"}}} /--></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|medium"}},"layout":{"type":"flex","justifyContent":"right","flexWrap":"nowrap","verticalAlignment":"center"}} -->
<div class="wp-block-group"><!-- wp:navigation {"overlayMenu":"mobile","layout":{"type":"flex","justifyContent":"right"},"style":{"typography":{"fontWeight":"600"}}} /-->

<!-- wp:buttons {"layout":{"type":"flex","flexWrap":"nowrap"}} -->
<div class="wp-block-buttons"><!-- wp:button {"className":"is-style-outline","metadata":{"blockVisibility":{"viewport":{"mobile":false}},"bindings":{"url":{"source":"anypress/site-details","args":{"key":"phone_link"}},"text":{"source":"anypress/site-details","args":{"key":"phone"}}}}} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="tel:5550187"><?php esc_html_e( '555 0187', 'anypress' ); ?></a></div>
<!-- /wp:button -->

<!-- wp:button {"metadata":{"blockVisibility":{"viewport":{"mobile":false}}}} -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/book-a-visit/"><?php esc_html_e( 'Book a visit', 'anypress' ); ?></a></div>
<!-- /wp:button -->

<!-- wp:button {"metadata":{"blockVisibility":{"viewport":{"tablet":false,"desktop":false}},"bindings":{"url":{"source":"anypress/site-details","args":{"key":"phone_link"}}}}} -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="tel:5550187"><?php esc_html_e( 'Call', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
