<?php
/**
 * What every kit demo's build script shares: the kit's patterns as WordPress hands them out, the business's words in
 * place of the kit's, photos in place of the placeholders, Fluent Forms forms, pages, menu links and template parts.
 * demo/trades.php and demo/shop.php require it.
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

/** The registered pattern's content, as WordPress hands it out. */
function anypress_demo_pattern( $name ) {
	$pattern = WP_Block_Patterns_Registry::get_instance()->get_registered( 'anypress/' . $name );
	if ( ! $pattern ) {
		throw new RuntimeException( "Pattern anypress/$name is missing: is the AnyPress theme active?" );
	}
	return $pattern['content'];
}

/** Replaces text in block markup. Keys and values are plain text; the markup holds them HTML-escaped. */
function anypress_demo_swap( $content, $pairs ) {
	$escaped = array();
	foreach ( $pairs as $from => $to ) {
		$escaped[ esc_html( $from ) ] = esc_html( $to );
		$escaped[ $from ]             = $to;
	}
	return strtr( $content, $escaped );
}

/** The demo's own words in place of the kit's: this page's swaps first, then the site-wide ones, then raw swaps. */
function anypress_demo_copy( $content, $slug = '' ) {
	global $anypress_swap;
	if ( isset( $anypress_swap['pages'][ $slug ] ) ) {
		$content = anypress_demo_swap( $content, $anypress_swap['pages'][ $slug ] );
	}
	return strtr( anypress_demo_swap( $content, $anypress_swap['site'] ), $anypress_swap['raw'] );
}

// Links in the patterns are written as /slug/; on a site in a subfolder (such as Playground's) they need the full path.
function anypress_demo_links( $content ) {
	// The kit's social icons point at # for the owner to fill in; the demo points them at each network.
	$content = strtr(
		$content,
		array(
			'{"url":"#","service":"facebook"}'  => '{"url":"https://www.facebook.com/","service":"facebook"}',
			'{"url":"#","service":"instagram"}' => '{"url":"https://www.instagram.com/","service":"instagram"}',
			'{"url":"#","service":"google"}'    => '{"url":"https://www.google.com/maps","service":"google"}',
			'{"url":"#","service":"linkedin"}'  => '{"url":"https://www.linkedin.com/","service":"linkedin"}',
			'{"url":"#","service":"youtube"}'   => '{"url":"https://www.youtube.com/","service":"youtube"}',
			'{"url":"#","service":"x"}'         => '{"url":"https://x.com/","service":"x"}',
			'{"url":"#","service":"pinterest"}' => '{"url":"https://www.pinterest.com/","service":"pinterest"}',
			'{"url":"#","service":"behance"}'   => '{"url":"https://www.behance.net/","service":"behance"}',
		)
	);
	return preg_replace_callback(
		'#href="(/[a-z0-9/-]*)"#',
		fn( $m ) => 'href="' . esc_url( home_url( $m[1] ) ) . '"',
		$content
	);
}

/** Swaps each placeholder image for the demo photo that matches its alt text. */
function anypress_demo_photos( $content ) {
	global $anypress_photos, $anypress_media;
	return preg_replace_callback(
		'#<!-- wp:(image|cover) (\{.*?\}) -->(.*?)<!-- /wp:\1 -->#s',
		function ( $m ) use ( $anypress_photos, $anypress_media ) {
			if ( ! preg_match( '#placeholder-[a-z]+\.svg#', $m[0] ) ) {
				return $m[0];
			}
			$alt = '';
			if ( preg_match( '#alt="([^"]*)"#', $m[3], $a ) ) {
				$alt = html_entity_decode( $a[1], ENT_QUOTES );
			}
			// A cover with no alt can still pick its own photo by its placeholder's shape ("@tall", "@wide").
			if ( '' === $alt && preg_match( '#placeholder-([a-z]+)\.svg#', $m[0], $shape ) && isset( $anypress_photos['by_alt'][ '@' . $shape[1] ] ) ) {
				$alt = '@' . $shape[1];
			}
			$file = $anypress_photos['by_alt'][ $alt ] ?? $anypress_photos['fallback'];
			$media = $anypress_media[ $file ];
			$attrs = json_decode( $m[2], true );
			$attrs['id'] = $media['id'];
			if ( 'cover' === $m[1] ) {
				$attrs['url'] = $media['full'];
			}
			$inner = preg_replace( '#alt="[^"]*"#', 'alt="' . esc_attr( 'cover' === $m[1] ? '' : $anypress_photos['files'][ $file ] ) . '"', $m[3], 1 );
			$inner = preg_replace( '#src="[^"]*placeholder-[a-z]+\.svg"#', 'src="' . esc_url( 'cover' === $m[1] ? $media['full'] : $media['url'] ) . '"', $inner );
			if ( 'image' === $m[1] ) {
				$inner = preg_replace( '#<img #', '<img class="wp-image-' . $media['id'] . '" ', $inner, 1 );
			} else {
				$inner = str_replace( 'class="wp-block-cover__image-background"', 'class="wp-block-cover__image-background wp-image-' . $media['id'] . '"', $inner );
			}
			return '<!-- wp:' . $m[1] . ' ' . wp_json_encode( $attrs, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE ) . ' -->' . $inner . '<!-- /wp:' . $m[1] . ' -->';
		},
		$content
	);
}

