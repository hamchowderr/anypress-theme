<?php
/**
 * AnyPress theme setup.
 *
 * Presentation only: pattern categories and a few block styles. Everything a store does
 * (bindings, abilities, site tools) lives in the AnyPress Client plugin.
 *
 * @package AnyPress
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Pattern categories. Core categories are used where they fit; these group the
 * AnyPress sections so the inserter and the site tools can list them.
 */
function anypress_register_pattern_categories() {
	$categories = array(
		// AnyPress Blocks: the shared sections any site can use, whatever its kit. They take the site's colours and fonts.
		'anypress/blocks-heroes'          => array( __( 'AnyPress Blocks: Heroes', 'anypress' ), __( 'Opening sections that say what the business does and give one main action.', 'anypress' ) ),
		'anypress/blocks-about'           => array( __( 'AnyPress Blocks: About', 'anypress' ), __( 'The story, the team, a statement and photos of the work.', 'anypress' ) ),
		'anypress/blocks-services'        => array( __( 'AnyPress Blocks: Services and prices', 'anypress' ), __( 'Services, menus, features, steps, plans and products.', 'anypress' ) ),
		'anypress/blocks-proof'           => array( __( 'AnyPress Blocks: Proof', 'anypress' ), __( 'Reviews, credentials, logos and numbers that make visitors trust the business.', 'anypress' ) ),
		'anypress/blocks-calls-to-action' => array( __( 'AnyPress Blocks: Calls to action', 'anypress' ), __( 'Bands that ask visitors to do one thing: call, book, sign up, follow.', 'anypress' ) ),
		'anypress/blocks-contact'         => array( __( 'AnyPress Blocks: Contact', 'anypress' ), __( 'Contact details, a contact section ready for a form, and questions and answers.', 'anypress' ) ),
		'anypress/blocks-blog'            => array( __( 'AnyPress Blocks: Blog', 'anypress' ), __( 'Latest posts, an author box, pros and cons, and on-this-page links.', 'anypress' ) ),
		'anypress/blocks-footers'         => array( __( 'AnyPress Blocks: Footers', 'anypress' ), __( 'Site footers: columns of links, or one line.', 'anypress' ) ),
		'anypress/blocks-shop'            => array( __( 'AnyPress Blocks: Shop', 'anypress' ), __( 'Products from the shop (FluentCart): product lists with or without filters, and the headings of category and brand pages.', 'anypress' ) ),
		// The same category the store template's starter pages use, so the site tools find both.
		'anypress/pages'    => array( __( 'Starter pages', 'anypress' ), __( 'Whole pages to start from, for this kind of website.', 'anypress' ) ),
		// Kits: sections designed together for one kind of business, each with its own style variation.
		'anypress/kit-home-services' => array( __( 'Kit: Home services (Ridge)', 'anypress' ), __( 'Sections for trades and home services. They look as designed with the Ridge style.', 'anypress' ) ),
		'anypress/kit-electrical'    => array( __( 'Kit: Electricians (Circuit)', 'anypress' ), __( 'Sections for electricians and electrical contractors. They look as designed with the Circuit style.', 'anypress' ) ),
		'anypress/kit-food'          => array( __( 'Kit: Food and drink (Hearth)', 'anypress' ), __( 'Sections for cafés, bakeries and restaurants. They look as designed with the Hearth style.', 'anypress' ) ),
		'anypress/kit-wellness'      => array( __( 'Kit: Wellness (Still)', 'anypress' ), __( 'Sections for spas, therapists and studios. They look as designed with the Still style.', 'anypress' ) ),
		'anypress/kit-professional'  => array( __( 'Kit: Professional services (Ledger)', 'anypress' ), __( 'Sections for accountants, lawyers, consultants and agencies. They look as designed with the Ledger style.', 'anypress' ) ),
		'anypress/kit-shop'          => array( __( 'Kit: Online shop (Parcel)', 'anypress' ), __( 'Sections for online shops and makers. They look as designed with the Parcel style.', 'anypress' ) ),
		'anypress/kit-courses'       => array( __( 'Kit: Courses and community (Chapter)', 'anypress' ), __( 'Sections for online courses, coaching and memberships. They look as designed with the Chapter style.', 'anypress' ) ),
		'anypress/kit-salon'         => array( __( 'Kit: Salon and beauty (Gloss)', 'anypress' ), __( 'Sections for hair salons, barbers and beauty studios. They look as designed with the Gloss style.', 'anypress' ) ),
		'anypress/kit-community'     => array( __( 'Kit: Associations, chambers and churches (Commons)', 'anypress' ), __( 'Sections for chambers of commerce, associations, clubs, nonprofits and churches. They look as designed with the Commons style.', 'anypress' ) ),
		'anypress/kit-fitness'       => array( __( 'Kit: Gym and classes (Rep)', 'anypress' ), __( 'Sections for gyms, boxing clubs and fitness studios. They look as designed with the Rep style.', 'anypress' ) ),
		'anypress/kit-portfolio'     => array( __( 'Kit: Creative portfolio (Frame)', 'anypress' ), __( 'Sections for photographers, designers, illustrators and architects. They look as designed with the Frame style.', 'anypress' ) ),
		'anypress/kit-real-estate'   => array( __( 'Kit: Real estate (Keystone)', 'anypress' ), __( 'Sections for estate agents, realtors and property managers. They look as designed with the Keystone style.', 'anypress' ) ),
		'anypress/kit-software'      => array( __( 'Kit: Startup and software (Launch)', 'anypress' ), __( 'Sections for software products, apps and startups. They look as designed with the Launch style.', 'anypress' ) ),
		'anypress/kit-magazine'      => array( __( 'Kit: Blog and magazine (Byline)', 'anypress' ), __( 'Sections for blogs, magazines, newsletters and writers. They look as designed with the Byline style.', 'anypress' ) ),
		'anypress/kit-regulated'     => array( __( 'Kit: Regulated health products (Assay)', 'anypress' ), __( 'Sections for shops that sell peptides, supplements, CBD and other products that need lab results and careful wording. They look as designed with the Assay style.', 'anypress' ) ),
		'anypress/kit-franchise'     => array( __( 'Kit: Franchise and multi-location (Branch)', 'anypress' ), __( 'Sections for franchises and businesses with several locations. They look as designed with the Branch style.', 'anypress' ) ),
		'anypress/kit-store'         => array( __( 'Kit: Clothing store (Aisle)', 'anypress' ), __( 'Sections for online shops on FluentCart, written for a clothing brand. They look as designed with the Aisle style.', 'anypress' ) ),
		// Starting structures for blog posts (how-to, list, review).
		'anypress/posts'             => array( __( 'Post outlines', 'anypress' ), __( 'Starting structures for common kinds of blog post.', 'anypress' ) ),
	);
	foreach ( $categories as $slug => $category ) {
		if ( WP_Block_Pattern_Categories_Registry::get_instance()->is_registered( $slug ) ) {
			continue;
		}
		register_block_pattern_category(
			$slug,
			array(
				'label'       => $category[0],
				'description' => $category[1],
			)
		);
	}
}
add_action( 'init', 'anypress_register_pattern_categories' );

