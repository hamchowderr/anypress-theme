# Industry kits for the AnyPress theme: a style variation (styles/kit-*.json), a set of sections in the
# kit's own pattern category, and a starter home page per kit. Run from the theme folder:
#   python3 kits.py patterns
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "patterns.py")).read()
exec(src[: src.index("# 1. Split hero")])  # helpers: T, IMG, j, heading, para, buttons, image, group, columns, write, BODIES
SCHEMA = "https://schemas.wp.org/trunk/theme.json"
S = lambda slug: f"var:preset|spacing|{slug}"
V = lambda slug: f"var(--wp--preset--spacing--{slug})"

def padding(p):
    """p: (top, bottom, left, right) spacing slugs, None to skip a side. Returns (attr, css)."""
    sides = dict(zip(("top", "bottom", "left", "right"), p))
    attr = {k: S(v) for k, v in sides.items() if v}
    css = ";".join(f"padding-{k}:{V(v)}" for k, v in sides.items() if v)
    return attr, css

def grp(inner, style=None, pad=None, gap=None, layout=None, tag="div", align=None, name=None, minh=None, radius=None, valign=None, anchor=None):
    a, cls, css = {}, ["wp-block-group"], []
    if tag != "div": a["tagName"] = tag
    if name: a["metadata"] = {"name": name}
    if anchor: a["anchor"] = anchor
    if align: a["align"] = align; cls.append(f"align{align}")
    if style: a["className"] = f"is-style-{style}"; cls.append(f"is-style-{style}")
    st = {}
    if pad and any(pad):
        pa, pc = padding(pad); st.setdefault("spacing", {})["padding"] = pa; css.append(pc)
    if tag == "section":
        st.setdefault("spacing", {})["margin"] = {"top": "0", "bottom": "0"}; css.insert(0, "margin-top:0;margin-bottom:0")
    if gap: st.setdefault("spacing", {})["blockGap"] = "0" if gap == "0" else S(gap)
    if minh: st["dimensions"] = {"minHeight": minh}; css.append(f"min-height:{minh}")
    if radius: st["border"] = {"radius": f"var:preset|border-radius|{radius}"}; css.append(f"border-radius:var(--wp--preset--border-radius--{radius})")
    if st: a["style"] = st
    a["layout"] = layout or {"type": "default"}
    sc = f' style="{";".join(c for c in css if c)}"' if css else ""
    ida = f' id="{anchor}"' if anchor else ""
    return f'<!-- wp:group {j(a)} -->\n<{tag}{ida} class="{" ".join(cls)}"{sc}>{inner}</{tag}>\n<!-- /wp:group -->'

# Kit sections that buttons elsewhere on the kit's home page jump to (href="#<anchor>"), by section name.
ANCHORS = {"Menu": "menu", "Visit": "visit", "Call": "quote", "Practical": "book", "Contact": "contact", "Prices": "prices",
           "Book": "book", "Timetable": "timetable", "Trial": "trial", "Best sellers": "shop", "Story": "story", "Signup": "signup",
           "Pricing": "pricing", "Try it": "start", "Curriculum": "curriculum", "Events": "events", "Join": "join",
           "Listings": "listings", "Valuation": "valuation", "Agent": "agent", "Price": "buy"}

def sec(name, inner, style=None, pad=("xx-large", "xx-large", None, None), content="80rem", justify=None, minh=None, layout=None):
    lay = layout or {"type": "constrained", "contentSize": content}
    if justify: lay["justifyContent"] = justify
    return grp(inner, style, pad, None, lay, "section", "full", name, minh, anchor=ANCHORS.get(name))

def col(inner, width=None, style=None, pad=None, valign=None):
    a, cls, css = {}, ["wp-block-column"], []
    if valign: a["verticalAlignment"] = valign; cls.append(f"is-vertically-aligned-{valign}")
    if style: a["className"] = f"is-style-{style}"; cls.append(f"is-style-{style}")
    if pad:
        pa, pc = padding(pad); a["style"] = {"spacing": {"padding": pa}}; css.append(pc)
    if width: a["width"] = width; css.append(f"flex-basis:{width}")
    at = (" " + j(a)) if a else ""
    sc = f' style="{";".join(css)}"' if css else ""
    return f'<!-- wp:column{at} -->\n<div class="{" ".join(cls)}"{sc}>{inner}</div>\n<!-- /wp:column -->'

def cols(items, gap="large", align="wide", valign=None, stack=True):
    a = {}
    if valign: a["verticalAlignment"] = valign
    if align: a["align"] = align
    if not stack: a["isStackedOnMobile"] = False
    g = "0" if gap == "0" else S(gap)
    a["style"] = {"spacing": {"blockGap": {"top": g, "left": g}}}
    cls = ["wp-block-columns"] + ([f"align{align}"] if align else []) + ([f"are-vertically-aligned-{valign}"] if valign else []) + ([] if stack else ["is-not-stacked-on-mobile"])
    return f'<!-- wp:columns {j(a)} -->\n<div class="{" ".join(cls)}">' + "\n\n".join(items) + '</div>\n<!-- /wp:columns -->'

def h(text, level=2, size=None, align=None, family=None, typo=None, color=None):
    a, cls, css = {}, ["wp-block-heading"], []
    if align: a["textAlign"] = align; cls.append(f"has-text-align-{align}")
    if level != 2: a["level"] = level
    if color: a["textColor"] = color; cls += [f"has-{color}-color", "has-text-color"]
    if family: a["fontFamily"] = family; cls.append(f"has-{family}-font-family")
    if size: a["fontSize"] = size; cls.append(f"has-{size}-font-size")
    if typo:
        a["style"] = {"typography": typo}
        css += [f"{k2css(k)}:{v}" for k, v in typo.items()]
    sc = f' style="{";".join(css)}"' if css else ""
    at = (" " + j(a)) if a else ""
    return f'<!-- wp:heading{at} -->\n<h{level} class="{" ".join(cls)}"{sc}>{T(text)}</h{level}>\n<!-- /wp:heading -->'

