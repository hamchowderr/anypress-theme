<?php
/**
 * Title: Assay lab results: every batch, and how testing works
 * Slug: anypress/assay-results-full
 * Description: Every batch's results in a table, then how a batch is tested, step by step, and how to find your batch number. Part of the Assay kit; publish real reports and link each batch to its PDF.
 * Categories: anypress/kit-regulated
 * Keywords: lab results, certificate of analysis, COA, testing, purity, batches, compliance, assay
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"All results"},"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:table {"hasFixedLayout":false,"className":"is-style-stripes"} -->
<figure class="wp-block-table is-style-stripes"><table><thead><tr><th><?php esc_html_e( 'Batch', 'anypress' ); ?></th><th><?php esc_html_e( 'Product', 'anypress' ); ?></th><th><?php esc_html_e( 'Result', 'anypress' ); ?></th></tr></thead><tbody><tr><td><?php esc_html_e( 'TL-2611-04', 'anypress' ); ?></td><td><?php esc_html_e( 'NAD+ 500 mg, Nov 4', 'anypress' ); ?></td><td><?php esc_html_e( '99.4%', 'anypress' ); ?></td></tr><tr><td><?php esc_html_e( 'TL-2610-29', 'anypress' ); ?></td><td><?php esc_html_e( 'Sermorelin 9 mg, Oct 29', 'anypress' ); ?></td><td><?php esc_html_e( '99.1%', 'anypress' ); ?></td></tr><tr><td><?php esc_html_e( 'TL-2610-21', 'anypress' ); ?></td><td><?php esc_html_e( 'Glutathione 1,500 mg, Oct 21', 'anypress' ); ?></td><td><?php esc_html_e( '99.6%', 'anypress' ); ?></td></tr><tr><td><?php esc_html_e( 'TL-2610-14', 'anypress' ); ?></td><td><?php esc_html_e( 'Copper peptide serum, Oct 14', 'anypress' ); ?></td><td><?php esc_html_e( 'Passed', 'anypress' ); ?></td></tr><tr><td><?php esc_html_e( 'TL-2610-07', 'anypress' ); ?></td><td><?php esc_html_e( 'NAD+ 500 mg, Oct 7', 'anypress' ); ?></td><td><?php esc_html_e( '99.2%', 'anypress' ); ?></td></tr><tr><td><?php esc_html_e( 'TL-2609-30', 'anypress' ); ?></td><td><?php esc_html_e( 'Sermorelin 9 mg, Sep 30', 'anypress' ); ?></td><td><?php esc_html_e( '98.9%', 'anypress' ); ?></td></tr><tr><td><?php esc_html_e( 'TL-2609-22', 'anypress' ); ?></td><td><?php esc_html_e( 'Glutathione 1,500 mg, Sep 22', 'anypress' ); ?></td><td><?php esc_html_e( '99.5%', 'anypress' ); ?></td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"small"} -->
<p class="has-secondary-color has-text-color has-small-font-size"><?php esc_html_e( 'Purity by HPLC. Every injectable batch also passed sterility (USP 71) and endotoxin (USP 85) tests. Ask the care team for any report as a PDF.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:spacer {"height":"var:preset|spacing|large"} -->
<div style="height:var(--wp--preset--spacing--large)" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->

<!-- wp:columns {"verticalAlignment":"top","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|xx-large","left":"var:preset|spacing|xx-large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-top"><!-- wp:column {"width":"55%"} -->
<div class="wp-block-column" style="flex-basis:55%"><!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'How a batch is tested', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><?php esc_html_e( 'The pharmacy makes a batch and holds it', 'anypress' ); ?></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><?php esc_html_e( 'A sample goes to an independent lab we don\'t own', 'anypress' ); ?></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><?php esc_html_e( 'The lab checks identity, purity, strength, sterility and endotoxins', 'anypress' ); ?></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><?php esc_html_e( 'Only a batch that passes is labelled and shipped', 'anypress' ); ?></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><?php esc_html_e( 'The report is published here the same day', 'anypress' ); ?></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:group {"className":"is-style-section-tint","style":{"spacing":{"padding":{"top":"var:preset|spacing|large","bottom":"var:preset|spacing|large","left":"var:preset|spacing|large","right":"var:preset|spacing|large"},"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-section-tint" style="padding-top:var(--wp--preset--spacing--large);padding-bottom:var(--wp--preset--spacing--large);padding-left:var(--wp--preset--spacing--large);padding-right:var(--wp--preset--spacing--large)"><!-- wp:paragraph {"textColor":"primary","fontFamily":"monospace","fontSize":"small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.06em"}}} -->
<p class="has-primary-color has-text-color has-monospace-font-family has-small-font-size" style="text-transform:uppercase;letter-spacing:0.06em"><?php esc_html_e( 'Your batch', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3,"fontSize":"large"} -->
<h3 class="wp-block-heading has-large-font-size"><?php esc_html_e( 'Find your batch number', 'anypress' ); ?></h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><?php esc_html_e( 'It\'s printed on the side of every vial and box, starting TL-. Match it to the table above.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/contact/"><?php esc_html_e( 'Ask for a PDF', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->