/**
 * Block styles kept from the stores' previous theme, so pages built with it still render.
 */
function anypress_register_block_styles() {
	register_block_style(
		'core/cover',
		array(
			'name'         => 'blur-image-less',
			'label'        => __( 'Soft blur', 'anypress' ),
			'inline_style' => '.wp-block-cover.is-style-blur-image-less img.wp-block-cover__image-background{filter:blur(6px);transform:scale(1.04)}',
		)
	);

	// A list without bullets, for lists set large (towns served, opening times).
	register_block_style(
		'core/list',
		array(
			'name'         => 'no-bullets',
			'label'        => __( 'No bullets', 'anypress' ),
			'inline_style' => '.wp-block-list.is-style-no-bullets{list-style:none;padding-inline-start:0}',
		)
	);

	// A menu line: the first block (the dish), a dotted line, then the last block (the price).
	register_block_style(
		'core/group',
		array(
			'name'         => 'menu-leader',
			'label'        => __( 'Menu line', 'anypress' ),
			'inline_style' => '.wp-block-group.is-style-menu-leader{align-items:baseline}.wp-block-group.is-style-menu-leader>*{margin-block:0}.wp-block-group.is-style-menu-leader>:first-child{display:flex;flex:1 1 auto;align-items:baseline;gap:.4em}.wp-block-group.is-style-menu-leader>:first-child::after{content:"";flex:1 1 auto;min-width:1.5em;border-bottom:.12em dotted currentColor;opacity:.5}',
		)
	);

	// A header that stays at the top of the screen while visitors scroll. The template part wraps the group, so it is
	// the part that sticks.
	register_block_style(
		'core/group',
		array(
			'name'         => 'sticky',
			'label'        => __( 'Stays on screen', 'anypress' ),
			'inline_style' => '.wp-block-template-part:has(>.is-style-sticky),.is-style-sticky:not(.wp-block-template-part>*){position:sticky;top:var(--wp-admin--admin-bar--height,0px);z-index:100}.is-style-sticky .wp-block-button__link{white-space:nowrap}@media (max-width:600px){.admin-bar .wp-block-template-part:has(>.is-style-sticky){top:0}}',
		)
	);

	// Questions with a line between each, the question in the heading font.
	register_block_style(
		'core/accordion',
		array(
			'name'         => 'divided',
			'label'        => __( 'Lines between', 'anypress' ),
			'inline_style' => '.wp-block-accordion.is-style-divided{gap:0}.wp-block-accordion.is-style-divided>.wp-block-accordion-item{border-top:2px solid currentColor;margin:0}.wp-block-accordion.is-style-divided>.wp-block-accordion-item:last-child{border-bottom:2px solid currentColor}.wp-block-accordion.is-style-divided .wp-block-accordion-heading{margin:0;font-size:var(--wp--preset--font-size--large)}.wp-block-accordion.is-style-divided .wp-block-accordion-heading__toggle{padding-block:var(--wp--preset--spacing--small);min-height:2.75rem}.wp-block-accordion.is-style-divided .wp-block-accordion-panel{padding-bottom:var(--wp--preset--spacing--small)}',
		)
	);
}
add_action( 'init', 'anypress_register_block_styles' );

