import os, sys
OUT = sys.argv[1]
T = lambda s: "<?php esc_html_e( '%s', 'anypress' ); ?>" % s.replace("'", "\\'")
IMG = lambda f: "<?php echo esc_url( get_theme_file_uri( 'assets/images/%s' ) ); ?>" % f
def pad(t, b, lr=None):
    st = {"top": f"var:preset|spacing|{t}", "bottom": f"var:preset|spacing|{b}"}
    css = f"padding-top:var(--wp--preset--spacing--{t});padding-bottom:var(--wp--preset--spacing--{b})"
    if lr:
        st.update({"left": f"var:preset|spacing|{lr}", "right": f"var:preset|spacing|{lr}"})
        css += f";padding-left:var(--wp--preset--spacing--{lr});padding-right:var(--wp--preset--spacing--{lr})"
    return st, css
import json
def j(d): return json.dumps(d, separators=(",", ":"))

def section(name, style, inner, t="xx-large", b="xx-large", content=None, extra_cls=""):
    st, css = pad(t, b)
    attrs = {"metadata": {"name": name}, "align": "full"}
    cls = "wp-block-group alignfull"
    if style:
        attrs["className"] = f"is-style-{style}"; cls += f" is-style-{style}"
    attrs["style"] = {"spacing": {"padding": st, "margin": {"top": "0", "bottom": "0"}}}
    layout = {"type": "constrained"}
    if content: layout["contentSize"] = content
    attrs["layout"] = layout
    css = "margin-top:0;margin-bottom:0;" + css
    return f'<!-- wp:group {j(attrs)} -->\n<section class="{cls}" style="{css}">{inner}</section>\n<!-- /wp:group -->'.replace('<!-- wp:group {', '<!-- wp:group {"tagName":"section",', 1)

def heading(text, level=2, size=None, align=None, extra=None):
    a = {}
    if align: a["textAlign"] = align
    if level != 2: a["level"] = level
    if size: a["fontSize"] = size
    if extra: a.update(extra)
    cls = ["wp-block-heading"]
    if align: cls.append(f"has-text-align-{align}")
    if size: cls.append(f"has-{size}-font-size")
    at = (" " + j(a)) if a else ""
    return f'<!-- wp:heading{at} -->\n<h{level} class="{" ".join(cls)}">{T(text)}</h{level}>\n<!-- /wp:heading -->'

def para(text, size=None, color=None, align=None):
    a = {}; cls = []
    if align: a["align"] = align; cls.append(f"has-text-align-{align}")
    if color: a["textColor"] = color; cls += [f"has-{color}-color", "has-text-color"]
    if size: a["fontSize"] = size; cls.append(f"has-{size}-font-size")
    at = (" " + j(a)) if a else ""
    c = f' class="{" ".join(cls)}"' if cls else ""
    return f'<!-- wp:paragraph{at} -->\n<p{c}>{T(text)}</p>\n<!-- /wp:paragraph -->'

def buttons(items, justify=None):
    a = {"layout": {"type": "flex"}}
    if justify: a["layout"]["justifyContent"] = justify
    out = []
    for label, style in items:
        ba = {}; cls = "wp-block-button"
        if style: ba["className"] = f"is-style-{style}"; cls += f" is-style-{style}"
        at = (" " + j(ba)) if ba else ""
        out.append(f'<!-- wp:button{at} -->\n<div class="{cls}"><a class="wp-block-button__link wp-element-button" href="#">{T(label)}</a></div>\n<!-- /wp:button -->')
    return f'<!-- wp:buttons {j(a)} -->\n<div class="wp-block-buttons">' + "\n\n".join(out) + '</div>\n<!-- /wp:buttons -->'

