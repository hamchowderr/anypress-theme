# Nine more kits (0.4.0) and the sections and pages that fill the gaps found in JP Blocks' catalogue.
# Run by kits.py after the first four kits, so every helper above is in scope.
sys.path.insert(0, HERE)
from pal import PALS

def mono(text, color="secondary", size="small"):
    return p(text, size, color, None, "monospace", {"textTransform": "uppercase", "letterSpacing": "0.08em"})
def sep():
    return '<!-- wp:separator {"className":"is-style-wide"} -->\n<hr class="wp-block-separator has-alpha-channel-opacity is-style-wide"/>\n<!-- /wp:separator -->'
def details(summary, body, size=None):
    if size: return f'<!-- wp:details {{"fontSize":"{size}"}} -->\n<details class="wp-block-details has-{size}-font-size"><summary>{T(summary)}</summary>' + p(body) + '</details>\n<!-- /wp:details -->'
    return f'<!-- wp:details -->\n<details class="wp-block-details"><summary>{T(summary)}</summary>' + p(body) + '</details>\n<!-- /wp:details -->'
def captioned(file, alt, ratio, caption, family="monospace"):
    cap = f'<figcaption class="wp-element-caption">{T(caption)}</figcaption>'
    return img(file, alt, ratio).replace("/></figure>", "/>" + cap + "</figure>", 1)
def grid(items, n, minw="16rem", gap="large", style=None, pad=None):
    return grp(N(items), style, pad, gap, {"type": "grid", "columnCount": n, "minimumColumnWidth": minw}, align="wide")
def stackg(items, gap="small"):
    return grp(N(items), gap=gap, layout={"type": "default"})
def row(items, justify="space-between", gap=None, wrap=True, valign=None):
    lay = {"type": "flex", "justifyContent": justify}
    if not wrap: lay["flexWrap"] = "nowrap"
    if valign: lay["verticalAlignment"] = valign
    return grp(N(items), gap=gap, layout=lay)
def query(per, offset, ncols, inner, qid, empty="New posts will appear here.", layout=None):
    q = {"queryId": qid, "query": {"perPage": per, "pages": 0, "offset": offset, "postType": "post", "order": "desc", "orderBy": "date", "inherit": False}, "align": "wide", "layout": {"type": "default"}}
    tl = layout or ({"type": "grid", "columnCount": ncols} if ncols > 1 else {"type": "default"})
    return (f'<!-- wp:query {j(q)} -->\n<div class="wp-block-query alignwide"><!-- wp:post-template {j({"layout": tl})} -->\n' + inner +
            '\n<!-- /wp:post-template -->\n\n<!-- wp:query-no-results -->\n' + p(empty, None, "secondary") + '\n<!-- /wp:query-no-results --></div>\n<!-- /wp:query -->')
def dyn(name, attrs=None):
    return f'<!-- wp:{name} {j(attrs)} /-->' if attrs else f'<!-- wp:{name} /-->'
def social(services, justify=None):
    a = {"layout": {"type": "flex"}}
    if justify: a["layout"]["justifyContent"] = justify
    items = "\n\n".join(dyn("social-link", {"url": "#", "service": s}) for s in services)
    return f'<!-- wp:social-links {j(a)} -->\n<ul class="wp-block-social-links">{items}</ul>\n<!-- /wp:social-links -->'
def base_body(slug):
    return open(os.path.join(OUT, slug + ".php")).read().split("?>\n", 1)[1].strip()

def heading_t(family, weight, ls, lh, transform=None, style=None):
    t = {"fontFamily": f"var:preset|font-family|{family}", "fontWeight": weight, "letterSpacing": ls, "lineHeight": lh}
    if transform: t["textTransform"] = transform
    if style: t["fontStyle"] = style
    return {"heading": {"typography": t}}

# ---------------------------------------------------------------- variations
# Parcel: an online shop. A catalogue page: a narrow serif for names, a plain sans for everything else, clay and cream.
variation("kit-parcel", "Parcel (online shop)", PALS["parcel"], "instrument-sans", "instrument-serif", "400", "-0.01em", "1",
    button("0", "instrument-sans", "600"), blocks=site_title("instrument-serif", "400", None, "-0.01em"))
# Chapter: courses and community. A workbook: ink blue, school yellow, a friendly serif.
variation("kit-chapter", "Chapter (courses and community)", PALS["chapter"], "figtree", "fraunces", "600", "-0.02em", "1.05",
    button("var:preset|border-radius|sm", "figtree", "700"), blocks=site_title("fraunces", "700", None, "-0.02em"))
# Gloss: salon and beauty. A fashion page: high-contrast serif, blush and oxblood, small spaced capitals on buttons.
variation("kit-gloss", "Gloss (salon and beauty)", PALS["gloss"], "jost", "bodoni-moda", "500", "-0.01em", "1.05",
    button("var:preset|border-radius|full", "jost", "500", "uppercase", "var:preset|font-size|small", "0.14em"), blocks=site_title("bodoni-moda", "600"))
# Commons: associations, chambers and churches. A civic notice board: navy and brick, a book serif, a public sans.
variation("kit-commons", "Commons (associations, chambers and churches)", PALS["commons"], "public-sans", "crimson-pro", "600", "-0.005em", "1.1",
    button("var:preset|border-radius|xs", "public-sans", "600"), blocks=site_title("crimson-pro", "700"))
# Rep: gyms and classes. A training poster: heavy italic capitals, black and acid lime.
variation("kit-rep", "Rep (gym and classes)", PALS["rep"], "figtree", "archivo", "900", "-0.01em", "0.92",
    button("0", "archivo", "800", "uppercase", "var:preset|font-size|base", "0.02em"),
    extra_elements=heading_t("archivo", "900", "-0.01em", "0.92", "uppercase", "italic"),
    blocks=site_title("archivo", "900", "uppercase"))
# Frame: creative portfolio. A gallery wall: off-white, black, one cobalt, captions in a typewriter face.
variation("kit-frame", "Frame (creative portfolio)", PALS["frame"], "figtree", "bricolage-grotesque", "700", "-0.035em", "0.95",
    button("0", "figtree", "600"), blocks=site_title("bricolage-grotesque", "700", None, "-0.02em"))
# Keystone: real estate. A brochure: forest green and brass, a sharp display serif.
variation("kit-keystone", "Keystone (real estate)", PALS["keystone"], "manrope", "gloock", "400", "-0.01em", "1.05",
    button("var:preset|border-radius|xs", "manrope", "600"), blocks=site_title("gloock", "400"))
# Launch: startup and software. A changelog: one grotesk at every size, green on paper, labels in mono.
variation("kit-launch", "Launch (startup and software)", PALS["launch"], "schibsted-grotesk", "schibsted-grotesk", "800", "-0.035em", "1",
    button("var:preset|border-radius|sm", "schibsted-grotesk", "600"), blocks=site_title("schibsted-grotesk", "800", None, "-0.03em"))
# Byline: blog and magazine. A newspaper: one reading serif, masthead red, ruled lines.
variation("kit-byline", "Byline (blog and magazine)", PALS["byline"], "literata", "literata", "800", "-0.02em", "1.05",
    button("0", "system-sans", "700", "uppercase", "var:preset|font-size|small", "0.06em"), blocks=site_title("literata", "800", None, "-0.02em"))

# ---------------------------------------------------------------- Parcel (online shop)
K = "anypress/kit-shop"
kit("parcel-hero", K, "Parcel hero: product photo beside the collection",
 "Opening section for an online shop: a large product photo edge to edge beside a panel with the collection name, one sentence and two buttons. Part of the Parcel kit (online shop); use the owner's own product photo.",
 "hero, shop, store, products, collection, ecommerce, parcel",
 sec("Hero", cols([
   col(fill("placeholder-tall.svg", 40), "55%"),
   col(N([mono("New this autumn"), h("Stoneware, thrown by hand in small batches", 1, "xxx-large"),
          p("Mugs, bowls and vases made in our Asheville studio and fired twice. Every piece is a little different.", "medium"),
          btns([("Shop the collection", None, "#shop"), ("How it's made", "outline", "#story")])]), None, "section-tint", ("xx-large", "xx-large", "x-large", "x-large"), "center")], "0", "full", None),
   None, (None, None, None, None), layout={"type": "default"}))

kit("parcel-promise", K, "Parcel promise: shipping, returns and where it's made",
 "A thin band of three promises a shopper checks before buying: shipping, returns and where things are made. Part of the Parcel kit; put the shop's real policies here.",
 "shipping, returns, guarantee, trust, policies, parcel",
 sec("Promise", cols([col(stackg([h(a, 3, "medium"), p(b)])) for a, b in [
   ("Free shipping over $60", "Packed in paper and card, no plastic."), ("30 days to change your mind", "Send it back unused for a full refund."), ("Made in Asheville", "Every piece is thrown and glazed in our studio.")]],
   "large", "wide", None), "section-second-brand", ("large", "large", None, None)))

def tile(file, alt, name, count):
    return stackg([img(file, alt, "4/5"), row([h(name, 3, "large"), p(count, None, "secondary")], valign="bottom")])
kit("parcel-categories", K, "Parcel categories: three collections with photos",
 "Three collections as tall photos with the name and number of pieces under each, and a link to everything. Part of the Parcel kit; link each to its collection page.",
 "categories, collections, shop, departments, parcel",
 sec("Categories", N([row([h("Shop by collection", 2, "xx-large"), p('<a href="#shop">' + T("See everything") + "</a>", "medium", raw=True)], valign="bottom"),
   grid([tile("placeholder-tall.svg", "Three clay cups on a shelf", "Cups and mugs", "14 pieces"),
         tile("placeholder-tall.svg", "A small vase with a hole through the middle", "Vases", "9 pieces"),
         tile("placeholder-tall.svg", "A glazed blue bottle on a wooden table", "Bottles", "6 pieces")], 3, "16rem", "medium")])))