/**
 * Stores show only this theme's patterns: no remote Pattern Directory calls.
 */
add_filter( 'should_load_remote_block_patterns', '__return_false' );

/**
 * Core's generic patterns are removed so the inserter and the site tools only offer
 * sections built from this theme's tokens.
 */
function anypress_setup() {
	remove_theme_support( 'core-block-patterns' );
}
add_action( 'after_setup_theme', 'anypress_setup' );

/**
 * Sections run edge to edge: no page-level gap above the footer, so the last section meets it.
 */
function anypress_enqueue_styles() {
	wp_register_style( 'anypress', false, array(), wp_get_theme()->get( 'Version' ) );
	wp_enqueue_style( 'anypress' );
	// A photo alone in a column fills the column's height, so it meets the panel beside it.
	// Long links (an email address set huge) wrap instead of pushing the page sideways on phones, and wide tables scroll inside their box.
	wp_add_inline_style( 'anypress', '.wp-site-blocks>footer{margin-block-start:0}.wp-block-column>.wp-block-cover:only-child{height:100%}:where(p,h1,h2,h3,h4) a{overflow-wrap:anywhere}.wp-block-table{overflow-x:auto}' );
	// A category tile (Shop: shop by category) opens its category wherever it is clicked, not only on the name.
	wp_add_inline_style( 'anypress', '.anypress-category-tiles .fct-categories-list{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(10rem,1fr));gap:var(--wp--preset--spacing--small)}.anypress-category-tiles .fct-product-categories-list .fct-categories-list>li.fct-category-item{position:relative;min-height:7rem;padding:var(--wp--preset--spacing--medium);border-radius:var(--wp--preset--border-radius--md);background:var(--wp--preset--color--tertiary);color:var(--wp--preset--color--main)}.anypress-category-tiles .fct-category-link-wrap{display:flex;flex-direction:column;justify-content:space-between;height:100%;gap:var(--wp--preset--spacing--x-small)}.anypress-category-tiles .fct-category-link{color:inherit;text-decoration:none;font-size:var(--wp--preset--font-size--medium);font-weight:600}.anypress-category-tiles .fct-category-link::after{content:"";position:absolute;inset:0;border-radius:inherit}.anypress-category-tiles li:hover .fct-category-link,.anypress-category-tiles li:focus-within .fct-category-link{text-decoration:underline}.anypress-category-tiles .fct-product-categories-list .fct-category-count{margin:0;color:var(--wp--preset--color--secondary);font-size:var(--wp--preset--font-size--small)}' );
}
add_action( 'wp_enqueue_scripts', 'anypress_enqueue_styles' );

/**
 * A header menu that doesn't fit on one line folds into the menu button, at any screen width.
 *
 * Core folds the menu only below 600px, so a long menu wraps into a column on tablets and small laptops. This checks
 * whether the header's menu fits beside the logo on one line and, when it doesn't, switches it to core's own
 * "always show the menu button" mode, so the button and the full-screen menu behave exactly as they do on phones.
 * It runs once on load and again when the header changes size; pages without a header menu do nothing.
 */
