<?php
/**
 * Title: Keystone header: valuation offer, menu and a Valuation button
 * Slug: anypress/keystone-header
 * Description: A site header for an estate agent, realtor or property manager that stays at the top while visitors scroll: a bar with the free valuation and the phone number, then the logo, the menu (with dropdowns for homes and towns) and a Valuation button. Part of the Keystone kit; choose it for the header in the Site Editor.
 * Categories: header
 * Keywords: header, menu, navigation, sticky, valuation, phone, real estate, keystone
 * Viewport Width: 1400
 * Block Types: core/template-part/header
 */
?>
<!-- wp:group {"metadata":{"name":"Header"},"align":"full","className":"is-style-sticky","style":{"spacing":{"blockGap":"0"}},"layout":{"type":"default"}} -->
<div class="wp-block-group alignfull is-style-sticky"><!-- wp:group {"metadata":{"name":"Top bar"},"align":"full","className":"is-style-section-brand","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-brand" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Thinking of selling? Free valuation in writing', 'anypress' ); ?> · <a href="/valuation/"><?php esc_html_e( 'Book one', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Call the office', 'anypress' ); ?> <a href="tel:8455550117"><?php esc_html_e( '(845) 555-0117', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->

<!-- wp:group {"backgroundColor":"base","metadata":{"name":"Main bar"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull has-base-background-color has-background" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|medium"}},"layout":{"type":"flex","justifyContent":"space-between","flexWrap":"nowrap","verticalAlignment":"center"}} -->
<div class="wp-block-group"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"left","flexWrap":"nowrap","verticalAlignment":"center"}} -->
<div class="wp-block-group"><!-- wp:site-logo {"width":36,"shouldSyncIcon":true} /-->

<!-- wp:site-title {"level":0,"fontSize":"large","fontFamily":"gloock","style":{"typography":{"lineHeight":"1"}}} /--></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|medium"}},"layout":{"type":"flex","justifyContent":"right","flexWrap":"nowrap","verticalAlignment":"center"}} -->
<div class="wp-block-group"><!-- wp:navigation {"overlayMenu":"mobile","layout":{"type":"flex","justifyContent":"right"}} /-->

<!-- wp:buttons {"layout":{"type":"flex","flexWrap":"nowrap"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/valuation/"><?php esc_html_e( 'Valuation', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