/** One Fluent Forms field, from Fluent Forms' own default for that kind of field. */
function anypress_demo_field( $kind, $name, $label, $required = false, $extra = array() ) {
	global $anypress_elements;
	$anypress_elements = $anypress_elements ?? include WP_PLUGIN_DIR . '/fluentform/app/Services/FormBuilder/DefaultElements.php';
	$field = $anypress_elements['general'][ $kind ];
	$field['uniqElKey'] = 'el_' . $name;
	if ( 'input_name' === $kind ) {
		$field['fields']['first_name']['settings']['label']   = $label;
		$field['fields']['first_name']['attributes']['placeholder'] = '';
		$field['fields']['first_name']['settings']['validation_rules']['required']['value'] = $required;
		$field['fields']['middle_name']['settings']['visible'] = false;
		$field['fields']['last_name']['settings']['visible']   = false;
		return $field;
	}
	$field['attributes']['name']                                = $name;
	$field['settings']['label']                                 = $label;
	$field['settings']['validation_rules']['required']['value'] = $required;
	if ( isset( $field['attributes']['placeholder'] ) ) {
		$field['attributes']['placeholder'] = '';
	}
	foreach ( $extra as $path => $value ) {
		$ref  = &$field;
		$keys = explode( '.', $path );
		foreach ( $keys as $key ) {
			$ref = &$ref[ $key ];
		}
		$ref = $value;
		unset( $ref );
	}
	return $field;
}

function anypress_demo_form( $title, $fields, $button, $confirmation ) {
	$form = array(
		'fields'       => array_values( array_filter( $fields ) ),
		'submitButton' => array(
			'uniqElKey'      => 'el_submit',
			'element'        => 'button',
			'attributes'     => array( 'type' => 'submit', 'class' => 'wp-element-button' ),
			'settings'       => array( 'align' => 'left', 'button_style' => 'default', 'container_class' => '', 'help_message' => '', 'background_color' => '#1a7efb', 'button_size' => 'md', 'color' => 'var(--anypress-form-button-text, var(--wp--preset--color--base))', 'button_ui' => array( 'type' => 'default', 'text' => $button, 'img_url' => '' ) ),
			'editor_options' => array( 'title' => 'Submit Button' ),
		),
	);
	$now = current_time( 'mysql' );
	$id  = wpFluent()->table( 'fluentform_forms' )->insertGetId( array( 'title' => $title, 'status' => 'published', 'type' => 'form', 'form_fields' => wp_json_encode( $form ), 'created_at' => $now, 'updated_at' => $now ) );
	wpFluent()->table( 'fluentform_form_meta' )->insert(
		array(
			'form_id'    => $id,
			'meta_key'   => 'formSettings', // phpcs:ignore WordPress.DB.SlowDBQuery.slow_db_query_meta_key
			'value'      => wp_json_encode(
				array(
					'confirmation' => $confirmation,
					'restrictions' => array(),
					'layout'       => array( 'labelPlacement' => 'top', 'helpMessagePlacement' => 'with_label', 'errorMessagePlacement' => 'inline', 'cssClassName' => '', 'asteriskPlacement' => 'asterisk-right' ),
				)
			),
		)
	);
	return $id;
}

