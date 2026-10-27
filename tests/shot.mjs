// Renders one starter page from the theme on WordPress Playground and saves a 1200x900 picture of it:
// the theme's screenshot.png that WordPress shows under Appearance > Themes.
//
//   cd tests && npm ci && node shot.mjs [pattern] [style variation title]
//   (default: the trades home page in the default style, which is what screenshot.png shows)

import { createRequire } from 'node:module';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { runCLI } from '@wp-playground/cli';

// Playwright with Chromium, as theme-check.mjs uses for its screenshots.
const { chromium } = createRequire(import.meta.url)('playwright');

const HERE = dirname(fileURLToPath(import.meta.url));
const THEME = resolve(process.env.ANYPRESS_THEME || resolve(HERE, '..'));
const PATTERN = process.argv[2] || 'anypress/home-trades';
const STYLE = process.argv[3] || '';
const OUT = resolve(process.env.OUT || resolve(THEME, 'screenshot.png'));

const cli = await runCLI({
    command: 'server',
    wp: `https://wordpress.org/wordpress-${process.env.PLAYGROUND_WP || '7.1.3'}.zip`,
    php: process.env.PLAYGROUND_PHP || '8.3',
    port: Number(process.env.PLAYGROUND_PORT || 9411),
    blueprint: {
        steps: [
            { step: 'defineWpConfigConsts', consts: { AUTOMATIC_UPDATER_DISABLED: true } },
            { step: 'activateTheme', themeFolderName: 'anypress' },
            { step: 'setSiteOptions', options: { blogname: 'Springfield Roofing', blogdescription: 'Family-run roofers since 2001' } },
        ],
    },
    mount: [{ hostPath: THEME, vfsPath: '/wordpress/wp-content/themes/anypress' }],
    verbosity: 'quiet',
});
const base = cli.serverUrl.replace(/\/$/, '');
const res = await cli.playground.run({ code: `<?php require '/wordpress/wp-load.php';
    $p = WP_Block_Patterns_Registry::get_instance()->get_registered(${JSON.stringify(PATTERN)});
    if (!$p) { echo 'missing'; exit; }
    foreach (WP_Theme_JSON_Resolver::get_style_variations() as $v) {
        if ($v['title'] !== ${JSON.stringify(STYLE)}) continue;
        $id = WP_Theme_JSON_Resolver::get_user_global_styles_post_id();
        $data = ['version' => 3, 'isGlobalStylesUserThemeJSON' => true, 'settings' => $v['settings'] ?? [], 'styles' => $v['styles'] ?? []];
        wp_update_post(['ID' => $id, 'post_content' => wp_json_encode($data)]);
    }
    $page = wp_insert_post(['post_type' => 'page', 'post_status' => 'publish', 'post_title' => 'Home', 'post_content' => $p['content']]);
    update_option('show_on_front', 'page'); update_option('page_on_front', $page);
    update_post_meta($page, '_wp_page_template', 'page-no-title');
    echo 'ok';` });
if (res.text !== 'ok') throw new Error(`pattern ${PATTERN}: ${res.text}`);
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 900 } });
await page.goto(`${base}/`, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);
await page.screenshot({ path: OUT });
await browser.close();
console.log(`saved ${OUT}`);
await cli[Symbol.asyncDispose]?.();
process.exit(0);