function anypress_fold_header_menu() {
	?>
<script>
(function () {
	var navs = document.querySelectorAll('header .wp-block-navigation');
	if (!navs.length || !window.ResizeObserver) return;
	function mid(el) { var r = el.getBoundingClientRect(); return r.top + r.height / 2; }
	navs.forEach(function (nav) {
		var box = nav.querySelector('.wp-block-navigation__responsive-container');
		var btn = nav.querySelector('.wp-block-navigation__responsive-container-open');
		if (!box || !btn || box.classList.contains('hidden-by-default')) return;
		var brand = nav.closest('header').querySelector('.wp-block-site-title, .wp-block-site-logo');
		function fold(on) { box.classList.toggle('hidden-by-default', on); btn.classList.toggle('always-shown', on); }
		function check() {
			if (box.classList.contains('is-menu-open')) return;
			fold(false);
			if (getComputedStyle(btn).display !== 'none') return; // Phone width: core already folds it.
			var tops = {};
			nav.querySelectorAll('.wp-block-navigation__container > li').forEach(function (li) { tops[Math.round(li.getBoundingClientRect().top)] = 1; });
			var oneLine = Object.keys(tops).length <= 1;
			var besideBrand = !brand || Math.abs(mid(nav) - mid(brand)) < 16;
			fold(!(oneLine && besideBrand));
		}
		var frame;
		new ResizeObserver(function () { cancelAnimationFrame(frame); frame = requestAnimationFrame(check); }).observe(nav.closest('header'));
		check();
	});
})();
</script>
	<?php
}
add_action( 'wp_footer', 'anypress_fold_header_menu', 1 );

/**
 * FluentCart's shop, product cards, product page and cart take the site's own type and corners.
 *
 * FluentCart reads the site's colours itself (its Settings → Appearance → "Inherit from theme"), but not its fonts or
 * the corners of its product cards. Its buttons get the theme's button lettering and its product names and section
 * titles the heading lettering, both read from the site's Styles, so they change with the kit or style the owner
 * picks. Product cards and photos take the image corners. Nothing is added on sites without FluentCart.
 */
