#!/usr/bin/env python3
"""Writes every kit demo's WordPress Playground Blueprint (demo/<kit>/blueprint.json) from the files in its folder.

    python3 tools/demo/blueprints.py           # writes them
    python3 tools/demo/blueprints.py --check   # fails when one is out of date (CI runs this)

The demos open on any copy of Playground, including one with no download helper (CORS proxy) of its own, so every
file comes from an address any site may read, and nothing is pinned, so a demo always runs the newest releases:

- the theme and AnyPress Blocks: their newest release zips, from api.anypress.io (GitHub's release downloads can't be
  read by another site);
- the demo's own files and photos: raw.githubusercontent.com on main, one writeFile each (no git step, which needs
  Playground's download helper). Only the kit's own files and photos/; demos in subfolders have their own builds.

A shop kit (one with shop.json) also gets FluentCart from wordpress.org, and a small must-use plugin that teaches
Playground's SQLite database the few MySQL functions FluentCart uses (demo/playground-sqlite.php).

After the build, AnyPress Client is added with the store template's site types and the kit's site type ("online-store"
for a shop kit, "website" for the others), so wp-admin looks as on an AnyPress store of that type (its clean Dashboard
and wp-admin). Client's zip is its newest release, from
api.anypress.io like the others.

Each Blueprint keeps its meta, landing page and build step. Run this after adding, renaming or removing a demo file.
"""
import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DEMO = os.path.join(ROOT, "demo")
RAW = "https://raw.githubusercontent.com/hamchowderr/anypress-theme/main/"
ZIPS = "https://api.anypress.io/branding/demo-files/"
THEME_DIR = "/wordpress/wp-content/themes/anypress"
# Files the build reads; strings.txt and the photo credits are for people and tools, not the demo.
DATA = {".php", ".json"}
PHOTOS = {".jpg", ".jpeg", ".png", ".webp"}
# The store template's site types, read by AnyPress Client.
ROLES = "https://raw.githubusercontent.com/hamchowderr/waas-provisioning-api/main/templates/anypress-store/roles.json"
CLIENT_DATA = "/wordpress/wp-content/plugins/anypress-client-data"


def kit_files(kit):
    folder = os.path.join(DEMO, kit)
    files = [f for f in sorted(os.listdir(folder)) if os.path.isfile(os.path.join(folder, f))
             and os.path.splitext(f)[1] in DATA and f != "blueprint.json"]
    photos = os.path.join(folder, "photos")
    if os.path.isdir(photos):
        files += ["photos/" + f for f in sorted(os.listdir(photos)) if os.path.splitext(f)[1].lower() in PHOTOS]
    return files


def write_file(path, caption):
    return {"step": "writeFile", "path": f"{THEME_DIR}/{path}", "data": {"resource": "url", "url": RAW + path},
            "progress": {"caption": caption}}


def blueprint(kit, old):
    build = next(s for s in old["steps"] if s["step"] == "runPHP")
    name = kit.capitalize()
    files = kit_files(kit)
    shop = os.path.exists(os.path.join(DEMO, kit, "shop.json"))
    site_type = "online-store" if shop else "website"
    steps = [
        {"step": "login"},
        {"step": "installTheme", "themeData": {"resource": "url", "url": ZIPS + "anypress-theme.zip"},
         "options": {"activate": True, "targetFolderName": "anypress"}, "progress": {"caption": "Setting up the design"}},
        {"step": "installPlugin", "pluginData": {"resource": "url", "url": ZIPS + "anypress-blocks.zip"},
         "options": {"activate": True, "targetFolderName": "anypress-blocks"},
         "progress": {"caption": "Adding the page sections"}},
        {"step": "installPlugin", "pluginData": {"resource": "wordpress.org/plugins", "slug": "fluentform"},
         "options": {"activate": True}, "progress": {"caption": "Adding the forms"}},
        *([{"step": "installPlugin", "pluginData": {"resource": "wordpress.org/plugins", "slug": "fluent-cart"},
             "options": {"activate": True}, "progress": {"caption": "Adding the shop"}},
           {"step": "writeFile", "path": "/wordpress/wp-content/mu-plugins/anypress-playground-sqlite.php",
            "data": {"resource": "url", "url": RAW + "demo/playground-sqlite.php"}, "progress": {"caption": "Adding the shop"}}]
          if shop else []),
        {"step": "mkdir", "path": f"{THEME_DIR}/demo/{kit}/photos"},
        *[write_file(f"demo/{kit}/{f}", f"Adding the {name} photos" if f.startswith("photos/") else f"Writing the {name} pages")
          for f in files],
    ]
    # The shared builder the kit's build.php requires, and the helpers it shares with the other builder.
    build_php = open(os.path.join(DEMO, kit, "build.php")).read()
    for engine in ("trades.php", "shop.php"):
        if os.path.exists(os.path.join(DEMO, engine)) and engine in build_php:
            steps.append(write_file("demo/lib.php", f"Writing the {name} pages"))
            steps.append(write_file(f"demo/{engine}", f"Writing the {name} pages"))
    steps.append({"step": "runPHP", "code": build["code"], "progress": {"caption": f"Building the {name} demo"}})
    # wp-admin as on an AnyPress store of the kit's site type: AnyPress Client with that type.
    steps += [
        {"step": "mkdir", "path": CLIENT_DATA},
        {"step": "writeFile", "path": f"{CLIENT_DATA}/roles.json", "data": {"resource": "url", "url": ROLES},
         "progress": {"caption": "Setting up wp-admin"}},
        {"step": "writeFile", "path": "/wordpress/wp-content/mu-plugins/0-anypress-store-env.php",
         "data": "<?php putenv('ANYPRESS_IS_TENANT=true'); define('ANYPRESS_TENANT_ROLES', '" + site_type + "');"},
        {"step": "installPlugin", "pluginData": {"resource": "url", "url": ZIPS + "anypress-client.zip"},
         "options": {"activate": True, "targetFolderName": "anypress-client"}, "progress": {"caption": "Setting up wp-admin"}},
    ]
    out = {k: v for k, v in old.items() if k != "steps"}
    out["steps"] = steps
    return out


def main():
    check = "--check" in sys.argv
    stale = []
    for kit in sorted(os.listdir(DEMO)):
        path = os.path.join(DEMO, kit, "blueprint.json")
        if not os.path.isfile(path):
            continue
        with open(path) as f:
            text = f.read()
        new = json.dumps(blueprint(kit, json.loads(text)), indent="\t", ensure_ascii=False) + "\n"
        if new == text:
            continue
        if check:
            stale.append(os.path.relpath(path, ROOT))
        else:
            with open(path, "w") as f:
                f.write(new)
    if stale:
        sys.exit("Out of date (run python3 tools/demo/blueprints.py): " + ", ".join(stale))


if __name__ == "__main__":
    main()