def product(file, alt, name, price, note=None):
    meta = [h(name, 3, "medium"), p(price)]
    if note: meta.append(p(note, "small", "secondary"))
    return stackg([img(file, alt, "1"), stackg(meta, "x-small")])
kit("parcel-products", K, "Parcel products: four best sellers",
 "Four products in a row with a square photo, name and price. Part of the Parcel kit; when the shop's products are set up, the shop's own product blocks can replace these so prices and stock stay current.",
 "products, best sellers, featured products, shop, grid, parcel",
 sec("Best sellers", N([h("Best sellers", 2, "xx-large"), grid([
   product("placeholder-square.svg", "A cup and saucer with a crackle glaze", "Crackle cup and saucer", "$38"),
   product("placeholder-square.svg", "Three terracotta tumblers", "Ridged tumbler", "$24", "Set of three, $64"),
   product("placeholder-square.svg", "A round stoneware vase with a hole in the middle", "Moon vase", "$56"),
   product("placeholder-square.svg", "A blue glazed bottle with a brass stopper", "Indigo bottle", "$72", "Only two left")], 4, "13rem", "medium")]), "section-tint"))

kit("parcel-story", K, "Parcel story: the maker in their own words",
 "The maker's story in large italic type beside a photo of the workshop, with their name. Part of the Parcel kit; the owner's own words, two or three sentences.",
 "about, story, maker, handmade, studio, parcel",
 sec("Story", cols([
   col(N([p("I started with one wheel in a garage. Ten years on, every mug still goes through my hands at least four times before it reaches you.", "xx-large", None, None, "instrument-serif", {"fontStyle": "italic", "lineHeight": "1.15"}),
          p("June Park, potter and owner", "medium", "secondary"), btns([("Read our story", "outline", "#story")])]), "55%", valign="center"),
   col(img("placeholder-tall.svg", "The potter's wheel and shelves of drying pots", "4/5"))], "xx-large", "wide", "center")))

kit_page("kit-shop", "Home page: Parcel kit, online shop",
 "A complete home page for an online shop or maker in the Parcel kit: a product photo beside the collection, three promises, collections, best sellers, the maker's story and an email signup. Apply the Parcel style for the look it was designed with.",
 "home, shop, store, ecommerce, products, maker, handmade, kit, parcel",
 ["parcel-hero", "parcel-promise", "parcel-categories", "parcel-products", "parcel-story", "newsletter-signup"])

# ---------------------------------------------------------------- Chapter (courses and community)
K = "anypress/kit-courses"
kit("chapter-hero", K, "Chapter hero: the course and what's inside",
 "Opening section for an online course, membership or coaching programme on the second brand colour: what people will learn, the next start date and a card listing what is included. Part of the Chapter kit (courses and community).",
 "hero, course, online course, membership, coaching, community, chapter",
 sec("Hero", cols([
   col(N([mono("Next cohort starts 3 March", "primary-alt-accent"), h("Learn to draw people in 30 days", 1, "poster", None, None, {"lineHeight": "0.95"}),
          p("Fifteen minutes a day, one short lesson at a time, with feedback from a working illustrator.", "large"),
          btns([("Join the course", None, "#pricing"), ("Watch lesson one free", "outline", "#curriculum")])]), "60%", valign="center"),
   col(card(N([h("What's inside", 2, "large"), lst(["30 video lessons, 10 to 15 minutes each", "4 live drawing sessions", "A private group for feedback", "Keep everything for life"])]), "section-card"), None, None, None, "center")],
   "xx-large", "wide", "center"), "section-second-brand", ("xx-large", "xx-large", None, None)))

def outcome(n, title, text):
    return stackg([p(n, "xxx-large", "primary", None, "fraunces", {"lineHeight": "1", "fontWeight": "300"}), h(title, 3, "large"), p(text, None, "secondary")])
kit("chapter-outcomes", K, "Chapter outcomes: what people can do at the end",
 "Three things a student can do by the end, each with a large number, a heading and a sentence. Part of the Chapter kit; promise only what the course really teaches.",
 "outcomes, benefits, results, learn, chapter",
 sec("Outcomes", N([h("By the end you will", 2, "xx-large"), grid([
   outcome("01", "Draw a figure in two minutes", "Gesture first, details last. You will fill a sketchbook with quick poses."),
   outcome("02", "Get faces to look like people", "Proportions you can check with a pencil, not guesswork."),
   outcome("03", "Draw from life without freezing", "Cafés, trains and parks, with a routine that keeps you going.")], 3, "15rem", "x-large")])))

def module(n, title, lessons, text):
    return details(f"Week {n}: {title} ({lessons} lessons)", text, "medium")
kit("chapter-curriculum", K, "Chapter curriculum: the weeks, opening one at a time",
 "The course outline as a list of weeks that open to show what each covers, on the tint colour. Part of the Chapter kit; one line per week, and say how many lessons each has.",
 "curriculum, syllabus, modules, lessons, outline, course content, chapter",
 sec("Curriculum", cols([
   col(N([h("What you'll learn, week by week", 2, "xx-large"), p("Every lesson is a short video and one drawing exercise. Watch on any device; the exercises need paper and a pencil.", "medium", "secondary")]), "40%"),
   col(stackg([module(1, "Gesture and movement", 8, "Quick poses, lines of action and drawing the whole figure before any detail."),
               module(2, "Proportion and structure", 7, "Measuring with a pencil, simple boxes for the body, and the proportions that matter."),
               module(3, "Faces and hands", 8, "Placing features, expressions, and hands that don't look like bunches of bananas."),
               module(4, "Drawing from life", 7, "Working in public, quick studies, and building a daily habit.")], "small"))], "xx-large", "wide", None), "section-tint"))

kit("chapter-teacher", K, "Chapter teacher: who teaches the course",
 "The teacher beside a photo: who they are, what they have done and a few numbers about past students. Part of the Chapter kit; use real numbers only.",
 "teacher, instructor, coach, about, bio, chapter",
 sec("Teacher", cols([
   col(img("placeholder-tall.svg", "The teacher at a desk with a sketchbook", "4/5"), "40%"),
   col(N([mono("Your teacher"), h("Mara Lind has drawn for magazines and picture books for twenty years", 2, "xx-large"),
          p("She has taught life drawing at the city college since 2015. This course is that class, recorded properly and with the boring bits taken out.", "medium"),
          grid([stackg([p("4,800", "xx-large", None, None, "fraunces", {"lineHeight": "1"}), p("students since 2021", None, "secondary")], "x-small"),
                stackg([p("4.9 / 5", "xx-large", None, None, "fraunces", {"lineHeight": "1"}), p("average review", None, "secondary")], "x-small")], 2, "10rem", "large")]), None, None, None, "center")], "xx-large", "wide", "center")))

kit("chapter-community", K, "Chapter community: you won't do it alone",
 "What the community gives students on the dark section style: three short points and a quotation from a member. Part of the Chapter kit; for courses with a group, forum or live calls.",
 "community, group, membership, forum, live calls, chapter",
 sec("Community", cols([
   col(N([h("A course you don't do alone", 2, "xx-large"), stackg([stackg([h(a, 3, "medium"), p(b, None, "main-accent")], "x-small") for a, b in [
     ("Weekly feedback", "Post a drawing, get notes from Mara or a teaching assistant within two days."),
     ("Live sessions", "Draw along with a model once a week. Recordings for every time zone."),
     ("A group that keeps going", "Most students stay in the group long after the course ends.")]], "large")]), "50%"),
   col(quote("I had started and quit drawing three times. The group is why I finished this time.", "Tom B., student since 2023", "x-large", "fraunces"), None, None, None, "center")], "xx-large", "wide", None), "section-dark"))

def plan(name, price, per, items, label, style, featured=False):
    inner = [h(name, 3, "large"), row([p(price, "xxx-large", None, None, "fraunces", {"lineHeight": "1"}), p(per, None, None)], "left", "x-small", valign="bottom"), lst(items), btns([(label, None if featured else "outline", "/shop/")])]
    return card(N(inner), style)
kit("chapter-pricing", K, "Chapter pricing: course alone or with the community",
 "Two ways to join side by side: the course on its own for a single price, and the course with the community by the month. Part of the Chapter kit; match the prices to the shop's products.",
 "pricing, plans, join, buy, membership, chapter",
 sec("Pricing", N([h("Join the course", 2, "xx-large", "center"), p("Thirty days to ask for your money back, no questions.", "medium", "secondary", "center"), grid([
   plan("The course", "$149", "once", ["All 30 lessons", "Keep them for life", "Certificate at the end"], "Buy the course", "section-card"),
   plan("Course and community", "$29", "a month", ["All 30 lessons", "Weekly feedback on your drawings", "Live sessions and recordings", "Cancel any time"], "Join with the community", "section-brand-soft", True)], 2, "18rem", "medium")]), content="56rem"))

kit_page("kit-courses", "Home page: Chapter kit, courses and community",
 "A complete home page for an online course, coaching programme or membership in the Chapter kit: the course and what's inside, outcomes, the weeks of the curriculum, the teacher, the community and two ways to join. Apply the Chapter style for the look it was designed with.",
 "home, course, online course, coaching, membership, community, teacher, kit, chapter",
 ["chapter-hero", "chapter-outcomes", "chapter-curriculum", "chapter-teacher", "chapter-community", "chapter-pricing"])

