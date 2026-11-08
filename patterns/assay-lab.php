<?php
/**
 * Title: Assay lab results: the latest batches in a table
 * Slug: anypress/assay-lab
 * Description: The latest batches in a table (batch number, product, purity, which lab tested it and when) beside a short note on how testing works and a link to every report. Part of the Assay kit; publish real reports only.
 * Categories: anypress/kit-regulated
 * Keywords: lab results, certificate of analysis, COA, testing, purity, batches, compliance, assay
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"tagName":"section","metadata":{"name":"Lab results"},"align":"full","className":"is-style-section-tint","style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<section class="wp-block-group alignfull is-style-section-tint" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-bottom:var(--wp--preset--spacing--xx-large)"><!-- wp:columns {"verticalAlignment":"top","align":"wide","style":{"spacing":{"blockGap":{"top":"var:preset|spacing|xx-large","left":"var:preset|spacing|xx-large"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-top"><!-- wp:column {"width":"38%"} -->
<div class="wp-block-column" style="flex-basis:38%"><!-- wp:paragraph {"textColor":"primary","fontFamily":"monospace","fontSize":"small","style":{"typography":{"textTransform":"uppercase","letterSpacing":"0.06em"}}} -->
<p class="has-primary-color has-text-color has-monospace-font-family has-small-font-size" style="text-transform:uppercase;letter-spacing:0.06em"><?php esc_html_e( 'Lab results', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size"><?php esc_html_e( 'Read the report before you open the box', 'anypress' ); ?></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"medium"} -->
<p class="has-medium-font-size"><?php esc_html_e( 'An independent lab tests every batch for identity, purity, strength and sterility. Your batch number is on the label; its report is here.', 'anypress' ); ?></p>
<!-- /wp:paragraph -->

<!-- wp:buttons {"layout":{"type":"flex"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/lab-results/"><?php esc_html_e( 'All lab results', 'anypress' ); ?></a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:table {"hasFixedLayout":false,"className":"is-style-stripes"} -->
<figure class="wp-block-table is-style-stripes"><table><thead><tr><th><?php esc_html_e( 'Batch', 'anypress' ); ?></th><th><?php esc_html_e( 'Product', 'anypress' ); ?></th><th><?php esc_html_e( 'Result', 'anypress' ); ?></th></tr></thead><tbody><tr><td><?php esc_html_e( 'TL-2611-04', 'anypress' ); ?></td><td><?php esc_html_e( 'NAD+ 500 mg, Nov 4', 'anypress' ); ?></td><td><?php esc_html_e( '99.4%', 'anypress' ); ?></td></tr><tr><td><?php esc_html_e( 'TL-2610-29', 'anypress' ); ?></td><td><?php esc_html_e( 'Sermorelin 9 mg, Oct 29', 'anypress' ); ?></td><td><?php esc_html_e( '99.1%', 'anypress' ); ?></td></tr><tr><td><?php esc_html_e( 'TL-2610-21', 'anypress' ); ?></td><td><?php esc_html_e( 'Glutathione 1,500 mg, Oct 21', 'anypress' ); ?></td><td><?php esc_html_e( '99.6%', 'anypress' ); ?></td></tr><tr><td><?php esc_html_e( 'TL-2610-14', 'anypress' ); ?></td><td><?php esc_html_e( 'Copper peptide serum, Oct 14', 'anypress' ); ?></td><td><?php esc_html_e( 'Passed', 'anypress' ); ?></td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:paragraph {"textColor":"secondary","fontSize":"small"} -->
<p class="has-secondary-color has-text-color has-small-font-size"><?php esc_html_e( 'Tested by Kestrel Analytical and Saguaro Labs. Purity measured by HPLC; sterility and endotoxin tests passed on every injectable batch.', 'anypress' ); ?></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></section>
<!-- /wp:group -->
