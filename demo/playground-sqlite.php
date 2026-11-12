<?php
/**
 * Playground only: WordPress Playground keeps its database in SQLite, which lacks MySQL's JSON_MERGE_PATCH, JSON_UNQUOTE,
 * GET_LOCK and RELEASE_LOCK. FluentCart uses them for review counts, tax overrides and its checkout rate limit, so the
 * shop demos add them here (Playground runs one request at a time, so a lock is always free). Real stores run MariaDB.
 *
 * @package AnyPress
 */

defined( 'ABSPATH' ) || exit;

global $wpdb;
if ( isset( $wpdb->dbh ) && is_object( $wpdb->dbh ) && method_exists( $wpdb->dbh, 'get_connection' ) ) {
	$anypress_merge = function ( $target, $patch ) use ( &$anypress_merge ) {
		if ( ! is_array( $patch ) || array_is_list( $patch ) ) {
			return $patch;
		}
		$target = is_array( $target ) && ! array_is_list( $target ) ? $target : array();
		foreach ( $patch as $key => $value ) {
			if ( null === $value ) {
				unset( $target[ $key ] );
			} else {
				$target[ $key ] = $anypress_merge( $target[ $key ] ?? null, $value );
			}
		}
		return $target;
	};
	$anypress_pdo = $wpdb->dbh->get_connection()->get_pdo();
	$anypress_add = method_exists( $anypress_pdo, 'createFunction' ) ? 'createFunction' : 'sqliteCreateFunction';
	$anypress_pdo->$anypress_add(
		'JSON_MERGE_PATCH',
		fn( $a, $b ) => wp_json_encode( $anypress_merge( json_decode( (string) $a, true ), json_decode( (string) $b, true ) ) ),
		2
	);
	$anypress_pdo->$anypress_add(
		'JSON_UNQUOTE',
		fn( $a ) => is_string( $a ) && str_starts_with( $a, '"' ) ? json_decode( $a ) : $a,
		1
	);
	$anypress_pdo->$anypress_add( 'GET_LOCK', fn( $name, $wait ) => 1, 2 );
	$anypress_pdo->$anypress_add( 'RELEASE_LOCK', fn( $name ) => 1, 1 );
}