def k2css(k): return {"lineHeight": "line-height", "textTransform": "text-transform", "fontStyle": "font-style", "fontWeight": "font-weight", "letterSpacing": "letter-spacing"}[k]

def p(text, size=None, color=None, align=None, family=None, typo=None, raw=False):
    a, cls, css = {}, [], []
    if align: a["align"] = align; cls.append(f"has-text-align-{align}")
    if color: a["textColor"] = color; cls += [f"has-{color}-color", "has-text-color"]
    if family: a["fontFamily"] = family; cls.append(f"has-{family}-font-family")
    if size: a["fontSize"] = size; cls.append(f"has-{size}-font-size")
    if typo:
        a["style"] = {"typography": typo}
        css += [f"{k2css(k)}:{v}" for k, v in typo.items()]
    at = (" " + j(a)) if a else ""
    c = f' class="{" ".join(cls)}"' if cls else ""
    sc = f' style="{";".join(css)}"' if css else ""
    return f'<!-- wp:paragraph{at} -->\n<p{c}{sc}>{text if raw else T(text)}</p>\n<!-- /wp:paragraph -->'

def btns(items, justify=None):
    a = {"layout": {"type": "flex"}}
    if justify: a["layout"]["justifyContent"] = justify
    out = []
    for label, style, href in items:
        ba = {}; cls = "wp-block-button"
        if style: ba["className"] = f"is-style-{style}"; cls += f" is-style-{style}"
        at = (" " + j(ba)) if ba else ""
        out.append(f'<!-- wp:button{at} -->\n<div class="{cls}"><a class="wp-block-button__link wp-element-button" href="{href}">{T(label)}</a></div>\n<!-- /wp:button -->')
    return f'<!-- wp:buttons {j(a)} -->\n<div class="wp-block-buttons">' + "\n\n".join(out) + '</div>\n<!-- /wp:buttons -->'

def lst(items, size=None, family=None, typo=None, style=None):
    a, cls, css = {}, ["wp-block-list"], []
    if style: a["className"] = f"is-style-{style}"; cls.append(f"is-style-{style}")
    if family: a["fontFamily"] = family; cls.append(f"has-{family}-font-family")
    if size: a["fontSize"] = size; cls.append(f"has-{size}-font-size")
    if typo:
        a["style"] = {"typography": typo}; css += [f"{k2css(k)}:{v}" for k, v in typo.items()]
    at = (" " + j(a)) if a else ""
    sc = f' style="{";".join(css)}"' if css else ""
    lis = "\n\n".join(f'<!-- wp:list-item -->\n<li>{T(i)}</li>\n<!-- /wp:list-item -->' for i in items)
    return f'<!-- wp:list{at} -->\n<ul class="{" ".join(cls)}"{sc}>{lis}</ul>\n<!-- /wp:list -->'

def img(file, alt, ratio=None, radius=None):
    return image(file, alt, ratio, radius)

def cover(inner, name, file, dim=40, minh="80vh", pos="bottom left", pad=("xx-large", "xx-large", "medium", "medium"), content="80rem", overlay="main"):
    pa, pc = padding(pad)
    mh, unit = (minh[:-2], "vh") if minh.endswith("vh") else (minh, None)
    a = {"url": IMG(file), "dimRatio": dim, "overlayColor": overlay, "isUserOverlayColor": True, "minHeight": int(mh), "minHeightUnit": unit, "contentPosition": pos, "align": "full", "metadata": {"name": name},
         "style": {"spacing": {"padding": pa, "margin": {"top": "0", "bottom": "0"}}}, "layout": {"type": "constrained", "contentSize": content}}
    posc = "is-position-" + pos.replace(" ", "-")
    hc = " has-custom-content-position " + posc if pos != "center center" else ""
    dimc = "has-background-dim" if dim == 50 else f"has-background-dim-{dim} has-background-dim" if dim else "has-background-dim-0 has-background-dim"
    css = f"margin-top:0;margin-bottom:0;{pc};min-height:{mh}{unit or 'px'}"
    return (f'<!-- wp:cover {j(a)} -->\n<div class="wp-block-cover alignfull{hc}" style="{css}"><img class="wp-block-cover__image-background" alt="" src="{IMG(file)}" data-object-fit="cover"/>'
            f'<span aria-hidden="true" class="wp-block-cover__background has-{overlay}-background-color {dimc}"></span><div class="wp-block-cover__inner-container">{inner}</div></div>\n<!-- /wp:cover -->')

def fill(file, rem):
    """A photo that fills its column: a cover with no overlay and nothing on it."""
    a = {"url": IMG(file), "dimRatio": 0, "overlayColor": "main", "isUserOverlayColor": True, "minHeight": rem, "minHeightUnit": "rem", "layout": {"type": "constrained"}}
    return (f'<!-- wp:cover {j(a)} -->\n<div class="wp-block-cover" style="min-height:{rem}rem"><img class="wp-block-cover__image-background" alt="" src="{IMG(file)}" data-object-fit="cover"/>'
            f'<span aria-hidden="true" class="wp-block-cover__background has-main-background-color has-background-dim-0 has-background-dim"></span><div class="wp-block-cover__inner-container"></div></div>\n<!-- /wp:cover -->')

def on_photo(markup):
    """Text in a cover takes the background colour, which stays light whatever the palette."""
    return markup.replace('<!-- wp:group {', '<!-- wp:group {"textColor":"base",', 1).replace('class="wp-block-group', 'class="wp-block-group has-base-color has-text-color', 1)