# ---------------------------------------------------------------- Gloss (salon and beauty)
K = "anypress/kit-salon"
kit("gloss-hero", K, "Gloss hero: a big name beside a tall photo",
 "Opening section for a hair salon, nail bar, barber or beauty studio: a large serif headline, one sentence, the booking button and a tall photo. Part of the Gloss kit (salon and beauty).",
 "hero, salon, hair, beauty, nails, barber, booking, gloss",
 sec("Hero", cols([
   col(N([mono("Hair, colour and brows on Elm Street", "secondary"), h("Colour that grows out beautifully", 1, "xxx-large", None, None, {"lineHeight": "1"}),
          p("Lived-in colour, precise cuts and an hour that is just for you.", "large"),
          btns([("Book online", None, "#book"), ("See prices", "outline", "#prices")])]), "55%", valign="center"),
   col(img("placeholder-tall.svg", "Make-up brushes in a pot on a pink table", "3/4"))], "xx-large", "wide", "center"), "section-brand-soft", ("x-large", "x-large", None, None)))

def price_line(name, price, note=None):
    out = [grp(N([h(name, 3, "medium", None, "jost", {"fontWeight": "400"}), p(price, "medium")]), "menu-leader", layout={"type": "flex", "flexWrap": "nowrap", "justifyContent": "space-between", "verticalAlignment": "bottom"})]
    if note: out.append(p(note, "small", "secondary"))
    return stackg(out, "x-small")
def price_group(title, items):
    return stackg([h(title, 2, "x-large")] + [price_line(*i) for i in items], "medium")
kit("gloss-prices", K, "Gloss prices: services in groups, with dotted lines to the price",
 "The price list in two columns, grouped (hair, colour, brows), each service with a dotted line to its price and a short note where it helps. Part of the Gloss kit; use the salon's real prices.",
 "prices, price list, services, menu, hair, colour, gloss",
 sec("Prices", N([h("Prices", 2, "xxx-large", "center"), p("Prices depend on hair length and the stylist's level. We confirm before we start.", "medium", "secondary", "center"),
   cols([col(stackg([price_group("Cut and style", [("Women's cut and finish", "from $65"), ("Men's cut", "from $38"), ("Blow-dry", "from $40", "Add curls or waves for $10.")]),
                     price_group("Brows and lashes", [("Brow shape and tint", "$32"), ("Lash lift", "$60")])], "x-large")),
         col(stackg([price_group("Colour", [("Root colour", "from $75"), ("Balayage", "from $165", "Includes toner and a cut."), ("Gloss", "$45", "Shine and tone between colours.")]),
                     price_group("Treatments", [("Bond repair", "$30"), ("Scalp treatment", "$35")])], "x-large"))], "xx-large", "wide", None)]), content="64rem"))

def stylist(name, role):
    return stackg([img("placeholder-tall.svg", f"Portrait of {name}", "3/4"), h(name, 3, "large"), p(role, None, "secondary")])
kit("gloss-team", K, "Gloss team: the stylists",
 "The people who do the work, each with a portrait, name and what they love doing. Part of the Gloss kit; clients book a person, so show the real team.",
 "team, stylists, staff, people, barbers, gloss",
 sec("Team", N([h("Who you'll sit with", 2, "xx-large"), grid([
   stylist("Nadia", "Owner and colour director. Balayage and grey blending."), stylist("Ollie", "Senior stylist. Short cuts and curly hair."),
   stylist("Bea", "Brows and lashes. Fixes over-plucked brows.")], 3, "15rem", "large")])))

kit("gloss-gallery", K, "Gloss gallery: four photos of different sizes",
 "Four photos of recent work or the salon at different sizes, edge to edge. Part of the Gloss kit; the salon's own photos, with the client's permission.",
 "gallery, photos, work, portfolio, before and after, gloss",
 sec("Gallery", cols([col(fill("placeholder-tall.svg", 36), "50%"),
   col(grp(N([fill("placeholder-wide.svg", 18), cols([col(fill("placeholder-square.svg", 18)), col(fill("placeholder-square.svg", 18))], "0", None, None, False)]), gap="0", layout={"type": "default"}))], "0", "full", None),
   None, (None, None, None, None), layout={"type": "default"}))

kit("gloss-book", K, "Gloss booking: hours, address and how to book",
 "The closing section on the second brand colour: a big invitation to book, opening hours, the address and the cancellation policy. Part of the Gloss kit.",
 "booking, book now, hours, address, contact, policy, gloss",
 sec("Book", cols([
   col(N([h("Book in two minutes", 2, "xxx-large"), p("Choose your stylist and a time online, or call us.", "large"), btns([("Book online", None, "#book"), ("Call 555 0133", "outline", "tel:5550133", "phone")])]), "55%"),
   col(stackg([stackg([h("Hours", 3, "medium"), p("Tuesday to Friday, 9am to 8pm" + "", None), p("Saturday, 9am to 5pm")], "x-small"),
               stackg([h("Find us", 3, "medium"), p("21 Elm Street, Springfield", bind="address")], "x-small"),
               stackg([h("Changing a booking", 3, "medium"), p("Please give us 24 hours' notice to move or cancel.")], "x-small")], "large"))], "xx-large", "wide", None), "section-second-brand"))

kit_page("kit-salon", "Home page: Gloss kit, salon and beauty",
 "A complete home page for a hair salon, barber, nail bar or beauty studio in the Gloss kit: a big headline beside a photo, the price list, the team, a gallery and how to book. Apply the Gloss style for the look it was designed with.",
 "home, salon, hair, beauty, barber, nails, brows, kit, gloss",
 ["gloss-hero", "gloss-prices", "gloss-team", "gloss-gallery", "gloss-book"])

# ---------------------------------------------------------------- Commons (associations, chambers and churches)
K = "anypress/kit-community"
kit("commons-hero", K, "Commons hero: who you are and how to join",
 "Opening section for a chamber of commerce, association, club or church: a photo of members together, who the group is for and two buttons (join, and the next events). Part of the Commons kit.",
 "hero, chamber of commerce, association, club, church, nonprofit, membership, commons",
 cover(on_photo(grp(N([h("Springfield Chamber of Commerce", 1, "poster", None, None, {"lineHeight": "0.95"}),
   p("Four hundred local businesses that help each other grow. Meet them at our breakfasts, find them in our directory, and add your voice to the town's plans.", "large"),
   btns([("Become a member", None, "#join"), ("See upcoming events", "outline", "#events")])]), gap="medium", layout={"type": "constrained", "contentSize": "52rem", "justifyContent": "left"})),
   "Hero", "placeholder-wide.svg", 60, "85vh", "bottom left", ("xx-large", "x-large", "medium", "medium"), "80rem"))

def event(day, month, title, when, where):
    date = grp(N([p(day, "xx-large", None, "center", "crimson-pro", {"lineHeight": "1", "fontWeight": "700"}), p(month, "small", None, "center", None, {"textTransform": "uppercase", "letterSpacing": "0.08em"})]),
               "section-brand", ("small", "small", "small", "small"), "x-small")
    return cols([col(date, "6rem"), col(stackg([h(title, 3, "large"), p(f"{when} · {where}", None, "secondary"), p('<a href="#">' + T("Details") + "</a>", None, None, None, None, None, True)], "x-small"), None, None, None, "center")],
                "large", None, "center", False)
kit("commons-events", K, "Commons events: what's coming up",
 "The next few events as rows with a date block, the title, time and place, and a link to the details. Part of the Commons kit; keep it to the next four or five and take old ones down.",
 "events, calendar, upcoming, meetings, services, schedule, commons",
 sec("Events", N([row([h("Coming up", 2, "xx-large"), p('<a href="#">' + T("Full calendar") + "</a>", "medium", raw=True)], valign="bottom"),
   stackg([event("14", "Mar", "Business breakfast: hiring your first employee", "7:30am to 9am", "The Grand Hotel"),
           event("21", "Mar", "Main Street clean-up", "10am to 1pm", "Meet at the town hall"),
           event("04", "Apr", "Members' evening and awards", "6pm to 9pm", "Riverside Brewery"),
           event("18", "Apr", "Workshop: getting found on Google", "12pm to 1pm", "Online")], "medium")]), content="64rem"))

def tier(name, price, text, items, style):
    return card(N([h(name, 3, "large"), row([p(price, "xx-large", None, None, "crimson-pro", {"lineHeight": "1", "fontWeight": "700"}), p("a year")], "left", "x-small", valign="bottom"), p(text, None, "secondary"), lst(items)]), style)
kit("commons-join", K, "Commons membership: levels and what each includes",
 "Membership levels side by side with the yearly price, who each is for and what it includes, then one button. Part of the Commons kit; works for dues, giving levels or sponsorships.",
 "membership, join, dues, levels, sponsorship, pricing, commons",
 sec("Join", N([h("Become a member", 2, "xx-large"), p("Membership runs for a year from the day you join.", "medium", "secondary"), grid([
   tier("Individual", "$60", "For sole traders and retired members.", ["Breakfasts at member price", "The monthly newsletter", "A vote at the annual meeting"], "section-card"),
   tier("Small business", "$240", "For businesses with up to 25 staff.", ["Everything in Individual", "A listing in the directory", "Two places at every event"], "section-brand-soft"),
   tier("Corporate", "$900", "For larger employers and sponsors.", ["Everything in Small business", "Your logo on event pages", "A seat on a committee"], "section-card")], 3, "16rem", "medium"),
   btns([("Join online", None, "#join"), ("Ask a question", "outline", "mailto:hello@example.com", "email_link")])]), "section-tint"))