function anypress_fluent_cart_styles() {
	if ( ! defined( 'FLUENTCART_VERSION' ) ) {
		return;
	}
	$lettering = function ( $element ) {
		$type = (array) wp_get_global_styles( array( 'elements', $element, 'typography' ) );
		$type = array_intersect_key( $type, array_flip( array( 'fontFamily', 'fontWeight', 'fontStyle', 'letterSpacing', 'textTransform' ) ) );
		$css  = wp_style_engine_get_styles( array( 'typography' => $type ) );
		return $css['css'] ?? '';
	};
	$buttons  = '.fluent-cart-add-to-cart-button,.fluent-cart-direct-checkout-button,.fct-product-view-button,.fct-review-cta-btn,.fct-review-submit-btn';
	$headings = '.fct-product-card-title,.fct-product-list-heading,.fct-reviews-section-title,.fct-review-drawer-title';

	// The corners photos have in this style (core Image), else the theme's medium corner.
	$radius = wp_get_global_styles( array( 'blocks', 'core/image', 'border', 'radius' ) );
	$radius = is_string( $radius ) && '' !== $radius ? $radius : 'var:preset|border-radius|md';
	$radius = preg_replace( '/^var:preset\|border-radius\|([a-z0-9-]+)$/', 'var(--wp--preset--border-radius--$1)', $radius );
	$radius = preg_match( '/^(0|[0-9.]+(px|rem|em)|var\(--wp--preset--border-radius--[a-z0-9-]+\))$/', $radius ) ? $radius : 'var(--wp--preset--border-radius--md)';

	$css  = 'body{--fct-card-radius:' . $radius . ';--fct-container-radius:' . $radius . '}body .fct-product-gallery-thumb img{border-radius:var(--fct-container-radius)}';
	$css .= 'body :is(' . $buttons . '){' . $lettering( 'button' ) . '}';
	$css .= 'body :is(' . $headings . '){' . $lettering( 'heading' ) . '}';
	$css .= 'body .fct-product-card-title{font-size:var(--wp--preset--font-size--medium);line-height:1.25}';
	// Cards in a row line up: the price and button sit at the foot of every card, however long the name.
	$css .= 'body .fct-product-card{display:flex;flex-direction:column}body .fct-product-card .fct-product-card-prices{margin-top:auto}body .fct-product-card .fct-product-card-prices~*{margin-top:0}body .fct-product-list-item{display:flex}body .fct-product-list-item>.fct-product-card{flex:1}';
	// The product list lines up with the page's other sections, which already keep their distance from the screen edge.
	$css .= '.wp-block-fluent-cart-products .fct-products-wrapper{padding-inline:0;box-sizing:border-box}';
	$css .= 'body .fct-product-list-heading{font-size:var(--wp--preset--font-size--x-large);margin-block-end:var(--wp--preset--spacing--medium)}';
	$css .= '.anypress-related .fct-similar-product-list-container{padding-inline:0}';
	// Phones show two products side by side, as shops usually do, instead of one long column.
	$css .= '@media (max-width:600px){body .fct-products-wrapper .fct-products-wrapper-inner:not(.mode-list) .fct-products-container[class]{grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--wp--preset--spacing--small)}body .fct-product-list{--fct-product-list-columns:2!important;gap:var(--wp--preset--spacing--small)}body .fct-product-card-title{font-size:var(--wp--preset--font-size--base)}}';
	// With the cart in the header, FluentCart's floating cart button would be a second cart; it comes back if the owner
	// removes the header one.
	$css .= 'body:has(header .fct-mini-cart-button) .fct-cart-drawer-open-btn{display:none}';
	// A category page (FluentCart's own template) opens on a band of the brand's soft colour, with thread rings at its
	// right, like the theme's other page openings; the band runs edge to edge without widening the page.
	$band  = 'border-image:linear-gradient(var(--wp--preset--color--primary-accent) 0 0) fill 0//0 100vmax;color:var(--wp--preset--color--main)';
	$css  .= 'body.tax-product-categories main>.wp-block-query-title{margin-top:0!important;padding-top:var(--wp--preset--spacing--xx-large)!important;padding-bottom:var(--wp--preset--spacing--x-large);position:relative;isolation:isolate;' . $band . '}';
	$css  .= 'body.tax-product-categories main>.wp-block-query-title:has(+.wp-block-term-description){padding-bottom:var(--wp--preset--spacing--small)}';
	$css  .= 'body.tax-product-categories main>.wp-block-query-title+.wp-block-term-description{margin-top:0!important;padding-bottom:var(--wp--preset--spacing--x-large);font-size:var(--wp--preset--font-size--large);' . $band . '}';
	$css  .= 'body.tax-product-categories main>.wp-block-query-title+.wp-block-term-description>*{max-width:44rem;margin:0}';
	$css  .= 'body.tax-product-categories main>.wp-block-query-title::after{content:"";position:absolute;right:0;top:0;width:22rem;aspect-ratio:1;border-radius:50%;background:repeating-radial-gradient(circle,color-mix(in srgb,var(--wp--preset--color--primary) 22%,transparent) 0 .09rem,transparent .09rem 1.1rem);-webkit-mask:radial-gradient(circle,black 55%,transparent 71%);mask:radial-gradient(circle,black 55%,transparent 71%);pointer-events:none;z-index:-1}';
	$css  .= 'body.tax-product-categories .wp-site-blocks>main{margin-block-start:0}@media (max-width:781px){body.tax-product-categories main>.wp-block-query-title::after{width:10rem;top:auto;bottom:0;opacity:.6}}';
	// The Shop page's categories (FluentCart's Product Categories List) as a row of chips above the products.
	$css .= '.anypress-category-chips .fct-categories-list{display:flex;flex-wrap:wrap;justify-content:center;gap:var(--wp--preset--spacing--small);list-style:none;margin:0 0 var(--wp--preset--spacing--large);padding:0}.anypress-category-chips .fct-category-link{display:inline-block;padding:.55em 1.2em;border:1px solid var(--wp--preset--color--border-light);border-radius:var(--fct-card-radius);color:inherit;text-decoration:none;font-size:var(--wp--preset--font-size--small)}.anypress-category-chips .fct-category-link:hover,.anypress-category-chips .fct-category-link:focus-visible{border-color:currentColor}.anypress-category-chips .fct-category-count{display:none}';
	// Quick view (the window "View Options" opens) takes the style's corners too.
	$css .= 'body .fct-product-modal-body{border-radius:var(--fct-card-radius)}';
	wp_add_inline_style( 'anypress', $css );
}
add_action( 'wp_enqueue_scripts', 'anypress_fluent_cart_styles', 20 );