def table(head, rows, style=None):
    a = {"hasFixedLayout": False}
    cls = "wp-block-table"
    if style: a["className"] = f"is-style-{style}"; cls += f" is-style-{style}"
    th = "".join(f"<th>{T(c)}</th>" for c in head)
    tb = "".join("<tr>" + "".join(f"<td>{T(c)}</td>" for c in r) + "</tr>" for r in rows)
    return f'<!-- wp:table {j(a)} -->\n<figure class="{cls}"><table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></figure>\n<!-- /wp:table -->'

def quote(text, cite, size="x-large", family=None):
    return f'<!-- wp:quote {{"className":"is-style-plain"}} -->\n<blockquote class="wp-block-quote is-style-plain">' + p(text, size, None, None, family, {"lineHeight": "1.15"}) + f'<cite>{T(cite)}</cite></blockquote>\n<!-- /wp:quote -->'

N = "\n\n".join
PAD_CARD = ("large", "large", "large", "large")

# ---------------------------------------------------------------- variations
order = ["primary", "primary-accent", "primary-alt", "primary-alt-accent", "main", "main-accent", "base", "secondary", "tertiary", "border-light", "border-dark"]
theme = json.load(open("theme.json"))
names = {c["slug"]: c["name"] for c in theme["settings"]["color"]["palette"]}

def variation(slug, title, pal, body, head, weight, ls, lh, button, extra_elements=None, blocks=None, transform=None):
    assert set(pal) == set(order), slug
    heading_t = {"fontFamily": f"var:preset|font-family|{head}", "fontWeight": weight, "letterSpacing": ls, "lineHeight": lh}
    if transform: heading_t["textTransform"] = transform
    els = {"heading": {"typography": heading_t}, "button": button}
    if extra_elements: els.update(extra_elements)
    data = {"$schema": SCHEMA, "version": 3, "title": title, "slug": slug,
            "settings": {"color": {"palette": [{"color": pal[s], "name": names[s], "slug": s} for s in order]}},
            "styles": {"typography": {"fontFamily": f"var:preset|font-family|{body}"}, "elements": els,
                       "blocks": {**(blocks or {}), "core/image": {"border": {"radius": "0"}},
                                  "core/quote": {"border": {"left": {"width": "0"}}, "spacing": {"padding": {"left": "0"}}}}}}
    path = f"styles/{slug}.json"
    json.dump(data, open(path, "w"), indent="\t", ensure_ascii=False); open(path, "a").write("\n")

def button(radius, family=None, weight="600", transform=None, size="var:preset|font-size|base", ls=None):
    t = {"fontWeight": weight, "fontSize": size}
    if family: t["fontFamily"] = f"var:preset|font-family|{family}"
    if transform: t["textTransform"] = transform
    if ls: t["letterSpacing"] = ls
    return {"border": {"radius": radius}, "typography": t}

def site_title(family, weight, transform=None, ls=None):
    t = {"fontFamily": f"var:preset|font-family|{family}", "fontWeight": weight}
    if transform: t["textTransform"] = transform
    if ls: t["letterSpacing"] = ls
    return {"core/site-title": {"typography": t}}

# Ridge: home services. Loud and flat, like a site sign: condensed capitals, hi-vis yellow, no rounding.
variation("kit-ridge", "Ridge (home services)", {
    "primary": "#ad3209", "primary-accent": "#f6dccf", "primary-alt": "#ffb000", "primary-alt-accent": "#1a1205",
    "main": "#111417", "main-accent": "#d9d5cc", "base": "#f1eee7", "secondary": "#41454a", "tertiary": "#e6e1d6",
    "border-light": "#d6d0c3", "border-dark": "#2c3035"},
    "public-sans", "big-shoulders", "800", "0", "0.9",
    button("0", "big-shoulders", "800", "uppercase", "var:preset|font-size|medium", "0.02em"),
    blocks=site_title("big-shoulders", "900", "uppercase"), transform="uppercase")

# Hearth: food and drink. A printed menu card: a soft serif on olive and bone, mustard for the second colour.
variation("kit-hearth", "Hearth (food and drink)", {
    "primary": "#38450f", "primary-accent": "#dfe3c8", "primary-alt": "#d3a648", "primary-alt-accent": "#2b170a",
    "main": "#262c0c", "main-accent": "#d9dbc9", "base": "#efeee7", "secondary": "#4d5530", "tertiary": "#e3e1d5",
    "border-light": "#cfcdbf", "border-dark": "#3c4320"},
    "source-serif", "young-serif", "400", "-0.01em", "1.05",
    button("var:preset|border-radius|full", "source-serif", "600"),
    blocks=site_title("young-serif", "400"))

# Still: wellness. Quiet: light serif at large sizes, three stone colours, square buttons.
variation("kit-still", "Still (wellness)", {
    "primary": "#56644e", "primary-accent": "#dde2d6", "primary-alt": "#cdc3b6", "primary-alt-accent": "#333231",
    "main": "#333231", "main-accent": "#d8d5d0", "base": "#eeecea", "secondary": "#55514d", "tertiary": "#e4e1dd",
    "border-light": "#d3cfc9", "border-dark": "#4a4846"},
    "newsreader", "newsreader", "300", "-0.02em", "1.02",
    button("0", "newsreader", "500"),
    blocks=site_title("newsreader", "400", None, "-0.01em"))

# Ledger: professional services. An annual report: a strong sans for titles, a reading serif for text, deep teal.
variation("kit-ledger", "Ledger (professional services)", {
    "primary": "#06525c", "primary-accent": "#dcebe8", "primary-alt": "#c7dcd6", "primary-alt-accent": "#06343a",
    "main": "#06343a", "main-accent": "#cfdedc", "base": "#f7f9f8", "secondary": "#2f5f66", "tertiary": "#ebf0ee",
    "border-light": "#d3e0dd", "border-dark": "#1d4f55"},
    "source-serif", "libre-franklin", "700", "-0.02em", "1.05",
    button("0", "libre-franklin", "600"),
    blocks=site_title("libre-franklin", "800", None, "-0.02em"))