kit("commons-news", K, "Commons news: the latest three posts",
 "The three newest posts with the date and title, under a heading. Part of the Commons kit; posts are written in the site's blog and appear here on their own.",
 "news, announcements, blog, posts, updates, commons",
 sec("News", N([h("News", 2, "xx-large"), query(3, 0, 3, stackg([dyn("post-date", {"textColor": "secondary", "fontSize": "small"}), dyn("post-title", {"level": 3, "isLink": True, "fontSize": "large"}), dyn("post-excerpt", {"excerptLength": 20})]), 11, "News and announcements will appear here.")])))

def person(name, role):
    return stackg([h(name, 3, "medium"), p(role, None, "secondary")], "x-small")
kit("commons-leaders", K, "Commons leaders: the board or staff by name",
 "The people who run the group, by name and role, in a plain grid without photos. Part of the Commons kit; for a board, committee, clergy or staff.",
 "board, leaders, staff, committee, clergy, team, commons",
 sec("Leaders", cols([col(N([h("Who runs the chamber", 2, "xx-large"), p("Board members are elected by members each spring. Anyone can stand.", "medium", "secondary")]), "35%"),
   col(grid([person("Grace Okafor", "Chair, owner of Okafor Bakeries"), person("Dan Whitley", "Vice chair, Whitley & Sons Hardware"), person("Lena Ruiz", "Treasurer, Ruiz Accounting"),
             person("Sam Patel", "Secretary, Riverside Brewery"), person("Ann Kowalski", "Events, The Grand Hotel"), person("Joe Martin", "Executive director")], 3, "12rem", "large"))], "xx-large", "wide", None)))

kit("commons-involved", K, "Commons get involved: give, volunteer, sponsor",
 "The closing section on the second brand colour: three ways to help (give, volunteer, sponsor), each with a sentence and a link. Part of the Commons kit; change the three to what the group really needs.",
 "donate, give, volunteer, sponsor, get involved, support, commons",
 sec("Get involved", N([h("Get involved", 2, "xxx-large"), cols([col(stackg([h(a, 3, "large"), p(b), p(f'<a href="#">{T(c)}</a>', None, None, None, None, None, True)])) for a, b, c in [
   ("Volunteer", "Help at an event, mentor a new business or join a committee.", "See open roles"),
   ("Sponsor", "Put your name on the breakfast series or the summer street fair.", "Sponsorship packs"),
   ("Give", "Our scholarship fund sends two local students to college every year.", "Give to the fund")]], "x-large", "wide", None)]), "section-second-brand"))

kit_page("kit-community", "Home page: Commons kit, associations, chambers and churches",
 "A complete home page for a chamber of commerce, association, club, nonprofit or church in the Commons kit: a photo of members with how to join, upcoming events, membership levels, the latest news, the people who run it and ways to get involved. Apply the Commons style for the look it was designed with.",
 "home, chamber of commerce, association, nonprofit, church, club, membership, events, kit, commons",
 ["commons-hero", "commons-events", "commons-join", "commons-news", "commons-leaders", "commons-involved"])

# ---------------------------------------------------------------- Rep (gym and classes)
K = "anypress/kit-fitness"
kit("rep-hero", K, "Rep hero: a training photo with a loud headline",
 "Opening section for a gym, boxing club, CrossFit box or studio: a full-screen training photo, a headline in heavy capitals and the free trial as the main button. Part of the Rep kit (gym and classes).",
 "hero, gym, fitness, crossfit, boxing, studio, classes, trial, rep",
 cover(on_photo(grp(N([h("Lift with people who know your name", 1, "poster", None, None, {"lineHeight": "0.9"}),
   p("Small-group strength and conditioning in Eastside. Coached every session, from your first lift.", "large"),
   btns([("Try a week free", None, "#trial"), ("See the timetable", "outline", "#timetable")])]), gap="medium", layout={"type": "constrained", "contentSize": "72rem", "justifyContent": "left"})),
   "Hero", "placeholder-wide.svg", 60, "92vh", "bottom left", ("xx-large", "x-large", "medium", "medium"), "80rem"))

def cls_tile(name, length, level, style):
    return grp(N([h(name, 3, "xx-large"), p(f"{length} · {level}", "medium")]), style, ("x-large", "x-large", "large", "large"), "small")
kit("rep-classes", K, "Rep classes: four classes on bold tiles",
 "The main classes on tiles of different colours, each with its name in big capitals, length and level. Part of the Rep kit.",
 "classes, programs, workouts, sessions, rep",
 sec("Classes", N([h("Classes", 2, "xxx-large"), grid([
   cls_tile("Strength", "60 min", "All levels", "section-second-brand"), cls_tile("Conditioning", "45 min", "All levels", "section-dark"),
   cls_tile("Boxing", "50 min", "Beginners welcome", "section-brand"), cls_tile("Mobility", "30 min", "Easy", "section-tint")], 2, "18rem", "small")])))

kit("rep-timetable", K, "Rep timetable: the week in a table",
 "The weekly timetable as a table: days down the side, morning, lunchtime and evening across. Part of the Rep kit; keep it current, or link to the booking system's live timetable.",
 "timetable, schedule, class times, week, rep",
 sec("Timetable", N([row([h("This week", 2, "xxx-large"), btns([("Book a class", None, "#trial")])], valign="bottom"),
   table(["", "6:30am", "12:15pm", "6pm"], [["Mon", "Strength", "Conditioning", "Boxing"], ["Tue", "Conditioning", "Mobility", "Strength"],
     ["Wed", "Strength", "Conditioning", "Boxing"], ["Thu", "Conditioning", "Mobility", "Strength"], ["Fri", "Strength", "Conditioning", "Strength"],
     ["Sat", "Team workout, 9am", "", ""]], "stripes")])))

def membership(name, price, items, style):
    return card(N([h(name, 3, "x-large"), row([p(price, "xxx-large", None, None, "archivo", {"lineHeight": "1", "fontWeight": "900", "fontStyle": "italic"}), p("a month")], "left", "x-small", valign="bottom"), lst(items)]), style)
kit("rep-prices", K, "Rep memberships: three prices, big",
 "Membership options with the monthly price set very large and what each includes. Part of the Rep kit; match the prices to the gym's real memberships.",
 "prices, membership, pricing, plans, rep",
 sec("Memberships", N([h("Memberships", 2, "xx-large"), p("No joining fee. Freeze or cancel with 30 days' notice.", "medium"), grid([
   membership("Two a week", "$89", ["Any two classes a week", "Free first week"], "section-card"),
   membership("Unlimited", "$129", ["Every class, every day", "Open gym hours", "Free first week"], "section-second-brand"),
   membership("Ten-class pass", "$150", ["Use within three months", "Share with a friend"], "section-card")], 3, "15rem", "small")]), "section-dark"))

def coach(name, text):
    return stackg([img("placeholder-wide.svg", f"{name} coaching a class", "3/2"), h(name, 3, "xx-large"), p(text, "medium")])
kit("rep-coaches", K, "Rep coaches: who will coach you",
 "Two coaches side by side, each with a photo, name and what they are known for. Part of the Rep kit; use the real coaches.",
 "coaches, trainers, team, staff, rep",
 sec("Coaches", N([h("Your coaches", 2, "xxx-large"), cols([col(coach("Marcus", "Head coach. Former rugby player, now teaches beginners to deadlift without fear.")),
   col(coach("Priya", "Boxing and conditioning. Twelve years in the ring and endlessly patient."))], "x-large", "wide", None)])))

kit("rep-trial", K, "Rep trial: first week free, huge",
 "The closing section on the second brand colour: the trial offer in huge capitals, what it includes and the button. Part of the Rep kit.",
 "trial, free week, offer, call to action, join, rep",
 sec("Trial", cols([col(h("First week free", 2, "poster", None, None, None), "60%"),
   col(N([p("Come to any class for seven days. Bring trainers and water; we'll show you the rest.", "large"), btns([("Claim your free week", None, "#trial")])]), None, None, None, "bottom")], "x-large", "wide", "bottom"),
   "section-second-brand", ("xx-large", "xx-large", None, None)))

kit_page("kit-fitness", "Home page: Rep kit, gym and classes",
 "A complete home page for a gym, boxing club, CrossFit box or fitness studio in the Rep kit: a training photo with a loud headline, classes on bold tiles, the weekly timetable, memberships, coaches and a free-trial close. Apply the Rep style for the look it was designed with.",
 "home, gym, fitness, crossfit, boxing, studio, personal trainer, classes, kit, rep",
 ["rep-hero", "rep-classes", "rep-timetable", "rep-prices", "rep-coaches", "rep-trial"])

# ---------------------------------------------------------------- Frame (creative portfolio)
K = "anypress/kit-portfolio"
kit("frame-hero", K, "Frame hero: who you are, in one big sentence",
 "Opening section for a photographer, designer, illustrator or architect: one very large sentence saying who they are and what they make, with where they work and availability in small type. No photo, so the work below does the talking. Part of the Frame kit (creative portfolio).",
 "hero, portfolio, photographer, designer, illustrator, architect, statement, frame",
 sec("Hero", N([h("Ines Duarte photographs buildings and the people who use them.", 1, "poster", None, None, {"lineHeight": "0.95"}),
   row([mono("Lisbon and Porto"), mono("Taking commissions from March"), p('<a href="#contact">' + T("hello@example.com") + "</a>", "medium", raw=True)], "left", "large")]), pad=("xx-large", "x-large", None, None)))

def work(file, alt, ratio, cap):
    return captioned(file, alt, ratio, cap)
