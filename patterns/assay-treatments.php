<?php
/**
 * Title: Assay treatments: every product with its price
 * Slug: anypress/assay-treatments
 * Description: Every treatment or product as a card with a photo that opens full screen, its starting price, its name (linking to its own page) and a line about it. Part of the Assay kit; describe what it is, not what it cures.
 * Categories: anypress/kit-regulated
 * Keywords: treatments, products, catalogue, prices, peptides, shop, assay
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Treatments"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:group {"layout":{"type":"flex","justifyContent":"space-between","verticalAlignment":"bottom"}} -->
<div class="wp-block-group"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"textColor":"primary","fontFamily":"monospace","fontSize":"small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.06em"}}} -->
<p class="has-primary-color has-text-color has-monospace-font-family has-small-font-size" style="text-transform:uppercase;letter-spacing:0.06em"><?php esc_html_e( 'Treatments', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'What we prescribe', 'anypress' ); ?></h2>
<!-- /wp:heading --></div>
<!-- /wp:group -->

<!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/treatments/"><?php esc_html_e( 'All treatments', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group -->

<!-- wp:group {"align":"wide","style":{"spacing":{"blockGap":"var:preset|spacing|large"}},"layout":{"type":"grid","columnCount":4,"minimumColumnWidth":"14rem"}} -->
<div class="wp-block-group alignwide"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","aspectRatio":"4/3","scale":"cover","style":{"border":{"radius":"var:preset|border-radius|md"}}} -->
<figure class="wp-block-image size-large has-custom-border"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-wide.svg' ) ); ?>" alt="<?php esc_attr_e( 'Treatment: NAD+', 'anypress' ); ?>" style="border-radius:var(--wp--preset--border-radius--md);aspect-ratio:4/3;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"textColor":"primary","fontFamily":"monospace","fontSize":"small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.06em"}}} -->
<p class="has-primary-color has-text-color has-monospace-font-family has-small-font-size" style="text-transform:uppercase;letter-spacing:0.06em"><?php esc_html_e( 'From $149 a month', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3,"fontSize":"x-large"} -->
<h3 class="wp-block-heading has-x-large-font-size"><a href="/treatments/nad-plus/"><?php esc_html_e( 'NAD+', 'anypress' ); ?></a></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'Small injections at home, a few times a week, for people who want to support energy and healthy ageing.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"style":{"typography":{"fontWeight":"600"}}} -->
<p style="font-weight:600"><a href="/treatments/nad-plus/"><?php esc_html_e( 'Read more →', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","aspectRatio":"4/3","scale":"cover","style":{"border":{"radius":"var:preset|border-radius|md"}}} -->
<figure class="wp-block-image size-large has-custom-border"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-wide.svg' ) ); ?>" alt="<?php esc_attr_e( 'Treatment: Sermorelin', 'anypress' ); ?>" style="border-radius:var(--wp--preset--border-radius--md);aspect-ratio:4/3;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"textColor":"primary","fontFamily":"monospace","fontSize":"small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.06em"}}} -->
<p class="has-primary-color has-text-color has-monospace-font-family has-small-font-size" style="text-transform:uppercase;letter-spacing:0.06em"><?php esc_html_e( 'From $199 a month', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3,"fontSize":"x-large"} -->
<h3 class="wp-block-heading has-x-large-font-size"><a href="/treatments/sermorelin/"><?php esc_html_e( 'Sermorelin', 'anypress' ); ?></a></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'A nightly injection that asks your own body to make more growth hormone, often chosen for sleep and recovery.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"style":{"typography":{"fontWeight":"600"}}} -->
<p style="font-weight:600"><a href="/treatments/sermorelin/"><?php esc_html_e( 'Read more →', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","aspectRatio":"4/3","scale":"cover","style":{"border":{"radius":"var:preset|border-radius|md"}}} -->
<figure class="wp-block-image size-large has-custom-border"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-wide.svg' ) ); ?>" alt="<?php esc_attr_e( 'Treatment: Glutathione', 'anypress' ); ?>" style="border-radius:var(--wp--preset--border-radius--md);aspect-ratio:4/3;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"textColor":"primary","fontFamily":"monospace","fontSize":"small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.06em"}}} -->
<p class="has-primary-color has-text-color has-monospace-font-family has-small-font-size" style="text-transform:uppercase;letter-spacing:0.06em"><?php esc_html_e( 'From $119 a month', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3,"fontSize":"x-large"} -->
<h3 class="wp-block-heading has-x-large-font-size"><a href="/treatments/glutathione/"><?php esc_html_e( 'Glutathione', 'anypress' ); ?></a></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'A weekly injection of the body\'s own antioxidant, prescribed alongside a plan for everyday wellness.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"style":{"typography":{"fontWeight":"600"}}} -->
<p style="font-weight:600"><a href="/treatments/glutathione/"><?php esc_html_e( 'Read more →', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","aspectRatio":"4/3","scale":"cover","style":{"border":{"radius":"var:preset|border-radius|md"}}} -->
<figure class="wp-block-image size-large has-custom-border"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/placeholder-wide.svg' ) ); ?>" alt="<?php esc_attr_e( 'Treatment: Copper peptide serum', 'anypress' ); ?>" style="border-radius:var(--wp--preset--border-radius--md);aspect-ratio:4/3;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"textColor":"primary","fontFamily":"monospace","fontSize":"small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.06em"}}} -->
<p class="has-primary-color has-text-color has-monospace-font-family has-small-font-size" style="text-transform:uppercase;letter-spacing:0.06em"><?php esc_html_e( '$89 a bottle', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3,"fontSize":"x-large"} -->
<h3 class="wp-block-heading has-x-large-font-size"><a href="/treatments/copper-peptide-serum/"><?php esc_html_e( 'Copper peptide serum', 'anypress' ); ?></a></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"secondary"} -->
<p class="has-secondary-color has-text-color"><?php esc_html_e( 'GHK-Cu in a light serum for the face and neck. No prescription needed; tested like everything else.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"style":{"typography":{"fontWeight":"600"}}} -->
<p style="font-weight:600"><a href="/treatments/copper-peptide-serum/"><?php esc_html_e( 'Read more →', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></section>
<!-- /wp:group -->
