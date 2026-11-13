<?php
/**
 * Title: Rep footer: news by email, classes and the free-week popup
 * Slug: anypress/rep-footer
 * Description: A site footer for a gym, boxing club or fitness studio: a band for the email list, then the phone number, class and gym links and the address and hours on dark, and the free-week popup (needs the AnyPress Blocks plugin). Part of the Rep kit; choose it for the footer in the Site Editor.
 * Categories: footer
 * Keywords: footer, links, hours, newsletter, phone, popup, gym, rep
 * Viewport Width: 1400
 * Block Types: core/template-part/footer
 */
?>
<!-- wp:group {"metadata":{"name":"Footer"},"align":"full","style":{"spacing":{"blockGap":"0"}},"layout":{"type":"default"}} -->
<div class="wp-block-group alignfull"><!-- wp:group {"tagName":"section","metadata":{"name":"Signup"},"anchor":"signup","align":"full","className":"is-style-section-tint","style":{"spacing":{"padding":{"top":"var:preset|spacing|x-large","bottom":"var:preset|spacing|x-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section id="signup" class="wp-block-group alignfull is-style-section-tint" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--x-large);padding-bottom:var(--wp--preset--spacing--x-large)"><!-- wp:columns {"verticalAlignment":"center","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|x-large","left":"var:preset|spacing|x-large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-center"><!-- wp:column {"verticalAlignment":"center","width":"55%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:55%"><!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'New classes, first', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><?php esc_html_e( 'New classes, open days and the monthly challenge, once a month. Unsubscribe any time.', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center"} -->
<div class="wp-block-column is-vertically-aligned-center"><!-- wp:group {"metadata":{"name":"Form: newsletter"},"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/timetable/"><?php esc_html_e( 'See the timetable', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"Footer columns"},"align":"full","className":"is-style-section-dark","style":{"spacing":{"padding":{"top":"var:preset|spacing|x-large","bottom":"var:preset|spacing|large"},"blockGap":"var:preset|spacing|large"}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-dark" style="padding-top:var(--wp--preset--spacing--x-large);padding-bottom:var(--wp--preset--spacing--large)"><!-- wp:columns {"verticalAlignment":"top","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|large","left":"var:preset|spacing|large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-top"><!-- wp:column {"width":"34%"} -->
<div class="wp-block-column" style="flex-basis:34%"><!-- wp:site-title {"level":0,"fontSize":"x-large","fontFamily":"archivo","style":{"typography":{"lineHeight":"1","fontWeight":"900","textTransform":"uppercase"}}} /-->

<!-- wp:paragraph {"textColor":"main-accent"} -->
<p class="has-main-accent-color has-text-color"><?php esc_html_e( 'Coached strength, conditioning and boxing in Southeast Portland.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"metadata":{"bindings":{"content":{"source":"anypress/site-details","args":{"key":"phone_linked"}}}},"fontFamily":"archivo","fontSize":"x-large","style":{"typography":{"fontWeight":"900"}}} -->
<p class="has-archivo-font-family has-x-large-font-size" style="font-weight:900"><a href="tel:5035550162"><?php esc_html_e( '(503) 555-0162', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:social-links {"layout":{"type":"flex"}} -->
<ul class="wp-block-social-links"><!-- wp:social-link {"url":"#","service":"instagram"} /-->

<!-- wp:social-link {"url":"#","service":"facebook"} /-->

<!-- wp:social-link {"url":"#","service":"youtube"} /--></ul>
<!-- /wp:social-links --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":3,"fontSize":"medium"} -->
<h3 class="wp-block-heading has-medium-font-size"><?php esc_html_e( 'Classes', 'anypress' ); ?></h3>
<!-- /wp:heading -->

<!-- wp:list {"className":"is-style-no-bullets"} -->
<ul class="wp-block-list is-style-no-bullets"><!-- wp:list-item -->
<li><a href="/classes/strength/"><?php esc_html_e( 'Strength', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/classes/conditioning/"><?php esc_html_e( 'Conditioning', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/classes/boxing/"><?php esc_html_e( 'Boxing', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/classes/mobility/"><?php esc_html_e( 'Mobility', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/classes/personal-training/"><?php esc_html_e( 'Personal training', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/timetable/"><?php esc_html_e( 'Timetable', 'anypress' ); ?></a></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":3,"fontSize":"medium"} -->
<h3 class="wp-block-heading has-medium-font-size"><?php esc_html_e( 'The gym', 'anypress' ); ?></h3>
<!-- /wp:heading -->

<!-- wp:list {"className":"is-style-no-bullets"} -->
<ul class="wp-block-list is-style-no-bullets"><!-- wp:list-item -->
<li><a href="/about/"><?php esc_html_e( 'About us', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/coaches/"><?php esc_html_e( 'Coaches', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/memberships/"><?php esc_html_e( 'Memberships', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/reviews/"><?php esc_html_e( 'Reviews', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/careers/"><?php esc_html_e( 'Careers', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/faq/"><?php esc_html_e( 'Questions', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/blog/"><?php esc_html_e( 'Blog', 'anypress' ); ?></a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/contact/"><?php esc_html_e( 'Contact', 'anypress' ); ?></a></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":3,"fontSize":"medium"} -->
<h3 class="wp-block-heading has-medium-font-size"><?php esc_html_e( 'Visit', 'anypress' ); ?></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"metadata":{"bindings":{"content":{"source":"anypress/site-details","args":{"key":"address"}}}},"textColor":"main-accent"} -->
<p class="has-main-accent-color has-text-color"><?php esc_html_e( '740 SE Hawthorne Blvd, Portland, OR 97214', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"metadata":{"bindings":{"content":{"source":"anypress/site-details","args":{"key":"hours"}}}},"textColor":"main-accent"} -->
<p class="has-main-accent-color has-text-color"><?php esc_html_e( 'Monday to Friday, 6am to 9pm. Saturday, 8am to 1pm.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/trial/"><?php esc_html_e( 'Try a week free', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:separator {"className":"is-style-wide"} -->
<hr class="wp-block-separator has-alpha-channel-opacity is-style-wide"/>
<!-- /wp:separator -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"textColor":"main-accent","fontSize":"small"} -->
<p class="has-main-accent-color has-text-color has-small-font-size"><?php esc_html_e( '© Ironside Gym. Coached training in Portland.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"main-accent","fontSize":"small"} -->
<p class="has-main-accent-color has-text-color has-small-font-size"><a href="/privacy-policy/"><?php esc_html_e( 'Privacy', 'anypress' ); ?></a> · <a href="/faq/"><?php esc_html_e( 'Membership terms', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->

<!-- wp:anypress/popup {"popupId":"offer","trigger":"delay","delay":5,"showAgainDays":14,"size":"medium","label":"Your first week is free","style":{"spacing":{"padding":{"top":"0","bottom":"var:preset|spacing|large","left":"0","right":"0"}}}} -->
<!-- wp:image {"sizeSlug":"large","linkDestination":"none","aspectRatio":"16/9","scale":"cover"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-wide.svg' ) ); ?>" alt="<?php esc_attr_e( 'Kettlebells lined up on a gym floor', 'anypress' ); ?>" style="aspect-ratio:16/9;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:group {"style":{"spacing":{"padding":{"left":"var:preset|spacing|large","right":"var:preset|spacing|large"},"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group" style="padding-left:var(--wp--preset--spacing--large);padding-right:var(--wp--preset--spacing--large)"><!-- wp:paragraph {"textColor":"primary","fontFamily":"archivo","fontSize":"small","style":{"typography":{"fontWeight":"800","letterSpacing":"0.1em","textTransform":"uppercase"}}} -->
<p class="has-primary-color has-text-color has-archivo-font-family has-small-font-size" style="font-weight:800;letter-spacing:0.1em;text-transform:uppercase"><?php esc_html_e( 'New to the gym?', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'Your first week is free', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><?php esc_html_e( 'Leave your email and we\'ll send a pass for seven days of classes, plus the timetable.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:group {"metadata":{"name":"Form: offer"},"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/trial/"><?php esc_html_e( 'Claim your free week', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
<!-- /wp:anypress/popup --></div>
<!-- /wp:group -->
