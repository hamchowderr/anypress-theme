#!/usr/bin/env python3
"""Turns a demo's copy, written against the kit's numbered text, into the swaps the demo builder applies.

    python3 tools/demo/copy.py demo/ridge/ironclad-roofing/copy.txt   # writes swap.json next to it
    python3 tools/demo/copy.py --check demo/ridge/ironclad-roofing     # the swaps still match the kit's text

copy.txt, one line per piece of the kit's text (demo/<kit>/strings.txt, from tools/demo/strings.py):

    # comments and blank lines are skipped
    12<TAB>years in Oklahoma City          the kit's text number 12 becomes this
    13<TAB>=                               kept as it is
    [page:storm-damage]                    the lines after this apply to that page only, before the site-wide ones
    [raw]                                  "from<TAB>to" pairs swapped as they are, in block settings too
                                           (map positions, phone links, counter numbers)

Every number must have a site-wide line (or "="), so nothing from the kit's sample business is left on the demo.
swap.json is keyed by the kit's text itself, so it keeps working when the kit's numbering changes; --check fails
when a key no longer appears in the kit (the kit's wording changed and the demo's copy needs that line again).
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from strings import strings  # noqa: E402


def compile_copy(path):
    folder = os.path.dirname(os.path.abspath(path))
    kit = os.path.basename(os.path.dirname(folder))
    kit_text = strings(kit)
    out = {"site": {}, "pages": {}, "raw": {}}
    target, seen, problems = out["site"], set(), []
    for n, line in enumerate(open(path, encoding="utf-8").read().splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        if line.startswith("[page:") and line.endswith("]"):
            target = out["pages"].setdefault(line[6:-1], {})
            continue
        if line == "[raw]":
            target = out["raw"]
            continue
        if "\t" not in line:
            problems.append(f"line {n}: no tab between the number and the text")
            continue
        key, text = line.split("\t", 1)
        if target is out["raw"]:
            target[key] = text
            continue
        if not key.isdigit() or not 1 <= int(key) <= len(kit_text):
            problems.append(f"line {n}: {key} is not one of the kit's {len(kit_text)} numbers")
            continue
        original = kit_text[int(key) - 1]
        if target is out["site"]:
            seen.add(int(key))
        if text != "=" and text != original:
            target[original] = text
    missing = [i for i in range(1, len(kit_text) + 1) if i not in seen]
    if missing:
        problems.append(f"{len(missing)} of the kit's text have no site-wide line: " + ", ".join(map(str, missing[:40])) + (" ..." if len(missing) > 40 else ""))
    if problems:
        sys.exit("\n".join(problems))
    dest = os.path.join(folder, "swap.json")
    json.dump(out, open(dest, "w", encoding="utf-8"), ensure_ascii=False, indent="\t")
    print(f"{dest}: {len(out['site'])} site-wide swaps, {sum(map(len, out['pages'].values()))} page swaps, {len(out['raw'])} raw")


def check(folder):
    folder = os.path.abspath(folder)
    kit = os.path.basename(os.path.dirname(folder))
    kit_text = set(strings(kit))
    swap = json.load(open(os.path.join(folder, "swap.json"), encoding="utf-8"))
    stale = [k for k in swap["site"] if k not in kit_text] + [k for p in swap["pages"].values() for k in p if k not in kit_text]
    left = [t for t in kit_text if t not in swap["site"]]
    print(f"{folder}: {len(stale)} swaps no longer in the kit, {len(left)} pieces of the kit's text kept as they are")
    for k in stale[:20]:
        print("  stale:", k)
    sys.exit(1 if stale else 0)


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--check":
        check(sys.argv[2])
    elif len(sys.argv) == 2:
        compile_copy(sys.argv[1])
    else:
        sys.exit(__doc__)
