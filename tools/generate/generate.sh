#!/usr/bin/env bash
# Rewrites the theme's patterns and style variations from these scripts. Run from anywhere:
#   tools/generate/generate.sh
# Edit the scripts, not the generated files, then run this and `cd tests && npm run theme`.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
cd "$here/../.."
python3 "$here/variations.py"            # styles/colors and styles/typography
python3 "$here/patterns.py" patterns     # shared sections and starter pages
python3 "$here/kits.py" patterns         # kits (styles/kit-*.json and their sections), then the AnyPress Blocks groups
