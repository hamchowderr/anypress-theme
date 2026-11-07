#!/usr/bin/env python3
"""Lists every piece of text a kit's demo pages show, numbered, so a new demo can say what each one becomes.

    python3 tools/demo/strings.py ridge           # writes demo/ridge/strings.txt
    python3 tools/demo/strings.py ridge --print   # prints it instead

The text is what the kit's patterns print through esc_html_e() and esc_attr_e(), plus the place names and labels in
block settings ("address", "label"). It is read from the patterns the demo builder uses (demo/trades.php): the home
page, header, footer and every <kit>-page-* starter page, in that order. Each line is "<number><TAB><text>".
A demo's copy (tools/demo/copy.py) refers to these numbers; the numbers change when the kit's text does, so run this
again and check the demos (copy.py --check) after changing a kit.
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
HOMES = {"ridge": "kit-home-services", "circuit": "kit-home-electrical"}
TEXT = re.compile(r"esc_(?:html|attr)_e\(\s*'((?:[^'\\]|\\.)*)'")
ATTR = re.compile(r'"(?:address|label)":"((?:[^"\\]|\\.)*)"')


def pattern_files(kit):
    home = HOMES.get(kit)
    if not home:
        sys.exit(f"No home page known for the {kit} kit: add it to HOMES in {__file__}")
    files = [f"patterns/{home}.php", f"patterns/{kit}-header.php", f"patterns/{kit}-footer.php"]
    files += sorted(glob.glob(os.path.join(ROOT, f"patterns/{kit}-page-*.php")))
    return [os.path.join(ROOT, f) if not os.path.isabs(f) else f for f in files]


def strings(kit):
    seen = []
    for path in pattern_files(kit):
        body = open(path, encoding="utf-8").read().split("?>", 1)[1]
        for m in sorted([*TEXT.finditer(body), *ATTR.finditer(body)], key=lambda m: m.start()):
            text = m.group(1).replace("\\'", "'") if m.re is TEXT else json.loads('"' + m.group(1) + '"')
            if text.strip() and text not in seen:
                seen.append(text)
    return seen


def main():
    kit = sys.argv[1] if len(sys.argv) > 1 else sys.exit(__doc__)
    lines = [f"{i}\t{t}" for i, t in enumerate(strings(kit), 1)]
    if "--print" in sys.argv:
        print("\n".join(lines))
        return
    out = os.path.join(ROOT, "demo", kit, "strings.txt")
    open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"{out}: {len(lines)} pieces of text")


if __name__ == "__main__":
    main()