def kit(slug, kitcat, title, desc, kw, inner):
    write(slug, title, desc, kitcat, kw, inner)

def kit_page(slug, title, desc, kw, parts):
    write(slug, title, desc, "anypress/pages", kw, N(BODIES[x] for x in parts), "core/post-content", " * Post Types: page\n")

# ---------------------------------------------------------------- Ridge
R = "anypress/kit-home-services"
CAPS = {"lineHeight": "0.9"}
kit("ridge-hero", R, "Ridge hero: big words on hi-vis yellow",
 "Opening section for a trade: a very large headline in capitals on the second brand colour, one sentence, the phone number as the main button and a photo of the team at work. Part of the Ridge kit (home services); looks as designed with the Ridge style.",
 "hero, trades, roofer, builder, plumber, phone, quote, ridge",
 sec("Hero", cols([
   col(N([h("Burst pipe? We can be there within the hour.", 1, "poster"),
          p("Family-run plumbers and heating engineers covering the whole county since 2001. Licensed, insured and on call day and night.", "medium"),
          btns([("Call 555 0142", None, "tel:5550142"), ("Get a free quote", "outline", "#quote")])]), "58%", valign="center"),
   col(img("placeholder-tall.svg", "A plumber fitting a new dishwasher under a kitchen counter", "4/5"))], "x-large", "wide", "center"),
   "section-second-brand", ("x-large", "x-large", None, None)))

def panel(big, small, style, width=None):
    return col(N([h(big, 3, "x-large"), p(small, "medium")]), width, style, PAD_CARD)
kit("ridge-proof", R, "Ridge proof: three facts on coloured panels",
 "Three facts that make people trust a trade (years in business, guarantee, licence) on panels of different colours and widths, edge to edge. Part of the Ridge kit; only state facts the owner has confirmed.",
 "credentials, proof, licensed, insured, guarantee, years, ridge",
 sec("Proof", cols([
   panel("Since 2001", "In the same county. Most of our work comes from neighbors of past jobs.", "section-dark", "40%"),
   panel("1-year guarantee", "On every repair, parts and labour, in writing.", "section-brand"),
   panel("Licensed", "Master plumber licence 48213. Fully insured.", "section-tint")], "0", "full", None),
   None, (None, None, None, None), layout={"type": "default"}))

def svc_row(name, text, price):
    return cols([col(h(name, 3, "x-large"), "40%"), col(p(text, "medium")), col(p(price, "large", None, "right", "big-shoulders", {"fontWeight": "800"}), "20%")], "medium", "wide", "top")
kit("ridge-services", R, "Ridge services: big list with prices on dark",
 "Services as a big list on the dark section style: each row has the service in large capitals, one line about it and a starting price. No icons or cards. Part of the Ridge kit.",
 "services, prices, price list, repairs, trades, ridge",
 sec("Services", N([h("What we fix", 2, "xxx-large"), grp(N([
   svc_row("Leaks", "Found, fixed and photographed, the same day when we can.", "From $150"),
   svc_row("Drains", "Blocked sinks, toilets and main lines cleared, with a camera check.", "From $120"),
   svc_row("Water heaters", "Tank and tankless heaters repaired or replaced, old one taken away.", "From $950"),
   svc_row("Heating", "Boilers and furnaces serviced, repaired or replaced.", "From $110")]), gap="large", layout={"type": "default"}, align="wide")]),
   "section-dark"))

kit("ridge-photo", R, "Ridge photo: full-width job photo with a caption bar",
 "One full-width photo of a real job with a short caption on a solid bar in the corner: where it was and what was done. Part of the Ridge kit; use the owner's own photo.",
 "photo, gallery, job, project, full width, caption, ridge",
 cover(grp(p("A 1920s bathroom in Chatham, re-plumbed in new copper with the old clawfoot bath kept.", "medium"), "section-card", ("medium", "medium", "medium", "medium"), layout={"type": "constrained", "contentSize": "30rem", "justifyContent": "left"}),
   "Job photo", "placeholder-wide.svg", 0, "75vh", "bottom left", ("large", "large", "medium", "medium")))

kit("ridge-areas", R, "Ridge areas: towns served as a big list",
 "Where the business works: a heading and sentence beside a big list of towns in capitals. Part of the Ridge kit; list the owner's real areas.",
 "areas served, locations, towns, service area, ridge",
 sec("Areas served", cols([
   col(N([h("Where we work", 2, "xxx-large"), p("Every town within 30 miles of Springfield. Outside that, call and ask: we often say yes.", "medium", "secondary")]), "40%"),
   col(lst(["Springfield", "Oak Hill", "Riverside", "Millbrook", "Cedar Falls", "Ashford", "Kingsley"], "xx-large", "big-shoulders", {"lineHeight": "1", "textTransform": "uppercase", "fontWeight": "800"}, "no-bullets"))], "x-large", "wide", "top")))

kit("ridge-reviews", R, "Ridge reviews: one big, two small",
 "Customer reviews on panels of different sizes: one long review large on the brand colour, two short ones beside it. Part of the Ridge kit; use real reviews with the customer's name and town.",
 "reviews, testimonials, customers, proof, ridge",
 sec("Reviews", cols([
   col(quote("They found a leak two other plumbers missed, fixed it the same afternoon and sent photos of every step.", "Dana R., Springfield", "xx-large", "big-shoulders"), "62%", "section-brand", PAD_CARD, "bottom"),
   col(N([grp(N([p("Booked on Monday, fixed on Tuesday, and the price did not change.", "medium"), p("Jo M., Riverside", None, "secondary")]), "section-tint", PAD_CARD, "small"),
          grp(N([p("Tidy, polite and they explained every step in plain words.", "medium"), p("Carlos T., Oak Hill", None, "secondary")]), "section-tint", PAD_CARD, "small")]))], "small", "wide", None),
   None, ("x-large", "x-large", None, None)))