function anypress_demo_page( $slug, $title, $content, $parent = 0, $order = 0 ) {
	global $anypress_pages;
	$content = anypress_demo_copy( $content, $slug );
	$id = wp_insert_post(
		array(
			'post_type'    => 'page',
			'post_status'  => 'publish',
			'post_title'   => $title,
			'post_name'    => $slug,
			'post_parent'  => $parent,
			'menu_order'   => $order,
			'post_content' => anypress_demo_photos( $content ),
		)
	);
	update_post_meta( $id, '_wp_page_template', 'page-no-title' );
	$anypress_pages[ $slug ] = $id;
	return $id;
}

/** Photo credits from photos.json, for photos whose licence asks for them. */
function anypress_demo_credits() {
	global $anypress_photos;
	if ( empty( $anypress_photos['credits'] ) ) {
		return '';
	}
	$items = array();
	foreach ( $anypress_photos['credits'] as $c ) {
		$who     = empty( $c['creator'] ) ? '' : ' by ' . esc_html( $c['creator'] );
		$items[] = "<!-- wp:list-item -->\n<li><a href=\"" . esc_url( $c['source'] ) . '">' . esc_html( $c['title'] ) . '</a>' . $who . ', <a href="' . esc_url( $c['license_url'] ) . '">' . esc_html( $c['license'] ) . "</a></li>\n<!-- /wp:list-item -->";
	}
	return "\n\n<!-- wp:heading -->\n<h2 class=\"wp-block-heading\">Photo credits</h2>\n<!-- /wp:heading -->\n\n<!-- wp:list -->\n<ul class=\"wp-block-list\">" . implode( "\n", $items ) . "</ul>\n<!-- /wp:list -->";
}

function anypress_demo_link( $label, $slug_or_url ) {
	global $anypress_pages;
	$id  = $anypress_pages[ $slug_or_url ] ?? 0;
	$url = $id ? get_permalink( $id ) : $slug_or_url;
	$a   = array( 'label' => $label, 'url' => $url, 'kind' => $id ? 'post-type' : 'custom' );
	if ( $id ) {
		$a['type'] = 'page';
		$a['id']   = $id;
	}
	return $a;
}

function anypress_demo_menu_item( $item ) {
	if ( isset( $item['children'] ) ) {
		$a = anypress_demo_link( $item['label'], $item['slug'] );
		return '<!-- wp:navigation-submenu ' . wp_json_encode( $a, JSON_UNESCAPED_SLASHES ) . " -->\n" . implode( "\n", array_map( 'anypress_demo_menu_item', $item['children'] ) ) . "\n<!-- /wp:navigation-submenu -->";
	}
	return '<!-- wp:navigation-link ' . wp_json_encode( anypress_demo_link( $item['label'], $item['slug'] ), JSON_UNESCAPED_SLASHES ) . ' /-->';
}

function anypress_demo_part( $slug, $area, $content ) {
	foreach ( get_posts( array( 'post_type' => 'wp_template_part', 'name' => $slug, 'numberposts' => -1, 'post_status' => 'any' ) ) as $old ) {
		wp_delete_post( $old->ID, true );
	}
	$id = wp_insert_post(
		array(
			'post_type'    => 'wp_template_part',
			'post_status'  => 'publish',
			'post_name'    => $slug,
			'post_title'   => ucfirst( $slug ),
			'post_content' => $content,
			'tax_input'    => array( 'wp_theme' => array( get_stylesheet() ) ),
		)
	);
	wp_set_object_terms( $id, get_stylesheet(), 'wp_theme' );
	wp_set_object_terms( $id, $area, 'wp_template_part_area' );
	return $id;
}

/**
 * Starts a demo on an empty site: the kit's folder, prefix and swaps as globals, the site's name and settings, the
 * kit's style as the site's own styles, no default content, and the demo's photos in the media library (by file name
 * in $anypress_media, with photos.json in $anypress_photos).
 *
 * @param array $anypress_kit What the kit's build.php set.
 */