/**
 * Product card photos load at a size that fits the card.
 *
 * FluentCart prints each product card's photo at its full uploaded size, often 1500px or more for a card about 300px
 * wide, without a srcset. Its own hooks run just before and after that photo, so the theme catches the photo's markup
 * there and adds WordPress's srcset and sizes from the photo's Media Library copies; the browser then downloads the
 * smallest copy that fits the card. Nothing changes when a photo is not in the Media Library, when FluentCart already
 * adds a srcset, or on sites without FluentCart (the hooks never run).
 *
 * @param array $context FluentCart's render context; product cards have scope "product_card".
 */
function anypress_product_card_photo_start( $context ) {
	$GLOBALS['anypress_card_photo_open'] = is_array( $context ) && 'product_card' === ( $context['scope'] ?? '' ) && ob_start();
}
add_action( 'fluent_cart/product/group/before_image_block', 'anypress_product_card_photo_start', PHP_INT_MAX );

/**
 * Adds srcset and sizes to the product card photo caught by anypress_product_card_photo_start().
 *
 * @param array $context FluentCart's render context, with the card's product.
 */
function anypress_product_card_photo_end( $context ) {
	if ( empty( $GLOBALS['anypress_card_photo_open'] ) ) {
		return;
	}
	$GLOBALS['anypress_card_photo_open'] = false;
	$html                                = (string) ob_get_clean();
	$detail                              = $context['product']->detail ?? null;
	$media                               = $detail ? (array) $detail->featured_media : array();
	$id                                  = (int) ( $media['id'] ?? 0 );
	$meta                                = $id && wp_attachment_is_image( $id ) ? wp_get_attachment_metadata( $id ) : false;
	if ( is_array( $meta ) && ! empty( $meta['width'] ) && ! str_contains( $html, 'srcset=' ) ) {
		$html = preg_replace_callback(
			'/<img\b[^>]*\bclass="fct-product-card-image"[^>]*>/',
			function ( $img ) use ( $id, $meta ) {
				$src    = preg_match( '/\ssrc="([^"]+)"/', $img[0], $found ) ? html_entity_decode( $found[1] ) : '';
				$srcset = $src ? wp_calculate_image_srcset( array( (int) $meta['width'], (int) $meta['height'] ), $src, $meta, $id ) : false;
				if ( ! $srcset ) {
					return $img[0];
				}
				// Cards crop photos to a square. A photo wider than tall fills that square by its height, so each copy is
				// listed by the width of the square it fills sharply (its height); the browser then picks a copy big
				// enough for the card, also when it uses the card's real width ("auto", which WordPress adds to lazy
				// photos).
				$wide = max( 1, (int) $meta['width'] / max( 1, (int) $meta['height'] ) );
				if ( $wide > 1 ) {
					$srcset = preg_replace_callback(
						'/ (\d+)w(,|$)/',
						function ( $copy ) use ( $wide ) {
							return ' ' . (int) round( (int) $copy[1] / $wide ) . 'w' . $copy[2];
						},
						$srcset
					);
				}
				// Two cards a row on phones, three or four on wider screens.
				$sizes = '(max-width: 600px) 50vw, (max-width: 1024px) 33vw, 25vw';
				return str_replace( '<img ', '<img srcset="' . esc_attr( $srcset ) . '" sizes="' . esc_attr( $sizes ) . '" ', $img[0] );
			},
			$html,
			1
		);
	}
	echo $html; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped -- FluentCart's own card markup, already escaped by FluentCart; the added attributes are escaped above.
}
add_action( 'fluent_cart/product/group/after_image_block', 'anypress_product_card_photo_end', PHP_INT_MIN );

/**
 * Wishio (a wishlist add-on for FluentCart that sellers can install) in the store's own colours and lettering.
 *
 * Wishio's hearts already follow FluentCart's colours, which follow the theme. Its floating wishlist button, the
 * wishlist page's table and its buttons use Wishio's own greys and navy instead; this points them at the colours,
 * button style and corners of the kit or style the owner picks. Nothing is added on sites without Wishio.
 */