kit("ridge-call", R, "Ridge closing: the phone number, huge",
 "The last section of a trade's page: the phone number as large as the page allows, linked so phones can call it, with the hours under it. Part of the Ridge kit.",
 "call to action, phone, call, contact, emergency, ridge",
 sec("Call", N([p("Call us", "large", None, None, "big-shoulders", {"textTransform": "uppercase", "fontWeight": "800"}),
   p('<a href="tel:5550142">' + T("555 0142") + '</a>', "poster", None, None, "big-shoulders", {"lineHeight": "0.9", "fontWeight": "900"}, raw=True),
   p("Office hours 7am to 7pm, seven days. Emergencies day and night. Free quotes, with photos of what we find.", "medium")]), "section-brand", ("xx-large", "xx-large", None, None)))

kit_page("kit-home-services", "Home page: Ridge kit, home services",
 "A complete home page for a plumber, electrician, roofer or other trade in the Ridge kit: a loud hero with the phone number, proof on coloured panels, numbers that count up, services with prices and links to their pages, how it works, a job photo, reviews in a carousel, areas served with a map, answers to common questions and a huge phone number to close. Apply the Ridge style for the look it was designed with.",
 "home, trades, roofer, builder, plumber, electrician, cleaner, landscaper, kit, ridge",
 ["ridge-hero", "ridge-proof", "ridge-services", "ridge-photo", "ridge-areas", "ridge-reviews", "ridge-call"])

# ---------------------------------------------------------------- Hearth
H = "anypress/kit-food"
kit("hearth-hero", H, "Hearth hero: a menu card over a photo",
 "Opening section for a café, bakery or restaurant: a full-width food photo with a card on top that reads like the front of a menu, with the name of the place, what they serve, opening times and two buttons. Part of the Hearth kit (food and drink).",
 "hero, restaurant, cafe, bakery, menu, opening hours, hearth",
 cover(grp(N([h("Bread, coffee and a long lunch", 1, "xx-large", "center"),
   p("Baked on site every morning since 1989.", "medium", None, "center", None, {"fontStyle": "italic"}),
   p("Tuesday to Sunday, 7am to 3pm", None, None, "center"),
   btns([("See the menu", None, "#menu"), ("Order a cake", "outline", "#visit")], "center")]), "section-card", ("x-large", "x-large", "large", "large"), "medium", {"type": "constrained", "contentSize": "40rem"}),
   "Hero", "placeholder-wide.svg", 20, "92vh", "center center", ("xx-large", "xx-large", "medium", "medium"), "44rem"))

def item(name, text, price):
    return grp(N([grp(N([h(name, 3, "medium"), p(price, "medium")]), "menu-leader", layout={"type": "flex", "flexWrap": "nowrap", "justifyContent": "space-between", "verticalAlignment": "bottom"}),
                  p(text, None, "secondary", None, None, {"fontStyle": "italic"})]), gap="small", layout={"type": "default"})
def course(title, items):
    return grp(N([h(title, 2, "x-large", "center")] + [item(*i) for i in items]), gap="medium", layout={"type": "default"})
kit("hearth-menu", H, "Hearth menu: two courses with dotted leaders",
 "A menu in two columns, set like a printed card: each dish with a dotted line to its price and a line about it in italics. Part of the Hearth kit; one column per course, and change the dishes to the real menu.",
 "menu, food, dishes, price list, breakfast, lunch, hearth",
 sec("Menu", N([h("The menu", 2, "xxx-large", "center"), p("Everything is made here. Ask about allergies at the counter.", "medium", "secondary", "center", None, {"fontStyle": "italic"}),
   cols([col(course("Breakfast", [("Sourdough toast", "Cultured butter and this week's jam.", "6"), ("Eggs on rye", "Two eggs your way, greens, chilli oil.", "11"), ("Almond croissant", "Baked twice, filled with frangipane.", "5"), ("Granola", "Yoghurt, honey, fruit of the season.", "9")])),
         col(course("Lunch", [("Soup and bread", "Changes daily. Always a slab of sourdough.", "10"), ("Ham and pickles", "Rye, mustard butter, our own pickles.", "13"), ("Leek tart", "Gruyère, thyme, a sharp salad.", "14"), ("Cake of the day", "Whatever came out of the oven at noon.", "5")]))], "xx-large", "wide", None)]),
   "section-tint", content="68rem"))

def spec(file, alt, name, price, style):
    return grp(N([img(file, alt, "1"), grp(N([h(name, 3, "medium"), p(price)]), layout={"type": "flex", "flexWrap": "nowrap", "justifyContent": "space-between"})]), style, ("small", "medium", "small", "small"), "small")
kit("hearth-specimens", H, "Hearth favourites: four things to try, on coloured tiles",
 "Four signature items as photo tiles on alternating colours, each with its name and price. Part of the Hearth kit; use the owner's own photos of the food.",
 "favourites, specials, products, bakery, gallery, hearth",
 sec("Favourites", N([h("Worth the queue", 2, "xxx-large"), grp(N([
   spec("placeholder-square.svg", "A round sourdough loaf, floured and scored", "Country loaf", "$8", "section-brand"),
   spec("placeholder-square.svg", "Cinnamon buns on a plate beside two cups of coffee", "Cinnamon bun", "$4", "section-second-brand"),
   spec("placeholder-square.svg", "Sesame rolls on a baking tray", "Sesame rolls", "$1.50", "section-brand-soft"),
   spec("placeholder-square.svg", "An espresso and a small brownie", "Espresso and a brownie", "$6", "section-dark")]), gap="small", layout={"type": "grid", "columnCount": 4, "minimumColumnWidth": "14rem"}, align="wide")])))

