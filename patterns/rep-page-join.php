<?php
/**
 * Title: Free week page: Rep kit
 * Slug: anypress/rep-page-join
 * Description: A Free week page for a gym: a heading, the form to claim the trial beside what happens on the first visit, the coaches and reviews. Rep kit; put the site's form in the named Form group.
 * Categories: anypress/pages
 * Keywords: trial, free week, join, sign up, rep
 * Viewport Width: 1400
 * Block Types: core/post-content
 * Post Types: page
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Page hero"},"align":"full","className":"is-style-section-dark","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull is-style-section-dark" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|medium"}},"layout":{"type":"constrained","contentSize":"56rem","justifyContent":"left"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontFamily":"archivo","fontSize":"small","style":{"typography":{"fontWeight":"800","letterSpacing":"0.1em","textTransform":"uppercase"}}} -->
<p class="has-archivo-font-family has-small-font-size" style="font-weight:800;letter-spacing:0.1em;text-transform:uppercase"><?php esc_html_e( 'Free week', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1,"fontSize":"xxx-large","style":{"typography":{"lineHeight":"0.95"}}} -->
<h1 class="wp-block-heading has-xxx-large-font-size" style="line-height:0.95"><?php esc_html_e( 'Try a week free', 'anypress' ); ?></h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"large"} -->
<p class="has-large-font-size"><?php esc_html_e( 'Seven days of classes, as many as you like. No card needed, and no pressure at the end.', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></section>
<!-- /wp:group -->

<!-- wp:group {"tagName":"section","metadata":{"name":"Trial"},"anchor":"trial","align":"full","className":"is-style-section-tint","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section id="trial" class="wp-block-group alignfull is-style-section-tint" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:columns {"verticalAlignment":"top","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|xx-large","left":"var:preset|spacing|xx-large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-top"><!-- wp:column {"width":"58%"} -->
<div class="wp-block-column" style="flex-basis:58%"><!-- wp:group {"className":"is-style-section-card","style":{"spacing":{"padding":{"top":"var:preset|spacing|large","bottom":"var:preset|spacing|large","left":"var:preset|spacing|large","right":"var:preset|spacing|large"},"blockGap":"var:preset|spacing|medium"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-section-card" style="padding-top:var(--wp--preset--spacing--large);padding-bottom:var(--wp--preset--spacing--large);padding-left:var(--wp--preset--spacing--large);padding-right:var(--wp--preset--spacing--large)"><!-- wp:heading {"fontSize":"xxx-large"} -->
<h2 class="wp-block-heading has-xxx-large-font-size"><?php esc_html_e( 'Claim your free week', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><?php esc_html_e( 'Tell us a little about you and which classes you\'d like to try. We\'ll reply the same day with a time for your first visit.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:group {"metadata":{"name":"Form: quote"},"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'Rather talk now? Call the front desk.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button {"metadata":{"bindings":{"url":{"source":"anypress/site-details","args":{"key":"phone_link"}},"text":{"source":"anypress/site-details","args":{"key":"phone"}}}}} -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="tel:5035550162"><?php esc_html_e( 'Call (503) 555-0162', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":3,"fontSize":"x-large"} -->
<h3 class="wp-block-heading has-x-large-font-size"><?php esc_html_e( 'Your first visit', 'anypress' ); ?></h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><?php esc_html_e( 'A coach meets you at the door', 'anypress' ); ?></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><?php esc_html_e( 'Fifteen minutes on how you move', 'anypress' ); ?></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><?php esc_html_e( 'Then straight into a class, scaled for you', 'anypress' ); ?></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":3,"fontSize":"x-large"} -->
<h3 class="wp-block-heading has-x-large-font-size"><?php esc_html_e( 'Bring', 'anypress' ); ?></h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><?php esc_html_e( 'Trainers and something comfortable', 'anypress' ); ?></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><?php esc_html_e( 'A bottle of water', 'anypress' ); ?></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><?php esc_html_e( 'Any injuries we should know about', 'anypress' ); ?></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->

<!-- wp:group {"tagName":"section","metadata":{"name":"Coaches"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:group {"layout":{"type":"flex","justifyContent":"space-between","verticalAlignment":"bottom"}} -->
<div class="wp-block-group"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"textColor":"primary","fontFamily":"archivo","fontSize":"small","style":{"typography":{"fontWeight":"800","letterSpacing":"0.1em","textTransform":"uppercase"}}} -->
<p class="has-primary-color has-text-color has-archivo-font-family has-small-font-size" style="font-weight:800;letter-spacing:0.1em;text-transform:uppercase"><?php esc_html_e( 'Coaches', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xxx-large"} -->
<h2 class="wp-block-heading has-xxx-large-font-size"><?php esc_html_e( 'The people who\'ll coach you', 'anypress' ); ?></h2>
<!-- /wp:heading --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->

<!-- wp:group {"align":"wide","style":{"spacing":{"blockGap":"var:preset|spacing|large"}},"layout":{"type":"grid","columnCount":4,"minimumColumnWidth":"13rem"}} -->
<div class="wp-block-group alignwide"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"sizeSlug":"large","linkDestination":"none","aspectRatio":"3/4","scale":"cover"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-tall.svg' ) ); ?>" alt="<?php esc_attr_e( 'Coach: Marcus', 'anypress' ); ?>" style="aspect-ratio:3/4;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3,"fontSize":"x-large"} -->
<h3 class="wp-block-heading has-x-large-font-size"><a href="/coaches/marcus/"><?php esc_html_e( 'Marcus', 'anypress' ); ?></a></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"primary","fontFamily":"archivo","fontSize":"small","style":{"typography":{"fontWeight":"800","letterSpacing":"0.1em","textTransform":"uppercase"}}} -->
<p class="has-primary-color has-text-color has-archivo-font-family has-small-font-size" style="font-weight:800;letter-spacing:0.1em;text-transform:uppercase"><?php esc_html_e( 'Head coach', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><?php esc_html_e( 'Strength and beginners. Former rugby player.', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"sizeSlug":"large","linkDestination":"none","aspectRatio":"3/4","scale":"cover"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-tall.svg' ) ); ?>" alt="<?php esc_attr_e( 'Coach: Priya', 'anypress' ); ?>" style="aspect-ratio:3/4;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3,"fontSize":"x-large"} -->
<h3 class="wp-block-heading has-x-large-font-size"><a href="/coaches/priya/"><?php esc_html_e( 'Priya', 'anypress' ); ?></a></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"primary","fontFamily":"archivo","fontSize":"small","style":{"typography":{"fontWeight":"800","letterSpacing":"0.1em","textTransform":"uppercase"}}} -->
<p class="has-primary-color has-text-color has-archivo-font-family has-small-font-size" style="font-weight:800;letter-spacing:0.1em;text-transform:uppercase"><?php esc_html_e( 'Boxing coach', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><?php esc_html_e( 'Boxing and conditioning. Twelve years in the ring.', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"sizeSlug":"large","linkDestination":"none","aspectRatio":"3/4","scale":"cover"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-tall.svg' ) ); ?>" alt="<?php esc_attr_e( 'Coach: Dee', 'anypress' ); ?>" style="aspect-ratio:3/4;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3,"fontSize":"x-large"} -->
<h3 class="wp-block-heading has-x-large-font-size"><a href="/coaches/dee/"><?php esc_html_e( 'Dee', 'anypress' ); ?></a></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"primary","fontFamily":"archivo","fontSize":"small","style":{"typography":{"fontWeight":"800","letterSpacing":"0.1em","textTransform":"uppercase"}}} -->
<p class="has-primary-color has-text-color has-archivo-font-family has-small-font-size" style="font-weight:800;letter-spacing:0.1em;text-transform:uppercase"><?php esc_html_e( 'Strength coach', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><?php esc_html_e( 'Strength for women, and lifting through pregnancy.', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"sizeSlug":"large","linkDestination":"none","aspectRatio":"3/4","scale":"cover"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-tall.svg' ) ); ?>" alt="<?php esc_attr_e( 'Coach: Tom', 'anypress' ); ?>" style="aspect-ratio:3/4;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3,"fontSize":"x-large"} -->
<h3 class="wp-block-heading has-x-large-font-size"><a href="/coaches/tom/"><?php esc_html_e( 'Tom', 'anypress' ); ?></a></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"primary","fontFamily":"archivo","fontSize":"small","style":{"typography":{"fontWeight":"800","letterSpacing":"0.1em","textTransform":"uppercase"}}} -->
<p class="has-primary-color has-text-color has-archivo-font-family has-small-font-size" style="font-weight:800;letter-spacing:0.1em;text-transform:uppercase"><?php esc_html_e( 'Conditioning coach', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><?php esc_html_e( 'Conditioning, gymnastics and pull-ups.', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></section>
<!-- /wp:group -->

<!-- wp:group {"tagName":"section","metadata":{"name":"Reviews"},"align":"full","className":"is-style-section-tint","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull is-style-section-tint" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:group {"layout":{"type":"flex","justifyContent":"space-between","verticalAlignment":"bottom"}} -->
<div class="wp-block-group"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"textColor":"primary","fontFamily":"archivo","fontSize":"small","style":{"typography":{"fontWeight":"800","letterSpacing":"0.1em","textTransform":"uppercase"}}} -->
<p class="has-primary-color has-text-color has-archivo-font-family has-small-font-size" style="font-weight:800;letter-spacing:0.1em;text-transform:uppercase"><?php esc_html_e( 'Reviews', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xxx-large"} -->
<h2 class="wp-block-heading has-xxx-large-font-size"><?php esc_html_e( '4.9 stars from 310 members', 'anypress' ); ?></h2>
<!-- /wp:heading --></div>
<!-- /wp:group -->

<!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/reviews/"><?php esc_html_e( 'All reviews', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group -->

<!-- wp:anypress/carousel {"perView":3,"label":"Member reviews"} -->
<!-- wp:group {"className":"is-style-section-card","style":{"spacing":{"padding":{"top":"var:preset|spacing|large","bottom":"var:preset|spacing|large","left":"var:preset|spacing|large","right":"var:preset|spacing|large"},"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-section-card" style="padding-top:var(--wp--preset--spacing--large);padding-bottom:var(--wp--preset--spacing--large);padding-left:var(--wp--preset--spacing--large);padding-right:var(--wp--preset--spacing--large)"><!-- wp:paragraph {"textColor":"primary"} -->
<p class="has-primary-color has-text-color"><?php esc_html_e( '★★★★★', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"medium","style":{"typography":{"lineHeight":"1.45"}}} -->
<p class="has-medium-font-size" style="line-height:1.45"><?php esc_html_e( '“I\'d never lifted a barbell. Six months later I deadlifted my body weight, and Marcus was more excited than me.”', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"secondary","fontFamily":"archivo","fontSize":"small","style":{"typography":{"fontWeight":"800","letterSpacing":"0.1em","textTransform":"uppercase"}}} -->
<p class="has-secondary-color has-text-color has-archivo-font-family has-small-font-size" style="font-weight:800;letter-spacing:0.1em;text-transform:uppercase"><?php esc_html_e( 'Hannah K. · Strength, since March', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"className":"is-style-section-card","style":{"spacing":{"padding":{"top":"var:preset|spacing|large","bottom":"var:preset|spacing|large","left":"var:preset|spacing|large","right":"var:preset|spacing|large"},"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-section-card" style="padding-top:var(--wp--preset--spacing--large);padding-bottom:var(--wp--preset--spacing--large);padding-left:var(--wp--preset--spacing--large);padding-right:var(--wp--preset--spacing--large)"><!-- wp:paragraph {"textColor":"primary"} -->
<p class="has-primary-color has-text-color"><?php esc_html_e( '★★★★★', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"medium","style":{"typography":{"lineHeight":"1.45"}}} -->
<p class="has-medium-font-size" style="line-height:1.45"><?php esc_html_e( '“Priya\'s boxing class is the best hour of my week. Hard, funny and nobody takes themselves too seriously.”', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"secondary","fontFamily":"archivo","fontSize":"small","style":{"typography":{"fontWeight":"800","letterSpacing":"0.1em","textTransform":"uppercase"}}} -->
<p class="has-secondary-color has-text-color has-archivo-font-family has-small-font-size" style="font-weight:800;letter-spacing:0.1em;text-transform:uppercase"><?php esc_html_e( 'Leo M. · Boxing, twice a week', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"className":"is-style-section-card","style":{"spacing":{"padding":{"top":"var:preset|spacing|large","bottom":"var:preset|spacing|large","left":"var:preset|spacing|large","right":"var:preset|spacing|large"},"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-section-card" style="padding-top:var(--wp--preset--spacing--large);padding-bottom:var(--wp--preset--spacing--large);padding-left:var(--wp--preset--spacing--large);padding-right:var(--wp--preset--spacing--large)"><!-- wp:paragraph {"textColor":"primary"} -->
<p class="has-primary-color has-text-color"><?php esc_html_e( '★★★★★', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"medium","style":{"typography":{"lineHeight":"1.45"}}} -->
<p class="has-medium-font-size" style="line-height:1.45"><?php esc_html_e( '“Small classes mean the coach actually watches you. My back has never felt better.”', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"secondary","fontFamily":"archivo","fontSize":"small","style":{"typography":{"fontWeight":"800","letterSpacing":"0.1em","textTransform":"uppercase"}}} -->
<p class="has-secondary-color has-text-color has-archivo-font-family has-small-font-size" style="font-weight:800;letter-spacing:0.1em;text-transform:uppercase"><?php esc_html_e( 'Grace T. · Strength and mobility', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"className":"is-style-section-card","style":{"spacing":{"padding":{"top":"var:preset|spacing|large","bottom":"var:preset|spacing|large","left":"var:preset|spacing|large","right":"var:preset|spacing|large"},"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-section-card" style="padding-top:var(--wp--preset--spacing--large);padding-bottom:var(--wp--preset--spacing--large);padding-left:var(--wp--preset--spacing--large);padding-right:var(--wp--preset--spacing--large)"><!-- wp:paragraph {"textColor":"primary"} -->
<p class="has-primary-color has-text-color"><?php esc_html_e( '★★★★★', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"medium","style":{"typography":{"lineHeight":"1.45"}}} -->
<p class="has-medium-font-size" style="line-height:1.45"><?php esc_html_e( '“I came back after a knee operation and Tom built every session around it. No pain, real progress.”', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"secondary","fontFamily":"archivo","fontSize":"small","style":{"typography":{"fontWeight":"800","letterSpacing":"0.1em","textTransform":"uppercase"}}} -->
<p class="has-secondary-color has-text-color has-archivo-font-family has-small-font-size" style="font-weight:800;letter-spacing:0.1em;text-transform:uppercase"><?php esc_html_e( 'Sam R. · Personal training', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"className":"is-style-section-card","style":{"spacing":{"padding":{"top":"var:preset|spacing|large","bottom":"var:preset|spacing|large","left":"var:preset|spacing|large","right":"var:preset|spacing|large"},"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-section-card" style="padding-top:var(--wp--preset--spacing--large);padding-bottom:var(--wp--preset--spacing--large);padding-left:var(--wp--preset--spacing--large);padding-right:var(--wp--preset--spacing--large)"><!-- wp:paragraph {"textColor":"primary"} -->
<p class="has-primary-color has-text-color"><?php esc_html_e( '★★★★★', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"medium","style":{"typography":{"lineHeight":"1.45"}}} -->
<p class="has-medium-font-size" style="line-height:1.45"><?php esc_html_e( '“Everyone knows your name by the second week. It\'s the first gym I haven\'t quit.”', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"secondary","fontFamily":"archivo","fontSize":"small","style":{"typography":{"fontWeight":"800","letterSpacing":"0.1em","textTransform":"uppercase"}}} -->
<p class="has-secondary-color has-text-color has-archivo-font-family has-small-font-size" style="font-weight:800;letter-spacing:0.1em;text-transform:uppercase"><?php esc_html_e( 'Ade O. · Unlimited member', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"className":"is-style-section-card","style":{"spacing":{"padding":{"top":"var:preset|spacing|large","bottom":"var:preset|spacing|large","left":"var:preset|spacing|large","right":"var:preset|spacing|large"},"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-section-card" style="padding-top:var(--wp--preset--spacing--large);padding-bottom:var(--wp--preset--spacing--large);padding-left:var(--wp--preset--spacing--large);padding-right:var(--wp--preset--spacing--large)"><!-- wp:paragraph {"textColor":"primary"} -->
<p class="has-primary-color has-text-color"><?php esc_html_e( '★★★★★', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"medium","style":{"typography":{"lineHeight":"1.45"}}} -->
<p class="has-medium-font-size" style="line-height:1.45"><?php esc_html_e( '“Dee coached me through lifting all the way through my pregnancy. I felt strong the whole time.”', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"secondary","fontFamily":"archivo","fontSize":"small","style":{"typography":{"fontWeight":"800","letterSpacing":"0.1em","textTransform":"uppercase"}}} -->
<p class="has-secondary-color has-text-color has-archivo-font-family has-small-font-size" style="font-weight:800;letter-spacing:0.1em;text-transform:uppercase"><?php esc_html_e( 'Mia L. · Strength with Dee', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->
<!-- /wp:anypress/carousel --></section>
<!-- /wp:group -->