def image(file, alt, ratio=None, radius="md"):
    a = {"sizeSlug": "large", "linkDestination": "none"}
    style = {}
    img_style = []
    if ratio: style["dimensions"] = {"aspectRatio": ratio}; a["aspectRatio"] = ratio; a["scale"] = "cover"; img_style.append(f"aspect-ratio:{ratio}"); img_style.append("object-fit:cover")
    if radius:
        style["border"] = {"radius": f"var:preset|border-radius|{radius}"}
        img_style.insert(0, f"border-radius:var(--wp--preset--border-radius--{radius})")
    a.pop("aspectRatio", None) if not ratio else None
    if style.get("border"): a["style"] = {"border": style["border"]}
    cls = "wp-block-image size-large" + (" has-custom-border" if radius else "")
    st = f' style="{";".join(img_style)}"' if img_style else ""
    rc = ' class="has-border-radius"' if False else ""
    return f'<!-- wp:image {j(a)} -->\n<figure class="{cls}"><img src="{IMG(file)}" alt="{T(alt)}"{st}/></figure>\n<!-- /wp:image -->'

def group(inner, gap=None, layout=None, cls_extra=None):
    a = {}
    if gap: a["style"] = {"spacing": {"blockGap": f"var:preset|spacing|{gap}"}}
    a["layout"] = layout or {"type": "default"}
    return f'<!-- wp:group {j(a)} -->\n<div class="wp-block-group">{inner}</div>\n<!-- /wp:group -->'

def columns(cols, valign=None, gap="large", align="wide"):
    a = {"align": align}
    if valign: a["verticalAlignment"] = valign
    a["style"] = {"spacing": {"blockGap": {"top": f"var:preset|spacing|{gap}", "left": f"var:preset|spacing|{gap}"}}}
    cls = f"wp-block-columns align{align}" + (f" are-vertically-aligned-{valign}" if valign else "")
    out = []
    for width, inner in cols:
        ca = {}
        ccls = "wp-block-column" + (f" is-vertically-aligned-{valign}" if valign else "")
        if valign: ca["verticalAlignment"] = valign
        st = ""
        if width: ca["width"] = width; st = f' style="flex-basis:{width}"'
        at = (" " + j(ca)) if ca else ""
        out.append(f'<!-- wp:column{at} -->\n<div class="{ccls}"{st}>{inner}</div>\n<!-- /wp:column -->')
    return f'<!-- wp:columns {j(a)} -->\n<div class="{cls}">' + "\n\n".join(out) + '</div>\n<!-- /wp:columns -->'

BODIES = {}
def write(slug, title, desc, cats, kw, inner, block_types=None, extra_head=""):
    head = f"""<?php
/**
 * Title: {title}
 * Slug: anypress/{slug}
 * Description: {desc}
 * Categories: {cats}
 * Keywords: {kw}
 * Viewport Width: 1400
"""
    if block_types: head += f" * Block Types: {block_types}\n"
    head += extra_head + " */\n?>\n"
    BODIES[slug] = inner
    open(os.path.join(OUT, slug + ".php"), "w").write(head + inner + "\n")

# 1. Split hero
write("hero-split", "Hero: words and photo side by side",
 "Opening section with a headline that says what the business does, one short sentence, a main button and a photo beside it. Use as the first section of a home page when the owner has a strong photo.",
 "anypress-heroes, banner", "hero, header, intro, headline, photo, call to action",
 section("Hero", None, columns([
   ("55%", group(heading("Fresh sourdough, baked before sunrise", 1, "xxx-large") + "\n\n" +
     para("A small neighbourhood bakery making bread, pastries and celebration cakes by hand every morning.", "medium", "secondary") + "\n\n" +
     buttons([("Order for pickup", None), ("See the menu", "outline")]), "medium")),
   (None, image("placeholder-tall.svg", "Loaves of bread cooling on a wooden rack", "4/5"))], "center"), "x-large", "xx-large", "80rem"))

# 2. Statement hero
write("hero-statement", "Hero: big statement on brand colour",
 "Opening section without a photo: one large headline on the brand colour, a sentence and a button. Use when the business has no good photo yet, or when the words are the strongest thing.",
 "anypress-heroes, banner", "hero, statement, headline, brand colour, no image",
 section("Hero", "section-brand", group(
   heading("Roof leaking? We can be there today.", 1, "xxx-large") + "\n\n" +
   para("Family-run roofers covering the whole county for 25 years. Licensed, insured and on call seven days a week.", "medium") + "\n\n" +
   buttons([("Call 555 0142", None), ("Get a free quote", "outline")]), "medium"), "xx-large", "xx-large", "60rem"))