kit("hearth-story", H, "Hearth story: photo beside a story card",
 "The story of the place on a card of the brand colour, edge to edge with a tall photo: who runs it, since when, how things are made, signed by the owners. Part of the Hearth kit; the owner's own words.",
 "about, story, owner, history, family, hearth",
 sec("Story", cols([
   col(fill("placeholder-tall.svg", 34), "42%"),
   col(N([h("One oven, three generations", 2, "xx-large"), p("Maria opened the bakery in 1989 with one oven and her grandmother's recipes. Today her son Luca runs the early shift, and the rye is still made the same way.", "medium"),
          p("The flour comes from a mill forty miles away. The butter comes from the farm next to it.", "medium"), p("Maria and Luca", "large", None, None, "young-serif")]), None, "section-brand", ("xx-large", "xx-large", "x-large", "x-large"), "center")], "0", "full", None),
   None, (None, None, None, None), layout={"type": "default"}))

def visit(title, lines):
    return col(N([h(title, 3, "large"), grp(N(p(l, "medium") for l in lines), gap="small")]))
kit("hearth-visit", H, "Hearth visit: hours, address and how to order",
 "Practical details on the second brand colour in large type: opening hours, the address and how to order or book. Part of the Hearth kit; replace every detail with the real ones.",
 "contact, visit, opening hours, address, phone, order, hearth",
 sec("Visit", N([h("Come by", 2, "xxx-large"), cols([
   visit("Hours", ["Tuesday to Friday, 7am to 3pm", "Saturday and Sunday, 8am to 3pm", "Closed Monday"]),
   visit("Find us", ["14 Market Street, Springfield", "Two minutes from the station"]),
   visit("Order", ["Cakes with three days' notice", "555 0198", "hello@example.com"])], "x-large", "wide", None)]), "section-second-brand"))

kit_page("kit-food", "Home page: Hearth kit, food and drink",
 "A complete home page for a café, bakery or restaurant in the Hearth kit: a menu card over a food photo, the menu with dotted leaders, four favourites on coloured tiles, the story beside a photo and the practical details. Apply the Hearth style for the look it was designed with.",
 "home, restaurant, cafe, bakery, food, menu, kit, hearth",
 ["hearth-hero", "hearth-menu", "hearth-specimens", "hearth-story", "hearth-visit"])

# ---------------------------------------------------------------- Still
W = "anypress/kit-wellness"
kit("still-hero", W, "Still hero: full-screen photo with the name along the bottom",
 "Opening section for a spa, massage practice, therapist or studio: one calm photo filling the screen, the name very large and light along the bottom, and one line about what they offer. Part of the Still kit (wellness).",
 "hero, spa, massage, therapy, wellness, yoga, full screen, still",
 cover(on_photo(grp(N([h("Still Water", 1, "poster", None, None, {"lineHeight": "0.95"}), p("Massage and quiet rooms in the old mill, Hebden Bridge.", "large")]), gap="small", layout={"type": "default"})),
   "Hero", "placeholder-tall.svg", 50, "100vh", "bottom left", ("xx-large", "large", "medium", "medium"), "80rem"))

kit("still-intro", W, "Still welcome: a few words, set to one side",
 "A short welcome in large, light type, set off-centre with plenty of space around it. Part of the Still kit; two or three sentences at most.",
 "intro, welcome, about, statement, still",
 sec("Welcome", N([p("An hour where nobody needs anything from you.", "xx-large", None, None, None, {"lineHeight": "1.1", "fontWeight": "300"}),
   p("We keep the rooms warm, the lights low and the phones outside. Treatments are booked with gaps between them, so nobody rushes you in or out.", "medium", "secondary"),
   btns([("Book a treatment", None, "#book")])]), content="36rem", justify="right", pad=("xx-large", "x-large", None, None)))

kit("still-photos", W, "Still photos: two of different sizes",
 "Two photos side by side at different sizes and heights, with a short caption under the smaller one. Part of the Still kit; a calm room and a close detail work well.",
 "photos, gallery, rooms, interior, still",
 sec("Photos", cols([
   col(img("placeholder-wide.svg", "The treatment room with a bath and a plant", "4/3"), "62%"),
   col(N([img("placeholder-tall.svg", "A white peace lily", "3/4"), p("The garden room, open in summer.", None, "secondary")]), None, None, None, "bottom")], "x-large", "wide", "bottom"),
   pad=("x-large", "xx-large", None, None)))

def treat(name, detail, price):
    return cols([col(grp(N([h(name, 3, "large"), p(detail, None, "secondary")]), gap="small")), col(p(price, "large", None, "right"), "25%")], "medium", None, "top", False)
kit("still-treatments", W, "Still treatments: plain list with prices",
 "Treatments as a plain list with lots of space: the name, the length and what it is for, and the price on the right. No icons, no cards. Part of the Still kit.",
 "treatments, services, prices, massage, menu, still",
 sec("Treatments", N([h("Treatments", 2, "xx-large"), grp(N([
   treat("Deep tissue massage", "60 or 90 minutes. For tight shoulders, backs and legs.", "$85 / $120"),
   treat("Hot stone massage", "75 minutes. Slow and warm, for sleep.", "$100"),
   treat("Quiet room", "Two hours with tea, the bath and nothing to do.", "$40"),
   treat("Gift voucher", "Any amount, sent by email or in a card.", "From $40")]), gap="x-large", layout={"type": "default"})]), content="48rem"))

def practical(title, text):
    return col(N([h(title, 3, "medium"), p(text, None, "secondary")]))
kit("still-practical", W, "Still practical: how to find us, hours and what to know",
 "The practical details at the end of a page, on the tint colour: how to find the place, opening hours and what to know before coming, then the booking button. Part of the Still kit.",
 "contact, hours, location, before you come, booking, still",
 sec("Practical", N([cols([
   practical("Finding us", "Ground floor of the old mill, 3 Canal Street. Park on Station Road, two minutes' walk."),
   practical("Hours", "Tuesday to Saturday, 10am to 8pm. Sunday, 10am to 4pm."),
   practical("Before you come", "Arrive ten minutes early. Tell us about injuries or pregnancy when you book.")], "x-large", "wide", None),
   btns([("Book a treatment", None, "#book"), ("Call 555 0170", "outline", "tel:5550170")])]), "section-tint"))