function anypress_demo_start( $anypress_kit ) {
	global $anypress_demo, $anypress_pre, $anypress_swap, $anypress_photos, $anypress_media;
	$anypress_demo = $anypress_kit['dir'];
	$anypress_pre  = $anypress_kit['prefix'];
	$anypress_swap = is_file( $anypress_demo . '/swap.json' ) ? json_decode( file_get_contents( $anypress_demo . '/swap.json' ), true ) : array();
	$anypress_swap += array( 'site' => array(), 'pages' => array(), 'raw' => array() );
	foreach ( (array) ( $anypress_kit['font_map'] ?? array() ) as $anypress_from => $anypress_to ) {
		$anypress_swap['raw'][ '"fontFamily":"' . $anypress_from . '"' ] = '"fontFamily":"' . $anypress_to . '"';
		$anypress_swap['raw'][ 'has-' . $anypress_from . '-font-family' ]  = 'has-' . $anypress_to . '-font-family';
	}
	wp_set_current_user( 1 );
	require_once ABSPATH . 'wp-admin/includes/image.php';
	require_once ABSPATH . 'wp-admin/includes/file.php';
	require_once ABSPATH . 'wp-admin/includes/media.php';
	require_once ABSPATH . 'wp-admin/includes/taxonomy.php';

	// ---------------------------------------------------------------------------------------------------------- the site
	update_option( 'blogname', $anypress_kit['name'] );
	update_option( 'blogdescription', $anypress_kit['tagline'] );
	update_option( 'timezone_string', $anypress_kit['timezone'] );
	update_option( 'default_comment_status', 'closed' );
	$GLOBALS['wp_rewrite']->set_permalink_structure( '/%postname%/' );
	flush_rewrite_rules();

	// The kit's style variation, as the site's own styles.
	$anypress_variation = json_decode( file_get_contents( get_theme_file_path( 'styles/' . $anypress_kit['style'] . '.json' ) ), true );
	if ( ! empty( $anypress_kit['colors'] ) ) {
		$anypress_colors = json_decode( file_get_contents( get_theme_file_path( 'styles/colors/' . $anypress_kit['colors'] . '.json' ) ), true );
		$anypress_variation['settings']['color']['palette'] = $anypress_colors['settings']['color']['palette'];
	}
	if ( ! empty( $anypress_kit['fonts'] ) ) {
		$anypress_fonts                = json_decode( file_get_contents( get_theme_file_path( 'styles/typography/' . $anypress_kit['fonts'] . '.json' ) ), true );
		$anypress_variation['styles'] = array_replace_recursive( $anypress_variation['styles'], $anypress_fonts['styles'] );
	}
	WP_Theme_JSON_Resolver::clean_cached_data();
	$anypress_styles_id = WP_Theme_JSON_Resolver::get_user_global_styles_post_id();
	wp_update_post(
		array(
			'ID'           => $anypress_styles_id,
			'post_content' => wp_json_encode(
				array(
					'version'                     => 3,
					'isGlobalStylesUserThemeJSON' => true,
					'settings'                    => array( 'color' => array( 'palette' => array( 'theme' => $anypress_variation['settings']['color']['palette'] ) ) ),
					'styles'                      => $anypress_variation['styles'],
				)
			),
		)
	);
	WP_Theme_JSON_Resolver::clean_cached_data();

	// Start empty: the default post, page and comment go.
	foreach ( get_posts( array( 'post_type' => array( 'post', 'page', 'wp_navigation' ), 'numberposts' => -1, 'post_status' => 'any' ) ) as $anypress_old ) {
		wp_delete_post( $anypress_old->ID, true );
	}

	// ---------------------------------------------------------------------------------------------------------- photos
	// Each placeholder photo in the patterns has its own alt text; the demo puts a real photo in its place by that text.
	$anypress_photos = json_decode( file_get_contents( $anypress_demo . '/photos.json' ), true );
	$anypress_media  = array();
	foreach ( $anypress_photos['files'] as $file => $alt ) {
		$path = $anypress_demo . '/photos/' . $file;
		$tmp  = wp_tempnam( $file );
		copy( $path, $tmp );
		$id = media_handle_sideload( array( 'name' => $file, 'tmp_name' => $tmp ), 0, $alt );
		if ( is_wp_error( $id ) ) {
			throw new RuntimeException( $file . ': ' . $id->get_error_message() );
		}
		update_post_meta( $id, '_wp_attachment_image_alt', $alt );
		$anypress_media[ $file ] = array( 'id' => $id, 'url' => wp_get_attachment_image_url( $id, 'large' ), 'full' => wp_get_attachment_image_url( $id, 'full' ) );
	}
}