# 3. Services list
def svc(name, text, price):
    return columns([("70%", heading(name, 3, "medium") + "\n\n" + para(text, None, "secondary")), (None, para(price, "medium", None, "right"))], "top", "medium", "wide")
sep = '<!-- wp:separator {"className":"is-style-wide"} -->\n<hr class="wp-block-separator has-alpha-channel-opacity is-style-wide"/>\n<!-- /wp:separator -->'
write("services-list", "Services with prices, as a list",
 "A heading and services in rows, each with a name, one line about it and a price on the right, separated by thin lines. Use for salons, trades, clinics and anyone with a price list; easier to scan than cards.",
 "services, anypress-details", "services, prices, price list, menu, treatments",
 section("Services", None, heading("What we do", 2, None, None) + "\n\n" + para("Prices include everything. No call-out fee within the county.", None, "secondary") + "\n\n" +
   "\n\n".join([sep, svc("Leak repair", "Find and fix the leak, same day where we can.", "From $180"), sep, svc("Gutter clearing and repair", "Cleared, flushed and checked, with photos before and after.", "From $120"), sep, svc("New roof", "Full replacement with a 15-year workmanship warranty.", "Free quote"), sep]), "xx-large", "xx-large", "60rem"))

# 4. CTA band
write("call-to-action-dark", "Call to action on a dark band",
 "A short closing section on the dark section style with one sentence and one button. Use once, near the end of a page, to repeat the main action.",
 "call-to-action", "call to action, cta, closing, contact, book, buy",
 section("Call to action", "section-dark", group(heading("Ready when you are", 2, "xx-large", "center") + "\n\n" + para("Tell us what you need and we will reply within one working day.", "medium", None, "center") + "\n\n" + buttons([("Get in touch", None)], "center"), "medium"), "xx-large", "xx-large", "44rem"))

# 5. Contact details
def detail(label, lines):
    return group(heading(label, 3, "base") + "\n\n" + "\n\n".join(para(l, None, "secondary") for l in lines), "small")
write("contact-details", "Contact details: hours, address and phone",
 "Three columns with opening hours, the address and ways to get in touch, on the tint section style. Use on contact pages and near the bottom of home pages. Replace every detail with the owner's real ones.",
 "contact, anypress-details", "contact, opening hours, address, phone, email, location",
 section("Contact details", "section-tint", heading("Visit or get in touch", 2) + "\n\n" + columns([
   (None, detail("Opening hours", ["Monday to Friday, 7am to 4pm", "Saturday, 8am to 2pm", "Closed Sunday"])),
   (None, detail("Address", ["14 Market Street", "Springfield"])),
   (None, detail("Contact", ["555 0142", "hello@example.com"]))], None, "large"), "x-large", "x-large", "80rem"))

# 6. Single testimonial
def quote(text, cite):
    return f'<!-- wp:quote {{"className":"is-style-plain"}} -->\n<blockquote class="wp-block-quote is-style-plain">' + para(text, "large") + f'<cite>{T(cite)}</cite></blockquote>\n<!-- /wp:quote -->'
write("testimonial-single", "One customer review, large",
 "A single customer review shown large with the customer's name and town. Use one real review instead of a slider of many; leave the section out if the owner has no reviews yet.",
 "testimonials, anypress-proof", "testimonial, review, quote, customer, proof",
 section("Review", "section-brand-soft", quote("They found a leak two other roofers missed, fixed it the same afternoon and sent photos of every step.", "Dana R., Springfield"), "xx-large", "xx-large", "50rem"))

# 7. FAQ
def det(q, a):
    return f'<!-- wp:details -->\n<details class="wp-block-details"><summary>{T(q)}</summary>' + para(a) + '</details>\n<!-- /wp:details -->'
write("faq", "Questions and answers",
 "A heading and questions that open to show their answers. Use for the questions customers really ask (prices, areas served, how booking works). Each answer stays short.",
 "text, anypress-details", "faq, questions, answers, help",
 section("Questions", None, heading("Questions people ask", 2) + "\n\n" + "\n\n".join([
   det("Do you charge for a quote?", "No. Quotes are free and come with photos of what we found."),
   det("Which areas do you cover?", "Springfield and every town within 30 miles."),
   det("Are you insured?", "Yes, fully licensed and insured. We send certificates on request.")]), "xx-large", "xx-large", "44rem"))