kit("frame-work", K, "Frame work: selected projects, staggered",
 "Selected work as large photos in two staggered columns, each with a numbered caption in small type: the project, place and year. Part of the Frame kit; link each photo to its project page.",
 "work, projects, portfolio, gallery, case studies, frame",
 sec("Work", cols([
   col(stackg([work("placeholder-tall.svg", "A spiral staircase seen from above", "4/5", "01 — Spiral stair, Casa Moreira, Porto, 2025"),
               work("placeholder-wide.svg", "A white outdoor stair against a grey wall", "4/3", "03 — Fire stair, Marvila studios, 2024")], "xx-large"), "55%"),
   col(stackg([work("placeholder-tall.svg", "A blue painted building with white windows", "3/4", "02 — Azul, social housing in Setúbal, 2025"),
               work("placeholder-tall.svg", "A curving glass tower under a blue sky", "3/4", "04 — Tower One, for Atelier Sul, 2023")], "xx-large"), None, None, None, "bottom")], "x-large", "wide", None), pad=("large", "xx-large", None, None)))

kit("frame-project", K, "Frame project: one project with its details",
 "One project in depth: a full-width photo, then the details in small type on the left (client, year, role) and what was done on the right. Part of the Frame kit; use on a project page or to feature one project on the home page.",
 "project, case study, featured work, client, frame",
 N([cover("", "Project photo", "placeholder-wide.svg", 0, "80vh", "bottom left", ("large", "large", "medium", "medium")),
    sec("Project details", cols([
      col(stackg([stackg([mono(a), p(b)], "x-small") for a, b in [("Client", "Atelier Sul"), ("Year", "2023"), ("Role", "Photography, 3 days on site"), ("Used in", "Competition entry, book")]], "medium"), "30%"),
      col(N([h("Tower One", 2, "xxx-large"), p("A glass tower that changes colour with the weather. The architects wanted it shown on grey days as well as blue ones, so we shot over three weeks and chose the light, not the angle.", "large")]))], "xx-large", "wide", None))]))

kit("frame-clients", K, "Frame clients: names in a plain grid",
 "Past clients and publications as a plain grid of names in large type, without logos. Part of the Frame kit; only list clients who agreed to be named.",
 "clients, publications, logos, trust, selected clients, frame",
 sec("Clients", cols([col(mono("Selected clients"), "25%"),
   col(grid([p(n, "x-large", None, None, "bricolage-grotesque", {"lineHeight": "1.1", "fontWeight": "600"}) for n in ["Atelier Sul", "Casa Moreira", "Revista Linha", "Norte Weekly", "Studio Ferro", "Câmara de Vila Nova", "Oficina Azul", "Lisbon Design Week"]], 2, "14rem", "medium"))], "large", "wide", None),
   "section-tint"))

kit("frame-contact", K, "Frame contact: the email address, huge",
 "The closing section: an invitation to get in touch and the email address as large as the page allows, with social links in small type. Part of the Frame kit.",
 "contact, email, hire, commission, frame",
 sec("Contact", N([mono("Commissions, prints and talks"), p('<a href="mailto:hello@example.com">' + T("hello@example.com") + "</a>", "poster", None, None, "bricolage-grotesque", {"lineHeight": "1", "fontWeight": "700", "letterSpacing": "-0.04em"}, True, bind="email_linked"),
   row([mono("Instagram"), mono("Behance"), mono("Linkedin")], "left", "large")]), pad=("xx-large", "xx-large", None, None)))

kit_page("kit-portfolio", "Home page: Frame kit, creative portfolio",
 "A complete home page for a photographer, designer, illustrator, architect or artist in the Frame kit: one big sentence, selected work in staggered columns, one project in depth, clients and a huge email address. Apply the Frame style for the look it was designed with.",
 "home, portfolio, photographer, designer, illustrator, architect, artist, creative, kit, frame",
 ["frame-hero", "frame-work", "frame-project", "frame-clients", "frame-contact"])

# ---------------------------------------------------------------- Keystone (real estate)
K = "anypress/kit-real-estate"
kit("keystone-hero", K, "Keystone hero: a home photo with buy, sell and rent",
 "Opening section for an estate agent, realtor or property manager: a full-width photo of a home with the agency's promise and three buttons (buy, sell, rent). Part of the Keystone kit (real estate).",
 "hero, real estate, realtor, estate agent, property, homes, keystone",
 cover(on_photo(grp(N([h("Homes in the Hudson Valley, sold with care", 1, "poster", None, None, {"lineHeight": "1"}),
   p("A small agency that answers the phone, knows every town by name and has sold here for 22 years.", "large"),
   btns([("Homes for sale", None, "#listings"), ("Sell with us", "outline", "#valuation"), ("Rentals", "outline", "#listings")])]), gap="medium", layout={"type": "constrained", "contentSize": "52rem", "justifyContent": "left"})),
   "Hero", "placeholder-wide.svg", 50, "88vh", "bottom left", ("xx-large", "x-large", "medium", "medium"), "80rem"))

def listing(file, alt, status, price, address, facts):
    return stackg([img(file, alt, "4/3"), mono(status, "primary"), p(price, "xx-large", None, None, "gloock", {"lineHeight": "1"}), p(address, "medium"), p(facts, None, "secondary")])
kit("keystone-listings", K, "Keystone listings: three homes for sale",
 "Three homes as cards with a photo, status, price, address and the basic facts (beds, baths, size). Part of the Keystone kit; link each to its listing page, and remove a home when it sells.",
 "listings, homes for sale, properties, real estate, keystone",
 sec("Listings", N([row([h("Just listed", 2, "xx-large"), p('<a href="#">' + T("All homes for sale") + "</a>", "medium", raw=True)], valign="bottom"), grid([
   listing("placeholder-wide.svg", "A bright living room with a striped sofa", "Just listed", "$485,000", "12 Orchard Lane, Rhinebeck", "3 bed · 2 bath · 1,850 sq ft"),
   listing("placeholder-wide.svg", "A bedroom with an arched headboard wall", "Open house Sunday", "$629,000", "4 Mill Road, Kingston", "4 bed · 3 bath · 2,400 sq ft"),
   listing("placeholder-wide.svg", "A stone house with green shutters", "Price reduced", "$1,150,000", "The Old Rectory, Hudson", "5 bed · 4 bath · 3,900 sq ft")], 3, "16rem", "large")])))

kit("keystone-feature", K, "Keystone featured home: photo beside the details",
 "One home in depth: a large photo edge to edge beside a panel with the price, address, the main facts and a button to book a viewing. Part of the Keystone kit.",
 "featured property, featured listing, home, viewing, keystone",
 sec("Featured home", cols([
   col(fill("placeholder-wide.svg", 38), "58%"),
   col(N([mono("Featured home", "base"), h("The Old Rectory, Hudson", 2, "xx-large"), p("$1,150,000", "xx-large", None, None, "gloock"),
          p("An 1840s stone house on two acres, with the original floors, a walled garden and a barn ready to become a studio.", "medium"),
          lst(["5 bedrooms, 4 bathrooms", "3,900 sq ft on 2 acres", "Ten minutes to the Amtrak station"]), btns([("Book a viewing", None, "#agent")])]), None, "section-brand", ("xx-large", "xx-large", "x-large", "x-large"), "center")], "0", "full", None),
   None, (None, None, None, None), layout={"type": "default"}))

def stat(n, label, family):
    return stackg([p(n, "xxx-large", None, None, family, {"lineHeight": "1"}), p(label, None, "secondary")], "x-small")
kit("keystone-numbers", K, "Keystone numbers: the agency's record",
 "Four numbers that show the agency's record (homes sold, days on the market, asking price achieved, reviews) in a row. Part of the Keystone kit; use real, current figures.",
 "numbers, statistics, record, proof, results, keystone",
 sec("Record", grid([stat("340", "homes sold since 2019", "gloock"), stat("21 days", "on the market, on average", "gloock"), stat("98%", "of asking price achieved", "gloock"), stat("4.9 / 5", "from 210 reviews", "gloock")], 4, "12rem", "large"),
   "section-tint", ("x-large", "x-large", None, None)))

kit("keystone-agent", K, "Keystone agent: meet the agent",
 "The agent beside a portrait: who they are, how long they have worked in the area, their licence number and how to reach them directly. Part of the Keystone kit.",
 "agent, realtor, about, contact, licence, keystone",
 sec("Agent", cols([col(img("placeholder-tall.svg", "Portrait of the agent", "4/5"), "36%"),
   col(N([mono("Your agent"), h("Claire Hollis", 2, "xxx-large"), p("Claire grew up in Rhinebeck, sold her first house here in 2003 and still shows every home herself. She will tell you what a house is worth, not what you want to hear.", "medium"),
          p(T("Licensed real estate broker, NY 10491201234") + "<br>" + T("845 555 0117 · claire@example.com"), None, "secondary", raw=True), btns([("Call Claire", None, "tel:8455550117", "phone_link"), ("Send a message", "outline", "mailto:claire@example.com", "email_link")])]), None, None, None, "center")], "xx-large", "wide", "center")))

kit("keystone-valuation", K, "Keystone valuation: what's your home worth?",
 "The closing section on the second brand colour: an offer of a free valuation, how it works in one sentence and the button. Part of the Keystone kit.",
 "valuation, appraisal, sell, home value, call to action, keystone",
 sec("Valuation", cols([col(h("What is your home worth?", 2, "xxx-large"), "55%"),
   col(N([p("Claire visits, looks at what has sold nearby and gives you a price in writing within two days. Free, and no obligation.", "large"), btns([("Get a free valuation", None, "#valuation")])]), None, None, None, "center")], "xx-large", "wide", "center"),
   "section-second-brand"))