function anypress_wishio_styles() {
	if ( ! defined( 'WISHIO_FCT_VERSION' ) ) {
		return;
	}
	$color = function ( $path, $fallback ) {
		$value = wp_get_global_styles( $path );
		$value = is_string( $value ) ? preg_replace( '/^var:preset\|color\|([a-z0-9-]+)$/', 'var(--wp--preset--color--$1)', $value ) : '';
		return preg_match( '/^(var\(--wp--preset--color--[a-z0-9-]+\)|#[0-9a-fA-F]{3,8})$/', $value ) ? $value : $fallback;
	};
	$button = $color( array( 'elements', 'button', 'color', 'background' ), 'var(--wp--preset--color--primary)' );
	$label  = $color( array( 'elements', 'button', 'color', 'text' ), 'var(--wp--preset--color--base)' );
	$main   = 'var(--wp--preset--color--main)';
	$base   = 'var(--wp--preset--color--base)';
	$hover  = 'color-mix(in srgb,' . $button . ' 85%,' . $main . ')';

	$css  = 'body{--wishio-fct-text-dark:' . $main . ';--wishio-fct-text-mid:var(--wp--preset--color--secondary);--wishio-fct-text-light:color-mix(in srgb,var(--wp--preset--color--secondary) 75%,' . $base . ')';
	$css .= ';--wishio-fct-border:var(--wp--preset--color--border-light);--wishio-fct-border-strong:var(--wp--preset--color--main-accent)';
	$css .= ';--wishio-fct-surface:' . $base . ';--wishio-fct-surface-alt:var(--wp--preset--color--tertiary);--wishio-fct-bg-soft:var(--wp--preset--color--tertiary)';
	$css .= ';--wishio-fct-float-bg:' . $button . ';--wishio-fct-float-color:' . $label . '}';
	$css .= 'body .wishio-fct-wishlist-count.wishio-fct-wishlist-count--float{border-radius:var(--fct-card-radius,var(--wp--preset--border-radius--md))}';
	// The wishlist page's buttons look like the site's other buttons: filled for the main action, outlined otherwise.
	$css .= 'body .wishio-fct-btn-primary,body .wishio-fct-btn-primary:is(:focus,:active){background:' . $button . ';border-color:' . $button . ';color:' . $label . '}';
	$css .= 'body .wishio-fct-btn-primary:hover{background:' . $hover . ';border-color:' . $hover . ';color:' . $label . '}';
	$css .= 'body .wishio-fct-btn-secondary,body .wishio-fct-btn-secondary:is(:focus,:active){background:' . $base . ';border-color:var(--wp--preset--color--border-light);color:' . $main . '}';
	$css .= 'body .wishio-fct-btn-secondary:hover{background:' . $button . ';border-color:' . $button . ';color:' . $label . '}';
	$type = (array) wp_get_global_styles( array( 'elements', 'button', 'typography' ) );
	$type = wp_style_engine_get_styles( array( 'typography' => array_intersect_key( $type, array_flip( array( 'fontFamily', 'fontWeight', 'letterSpacing', 'textTransform' ) ) ) ) );
	if ( ! empty( $type['css'] ) ) {
		$css .= 'body :is(.wishio-fct-btn-primary,.wishio-fct-btn-secondary){' . $type['css'] . '}';
	}
	wp_add_inline_style( 'anypress', $css );
}
add_action( 'wp_enqueue_scripts', 'anypress_wishio_styles', 20 );

/**
 * Shop links in the header: product search, the shopper's account and the cart, beside the header menu.
 *
 * They appear once the site sells something (FluentCart is active and has a published product), in the theme's
 * header and in every kit's header, and owners can move or remove them in the Site Editor like any other block.
 * They use WordPress's Block Hooks, so headers the owner has already edited get them too, and a removed one
 * stays removed.
 *
 * @param string[]                        $hooked   Block types to insert.
 * @param string                          $position Where, relative to the anchor block.
 * @param string                          $anchor   The anchor block type.
 * @param WP_Block_Template|array|WP_Post $context  The template part, pattern or post being rendered.
 * @return string[]
 */
function anypress_shop_links_hook( $hooked, $position, $anchor, $context ) {
	if ( 'core/navigation' !== $anchor || 'after' !== $position || ! anypress_sells_products() ) {
		return $hooked;
	}
	$is_header = ( $context instanceof WP_Block_Template && 'header' === $context->area )
		|| ( is_array( $context ) && isset( $context['slug'] ) && str_ends_with( $context['slug'], '-header' ) );
	if ( $is_header ) {
		$hooked[] = 'core/group';
	}
	return $hooked;
}
add_filter( 'hooked_block_types', 'anypress_shop_links_hook', 10, 4 );

/**
 * The header shop links' look (see anypress_shop_links_hook()), in the editor as on the site: plain icons in the
 * header's own colour, beside the menu. FluentCart's product search shows there on wide screens when the header has no buttons of its own;
 * the Shop page always has it. On phones the menu button comes last and the account link shows only its icon.
 */
