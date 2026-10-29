# Generators

The theme's patterns (`patterns/*.php`) and style variations (`styles/kit-*.json`, `styles/colors/`, `styles/typography/`) are written by these scripts. Change a section, kit or palette here, then run:

```sh
tools/generate/generate.sh
cd tests && npm run theme
```

| Script | Writes |
|---|---|
| `variations.py` | Colour palettes and font pairings |
| `patterns.py` | Shared sections and starter pages |
| `kits.py` | The first four kits, then runs `kits_more.py` (the other nine, the everyday sections and the remaining starter pages) and `blocks_cats.py` (the AnyPress Blocks groups) |
| `pal.py` | Kit palettes; run it alone to print their contrast |

Sections whose names are in `ANCHORS` (in `kits.py`) get an anchor, so buttons elsewhere on a kit's home page can jump to them.