kit_page("kit-real-estate", "Home page: Keystone kit, real estate",
 "A complete home page for an estate agent, realtor or property manager in the Keystone kit: a home photo with buy, sell and rent, three listings, a featured home, the agency's record, the agent and a free valuation. Apply the Keystone style for the look it was designed with.",
 "home, real estate, realtor, estate agent, property, homes for sale, rentals, kit, keystone",
 ["keystone-hero", "keystone-listings", "keystone-feature", "keystone-numbers", "keystone-agent", "keystone-valuation"])

# ---------------------------------------------------------------- Launch (startup and software)
K = "anypress/kit-software"
kit("launch-hero", K, "Launch hero: what the product does, and a screenshot",
 "Opening section for a software product, app or startup: a label, a headline that says what the product does for whom, one sentence, two buttons and a wide screenshot under it. Part of the Launch kit (startup and software).",
 "hero, saas, software, app, startup, product, screenshot, launch",
 sec("Hero", N([mono("Invoicing for freelancers", "primary"), h("Send the invoice. Get paid. Get back to work.", 1, "poster", None, None, {"lineHeight": "0.95"}),
   grp(N([p("Tally sends your invoices, chases late payers politely and tells you what to put aside for tax. Free for your first ten clients.", "large"),
          btns([("Start free", None, "#start"), ("See pricing", "outline", "#pricing")])]), gap="medium", layout={"type": "constrained", "contentSize": "40rem", "justifyContent": "left"}),
   img("placeholder-wide.svg", "The app's dashboard showing paid and unpaid invoices", "16/9")]), pad=("xx-large", "x-large", None, None), content="72rem"))

kit("launch-logos", K, "Launch customers: a line of customer names",
 "A line of customer or press names under a short sentence, set in grey type rather than logos. Part of the Launch kit; only name customers who agreed to it, and swap in logo images when they are ready.",
 "logos, customers, trusted by, social proof, press, launch",
 sec("Customers", N([p("Used by 3,000 studios and freelancers, including", None, "secondary", "center"),
   row([p(n, "large", "secondary", None, "schibsted-grotesk", {"fontWeight": "800", "letterSpacing": "-0.02em"}) for n in ["Northwind", "Halcyon", "Fieldnote", "Pine & Co", "Brightside"]], "center", "x-large")]),
   "section-tint", ("large", "large", None, None)))

def feat(n, title, text):
    return stackg([sep(), mono(n, "primary"), h(title, 3, "large"), p(text, None, "secondary")], "small")
kit("launch-features", K, "Launch features: six things it does, without icons",
 "Six features in a grid, each with a thin rule, a number, a short heading and one sentence. No icons. Part of the Launch kit; say what each feature does for the customer, not how it works.",
 "features, benefits, product, how it works, launch",
 sec("Features", N([cols([col(h("Everything after you finish the work", 2, "xxx-large"), "55%"), col(p("You do the job. Tally does the paperwork that used to eat your Fridays.", "large", "secondary"), None, None, None, "bottom")], "x-large", "wide", "bottom"),
   grid([feat("01", "Invoices in a minute", "Pick the client, add the hours, send. Your logo and payment details are already on it."),
         feat("02", "Polite reminders", "Late payers get a friendly nudge at 3, 7 and 14 days, in your words."),
         feat("03", "Paid by card or bank", "Clients pay from the invoice. Money lands in your account in two days."),
         feat("04", "Tax set aside", "See what to save for tax from every payment, as you go."),
         feat("05", "Works with your bank", "Payments match themselves to invoices. No spreadsheets."),
         feat("06", "Your accountant can log in", "Give them read-only access at year end, and skip the shoebox.")], 3, "16rem", "x-large")])))

def step(n, title, text):
    return stackg([p(n, "xxx-large", "primary-alt", None, "schibsted-grotesk", {"lineHeight": "1", "fontWeight": "800"}), h(title, 3, "large"), p(text)])
kit("launch-steps", K, "Launch how it works: three steps",
 "How to get started in three numbered steps across the page, on the second brand colour. Part of the Launch kit; three steps, each one sentence.",
 "how it works, steps, getting started, onboarding, launch",
 sec("How it works", N([h("Up and running before lunch", 2, "xxx-large"), grid([
   step("1", "Add your clients", "Import them from a spreadsheet or your old tool."), step("2", "Connect your bank", "Read-only, so payments can match themselves."),
   step("3", "Send your first invoice", "Pick a template, check it, send.")], 3, "15rem", "x-large")]), "section-dark"))

def sw_plan(name, price, per, text, items, style, label, primary=False):
    return card(N([h(name, 3, "large"), row([p(price, "xxx-large", None, None, "schibsted-grotesk", {"lineHeight": "1", "fontWeight": "800"}), p(per)], "left", "x-small", valign="bottom"),
                   p(text, None, "secondary" if style != "section-dark" else "main-accent"), lst(items), btns([(label, None if primary else "outline", "#start")])]), style)
kit("launch-pricing", K, "Launch pricing: free, pro and team",
 "Three plans side by side with the monthly price, who each is for, what it includes and a button; the plan most people choose is on the dark style. Part of the Launch kit; match it to the real plans.",
 "pricing, plans, subscription, free plan, saas, launch",
 sec("Pricing", N([h("Simple pricing", 2, "xxx-large", "center"), p("Every plan has a 30-day free trial. No card needed to start.", "medium", "secondary", "center"), grid([
   sw_plan("Free", "$0", "a month", "For your first clients.", ["Up to 10 clients", "Card and bank payments", "Reminders"], "section-card", "Start free"),
   sw_plan("Pro", "$12", "a month", "For full-time freelancers.", ["Unlimited clients", "Tax set aside", "Bank matching", "Your own domain on invoices"], "section-dark", "Start a free trial", True),
   sw_plan("Team", "$29", "a month", "For studios of up to ten.", ["Everything in Pro", "Up to 10 people", "Shared clients and approvals"], "section-card", "Start a free trial")], 3, "16rem", "medium")]), "section-tint"))

kit("launch-faq", K, "Launch questions: what people ask before signing up",
 "Common questions that open one at a time, beside a heading and a link to support. Part of the Launch kit; answer the real questions from sales and support.",
 "faq, questions, answers, support, launch",
 sec("Questions", cols([col(N([h("Questions", 2, "xxx-large"), p('<a href="mailto:help@example.com">' + T("Ask us anything") + "</a>", "medium", raw=True)]), "35%"),
   col(stackg([details("Is my data safe?", "Your data is encrypted, backed up every day and never sold. You can export or delete it at any time.", "medium"),
               details("Can I import my old invoices?", "Yes. Upload a spreadsheet or connect your old tool and we bring everything across.", "medium"),
               details("What happens when the trial ends?", "You choose a plan or stay on Free. Nothing is deleted.", "medium"),
               details("Do you take a cut of payments?", "No. Card payments cost the processor's fee, and bank payments are free.", "medium")], "small"))], "xx-large", "wide", None)))

kit("launch-cta", K, "Launch closing: try it free",
 "The closing section on the brand colour: one line saying what to do next, and the sign-up button. Part of the Launch kit.",
 "call to action, sign up, free trial, get started, launch",
 sec("Try it", cols([col(h("Your next invoice could be your last chore", 2, "xxx-large"), "62%"),
   col(N([p("Free for your first ten clients. Set up in ten minutes.", "large"), btns([("Start free", None, "#start")])]), None, None, None, "bottom")], "x-large", "wide", "bottom"), "section-brand"))

kit_page("kit-software", "Home page: Launch kit, startup and software",
 "A complete home page for a software product, app or startup in the Launch kit: what the product does with a screenshot, customer names, six features, three steps, pricing, questions and a sign-up close. Apply the Launch style for the look it was designed with.",
 "home, saas, software, app, startup, product, pricing, kit, launch",
 ["launch-hero", "launch-logos", "launch-features", "launch-steps", "launch-pricing", "launch-faq", "launch-cta"])

# ---------------------------------------------------------------- Byline (blog and magazine)
K = "anypress/kit-magazine"
kit("byline-masthead", K, "Byline masthead: the publication's name between rules",
 "The top of a blog or magazine home page: the name set very large between two rules, with a line saying what it covers and how often. Part of the Byline kit (blog and magazine).",
 "masthead, blog, magazine, newsletter, publication, title, byline",
 sec("Masthead", N([sep(), h("Field Notes", 1, "poster", "center", None, {"lineHeight": "0.9", "letterSpacing": "-0.04em"}),
   row([p("Walking, eating and sleeping outdoors", "small", "secondary", None, "system-sans", {"textTransform": "uppercase", "letterSpacing": "0.08em"}),
        p("New stories every Thursday", "small", "secondary", None, "system-sans", {"textTransform": "uppercase", "letterSpacing": "0.08em"})]), sep()]),
   pad=("x-large", "medium", None, None)))

kit("byline-lead", K, "Byline lead story: the newest post, large",
 "The newest post, large: its photo beside the category, title, excerpt and date. Part of the Byline kit; it updates on its own when a new post is published.",
 "featured post, lead story, latest post, blog, byline",
 sec("Lead story", query(1, 0, 1, cols([
   col(dyn("post-featured-image", {"isLink": True, "aspectRatio": "4/3"}), "55%"),
   col(stackg([dyn("post-terms", {"term": "category", "textColor": "primary", "fontSize": "small"}), dyn("post-title", {"level": 2, "isLink": True, "fontSize": "xx-large"}),
               dyn("post-excerpt", {"excerptLength": 32, "fontSize": "medium"}), dyn("post-date", {"textColor": "secondary", "fontSize": "small"})], "medium"), None, None, None, "center")], "x-large", None, "center"), 21,
   "Your newest post will appear here, large."), pad=("medium", "x-large", None, None)))

