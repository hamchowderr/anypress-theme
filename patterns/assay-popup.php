<?php
/**
 * Title: Assay popup: $50 off the first month
 * Slug: anypress/assay-popup
 * Description: A popup that opens five seconds into a first visit with a photo, a first-month discount and one field for an email address; it closes with its button, Escape or a click outside and stays closed for two weeks. Needs the AnyPress Blocks plugin. Part of the Assay kit; put it in the footer to show it on every page.
 * Categories: anypress/kit-regulated
 * Keywords: popup, offer, discount, first order, newsletter, email, modal, assay
 * Viewport Width: 1400
 */
?>
<!-- wp:anypress/popup {"popupId":"offer","trigger":"delay","delay":5,"showAgainDays":14,"size":"medium","label":"$50 off your first month","style":{"spacing":{"padding":{"top":"0","bottom":"var:preset|spacing|large","left":"0","right":"0"}}}} -->
<!-- wp:image {"sizeSlug":"large","linkDestination":"none","aspectRatio":"16/9","scale":"cover"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-wide.svg' ) ); ?>" alt="<?php esc_attr_e( 'Gloved hands holding a small glass vial', 'anypress' ); ?>" style="aspect-ratio:16/9;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:group {"style":{"spacing":{"padding":{"left":"var:preset|spacing|large","right":"var:preset|spacing|large"},"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group" style="padding-left:var(--wp--preset--spacing--large);padding-right:var(--wp--preset--spacing--large)"><!-- wp:paragraph {"textColor":"primary","fontFamily":"monospace","fontSize":"small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.06em"}}} -->
<p class="has-primary-color has-text-color has-monospace-font-family has-small-font-size" style="text-transform:uppercase;letter-spacing:0.06em"><?php esc_html_e( 'New patients', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( '$50 off your first month', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><?php esc_html_e( 'Leave your email and we\'ll send the code, plus a short guide to how peptide therapy works.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:group {"metadata":{"name":"Form: offer"},"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/pricing/"><?php esc_html_e( 'See pricing', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
<!-- /wp:anypress/popup -->