print("ok")

# ---------- batch 2 ----------
def ul(items, cls=None):
    a = {}
    c = "wp-block-list"
    if cls: a["className"] = cls; c += " " + cls
    at = (" " + j(a)) if a else ""
    lis = "\n\n".join(f'<!-- wp:list-item -->\n<li>{T(i)}</li>\n<!-- /wp:list-item -->' for i in items)
    return f'<!-- wp:list{at} -->\n<ul class="{c}">{lis}</ul>\n<!-- /wp:list -->'

# 8. Cover hero
cover_inner = group(heading("Classes for every body, in the middle of town", 1, "xxx-large") + "\n\n" + para("Yoga, pilates and strength, seven days a week. Your first class is free.", "medium") + "\n\n" + buttons([("Book a class", None)]), "medium", {"type": "constrained", "contentSize": "44rem", "justifyContent": "left"})
# Text colour "base" over a "main" overlay: they swap together in dark palettes, so the words stay readable.
cover_inner = cover_inner.replace('<!-- wp:group {', '<!-- wp:group {"textColor":"base",', 1).replace('<div class="wp-block-group">', '<div class="wp-block-group has-base-color has-text-color">', 1)
cover = ('<!-- wp:cover {"url":"' + IMG("placeholder-wide.svg") + '","dimRatio":60,"overlayColor":"main","isUserOverlayColor":true,"minHeight":80,"minHeightUnit":"vh","contentPosition":"bottom left","align":"full","metadata":{"name":"Hero"},"style":{"spacing":{"padding":{"top":"var:preset|spacing|xx-large","bottom":"var:preset|spacing|xx-large","left":"var:preset|spacing|medium","right":"var:preset|spacing|medium"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained","contentSize":"80rem"}} -->\n'
  '<div class="wp-block-cover alignfull has-custom-content-position is-position-bottom-left" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--xx-large);padding-right:var(--wp--preset--spacing--medium);padding-bottom:var(--wp--preset--spacing--xx-large);padding-left:var(--wp--preset--spacing--medium);min-height:80vh"><img class="wp-block-cover__image-background" alt="" src="' + IMG("placeholder-wide.svg") + '" data-object-fit="cover"/><span aria-hidden="true" class="wp-block-cover__background has-main-background-color has-background-dim-60 has-background-dim"></span><div class="wp-block-cover__inner-container">'
  + cover_inner + '</div></div>\n<!-- /wp:cover -->')
write("hero-cover", "Hero: full-width photo with words over it",
 "Opening section with a full-width photo darkened by the text colour, a headline, one sentence and one button in the lower left. Use when the owner has a wide, atmospheric photo (a salon, a restaurant room, a finished job).",
 "anypress-heroes, banner", "hero, cover, full width, photo, background image", cover)

# 9. About split
write("about-story", "About: photo and story side by side",
 "A photo beside a short story of the business: who runs it, since when and what they care about. Use on About pages or below the hero on a home page. Keep it to two short paragraphs in the owner's own words.",
 "about", "about, story, owner, history, who we are",
 section("About", None, columns([
   ("45%", image("placeholder-square.svg", "The owner standing outside the shop", "1", "md")),
   (None, group(heading("Three generations on the same street", 2) + "\n\n" + para("Maria opened the bakery in 1989 with one oven and her grandmother's recipes. Today her son Luca runs the early shift, and the rye is still made the same way.") + "\n\n" + para("Everything is baked on site, every morning, from flour milled less than fifty miles away.", None, "secondary"), "medium"))], "center", "x-large"), "xx-large", "xx-large", "80rem"))

# 10. Steps
def step(n, title, text):
    return group(para(n, "xx-large", "primary") + "\n\n" + heading(title, 3, "medium") + "\n\n" + para(text, None, "secondary"), "small")
