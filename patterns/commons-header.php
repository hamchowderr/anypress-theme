<?php
/**
 * Title: Commons header: next event, menu and a Join button
 * Slug: anypress/commons-header
 * Description: A site header for a chamber, association or church that stays at the top while visitors scroll: a dark bar with the next event and the office number, then the logo, the menu (with dropdowns for programs, the directory and about), the phone number and a Join button. Part of the Commons kit; choose it for the header in the Site Editor.
 * Categories: header
 * Keywords: header, menu, navigation, sticky, join, phone, chamber, association, commons
 * Viewport Width: 1400
 * Block Types: core/template-part/header
 */
?>
<!-- wp:group {"metadata":{"name":"Header"},"align":"full","className":"is-style-sticky","style":{"spacing":{"blockGap":"0"}},"layout":{"type":"default"}} -->
<div class="wp-block-group alignfull is-style-sticky"><!-- wp:group {"metadata":{"name":"Top bar"},"align":"full","className":"is-style-section-dark","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-dark" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Next breakfast: Thursday 14 March, The Grand Hotel', 'anypress' ); ?> · <a href="/events/"><?php esc_html_e( 'All events', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small","metadata":{"blockVisibility":{"viewport":{"mobile":false}}}} -->
<p class="has-small-font-size"><?php esc_html_e( 'Office: Mon to Fri, 9am to 5pm', 'anypress' ); ?> · <a href="tel:5550164"><?php esc_html_e( '555 0164', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->

<!-- wp:group {"backgroundColor":"base","metadata":{"name":"Main bar"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull has-base-background-color has-background" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|medium"}},"layout":{"type":"flex","justifyContent":"space-between","flexWrap":"nowrap","verticalAlignment":"center"}} -->
<div class="wp-block-group"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"left","flexWrap":"nowrap","verticalAlignment":"center"}} -->
<div class="wp-block-group"><!-- wp:site-logo {"width":44,"shouldSyncIcon":true} /-->

<!-- wp:site-title {"level":0,"fontSize":"medium","fontFamily":"crimson-pro","style":{"typography":{"lineHeight":"1","fontWeight":"600"}}} /--></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|medium"}},"layout":{"type":"flex","justifyContent":"right","flexWrap":"nowrap","verticalAlignment":"center"}} -->
<div class="wp-block-group"><!-- wp:navigation {"overlayMenu":"mobile","layout":{"type":"flex","justifyContent":"right"},"style":{"typography":{"fontWeight":"600"}}} /-->

<!-- wp:buttons {"layout":{"type":"flex","flexWrap":"nowrap"}} -->
<div class="wp-block-buttons"><!-- wp:button {"className":"is-style-outline","metadata":{"blockVisibility":{"viewport":{"mobile":false}},"bindings":{"url":{"source":"anypress/site-details","args":{"key":"phone_link"}},"text":{"source":"anypress/site-details","args":{"key":"phone"}}}}} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="tel:5550164"><?php esc_html_e( '555 0164', 'anypress' ); ?></a></div>
<!-- /wp:button -->

<!-- wp:button {"metadata":{"blockVisibility":{"viewport":{"mobile":false}}}} -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/join/"><?php esc_html_e( 'Join the chamber', 'anypress' ); ?></a></div>
<!-- /wp:button -->

<!-- wp:button {"metadata":{"blockVisibility":{"viewport":{"tablet":false,"desktop":false}},"bindings":{"url":{"source":"anypress/site-details","args":{"key":"phone_link"}}}}} -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="tel:5550164"><?php esc_html_e( 'Call', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
