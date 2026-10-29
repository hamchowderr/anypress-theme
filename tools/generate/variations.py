# Writes styles/colors/*.json and styles/typography/*.json for the AnyPress theme. Run from the theme folder.
import json, os
theme = json.load(open('theme.json'))
names = {c['slug']: c['name'] for c in theme['settings']['color']['palette']}
order = [c['slug'] for c in theme['settings']['color']['palette']]
SCHEMA = "https://schemas.wp.org/trunk/theme.json"

palettes = {
 "forest":  ("Forest", dict(primary="#1f5f3f", **{"primary-accent":"#e2efe6","primary-alt":"#e3a33b","primary-alt-accent":"#3a2306"}, main="#14201a", **{"main-accent":"#d6ddd8"}, base="#ffffff", secondary="#4a564f", tertiary="#f3f6f3", **{"border-light":"#dfe6e1","border-dark":"#34413a"})),
 "plum":    ("Plum", dict(primary="#6b2d6b", **{"primary-accent":"#f3e6f2","primary-alt":"#eeb0bf","primary-alt-accent":"#4a1626"}, main="#1d1420", **{"main-accent":"#e0d8e2"}, base="#ffffff", secondary="#574d5a", tertiary="#f7f3f7", **{"border-light":"#e8e0e9","border-dark":"#3e3341"})),
 "ocean":   ("Ocean", dict(primary="#0b636b", **{"primary-accent":"#def1f2","primary-alt":"#f4876a","primary-alt-accent":"#3f1508"}, main="#112326", **{"main-accent":"#d4e0e1"}, base="#ffffff", secondary="#48595c", tertiary="#f2f7f7", **{"border-light":"#dbe6e7","border-dark":"#2f4245"})),
 "charcoal-gold": ("Charcoal and gold", dict(primary="#6e5212", **{"primary-accent":"#f5eedc","primary-alt":"#d8b25a","primary-alt-accent":"#2a1f05"}, main="#1c1c1c", **{"main-accent":"#dddad3"}, base="#fbfaf7", secondary="#55524b", tertiary="#f3f1ec", **{"border-light":"#e4e0d6","border-dark":"#3b3934"})),
 "rose":    ("Rose", dict(primary="#a82c55", **{"primary-accent":"#fbe6ec","primary-alt":"#f6cdb2","primary-alt-accent":"#4d2512"}, main="#24161b", **{"main-accent":"#e5dade"}, base="#ffffff", secondary="#5c4a50", tertiary="#fbf5f6", **{"border-light":"#eddfe3","border-dark":"#45333a"})),
 "night":   ("Night", dict(primary="#8fb3ff", **{"primary-accent":"#1c2740","primary-alt":"#f0b93a","primary-alt-accent":"#2b1f04"}, main="#eceef2", **{"main-accent":"#2a2e37"}, base="#111318", secondary="#a9afbb", tertiary="#1a1d23", **{"border-light":"#2c3039","border-dark":"#c9cdd6"})),
}
os.makedirs('styles/colors', exist_ok=True)
for slug, (title, pal) in palettes.items():
    assert set(pal) == set(order), (slug, set(order) ^ set(pal))
    data = {"$schema": SCHEMA, "version": 3, "title": title, "slug": slug,
            "settings": {"color": {"palette": [{"color": pal[s], "name": names[s], "slug": s} for s in order]}}}
    json.dump(data, open(f'styles/colors/{slug}.json', 'w'), indent='\t'); open(f'styles/colors/{slug}.json', 'a').write('\n')

# Typography: body font, heading font and heading weight/spacing. The size scale stays the theme's.
fonts = {
 "warm-serif": ("Warm serif", "figtree", "fraunces", "600", "-0.01em"),
 "editorial":  ("Editorial", "newsreader", "newsreader", "500", "-0.01em"),
 "sturdy":     ("Sturdy", "archivo", "archivo", "800", "-0.02em"),
 "friendly":   ("Friendly", "figtree", "figtree", "700", "-0.01em"),
}
os.makedirs('styles/typography', exist_ok=True)
for slug, (title, body, head, weight, ls) in fonts.items():
    data = {"$schema": SCHEMA, "version": 3, "title": title, "slug": slug, "styles": {
        "typography": {"fontFamily": f"var:preset|font-family|{body}"},
        "elements": {"heading": {"typography": {"fontFamily": f"var:preset|font-family|{head}", "fontWeight": weight, "letterSpacing": ls}}}}}
    json.dump(data, open(f'styles/typography/{slug}.json', 'w'), indent='\t'); open(f'styles/typography/{slug}.json', 'a').write('\n')
print('ok')