write("steps", "How it works, in three steps",
 "Three numbered steps that explain how working with the business goes, from first contact to the finished job. Use only for a real sequence (booking, quoting, ordering); the numbers mean order.",
 "text, anypress-details", "how it works, steps, process, booking, ordering",
 section("How it works", "section-tint", heading("How it works", 2) + "\n\n" + columns([
   (None, step("1", "Tell us what you need", "Call, or send a few photos through the form.")),
   (None, step("2", "Get a fixed price", "We visit within two days and quote in writing.")),
   (None, step("3", "We do the work", "On the agreed day, cleaned up and checked before we leave."))], None, "large"), "xx-large", "xx-large", "80rem"))

# 11. Pricing plans
def plan(name, price, per, items, btn, highlight=False):
    inner = heading(name, 3, "medium") + "\n\n" + para(price, "xx-large") + "\n\n" + para(per, "small", None if highlight else "secondary") + "\n\n" + ul(items) + "\n\n" + buttons([(btn, None if highlight else "outline")])
    style = "section-brand" if highlight else "section-card"
    a = {"className": f"is-style-{style}", "style": {"spacing": {"blockGap": "var:preset|spacing|small", "padding": {"top": "var:preset|spacing|medium", "bottom": "var:preset|spacing|medium", "left": "var:preset|spacing|medium", "right": "var:preset|spacing|medium"}}, "border": {"radius": "var:preset|border-radius|md"}}, "layout": {"type": "default"}}
    css = "border-radius:var(--wp--preset--border-radius--md);padding-top:var(--wp--preset--spacing--medium);padding-right:var(--wp--preset--spacing--medium);padding-bottom:var(--wp--preset--spacing--medium);padding-left:var(--wp--preset--spacing--medium)"
    return f'<!-- wp:group {j(a)} -->\n<div class="wp-block-group is-style-{style}" style="{css}">{inner}</div>\n<!-- /wp:group -->'
write("pricing-plans", "Prices: three plans side by side",
 "Three plans or packages in columns with name, price, what is included and a button; the middle one stands out on the brand colour. Use for memberships, packages or service tiers with fixed prices.",
 "call-to-action, services", "pricing, plans, packages, membership, prices",
 section("Prices", None, group(heading("Simple prices", 2, None, "center") + "\n\n" + para("No joining fee. Cancel any time.", None, "secondary", "center"), "small") + "\n\n" + columns([
   (None, plan("Drop in", "$18", "per class", ["Any class, any day", "Mat and towel included"], "Book a class")),
   (None, plan("Monthly", "$89", "per month", ["Unlimited classes", "One guest pass a month", "Freeze up to 4 weeks"], "Join monthly", True)),
   (None, plan("Ten classes", "$150", "use within 6 months", ["Share with a friend", "Mat and towel included"], "Buy ten classes"))], None, "medium"), "xx-large", "xx-large", "80rem"))

# 12. Team
def person(name, role, alt):
    return group(image("placeholder-square.svg", alt, "1", "md") + "\n\n" + heading(name, 3, "medium") + "\n\n" + para(role, None, "secondary"), "small")
write("team", "Team: photos, names and roles",
 "The people behind the business in a row, each with a photo, name and role. Use on About pages or for clinics, salons and agencies where customers choose who they see.",
 "team, about", "team, staff, people, who we are",
 section("Team", None, heading("Meet the team", 2) + "\n\n" + columns([
   (None, person("Ana Ortiz", "Founder, yoga teacher", "Ana Ortiz in the main studio")),
   (None, person("Sam Lee", "Pilates", "Sam Lee leading a mat class")),
   (None, person("Priya Nair", "Strength and conditioning", "Priya Nair coaching a strength class"))], None, "medium"), "xx-large", "xx-large", "80rem"))

# 13. Gallery (as grid of images in a group grid layout)
grid_imgs = "\n\n".join(image("placeholder-square.svg", f"Finished work, photo {i}", "1", "sm") for i in range(1, 7))
write("gallery-grid", "Gallery: grid of photos",
 "A heading and six square photos in a grid that drops to two columns on phones. Use to show finished work, dishes, rooms or products; replace every photo with the owner's own.",
 "gallery, media", "gallery, photos, portfolio, our work, images",
 section("Gallery", None, heading("Recent work", 2) + "\n\n" + group(grid_imgs, "small", {"type": "grid", "columnCount": 3, "minimumColumnWidth": "10rem"}), "xx-large", "xx-large", "80rem"))