kit_page("kit-wellness", "Home page: Still kit, wellness",
 "A complete home page for a spa, massage therapist, yoga studio or clinic in the Still kit: a full-screen photo with the name along the bottom, a short welcome, two photos, treatments as a plain list and the practical details. Apply the Still style for the look it was designed with.",
 "home, spa, massage, wellness, therapy, yoga, clinic, kit, still",
 ["still-hero", "still-intro", "still-photos", "still-treatments", "still-practical"])

# ---------------------------------------------------------------- Ledger
L = "anypress/kit-professional"
kit("ledger-masthead", L, "Ledger masthead: title panel beside a photo",
 "Opening section for an accountant, lawyer, consultant or agency: a title panel on the brand colour beside a photo, edge to edge, with what the firm does, for whom and one button. Part of the Ledger kit (professional services).",
 "hero, accountant, lawyer, consultant, firm, professional, ledger",
 sec("Masthead", cols([
   col(N([h("Accounts, tax and payroll for small firms in Leeds", 1, "xxx-large"), p("Fixed monthly fees. One accountant who knows your business, and answers the phone.", "medium"),
          btns([("Book a free call", None, "#contact")])]), "42%", "section-brand", ("xx-large", "xx-large", "x-large", "x-large"), "center"),
   col(fill("placeholder-tall.svg", 34))], "0", "full", None),
   None, (None, None, None, None), layout={"type": "default"}))

def axis(title, body, note=None):
    right = [p(body, "medium")] + ([p(note, None, "secondary")] if note else [])
    return cols([col(h(title, 3, "large"), "42%"), col(grp(N(right), gap="small"))], "large", "wide", None)
kit("ledger-services", L, "Ledger services: headings on the left, detail on the right",
 "Services set like a report: each heading in the left column, what it covers and a side note on the right, on a shared line down the page. Part of the Ledger kit.",
 "services, what we do, practice areas, accounting, legal, ledger",
 sec("Services", grp(N([cols([col(h("What we do", 2, "xx-large"), "42%"), col(p("Most clients use us for all three. Some start with one and add the rest later.", "medium", "secondary"))], "large", "wide", None),
   grp(N([axis("Year-end accounts", "Accounts and the company tax return, filed weeks before the deadline.", "Includes a meeting to go through the numbers."),
          axis("Bookkeeping and VAT", "We keep the books in your software and file VAT every quarter.", "Xero, QuickBooks or FreeAgent."),
          axis("Payroll", "Payslips, pension and filings for teams of one to fifty.", "Monthly or weekly runs.")]), gap="x-large", layout={"type": "default"}, align="wide")]), gap="xx-large", layout={"type": "default"}, align="wide")))

kit("ledger-quote", L, "Ledger quotation: full-width colour page",
 "One client quotation large on a full-width page of the second brand colour, with the client's name and business. Part of the Ledger kit; use a real client's words, with permission.",
 "testimonial, quote, client, review, proof, ledger",
 sec("Quotation", quote("They found us eleven thousand pounds in the first year, and they explained how in plain English.", "Priya S., owner, Northside Dental", "xx-large", "libre-franklin"), "section-second-brand", content="56rem"))

kit("ledger-fees", L, "Ledger fees: a table of prices",
 "Fees in a plain table: the service, what is included and the starting price. Part of the Ledger kit; fixed prices build trust with professional clients.",
 "fees, prices, pricing table, costs, ledger",
 sec("Fees", N([h("Fees", 2, "xx-large"), p("Fixed monthly fees, agreed before we start. No charge for phone calls or emails.", "medium", "secondary"),
   table(["Service", "Included", "From"], [["Sole trader", "Accounts, tax return, bookkeeping", "$95 a month"], ["Limited company", "Accounts, company tax, payroll for two", "$180 a month"], ["Growing team", "Everything, plus quarterly reviews", "$420 a month"]], "stripes")]), "section-tint", content="56rem"))

kit("ledger-contact", L, "Ledger contact: talk to us",
 "A closing section in two columns: a heading on the left and on the right how to reach the firm, the office address and a button to book a call. Part of the Ledger kit.",
 "contact, call, book a call, address, ledger",
 sec("Contact", cols([col(h("Talk to an accountant this week", 2, "xx-large"), "42%"),
   col(N([p("Book a free 30-minute call, or ring the office. You will speak to the person who would do your accounts.", "medium"),
          p(T("2 Park Square, Leeds LS1 2NE") + "<br>" + T("0113 555 0190"), None, "secondary", raw=True), btns([("Book a free call", None, "#contact")])]))], "large", "wide", None)))

kit_page("kit-professional", "Home page: Ledger kit, professional services",
 "A complete home page for an accountant, lawyer, consultant or agency in the Ledger kit: a title panel beside a photo, services set like a report, a client quotation, a fees table and contact. Apply the Ledger style for the look it was designed with.",
 "home, accountant, lawyer, consultant, agency, professional, firm, kit, ledger",
 ["ledger-masthead", "ledger-services", "ledger-quote", "ledger-fees", "ledger-contact"])
print("kits ok")

# ---------------------------------------------------------------- Everyday sections (gaps found in JP Blocks' catalogue)
def card(inner, style):
    return grp(inner, style, PAD_CARD, "small")
def links(items):
    lis = "\n\n".join(f'<!-- wp:list-item -->\n<li><a href="{href}">{T(label)}</a></li>\n<!-- /wp:list-item -->' for label, href in items)
    return f'<!-- wp:list {{"className":"is-style-no-bullets"}} -->\n<ul class="wp-block-list is-style-no-bullets">{lis}</ul>\n<!-- /wp:list -->'