function anypress_shop_links_styles() {
	if ( ! defined( 'FLUENTCART_VERSION' ) ) {
		return;
	}
	$css  = '';
	$css .= 'header .wp-block-navigation:has(+.anypress-shop-links){margin-inline-start:auto}';
	$css .= '.anypress-shop-links{align-items:center}.anypress-shop-links svg{width:1.35em;height:1.35em}';
	$css .= '.anypress-shop-links .fluent-cart-search-bar-app-wrapper{width:11rem;flex-shrink:1;min-width:0}header:has(.wp-block-buttons) .anypress-shop-links .fluent-cart-search-bar-app-wrapper{display:none}@media (max-width:1279px){.anypress-shop-links .fluent-cart-search-bar-app-wrapper{display:none}}';
	$css .= '.anypress-shop-links .fct-customer-dashboard-link{display:inline-flex;align-items:center;gap:.35em;color:inherit;text-decoration:none}.anypress-shop-links .fct-customer-dashboard-icon{display:inline-flex}';
	$css .= '.anypress-shop-links .fct-mini-cart-button{background:none;color:inherit;border:0;padding:.25em;cursor:pointer}';
	$css .= '@media (max-width:781px){.anypress-shop-links .fct-customer-dashboard-link>span:last-child{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}header .wp-block-group:has(>.anypress-shop-links)>.wp-block-navigation{order:2;margin-inline-start:0}.anypress-shop-links{margin-inline-start:auto;gap:.35rem}header:has(.anypress-shop-links) .wp-block-site-title a{overflow-wrap:normal}}@media (max-width:600px){header:has(.anypress-shop-links) .wp-block-buttons .wp-block-button__link{padding:.5em .8em;font-size:var(--wp--preset--font-size--small);white-space:nowrap}.anypress-shop-links,header:has(.anypress-shop-links) .wp-block-buttons{flex-shrink:0}header:has(.anypress-shop-links) .wp-block-group:has(>.wp-block-site-title){min-width:0;flex-shrink:1}header:has(.anypress-shop-links) .wp-block-site-title{min-width:0}}';
	wp_register_style( 'anypress-shop-links', false, array(), wp_get_theme()->get( 'Version' ) );
	wp_enqueue_style( 'anypress-shop-links' );
	wp_add_inline_style( 'anypress-shop-links', $css );
}
add_action( 'enqueue_block_assets', 'anypress_shop_links_styles' );

/**
 * The group of shop links that anypress_shop_links_hook() inserts after the header menu.
 *
 * @param array|null $block    The parsed block WordPress would insert.
 * @param string     $type     The hooked block type.
 * @param string     $position Where, relative to the anchor block.
 * @param array      $anchor   The parsed anchor block.
 * @return array|null
 */
function anypress_shop_links_block( $block, $type, $position, $anchor ) {
	if ( null === $block || 'after' !== $position || 'core/navigation' !== ( $anchor['blockName'] ?? '' ) ) {
		return $block;
	}
	$account = esc_html__( 'Account', 'anypress' );
	$markup  = '<!-- wp:group {"metadata":{"name":"' . esc_attr__( 'Shop links', 'anypress' ) . '"},"className":"anypress-shop-links","style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"flex","flexWrap":"nowrap"}} -->'
		. '<div class="wp-block-group anypress-shop-links">'
		. '<!-- wp:fluent-cart/fluent-products-search-bar {"url_mode":"current-tab"} /-->'
		. '<!-- wp:fluent-cart/customer-dashboard-button {"display_type":"link","button_text":"' . $account . '"} /-->'
		. '<!-- wp:fluent-cart/mini-cart {"show_total_price":false,"count_mode":"total_quantity"} /-->'
		. '</div><!-- /wp:group -->';
	$parsed = parse_blocks( $markup );
	return $parsed[0] ?? $block;
}
add_filter( 'hooked_block_core/group', 'anypress_shop_links_block', 10, 4 );

/**
 * Whether the site sells something: FluentCart is active and has at least one published product.
 *
 * @return bool
 */
function anypress_sells_products() {
	if ( ! defined( 'FLUENTCART_VERSION' ) || ! post_type_exists( 'fluent-products' ) ) {
		return false;
	}
	return (int) ( wp_count_posts( 'fluent-products' )->publish ?? 0 ) > 0;
}