# 14. Credentials
def fact(title, text):
    return group(heading(title, 3, "medium") + "\n\n" + para(text, "small", "secondary"), "small")
write("credentials", "Proof: credentials in a row",
 "Three short facts that build trust, such as licences, years in business and guarantees. Use under a hero or near a price list. Only state facts the owner has confirmed.",
 "anypress-proof", "credentials, trust, licensed, insured, guarantee, proof",
 section("Credentials", None, columns([
   (None, fact("Licensed and insured", "State licence 48213. Certificates on request.")),
   (None, fact("Trading since 2001", "Two generations of the same family.")),
   (None, fact("15-year warranty", "On every new roof, in writing."))], None, "large"), "large", "large", "80rem"))

# 15. Latest posts
q = ('<!-- wp:query {"queryId":1,"query":{"perPage":3,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false},"align":"wide","layout":{"type":"default"}} -->\n<div class="wp-block-query alignwide"><!-- wp:post-template {"layout":{"type":"grid","columnCount":3}} -->\n'
     '<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|small"}},"layout":{"type":"default"}} -->\n<div class="wp-block-group"><!-- wp:post-featured-image {"isLink":true,"aspectRatio":"3/2"} /-->\n\n<!-- wp:post-title {"level":3,"isLink":true,"fontSize":"medium"} /-->\n\n<!-- wp:post-date {"textColor":"secondary","fontSize":"small"} /--></div>\n<!-- /wp:group -->\n'
     '<!-- /wp:post-template -->\n\n<!-- wp:query-no-results -->\n' + para("News and updates will appear here.", None, "secondary") + '\n<!-- /wp:query-no-results --></div>\n<!-- /wp:query -->')
write("latest-posts", "News: latest three posts",
 "A heading and the three newest blog posts with image, title and date. Use on home pages of businesses that post news, offers or events.",
 "posts", "blog, news, posts, updates, articles", section("Latest news", None, heading("Latest news", 2) + "\n\n" + q, "xx-large", "xx-large", "80rem"))

# 16. Booking band
write("call-to-action-split", "Call to action: two choices on second brand colour",
 "A band in the second brand colour with a short headline on the left and two buttons on the right. Use mid-page to offer the two main ways to act, such as booking online or calling.",
 "call-to-action", "call to action, cta, book, call, band",
 section("Call to action", "section-second-brand", columns([
   ("60%", heading("Need a table tonight?", 2, "x-large") + "\n\n" + para("Book online in under a minute, or call and we will find you a spot.")),
   (None, buttons([("Book a table", None), ("Call 555 0198", "outline")], "right"))], "center", "medium"), "x-large", "x-large", "80rem"))

# 17. Statement
write("text-statement", "Statement: one big sentence",
 "One large sentence on the tint colour that says what the business stands for. Use between busier sections to give the page a pause; keep it under thirty words.",
 "text, about", "statement, mission, quote, values, intro",
 section("Statement", "section-tint", para("We fix what we can, replace only what we must, and tell you which is which before we start.", "x-large"), "xx-large", "xx-large", "56rem"))

# 18. Three reviews
def review(text, who):
    a = {"className": "is-style-section-card", "style": {"spacing": {"blockGap": "var:preset|spacing|small", "padding": {"top": "var:preset|spacing|medium", "bottom": "var:preset|spacing|medium", "left": "var:preset|spacing|medium", "right": "var:preset|spacing|medium"}}, "border": {"radius": "var:preset|border-radius|md"}}, "layout": {"type": "default"}}
    css = "border-radius:var(--wp--preset--border-radius--md);padding-top:var(--wp--preset--spacing--medium);padding-right:var(--wp--preset--spacing--medium);padding-bottom:var(--wp--preset--spacing--medium);padding-left:var(--wp--preset--spacing--medium)"
    return f'<!-- wp:group {j(a)} -->\n<div class="wp-block-group is-style-section-card" style="{css}">' + para(text) + "\n\n" + para(who, "small", "secondary") + '</div>\n<!-- /wp:group -->'
