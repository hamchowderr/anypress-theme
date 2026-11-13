<?php
/**
 * Title: Assay top bar: prescription only, and the care team's number
 * Slug: anypress/assay-topbar
 * Description: A thin bar above the header saying treatments are prescribed by licensed providers and every batch is tested, with the care team's phone number. Part of the Assay kit (regulated health products); keep the wording your lawyer approves.
 * Categories: anypress/kit-regulated
 * Keywords: top bar, announcement, prescription, lab tested, phone, header, compliance, assay
 * Viewport Width: 1400
 */
?>
<!-- wp:group {"metadata":{"name":"Top bar"},"align":"full","className":"is-style-section-dark","style":{"spacing":{"padding":{"top":"var:preset|spacing|small","bottom":"var:preset|spacing|small"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->
<div class="wp-block-group alignfull is-style-section-dark" style="padding-top:var(--wp--preset--spacing--small);padding-bottom:var(--wp--preset--spacing--small)"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Prescribed by licensed US providers. Every batch tested by an independent lab.', 'anypress' ); ?> <a href="/lab-results/"><?php esc_html_e( 'See the results', 'anypress' ); ?></a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><?php esc_html_e( 'Care team', 'anypress' ); ?> <a href="tel:4805550162"><?php esc_html_e( '(480) 555-0162', 'anypress' ); ?></a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