kit("byline-latest", K, "Byline latest: six more stories in a grid",
 "The next six posts after the lead story in a three-column grid with photo, category, title and date. Part of the Byline kit; place it after the lead story.",
 "latest posts, recent posts, blog grid, articles, byline",
 sec("Latest", N([sep(), h("Latest", 2, "large", None, "system-sans", {"textTransform": "uppercase", "letterSpacing": "0.08em"}),
   query(6, 1, 3, stackg([dyn("post-featured-image", {"isLink": True, "aspectRatio": "3/2"}), dyn("post-terms", {"term": "category", "textColor": "primary", "fontSize": "small"}),
                          dyn("post-title", {"level": 3, "isLink": True, "fontSize": "large"}), dyn("post-date", {"textColor": "secondary", "fontSize": "small"})], "small"), 22)]),
   pad=("large", "xx-large", None, None)))

kit("byline-topics", K, "Byline topics: the subjects you write about",
 "The publication's main topics as a large list of links on the tint colour, so readers can go straight to what they like. Part of the Byline kit; link each to its category page.",
 "topics, categories, sections, browse, byline",
 sec("Topics", cols([col(h("Read by topic", 2, "xx-large"), "30%"),
   col(row([p(f'<a href="#">{T(t)}</a>', "x-large", None, None, None, {"lineHeight": "1.1"}, True) for t in ["Long walks", "Huts and bothies", "Cooking outside", "Gear that lasts", "Trip notes", "Interviews"]], "left", "large"))], "x-large", "wide", None),
   "section-tint", ("x-large", "x-large", None, None)))

kit("byline-about", K, "Byline about: who writes it, and how to subscribe",
 "A short note from the writer beside a small portrait, with the email signup button: who they are, what they write and how often. Part of the Byline kit.",
 "about, author, writer, newsletter, subscribe, byline",
 sec("About", cols([col(img("placeholder-square.svg", "Portrait of the writer outdoors", "1"), "25%"),
   col(N([h("Written by Hanna Berg", 2, "xx-large"), p("I've walked across six countries with a stove and a notebook. Field Notes is what I learned: where to go, what to eat, what to carry and what to leave at home.", "large"),
          p("One story a week, by email. Free, and no adverts.", None, "secondary"), btns([("Subscribe", None, "mailto:hello@example.com?subject=Subscribe")])]), None, None, None, "center")], "x-large", "wide", "center"), content="60rem"))

kit_page("kit-magazine", "Home page: Byline kit, blog and magazine",
 "A complete home page for a blog, magazine, newsletter or writer in the Byline kit: the name between rules, the newest post large, six more in a grid, topics and a note from the writer with a signup. Posts appear on their own. Apply the Byline style for the look it was designed with.",
 "home, blog, magazine, newsletter, writer, publication, kit, byline",
 ["byline-masthead", "byline-lead", "byline-latest", "byline-topics", "byline-about"])
print("more kits ok")

# ---------------------------------------------------------------- Everyday sections and pages (more JP Blocks gaps)
author = avatar.replace("8rem", "6rem").replace('"align":"center",', "").replace("aligncenter ", "")
write("author-box", "Author box: who wrote this",
 "A box at the end of a post with the writer's photo, name, a two-line bio and where to follow them. Use at the end of blog posts and guides; it builds trust in the advice.",
 "text, posts", "author, author box, bio, writer, about the author",
 sec("Author", card(cols([col(author, "6rem"), col(N([h("Written by Ana Ortiz", 3, "large"), p("Ana has taught yoga in Springfield since 2012 and writes about moving well at any age.", None, "secondary"),
   social(["instagram", "youtube"])]), None, None, None, "center")], "medium", None, "center", False), "section-tint"), pad=("large", "large", None, None), content="48rem"))

write("contact-form-section", "Contact: details beside a message box",
 "A contact section in two columns: how to reach the business on the left (phone, email, address, hours) and a box on the right for sending a message. Put the site's contact form block in the right-hand box in place of the button when a form exists.",
 "anypress-details, call-to-action", "contact, contact form, get in touch, message, enquiry",
 sec("Contact", cols([
   col(N([h("Get in touch", 2, "xx-large"), p("We answer every message within one working day.", "medium", "secondary"),
          stackg([stackg([h(a, 3, "medium"), p(b, bind=k)], "x-small") for a, b, k in [("Phone", "555 0142", "phone_linked"), ("Email", "hello@example.com", "email_linked"), ("Visit", "14 Market Street, Springfield", "address"), ("Hours", "Monday to Friday, 9am to 5pm", "hours")]], "medium")]), "45%"),
   col(card(N([h("Send us a message", 3, "large"), p("Tell us what you need and the best way to reach you.", None, "secondary"), btns([("Email us", None, "mailto:hello@example.com", "email_link")])]), "section-tint"))], "xx-large", "wide", None)))

def tfeat(title, text):
    return stackg([sep(), h(title, 3, "medium"), p(text, None, "secondary")], "small")
write("features-text", "Features: six points in a grid, no icons",
 "Six short points in a three-column grid, each with a thin rule, a heading and one sentence. Use for features, benefits or reasons to choose the business, where icons would add nothing.",
 "features, services", "features, benefits, reasons, why us, grid",
 sec("Features", N([h("Why people choose us", 2, "xx-large"), grid([
   tfeat("Fixed prices", "You know the cost before we start. No surprises on the bill."), tfeat("On time", "We turn up when we say, or we call you first."),
   tfeat("Tidy work", "We clean up every day, not just at the end."), tfeat("Local", "Everyone on the team lives within twenty miles."),
   tfeat("Guaranteed", "If something we did goes wrong, we come back and fix it."), tfeat("Easy to reach", "A real person answers the phone, six days a week.")], 3, "15rem", "x-large")])))

def fcol(title, items):
    return col(stackg([h(title, 2, "small", None, None, {"textTransform": "uppercase", "letterSpacing": "0.08em"}), links(items)], "small"))
write("footer-columns", "Footer: columns of links",
 "A full footer on the dark style: the site name, a sentence and social links in the first column, then columns of links (pages, help, visit), and a small line at the bottom. Use as the site footer for sites with more than a few pages.",
 "footer", "footer, links, columns, sitemap, social",
 grp(N([cols([col(stackg([dyn("site-title", {"level": 0}), p("Family-run roofers covering the whole county since 2001.", None, "main-accent"), social(["facebook", "instagram"])], "medium"), "34%"),
   fcol("Pages", [("Services", "#"), ("About", "#"), ("Reviews", "#"), ("Blog", "#")]), fcol("Help", [("Get a quote", "#"), ("Questions", "#"), ("Privacy", "#")]),
   col(stackg([h("Visit", 2, "small", None, None, {"textTransform": "uppercase", "letterSpacing": "0.08em"}), p(T("14 Market Street") + "<br>" + T("Springfield"), raw=True, bind="address"), p("555 0142", bind="phone")], "small"))], "large", None, None),
   sep(), row([p("All rights reserved.", "small", "main-accent"), p('<a href="#">' + T("Back to top") + "</a>", "small", raw=True)])]),
   "section-dark", ("x-large", "large", None, None), "large", {"type": "constrained", "contentSize": "80rem"}, align="full", name="Footer"), "core/template-part/footer")