write("pros-cons", "Pros and cons, side by side",
 "Two lists side by side: what is good about something and what is not, on two tint colours. Use in reviews, comparisons and buying guides; keep each point to one line.",
 "text, anypress-details", "pros and cons, comparison, review, good, bad, buying guide",
 sec("Pros and cons", N([h("Is a metal roof worth it?", 2), cols([
   col(card(N([h("Good", 3, "medium"), lst(["Lasts 40 to 70 years", "Sheds snow and rain fast", "Fire resistant"])]), "section-brand-soft")),
   col(card(N([h("Not so good", 3, "medium"), lst(["Costs two to three times more", "Louder in heavy rain without insulation", "Fewer roofers fit it"])]), "section-tint"))], "medium", "wide", None)]),
   content="60rem"))

write("product-box", "Product box: photo, price and reasons to buy",
 "One product in a box: photo, name, a sentence, three reasons to buy, the price and a button. Use in reviews and guides to recommend a product, or to feature one item on a page.",
 "call-to-action, services", "product, product box, recommendation, review, buy, affiliate, featured",
 sec("Product", grp(cols([
   col(img("placeholder-square.svg", "The product on a plain background", "1"), "40%"),
   col(N([h("Linen bath towel", 3, "large"), p("Heavy, quick to dry and softer with every wash.", "medium", "secondary"),
          lst(["Stonewashed European linen", "Dries in half the time of cotton", "Five colours"]),
          p("$48", "x-large"), btns([("Buy now", None, "#")])]), None, None, None, "center")], "large", None, "center"),
   "section-card", ("large", "large", "large", "large"), radius="md", layout={"type": "default"}), content="56rem"))

write("notice", "Notice: one short message on a band",
 "A short band with one message in bold and a link, such as holiday hours, a delivery cut-off or an announcement. Use at the top of a page and take it down when it no longer applies.",
 "text, call-to-action", "notice, alert, announcement, holiday hours, banner, message",
 sec("Notice", p("<strong>" + T("Closed 24 to 26 December.") + "</strong> " + T("Orders placed after noon on the 23rd go out on the 27th.") + ' <a href="#">' + T("See holiday hours") + "</a>", None, None, "center", raw=True),
   "section-second-brand", ("small", "small", None, None), content="60rem"))

write("table-of-contents", "On this page: links to each section",
 "A short list of links to the sections further down a long page, in a tint box. Use on guides, policies and long service pages; give each linked heading a matching HTML anchor.",
 "text", "table of contents, contents, on this page, jump links, navigation",
 sec("On this page", card(N([h("On this page", 2, "medium"), links([("What it costs", "#costs"), ("How long it takes", "#time"), ("What to ask before you hire", "#questions"), ("Our guarantee", "#guarantee")])]), "section-tint"),
   pad=("large", "large", None, None), content="44rem"))

write("newsletter-signup", "Signup: join the email list",
 "A band asking visitors to join the email list: a heading, what they will get and how often, and a button. Put the store's signup form in place of the button when one exists.",
 "call-to-action", "newsletter, signup, email list, subscribe, mailing list",
 sec("Signup", cols([
   col(N([h("One email a month, worth opening", 2, "x-large"), p("New work, seasonal offers and the odd early invitation. Unsubscribe in one click.")]), "62%"),
   col(btns([("Sign up", None, "#signup")], "right"), None, None, None, "center")], "large", "wide", "center"), "section-brand-soft", ("x-large", "x-large", None, None)))

def stack(items):
    out = []
    for label, href in items:
        out.append(f'<!-- wp:button {{"style":{{"dimensions":{{"width":"100%"}}}}}} -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{href}">{T(label)}</a></div>\n<!-- /wp:button -->')
    return '<!-- wp:buttons {"layout":{"type":"flex","orientation":"vertical","justifyContent":"stretch"}} -->\n<div class="wp-block-buttons">' + "\n\n".join(out) + '</div>\n<!-- /wp:buttons -->'
avatar = '<!-- wp:image {"width":"8rem","aspectRatio":"1","scale":"cover","sizeSlug":"large","linkDestination":"none","align":"center","style":{"border":{"radius":"var:preset|border-radius|full"}}} -->\n<figure class="wp-block-image aligncenter size-large is-resized has-custom-border"><img src="' + IMG("placeholder-square.svg") + '" alt="' + A("Portrait of the owner") + '" style="border-radius:var(--wp--preset--border-radius--full);aspect-ratio:1;object-fit:cover;width:8rem;height:auto"/></figure>\n<!-- /wp:image -->'
write("page-links", "Links page (link in bio)",
 "A one-column page of large buttons for the link in a social media bio: a round photo, the name, one line and a button for each place to go. Keep it to the five or six links that matter.",
 "anypress/pages", "link in bio, links, social media, instagram, tiktok, linktree",
 sec("Links", N([avatar, h("Ana Ortiz", 1, "x-large", "center"), p("Yoga and pilates in Springfield. Classes every day.", None, "secondary", "center"),
   stack([("Book a class", "/book/"), ("This week's timetable", "/timetable/"), ("Gift vouchers", "/gift-vouchers/"), ("Read the blog", "/blog/"), ("Get in touch", "/contact/")])]),
   pad=("xx-large", "xx-large", None, None), content="28rem"), "core/post-content", " * Post Types: page\n")
print("everyday ok")

exec(open(os.path.join(HERE, "kits_more.py")).read())
exec(open(os.path.join(HERE, "kit_ridge.py")).read())

import importlib.util as _u
_s = _u.spec_from_file_location("bc", os.path.join(HERE, "blocks_cats.py")); _m = _u.module_from_spec(_s); _s.loader.exec_module(_m); _m.apply(OUT)
