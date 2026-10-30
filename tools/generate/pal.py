PALS = {
 "parcel": {"primary": "#9a3b1b", "primary-accent": "#f0dccf", "primary-alt": "#2f4a3a", "primary-alt-accent": "#eef0e6",
   "main": "#1f1a17", "main-accent": "#ddd5cb", "base": "#f5f0e8", "secondary": "#5c524a", "tertiary": "#ebe3d7", "border-light": "#d8cdbf", "border-dark": "#3a322c"},
 "chapter": {"primary": "#25319a", "primary-accent": "#dfe2f7", "primary-alt": "#ffcf3f", "primary-alt-accent": "#1d1a10",
   "main": "#16182b", "main-accent": "#d6d8e6", "base": "#fbfaf6", "secondary": "#4a4d63", "tertiary": "#f1efe6", "border-light": "#dedbd0", "border-dark": "#2b2e48"},
 "gloss": {"primary": "#7a2335", "primary-accent": "#f3dde0", "primary-alt": "#e9c6c0", "primary-alt-accent": "#3b1119",
   "main": "#2a1a1d", "main-accent": "#e2d6d4", "base": "#fbf6f4", "secondary": "#5e4a4e", "tertiary": "#f3e9e6", "border-light": "#e5d6d3", "border-dark": "#4a2e34"},
 "commons": {"primary": "#1f3a5f", "primary-accent": "#dce4ee", "primary-alt": "#9c3d24", "primary-alt-accent": "#fbf3ec",
   "main": "#14202e", "main-accent": "#d4dae2", "base": "#f8f6f1", "secondary": "#4b5563", "tertiary": "#eeeae0", "border-light": "#dcd6ca", "border-dark": "#2a3a4e"},
 "rep": {"primary": "#b81f17", "primary-accent": "#f6e0dc", "primary-alt": "#d4ff3a", "primary-alt-accent": "#111111",
   "main": "#0e0e0e", "main-accent": "#d9d9d4", "base": "#f2f2ef", "secondary": "#4a4a48", "tertiary": "#e6e6e1", "border-light": "#d4d4ce", "border-dark": "#2a2a2a"},
 "frame": {"primary": "#1f3fd1", "primary-accent": "#dfe5fb", "primary-alt": "#e3dfd4", "primary-alt-accent": "#1a1a1a",
   "main": "#111111", "main-accent": "#d7d7d7", "base": "#f6f5f1", "secondary": "#555555", "tertiary": "#ebe9e3", "border-light": "#d9d6ce", "border-dark": "#2b2b2b"},
 "keystone": {"primary": "#24453a", "primary-accent": "#dbe6df", "primary-alt": "#c9a66b", "primary-alt-accent": "#22190b",
   "main": "#18201c", "main-accent": "#d6dbd6", "base": "#f6f4ef", "secondary": "#4d5852", "tertiary": "#ebe8df", "border-light": "#d9d5ca", "border-dark": "#2c3a33"},
 "launch": {"primary": "#1c6844", "primary-accent": "#dcefe3", "primary-alt": "#cfe9d9", "primary-alt-accent": "#13241a",
   "main": "#121212", "main-accent": "#d8d6cf", "base": "#f4f3ef", "secondary": "#55534e", "tertiary": "#e9e7e0", "border-light": "#d8d5cc", "border-dark": "#2a2a28"},
 "byline": {"primary": "#a91f1b", "primary-accent": "#f5dcd9", "primary-alt": "#1d2b3a", "primary-alt-accent": "#f3efe6",
   "main": "#1a1a1a", "main-accent": "#dad6cc", "base": "#faf8f3", "secondary": "#57534c", "tertiary": "#efebe1", "border-light": "#ddd7ca", "border-dark": "#2e2e2e"},
 "circuit": {"primary": "#123c8c", "primary-accent": "#dfe8f8", "primary-alt": "#ffd23f", "primary-alt-accent": "#1b1606",
   "main": "#0c1626", "main-accent": "#d3d9e3", "base": "#ffffff", "secondary": "#475163", "tertiary": "#f1f3f7", "border-light": "#dde2ea", "border-dark": "#24324a"},
}
def lum(h):
    h = h[1:]; c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
def ratio(a, b):
    x, y = sorted([lum(a), lum(b)], reverse=True); return (x + 0.05) / (y + 0.05)
PAIRS = [("main", "base"), ("base", "primary"), ("main", "primary-accent"), ("base", "main"), ("primary-alt-accent", "primary-alt"), ("main", "tertiary"),
         ("secondary", "base"), ("secondary", "tertiary"), ("secondary", "primary-accent"), ("primary", "base"), ("primary", "tertiary"), ("primary", "primary-accent")]
if __name__ == "__main__":
    for k, p in PALS.items():
        bad = [(a, b, round(ratio(p[a], p[b]), 2)) for a, b in PAIRS if ratio(p[a], p[b]) < 4.6]
        print(k, "ok" if not bad else bad, "min", round(min(ratio(p[a], p[b]) for a, b in PAIRS), 2))