write("footer-small", "Footer: one line",
 "A small one-line footer: the site name on the left and a few links on the right. Use for small sites and landing pages.",
 "footer", "footer, small footer, simple, one line",
 grp(row([dyn("site-title", {"level": 0, "fontSize": "medium"}), row([p(f'<a href="#">{T(t)}</a>', "small", None, None, None, None, True) for t in ["Contact", "Privacy", "Instagram"]], "right", "medium")], valign="center"),
   None, ("medium", "medium", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Footer"), "core/template-part/footer")

write("social-follow", "Follow us: social links on a band",
 "A band asking visitors to follow the business on social media, with one line about what they post and the social icons. Use near the end of a page; link only the accounts the business keeps up.",
 "call-to-action, text", "social media, follow, instagram, facebook, tiktok, social links",
 sec("Follow", N([h("Follow along", 2, "x-large", "center"), p("New work, behind the scenes and the odd offer, a few times a week.", None, None, "center"), social(["instagram", "facebook", "tiktok", "youtube"], "center")]),
   "section-brand-soft", ("x-large", "x-large", None, None), content="40rem"))

write("logo-row", "Logos: a row of client or partner names",
 "A short line and a row of client, partner or press names. Shows names as text until logo images are added; replace each name with an image block of the logo, all the same height.",
 "anypress-proof", "logos, clients, partners, as seen in, press, trusted by",
 sec("Logos", N([p("Trusted by businesses across the county", None, "secondary", "center"),
   row([p(n, "large", "secondary", None, None, {"fontWeight": "700"}) for n in ["Oak Hill Dental", "Riverside Brewery", "The Grand Hotel", "Ashford School", "Millbrook Farm"]], "center", "x-large")]),
   pad=("large", "large", None, None)))

write("numbers-band", "Numbers: four figures in a row",
 "Four large figures in a row with a short label under each, such as years in business, jobs done, reviews and response time. Use as proof; only use real, current numbers.",
 "anypress-proof", "numbers, statistics, stats, figures, counter, proof",
 sec("Numbers", grid([stackg([p(n, "xxx-large", None, None, None, {"lineHeight": "1", "fontWeight": "700"}), p(l)], "x-small") for n, l in [("25", "years in business"), ("4,000+", "jobs finished"), ("4.9", "average from 380 reviews"), ("2 hrs", "average reply time")]], 4, "12rem", "large"),
   "section-brand", ("x-large", "x-large", None, None)))
print("everyday 2 ok")

# Starter pages that reuse the base sections.
def page(slug, title, desc, kw, parts, ptype="page"):
    write(slug, title, desc, "anypress/pages" if ptype == "page" else "anypress/posts", kw, N(parts), "core/post-content", f" * Post Types: {ptype}\n")

page("page-services", "Services page",
 "A Services page: a short introduction, the services with prices, how working together goes in steps, common questions and a closing call to action.",
 "services, what we do, prices, process, faq",
 [sec("Introduction", N([h("Services", 1, "xxx-large"), p("Everything we do, what it costs and how it works. Not sure what you need? Call us and we'll tell you honestly.", "large", "secondary")]), pad=("xx-large", "large", None, None), content="48rem"),
  base_body("services-list"), base_body("steps"), base_body("faq"), base_body("call-to-action-dark")])

page("page-sales", "Sales page: one offer, start to finish",
 "A long sales page for one product, course or service: the promise, the problem, what's included, who it is for and not for, a review, the price with a guarantee, questions and a last call. Write it for one offer only.",
 "sales page, landing page, offer, launch, product, course, long form",
 [sec("Promise", N([mono("For new freelancers"), h("Find your first five clients in six weeks", 1, "poster", None, None, {"lineHeight": "0.95"}),
       p("A short, practical programme for people who are good at their work and bad at selling it.", "large"), btns([("Join for $199", None, "#buy")])]), pad=("xx-large", "x-large", None, None), content="56rem"),
  sec("Problem", N([h("Sound familiar?", 2, "xx-large"), lst(["Your portfolio is ready, and nobody is looking at it", "You've sent fifty messages and had two replies", "You hate the idea of selling"], "large")]), "section-tint", content="56rem"),
  sec("What's included", N([h("What you get", 2, "xx-large"), grid([tfeat(a, b) for a, b in [("Six weekly lessons", "Short videos and one task each week."), ("Message templates", "Tested words for first emails and follow-ups."),
       ("Two group calls", "Bring your questions and your drafts."), ("Lifetime access", "Including every future update.")]], 2, "16rem", "x-large")]), content="56rem"),
  sec("Who it's for", cols([col(card(N([h("For you if", 3, "large"), lst(["You have skills people pay for", "You can give it two hours a week", "You want clients, not followers"])]), "section-brand-soft")),
       col(card(N([h("Not for you if", 3, "large"), lst(["You want a passive income scheme", "You haven't picked what you offer yet"])]), "section-tint"))], "medium", "wide", None), content="56rem"),
  sec("Review", quote("Three clients in the first month. The follow-up template alone paid for it.", "Rosa K., illustrator", "xx-large"), "section-brand", content="48rem"),
  sec("Price", N([h("$199, once", 2, "xxx-large", "center"), p("Or three payments of $69. If you do the work and don't land a client in 60 days, you get your money back.", "large", None, "center"), btns([("Join now", None, "#buy")], "center")]), content="44rem"),
  sec("Questions", N([h("Questions", 2, "xx-large"), stackg([details("How long do I have access?", "For as long as the course exists, including updates."), details("What if I'm not a designer?", "It works for any skill you sell by the project: writing, photography, development, bookkeeping."),
       details("Can I get an invoice for my business?", "Yes, one is emailed with your receipt.")], "small")]), "section-tint", content="56rem"),
  sec("Last call", N([h("Ready to find your first five?", 2, "xx-large", "center"), btns([("Join for $199", None, "#buy")], "center")]), "section-dark", content="44rem")])

page("page-signup", "Signup page: join the email list",
 "A short page whose only job is getting an email signup: what people get, how often, a sample of past issues and the signup button. Put the site's signup form in place of the button when one exists.",
 "signup, newsletter, email list, subscribe, lead magnet, opt in",
 [sec("Signup", N([h("The Sunday letter", 1, "xxx-large"), p("One email every Sunday morning: three things worth your time, one recipe, no adverts. 12,000 people read it.", "large"),
       btns([("Subscribe free", None, "mailto:hello@example.com?subject=Subscribe")]), p("Unsubscribe in one click. We never share your address.", "small", "secondary")]), pad=("xx-large", "x-large", None, None), content="40rem"),
  sec("Past letters", N([h("Recent letters", 2, "large"), links([("No. 112: The best bread is two days old", "#"), ("No. 111: A walk with no destination", "#"), ("No. 110: Soup for people who don't like soup", "#")])]), "section-tint", ("x-large", "x-large", None, None), content="40rem")])

page("page-thank-you", "Thank you page: after a signup or purchase",
 "The page people see after they sign up, buy or send a form: a thank you, what happens next in three steps and one next thing to do. Set the form or checkout to send people here.",
 "thank you, confirmation, success, after purchase, after signup",
 [sec("Thank you", N([h("Thank you, you're in", 1, "xxx-large", "center"), p("Check your email: we've sent a confirmation and everything you need.", "large", None, "center")]), pad=("xx-large", "large", None, None), content="40rem"),
  sec("Next", N([h("What happens next", 2, "large"), stackg([stackg([h(a, 3, "medium"), p(b, None, "secondary")], "x-small") for a, b in [("1. Check your inbox", "The email comes from hello@example.com. Look in spam if it isn't there in five minutes."),
       ("2. Save the date", "Your first lesson arrives on Monday morning."), ("3. Say hello", "Reply to the email and tell us what you hope to get out of it.")]], "medium"), btns([("Back to the home page", "outline", "/")])]), "section-tint", ("x-large", "x-large", None, None), content="40rem")])

# Post outlines: starting structures for the three most common kinds of blog post.
page("post-how-to", "Post outline: how-to guide",
 "A how-to blog post outline: what the reader will be able to do, what they need, numbered steps with a tip, and a short wrap-up. Replace every line with the real guide.",
 "how to, guide, tutorial, steps, instructions, blog post",
 [p("By the end of this guide you'll be able to clear a blocked gutter safely in under an hour, without hiring anyone.", "large"),
  h("What you need", 2), lst(["A sturdy ladder and someone to hold it", "Work gloves", "A small trowel or gutter scoop", "A bucket and a hose"]),
  h("1. Set up the ladder safely", 2), p("Put the feet on firm, level ground, one foot out for every four feet up. Never lean the ladder on the gutter itself."),
  h("2. Scoop out the debris", 2), p("Start at the downpipe end and work away from it, dropping leaves into the bucket."),
  grp(p("<strong>" + T("Tip:") + "</strong> " + T("Do this on a dry day. Wet leaves are twice as heavy and slide off the trowel."), raw=True), "section-brand-soft", PAD_CARD, layout={"type": "default"}),
  h("3. Flush with the hose", 2), p("Run water from the far end. If it backs up, the downpipe is blocked: push the hose up from the bottom."),
  h("That's it", 2), p("Do it twice a year, in late autumn and spring. If water still overflows, the gutter may need re-hanging.")], "post")

page("post-list", "Post outline: list post",
 "A list blog post outline (such as 'seven best' or 'ten ideas'): a short introduction, numbered items each with a photo and a few sentences, and a wrap-up. Replace every item with the real ones.",
 "list, listicle, best, top, ideas, roundup, blog post",
 [p("Five walks within an hour of Springfield, all under ten miles, with a good place to eat at the end.", "large")] +
 [N([h(f"{i}. {t}", 2), img("placeholder-wide.svg", alt, "3/2"), p(text)]) for i, (t, alt, text) in enumerate([
   ("Oak Hill ridge", "A path along a grassy ridge", "Eight miles with views over three counties. Muddy in winter; boots, not trainers."),
   ("The river loop", "A river with trees on both banks", "Flat and easy, five miles, with the Riverside Brewery at the end."),
   ("Cedar Falls", "A small waterfall in a wood", "Short but steep. Go after rain, when the falls are at their best.")], 1)] +
 [h("Which to pick", 2), p("New to walking? Start with the river loop. Want a day out? Oak Hill, with lunch in the village.")], "post")

page("post-review", "Post outline: product review",
 "A product review blog post outline: a verdict box up top (rating, who it suits, price, where to buy), what it is, what was tested, pros and cons, and the final verdict. Replace every line with the real review.",
 "review, product review, rating, verdict, pros and cons, blog post",
 [card(N([h("The verdict", 2, "large"), p("<strong>" + T("4 out of 5.") + "</strong> " + T("The best-made walking pole we tested, but heavy for long days."), raw=True),
     p("Best for: day walks and steep ground. Price: $89 a pair."), btns([("Check the price", None, "#")])]), "section-tint"),
  h("What it is", 2), p("A three-section aluminium pole with a cork grip and a flick lock, sold in pairs."),
  h("How we tested it", 2), p("Two of us used a pair for six weeks: 140 miles, mostly on rocky hill paths, in rain and dry weather."),
  cols([col(card(N([h("Good", 3, "medium"), lst(["Locks never slipped", "Cork grip stays dry", "Easy to adjust with gloves"])]), "section-brand-soft")),
        col(card(N([h("Not so good", 3, "medium"), lst(["Heavier than carbon poles", "Basket falls off easily"])]), "section-tint"))], "medium", None, None),
  h("The verdict", 2), p("If you walk mostly on steep, rough ground, these are worth it. For long-distance hikes, a lighter carbon pole will save your arms.")], "post")
print("pages ok")
