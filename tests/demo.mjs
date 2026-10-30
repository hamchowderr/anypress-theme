// Builds a kit's demo website on WordPress Playground and leaves it running, or checks it against the kit checklist.
//
//   cd tests && npm ci
//   npm run demo -- ridge            # build the Ridge demo and serve it at http://127.0.0.1:9411 (admin / password)
//   npm run demo -- ridge --check    # build it, click through it at desktop and phone width, take screenshots, exit
//
// The demo is the theme's starter pages and sections plus the business's own words, photos, forms, menus and posts,
// built by demo/<kit>/build.php. It needs the AnyPress Blocks plugin (ANYPRESS_BLOCKS for a local folder, otherwise its
// latest release) and Fluent Forms (from wordpress.org).

import { mkdirSync } from 'node:fs';
import { createRequire } from 'node:module';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { runCLI } from '@wp-playground/cli';

const require = createRequire(import.meta.url);
const HERE = dirname(fileURLToPath(import.meta.url));
const THEME = resolve(process.env.ANYPRESS_THEME || resolve(HERE, '..'));
const KIT = process.argv.slice(2).find((a) => !a.startsWith('--')) || 'ridge';
const CHECK = process.argv.includes('--check');
const BLOCKS_DIR = process.env.ANYPRESS_BLOCKS ? resolve(process.env.ANYPRESS_BLOCKS) : null;
const BLOCKS_ZIP = process.env.ANYPRESS_BLOCKS_ZIP || 'https://github.com/hamchowderr/anypress-blocks/releases/latest/download/anypress-blocks.zip';
const PORT = Number(process.env.PLAYGROUND_PORT || 9411);
const SHOTS = resolve(process.env.SHOTS || resolve(HERE, 'shots', `demo-${KIT}`));

const cli = await runCLI({
    command: 'server',
    wp: `https://wordpress.org/wordpress-${process.env.PLAYGROUND_WP || '7.1.3'}.zip`,
    php: process.env.PLAYGROUND_PHP || '8.3',
    port: PORT,
    blueprint: {
        login: !CHECK,
        steps: [
            { step: 'defineWpConfigConsts', consts: { WP_DEBUG: true, WP_DEBUG_LOG: '/tmp/debug.log', WP_DEBUG_DISPLAY: false, AUTOMATIC_UPDATER_DISABLED: true } },
            { step: 'activateTheme', themeFolderName: 'anypress' },
            BLOCKS_DIR
                ? { step: 'activatePlugin', pluginPath: 'anypress-blocks/anypress-blocks.php' }
                : { step: 'installPlugin', pluginData: { resource: 'url', url: BLOCKS_ZIP }, options: { activate: true } },
            { step: 'installPlugin', pluginData: { resource: 'wordpress.org/plugins', slug: 'fluentform' }, options: { activate: true } },
        ],
    },
    mount: [
        { hostPath: THEME, vfsPath: '/wordpress/wp-content/themes/anypress' },
        ...(BLOCKS_DIR ? [{ hostPath: BLOCKS_DIR, vfsPath: '/wordpress/wp-content/plugins/anypress-blocks' }] : []),
    ],
    verbosity: 'quiet',
});
const base = cli.serverUrl.replace(/\/$/, '');
const built = await cli.playground.run({ code: `<?php require '/wordpress/wp-load.php'; require get_theme_file_path('demo/${KIT}/build.php');` });
if (built.errors || !built.text.trim().startsWith('{')) {
    console.error(built.errors || built.text);
    process.exit(1);
}
console.log(`Demo built: ${built.text}`);

if (!CHECK) {
    console.log(`Serving the ${KIT} demo at ${base} (admin / password). Ctrl+C to stop.`);
    await new Promise(() => {});
}

const { checkDemo } = await import('./demo-check.mjs');
mkdirSync(SHOTS, { recursive: true });
const failures = await checkDemo({ base, shots: SHOTS, quote: JSON.parse(built.text).quote, php: (code) => cli.playground.run({ code: `<?php require '/wordpress/wp-load.php'; ${code}` }) });
console.log(failures.length ? `\n${failures.length} problem(s)` : '\nThe demo passes the kit checklist checks');
await cli[Symbol.asyncDispose]?.();
process.exit(failures.length ? 1 : 0);