write("reviews-three", "Reviews: three short ones in cards",
 "Three short customer reviews side by side in cards, each with the customer's name and town. Use when the owner has several real reviews; no sliders, and never invent reviews.",
 "testimonials, anypress-proof", "reviews, testimonials, customers, quotes, proof",
 section("Reviews", "section-tint", heading("What customers say", 2) + "\n\n" + columns([
   (None, review("Booked on Monday, fixed on Tuesday, and the price did not change.", "Jo M., Riverside")),
   (None, review("Friendly, tidy and they explained every step in plain words.", "Carlos T., Springfield")),
   (None, review("They found the real cause of a leak two others missed.", "Dana R., Oak Hill"))], None, "medium"), "xx-large", "xx-large", "80rem"))

# 19. Menu (two-column price list)
def dish(name, text, price):
    return columns([("75%", heading(name, 3, "base") + "\n\n" + para(text, "small", "secondary")), (None, para(price, None, None, "right"))], "top", "small", None) if False else group(group(heading(name, 3, "base") + "\n\n" + para(price), None, {"type": "flex", "flexWrap": "nowrap", "justifyContent": "space-between"}) + "\n\n" + para(text, "small", "secondary"), "small")
write("menu", "Menu: dishes and prices in two columns",
 "A menu or price list in two columns, each item with a name, price and one line of description. Use for restaurants, cafés, bakeries and salons with many items; split long menus into one section per course.",
 "services, anypress-details", "menu, food, dishes, price list, drinks",
 section("Menu", None, heading("Breakfast", 2) + "\n\n" + columns([
   (None, group("\n\n".join([dish("Sourdough toast", "With cultured butter and house jam.", "$6"), dish("Eggs your way", "Two eggs on rye, with greens.", "$11")]), "medium")),
   (None, group("\n\n".join([dish("Almond croissant", "Baked twice, filled with frangipane.", "$5"), dish("Granola bowl", "Yoghurt, honey and fruit of the season.", "$9")]), "medium"))], None, "x-large"), "xx-large", "xx-large", "60rem"))
print("batch2 ok")

# Starter pages: whole pages made of the sections above, copied in full (the site tools hand out a
# pattern's content as it is, so core/pattern references would not become editable sections).
def ref(slug): return BODIES[slug]
def page(slug, title, desc, kw, parts):
    write(slug, title, desc, "anypress/pages", kw, "\n\n".join(ref(p) for p in parts), "core/post-content", " * Post Types: page\n")
page("home-trades", "Home page: trades and local services",
 "A home page for a trade or local service (roofer, plumber, cleaner, landscaper): what they do and that they come quickly, proof they are licensed, services with prices, how a job goes, reviews, questions and contact details. The phone number is the main action.",
 "home, trades, roofer, plumber, electrician, cleaner, local service, quote",
 ["hero-statement", "credentials", "services-list", "steps", "reviews-three", "faq", "call-to-action-dark", "contact-details"])
page("home-food", "Home page: food and drink",
 "A home page for a bakery, café or restaurant: a photo of the food beside what they make, their story, the menu, photos, booking or ordering, then opening hours and address.",
 "home, restaurant, cafe, bakery, food, menu, opening hours",
 ["hero-split", "about-story", "menu", "gallery-grid", "call-to-action-split", "contact-details"])
page("home-studio", "Home page: classes and memberships",
 "A home page for a studio, gym or school that sells classes or memberships: an atmospheric photo, the prices, the teachers, news, and where to find them.",
 "home, studio, gym, yoga, fitness, classes, membership, school",
 ["hero-cover", "pricing-plans", "team", "testimonial-single", "latest-posts", "contact-details"])
page("page-about", "About page",
 "An About page: the business's story beside a photo, one sentence about how they work, photos of their work and a closing call to action.",
 "about, story, who we are, history",
 ["about-story", "text-statement", "gallery-grid", "call-to-action-dark"])
page("page-contact", "Contact page",
 "A Contact page: opening hours, address and phone, then the questions people ask before getting in touch.",
 "contact, hours, address, phone, location",
 ["contact-details", "faq"])
print("pages ok")
