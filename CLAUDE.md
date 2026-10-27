# AnyPress theme: agent guide

The AnyPress block theme, installed on every new AnyPress store and free for any WordPress site. The theme files sit at the repository root, as WordPress installs them (`style.css`, `theme.json`, `templates/`, `parts/`, `patterns/`, `styles/`, `assets/`). `tests/` holds the Playground checks; `bin/build-zip.sh` builds the release zip.

| Folder | What's there |
|---|---|
| `patterns/` | Every section and starter page. Kit sections are named after their kit (`ridge-*`, `hearth-*`...); AnyPress Blocks are the shared ones (categories `anypress/blocks-*`) |
| `styles/` | Kit style variations (`styles/kit-*.json`), colour palettes and font pairings (`styles/colors/`, `styles/typography/`), section styles (`styles/sections/`) and block styles (`styles/blocks/`) |
| `tests/` | `theme-check.mjs` (Playground), `contrast.mjs` (WCAG AA), `shot.mjs` (remakes `screenshot.png`) |

## Building and testing

Node 22+: `cd tests && npm ci && npm run theme`. It must pass before pushing; CI runs the same check plus `php -l` on PHP 8.1. Patterns use theme tokens only (no hex colours, no pixel sizes), each has a description and keywords, and every palette keeps WCAG AA contrast in every section style.

## Releasing

Bump `Version` in `style.css`, `Stable tag` in `readme.txt` and add a changelog entry, in the same PR as the change. After merging, run the **Release** workflow (`release.yml`, GitHub `actions_run_trigger`) with the version; it tags `v<version>` and attaches `anypress.zip` and `SHA256SUMS`. Stores get a new theme version only when `waas-provisioning-api/templates/anypress-store/build.sh` pins it (version and checksum) and a new store template version is built, published and made production. That is a publish to customers: do it when the owner has asked for it.

## Building for WordPress

Use the WordPress skills in `.claude/skills/` (list in its README): `wp-block-themes` and `wp-patterns` for the theme and its patterns, `wp-playground` and `blueprint` for trying it, `wp-performance` for speed. Stores run WordPress 7.1 on PHP 8.3. Owners restyle their site in the Site Editor and agents edit it through the AnyPress site tools, so keep everything on the `theme.json` colour, font and spacing slugs, and keep the slugs stable: live stores' pages use them.

## Rules for every change

- **Beads, every time.** Each piece of work gets a Beads issue before it starts (check for a duplicate first). Put the id in the branch, the PR and the status, and close the issue when the PR merges or the change is live. Run `bd` in the session doing the work; the SessionStart hook in `.claude/settings.json` loads the Dolt login, then `bd dolt push` syncs it. This repository's issues are in DoltHub `chowderr/waas_api` (ids `waas-api-*`; run `bd` from a waas-provisioning-api checkout).
- **Pull requests:** open them ready for review, not as drafts, so CI runs. Merge a PR yourself once CI is green and the work was asked for.
- **No "WPCS" wording.** The old platform is gone. Say "the AnyPress API" or "the API's key and secret login". Don't add the word anywhere.
- **Public docs are for users.** READMEs and `readme.txt` explain how to use the theme. Internal notes (server and Coolify ids, Beads, deployment steps) go in the obsidian-vault repository under `1. Projects/WaaS/`. Never put how or why AnyPress started in public copy.
- **Verify before claiming.** Check npm, wordpress.org or the official docs before calling a version or spec "the latest", and check a fix on the running system before calling it fixed.
