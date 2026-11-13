// wordpress.org's own Theme Check (the Theme Check plugin the theme review team uses) on the release zip, on WordPress
// Playground. Fails on every REQUIRED and WARNING result, the ones that block a wordpress.org submission, and lists
// the RECOMMENDED and INFO ones.
//
//   bin/build-zip.sh && cd tests && npm ci && npm run wporg
//
// Environment: THEME_ZIP (default ../dist/anypress.zip), THEME_CHECK (a Theme Check release, default the newest on
// wordpress.org), PLAYGROUND_WP, PLAYGROUND_PHP (default 7.1.3 and 8.3), PLAYGROUND_PORT (9411).

import { existsSync, readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { runCLI } from '@wp-playground/cli';

const HERE = dirname(fileURLToPath(import.meta.url));
const ZIP = process.env.THEME_ZIP || resolve(HERE, '../dist/anypress.zip');
const THEME_CHECK = process.env.THEME_CHECK || 'latest-stable';
const WP = process.env.PLAYGROUND_WP || '7.1.3';
const PHP = process.env.PLAYGROUND_PHP || '8.3';
const PORT = Number(process.env.PLAYGROUND_PORT || 9411);

if (!existsSync(ZIP)) {
    console.error(`${ZIP} is missing: run bin/build-zip.sh first.`);
    process.exit(1);
}

const cli = await runCLI({
    command: 'server',
    wp: `https://wordpress.org/wordpress-${WP}.zip`,
    php: PHP,
    port: PORT,
    blueprint: {
        features: { networking: true },
        steps: [
            { step: 'installTheme', themeData: { resource: 'literal', name: 'anypress.zip', contents: readFileSync(ZIP) }, options: { activate: true } },
            { step: 'installPlugin', pluginData: { resource: 'url', url: `https://downloads.wordpress.org/plugin/theme-check.${THEME_CHECK}.zip` }, options: { activate: true } },
        ],
    },
    verbosity: 'quiet',
});

// The same checks and messages as `wp theme-check run anypress`, run without WP-CLI.
const res = await cli.playground.run({
    code: `<?php require '/wordpress/wp-load.php'; require_once ABSPATH . 'wp-admin/includes/admin.php';
    require_once WP_PLUGIN_DIR . '/theme-check/checkbase.php';
    global $themechecks; $theme = wp_get_theme('anypress');
    run_themechecks_against_theme($theme, 'anypress');
    $out = ['version' => get_plugin_data(WP_PLUGIN_DIR . '/theme-check/theme-check.php')['Version'], 'messages' => []];
    foreach ($themechecks as $check) {
        foreach ((array) $check->getError() as $message) {
            preg_match('/<span[^>]*>(.*?)<\\/span>(.*)/s', $message, $m);
            $out['messages'][] = ['type' => trim(rtrim(wp_strip_all_tags($m[1] ?? ''), ':')), 'text' => trim(ltrim(html_entity_decode(wp_strip_all_tags($m[2] ?? $message), ENT_QUOTES), ': '))];
        }
    }
    echo json_encode($out);`,
});
const report = JSON.parse(res.text.slice(res.text.indexOf('{')));
console.log(`Theme Check ${report.version} on WordPress ${WP}, PHP ${PHP}: ${report.messages.length} results`);
const blocking = report.messages.filter((m) => ['REQUIRED', 'WARNING'].includes(m.type.toUpperCase()));
for (const m of report.messages) console.log(`  ${blocking.includes(m) ? 'FAIL' : 'note'}  ${m.type || 'INFO'}: ${m.text.slice(0, 400)}`);
console.log(blocking.length ? `\n${blocking.length} REQUIRED or WARNING result(s): wordpress.org would reject the theme.` : '\nNo REQUIRED or WARNING results.');
await cli[Symbol.asyncDispose]();
process.exit(blocking.length ? 1 : 0);
