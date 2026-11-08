# Byline (0.19.0): a whole website for a blog, magazine or newsletter, written for a small outdoor magazine that also
# publishes route guides, runs guided walks and sells a print subscription.
# Run by kits.py after kit_keystone.py, so every helper in kits.py, kits_more.py, kit_ridge.py and the kits before it
# is in scope.
#
# A printed page: a heavy serif, thin rules, small capitals in a plain sans. Pages link to each other by slug:
# /stories/ (the blog) and its topics under /category/, /routes/ and one page per route under it, /walks/ and one page
# per walk under it, /book-a-walk/, /subscribe/, /about/, /readers/, /write-for-us/, /faq/, /contact/, /thank-you/.
# Forms are named groups, as in Ridge: "Form: quote" books a walk, "Form: apply" is the contributor application.

BK = "anypress/kit-magazine"
BSERIF = "literata"
BPH = "(406) 555-0139"
BTL = "tel:4065550139"
BSUB = "/subscribe/"
BADDR = "21 West Main Street, Bozeman, MT 59715"
BLAT, BLON = 45.6793, -111.0386
BHOURS = "Monday to Friday, 9am to 5pm. The shop is open Saturdays too."
BCAPS = {"textTransform": "uppercase", "letterSpacing": "0.08em"}

def bcaps(text, color="secondary", size="small"):
    """A small label in capitals, in the plain sans the kit uses for its section labels."""
    return p(text, size, color, None, "system-sans", BCAPS)

def bhead(label, title, link=None, size="xx-large"):
    left = stackg([bcaps(label, "primary"), h(title, 2, size)])
    return row([left, btns([(link[0], "outline", link[1])])] if link else [left], valign="bottom")

def b_buttons():
    """The header's button: subscribe, everywhere."""
    return '<!-- wp:buttons {"layout":{"type":"flex","flexWrap":"nowrap"}} -->\n<div class="wp-block-buttons"><!-- wp:button -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="' + BSUB + '">' + T("Subscribe") + '</a></div>\n<!-- /wp:button --></div>\n<!-- /wp:buttons -->'

def bwide(markup):
    """An image that fills its column even when the photo is narrower than the page."""
    return (markup.replace('"scale":"cover"}', '"scale":"cover","width":"100%"}', 1)
                  .replace('class="wp-block-image size-large"', 'class="wp-block-image size-large is-resized"', 1)
                  .replace('object-fit:cover"', 'object-fit:cover;width:100%;height:auto"', 1))

def bpage_hero(title, text, crumb=None, buttons=None, alt=None):
    words = N(([bcaps(crumb, "primary")] if crumb else []) + [h(title, 1, "xxx-large", None, None, {"lineHeight": "1.05"}), p(text, "large")] + ([btns(buttons)] if buttons else []))
    head = sec("Page hero", N([sep(), grp(words, gap="medium", layout={"type": "constrained", "contentSize": "52rem", "justifyContent": "left"})]), None, ("x-large", "large", None, None), "80rem")
    if not alt:
        return head
    return N([head, sec("Page photo", bwide(img("placeholder-wide.svg", alt, "21/9")), None, (None, "x-large", None, None), "80rem")])

def bfact(label, value):
    """A label in small capitals and its value on one line; never wraps in a narrow card."""
    return grp(N([bcaps(label), p(value)]), layout={"type": "flex", "flexWrap": "nowrap", "justifyContent": "space-between", "verticalAlignment": "top"}, gap="small")

def bcard(inner, style="section-tint", gap="medium"):
    return grp(N(inner), style, PAD_CARD, gap, {"type": "default"})

# ---------------------------------------------------------------- content
BTOPICS = [("Long walks", "long-walks"), ("Huts and cabins", "huts-and-cabins"), ("Cooking outside", "cooking-outside"),
           ("Gear that lasts", "gear-that-lasts"), ("Trip notes", "trip-notes"), ("Interviews", "interviews")]
BWALKS = [  # name, slug, price, line
    ("Sunrise ridge walk", "sunrise-ridge-walk", "$95 a person", "Up Bridger Ridge in the dark, breakfast on top as the sun comes up."),
    ("Cabin weekend", "cabin-weekend", "$340 a person", "Two days in the Gallatins with a night in a forest cabin."),
    ("Cook on the trail", "cook-on-the-trail", "$120 a person", "A short walk to a lake and a long lunch cooked on one stove."),
    ("Map and compass day", "map-and-compass", "$110 a person", "Find your way without a phone, on easy trails near town."),
]
BROUTES = [  # name, slug, distance, climb, line
    ("Hyalite Lake", "hyalite-lake", "11 miles", "1,800 ft", "Eleven waterfalls on the way up to a lake under Hyalite Peak."),
    ("Lava Lake", "lava-lake", "6 miles", "1,600 ft", "A steep forest climb to a deep green lake in the Madison Range."),
    ("Bridger Ridge", "bridger-ridge", "20 miles", "6,500 ft", "The whole ridge above town, end to end, in one long day."),
    ("Sypes Canyon", "sypes-canyon", "6 miles", "1,700 ft", "The after-work walk: a canyon trail to a view over the valley."),
]
BTEAM = [("Hanna Berg", "Editor", "Walked across six countries before settling in Bozeman to start Field Notes."),
         ("Tom Reyes", "Routes editor", "Checks every route we publish on foot, twice, in two seasons."),
         ("June Okafor", "Walks and cooking", "Leads our guided walks and writes the cooking column.")]
BLETTERS = [
    ("The Hyalite guide was so exact we never once looked at our phones. We counted the waterfalls out loud.", "Rachel S.", "Reader in Billings"),
    ("I've read every issue on the bus to work. It's the closest I get to the mountains most weeks.", "Daniel P.", "Reader in Chicago"),
    ("June's one-pot chili is now the only thing we cook on the trail. Thank you.", "Mia and Sam T.", "Readers in Missoula"),
    ("The map and compass day gave me the nerve to walk alone. Best $110 I've spent.", "Grace L.", "Walked with us"),
    ("No adverts, no lists of ten things. Just good writing about being outside.", "Owen H.", "Print subscriber"),
    ("The interview with the fire lookout made me cry on a plane.", "Priya N.", "Reader in Denver"),
]

def bletter(text, name, what, size="medium"):
    return grp(N([p("“" + text + "”", size, None, None, BSERIF, {"lineHeight": "1.45"}), bcaps(f"{name} · {what}")]),
               "section-card", PAD_CARD, "small", {"type": "default"})

# ---------------------------------------------------------------- sections
kit("byline-topbar", BK, "Byline top bar: the new issue and the phone number",
 "A thin bar above the header with the newest print issue and a link to subscribe, and the office phone number. Part of the Byline kit.",
 "top bar, announcement, subscribe, phone, header, byline",
 grp(row([p(T("The autumn issue is out now") + f' · <a href="{BSUB}">' + T("Subscribe") + '</a>', "small", None, None, None, None, raw=True),
          p(T("Subscriptions and walks") + f' <a href="{BTL}">' + T(BPH) + '</a>', "small", None, None, None, None, raw=True)], gap="small"),
     "section-dark", ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Top bar"))

BHEADER = grp(N([
    BODIES["byline-topbar"],
    grp(row([
        row([dyn("site-logo", {"width": 36, "shouldSyncIcon": True}), dyn("site-title", {"level": 0, "fontSize": "large", "fontFamily": BSERIF, "style": {"typography": {"lineHeight": "1"}}})], "left", "small", False, "center"),
        row([dyn("navigation", {"overlayMenu": "mobile", "layout": {"type": "flex", "justifyContent": "right"}}), b_buttons()], "right", "medium", False, "center")], "space-between", "medium", False, "center"),
        None, ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Main bar").replace(
        '<!-- wp:group {', '<!-- wp:group {"backgroundColor":"base",', 1).replace('class="wp-block-group alignfull', 'class="wp-block-group alignfull has-base-background-color has-background', 1),
]), "sticky", None, "0", {"type": "default"}, align="full", name="Header")
write("byline-header", "Byline header: the new issue, menu and a Subscribe button",
 "A site header for a blog, magazine or newsletter that stays at the top while visitors scroll: a bar with the newest issue and the phone number, then the logo, the menu (with dropdowns for routes and walks) and a Subscribe button. Part of the Byline kit; choose it for the header in the Site Editor.",
 "header", "header, menu, navigation, sticky, subscribe, magazine, byline", BHEADER, "core/template-part/header")

# Topics now link to their category pages.
kit("byline-topics", BK, "Byline topics: the subjects you write about",
 "The publication's main topics as a large list of links on the tint colour, each going to its category page, so readers can go straight to what they like. Part of the Byline kit; match the topics to your categories.",
 "topics, categories, sections, browse, byline",
 sec("Topics", cols([col(h("Read by topic", 2, "xx-large"), "30%"),
   col(row([p(f'<a href="/category/{s}/">{T(t)}</a>', "x-large", None, None, None, {"lineHeight": "1.1"}, True) for t, s in BTOPICS], "left", "large"))], "x-large", "wide", None),
   "section-tint", ("x-large", "x-large", None, None)))

kit("byline-numbers", BK, "Byline numbers: the publication in figures",
 "Four numbers that count up as they scroll into view: readers, stories, routes walked and years. Needs the AnyPress Blocks plugin. Part of the Byline kit; use real, current figures.",
 "numbers, statistics, readers, proof, counter, byline",
 sec("Numbers", N([sep(), grid([stackg([counter(n, sfx, "", "xxx-large", BSERIF, d).replace('"fontWeight":"900"', '"fontWeight":"800"'), bcaps(lbl)], "small") for n, sfx, d, lbl in
     [(18000, "", 0, "readers every week"), (340, "", 0, "stories published"), (52, "", 0, "routes walked and checked"), (9, "", 0, "years with no adverts")]], 4, "12rem", "large"), sep()]),
   pad=("x-large", "x-large", None, None)))

kit("byline-letters", BK, "Byline letters: what readers say, in a carousel",
 "Letters from readers in a carousel, three at a time on a computer and one on a phone, each with the reader's name and where they read from. Needs the AnyPress Blocks plugin. Part of the Byline kit; use real letters, with permission.",
 "letters, readers, testimonials, reviews, carousel, byline",
 sec("Letters", N([bhead("Letters", "From our readers", ("All letters", "/readers/")),
                   carousel([bletter(*r) for r in BLETTERS], 3, "Letters from readers")]), "section-tint"))

kit("byline-route-month", BK, "Byline route of the month: one walk with a map",
 "One route guide picked out: a photo, the distance, climb and time, a line about it and a link to the full guide, beside a map of the start. Needs the AnyPress Blocks plugin for the map. Part of the Byline kit; change it every month.",
 "route, featured, walk, trail, map, guide, byline",
 sec("Route of the month", cols([
   col(N([bcaps("Route of the month", "primary"), h("Hyalite Lake", 2, "xx-large"),
          p("Eleven waterfalls on the way up to a lake under Hyalite Peak. Go early on a weekday in September, when the crowds have gone and the willows have turned.", "medium"),
          bfact("Distance", "11 miles"), bfact("Climb", "1,800 ft"), bfact("Time", "5 to 6 hours"),
          btns([("Read the route", None, "/routes/hyalite-lake/"), ("All routes", "outline", "/routes/")])]), "40%"),
   col(mapb("Hyalite Lake trailhead, Gallatin National Forest, MT", 45.4383, -110.9603, 11, "4/3"))], "xx-large", "wide", "center")))

kit("byline-faq-open", BK, "Byline questions: answers that open and close",
 "The questions readers ask first, about subscriptions, walks and writing for the publication, as answers that open and close beside a heading and a link to all questions. Part of the Byline kit; answer the real questions.",
 "faq, questions, subscribe, newsletter, accordion, byline",
 sec("Questions", cols([
   col(N([bcaps("Before you write in", "primary"), h("Good to know", 2, "xx-large"), p("Something else? Call the office or send us a note.", None, "secondary"), btns([("All questions", "outline", "/faq/")])]), "36%"),
   col(accordion([
     ("Is the email edition really free?", "Yes. One story every Thursday, free for good. The print edition and the archive are for subscribers."),
     ("When does the print edition come out?", "Four times a year, at the start of each season. Subscribers get it first."),
     ("Can I cancel my subscription?", "Any time, from the link in any email. We'll refund the issues you haven't had."),
     ("Do I need to be fit for a guided walk?", "Each walk says how far and how steep. The map and compass day and the cooking walk suit almost anyone."),
     ("Can I write for Field Notes?", "Yes. Send us an idea, not a finished piece. We pay for every story we publish.")]))], "xx-large", "wide", "top")))

kit("byline-signup", BK, "Byline signup: the free weekly email",
 "A band asking readers to get one story a week by email, with the signup form beside it. Part of the Byline kit; sits above the footer on every page.",
 "newsletter, signup, email, subscribe, byline",
 sec("Signup", cols([
   col(N([h("One story a week, free", 2, "xx-large"), p("The best of Field Notes by email every Thursday. No adverts, and you can leave any time.", None, "secondary")]), "55%", valign="center"),
   col(form("newsletter", "See subscriptions", BSUB), valign="center")], "x-large", "wide", "center"), "section-tint", ("x-large", "x-large", None, None)))

BPOP = popup("offer", N([
    img("placeholder-wide.svg", "A lake below the mountains at first light", "16/9"),
    grp(N([bcaps("Free, every Thursday", "primary"), h("One good story a week", 2, "xx-large"),
           p("Leave your email and get our best story each Thursday, plus a free route guide to start."),
           form("offer", "See subscriptions", BSUB)]), None, (None, None, "large", "large"), "small", {"type": "default"})]),
    label="One good story a week")
kit("byline-popup", BK, "Byline popup: the free weekly email",
 "A popup that opens five seconds into a first visit with a photo, the free weekly email and one field for an email address; it closes with its button, Escape or a click outside and stays closed for two weeks. Needs the AnyPress Blocks plugin. Part of the Byline kit; put it in the footer to show it on every page.",
 "popup, newsletter, email, subscribe, modal, byline", BPOP)

BFOOT = grp(N([
    BODIES["byline-signup"],
    grp(N([cols([
        col(N([dyn("site-title", {"level": 0, "fontSize": "x-large", "fontFamily": BSERIF, "style": {"typography": {"lineHeight": "1"}}}),
               p("Walking, eating and sleeping outdoors. Independent, reader-funded, no adverts.", None, "main-accent"),
               p(f'<a href="{BTL}">' + T(BPH) + '</a>', "x-large", None, None, BSERIF, None, raw=True, bind="phone_linked"),
               social(["instagram", "youtube", "pinterest"])]), "34%"),
        col(flinks("Read", [("Stories", "/stories/")] + [(t, f"/category/{s}/") for t, s in BTOPICS[:4]] + [("Routes", "/routes/")])),
        col(flinks("Field Notes", [("Walks", "/walks/"), ("Subscribe", BSUB), ("About", "/about/"), ("Letters", "/readers/"), ("Write for us", "/write-for-us/"), ("Questions", "/faq/"), ("Contact", "/contact/")])),
        col(N([h("The office", 3, "medium"), p(BADDR, None, "main-accent", bind="address"), p(BHOURS, None, "main-accent", bind="hours"),
               btns([("Subscribe", None, BSUB)])]))], "large", "wide", "top"),
        sep(),
        row([p("© Field Notes. Independent and reader-funded.", "small", "main-accent"),
             p('<a href="/privacy-policy/">' + T("Privacy") + '</a> · <a href="/write-for-us/">' + T("Write for us") + '</a>', "small", "main-accent", None, None, None, raw=True)], gap="small")]),
        "section-dark", ("x-large", "large", None, None), "large", {"type": "constrained", "contentSize": "80rem"}, align="full", name="Footer columns"),
    BPOP,
]), None, None, "0", {"type": "default"}, align="full", name="Footer")
write("byline-footer", "Byline footer: the weekly email, links and the newsletter popup",
 "A site footer for a blog, magazine or newsletter: a band for the free weekly email, then the phone number, reading and publication links and the office address on dark, and the newsletter popup (needs the AnyPress Blocks plugin). Part of the Byline kit; choose it for the footer in the Site Editor.",
 "footer", "footer, links, newsletter, subscribe, phone, popup, magazine, byline", BFOOT, "core/template-part/footer")

kit("byline-about", BK, "Byline about: who writes it, and how to subscribe",
 "A short note from the writer beside a small portrait, with a link to subscribe: who they are, what they write and how often. Part of the Byline kit.",
 "about, author, writer, newsletter, subscribe, byline",
 sec("About", cols([col(img("placeholder-square.svg", "Portrait of the writer outdoors", "1"), "25%"),
   col(N([h("Written by Hanna Berg", 2, "xx-large"), p("I've walked across six countries with a stove and a notebook. Field Notes is what I learned: where to go, what to eat, what to carry and what to leave at home.", "large"),
          p("One story a week, by email. Free, and no adverts.", None, "secondary"), btns([("Subscribe", None, BSUB), ("About Field Notes", "outline", "/about/")])]), None, None, None, "center")], "x-large", "wide", "center"), content="60rem"))

def walk_card(name, slug, price, line):
    return stackg([zoom(img("placeholder-wide.svg", f"Walk: {name}", "4/3")), bcaps(price, "primary"), hlink(name, f"/walks/{slug}/", 3, "large"), p(line, None, "secondary")])

kit("byline-walks", BK, "Byline walks: every guided walk",
 "Every guided walk the publication runs as a card with a photo that opens full screen, its price, its name (linking to its own page) and a line about it. Part of the Byline kit; keep the walks current.",
 "walks, guided walks, events, trips, tours, byline",
 sec("Walks", N([bhead("Walk with us", "Guided walks from Bozeman", ("Book a walk", "/book-a-walk/")),
   grid([walk_card(*w) for w in BWALKS], 4, "14rem", "large")])))

kit("byline-walk-detail", BK, "Byline walk: the plan, what's included and photos",
 "The body of a page for one guided walk: what happens on the day, what's included, a card with the price, length, group size and dates, and four photos that open full screen. Part of the Byline kit; make one per walk.",
 "walk, guided walk, trip, event, details, gallery, byline",
 sec("Walk details", N([cols([
   col(N([h("Breakfast above the clouds", 2, "xx-large"),
          p("We meet at the Bridger Bowl lot at 4.30am and climb by headlamp to the ridge. As the sun comes up over the Crazy Mountains we stop for coffee and a hot breakfast, then walk the ridge north before dropping back down by mid-morning.", "medium"),
          h("What's included", 3, "large"),
          lst(["A guide who knows the ridge in the dark", "Coffee and a hot breakfast on top", "Headlamps and poles to borrow", "A printed route card to keep", "Photos from the morning, by email"])]), "58%"),
   col(bcard([bcaps("At a glance", "primary"), p("$95 a person", "x-large", None, None, BSERIF, {"lineHeight": "1.05"}), bfact("Length", "6 miles"), bfact("Climb", "2,100 ft"), bfact("Group", "Up to 8"), bfact("When", "Saturdays, June to October"),
              btns([("Book this walk", None, "/book-a-walk/"), ("Call", "outline", BTL)])]))], "xx-large", "wide", "top"),
   grid([zoom(img("placeholder-wide.svg", a, "4/3")) for a in ["This walk: the climb by headlamp", "This walk: first light on the ridge", "This walk: breakfast on top", "This walk: the way down"]], 2, "18rem", "medium")]), content="80rem"))

def route_card(name, slug, dist, climb, line):
    return stackg([img("placeholder-wide.svg", f"Route: {name}", "4/3"), bcaps(f"{dist} · {climb} climb", "primary"), hlink(name, f"/routes/{slug}/", 3, "x-large"), p(line, None, "secondary")])

kit("byline-routes", BK, "Byline routes: every route guide",
 "Every route guide as a card with a photo, the distance and climb, the route's name (linking to its own guide) and a line about it. Part of the Byline kit; add a card for each new guide.",
 "routes, trails, hikes, guides, walks, byline",
 sec("Routes", N([bhead("Route guides", "Walked, checked and written up"), grid([route_card(*r) for r in BROUTES], 4, "13rem", "large")])))

kit("byline-route-detail", BK, "Byline route guide: the facts, the way and a map",
 "The body of a page for one route: what it's like, the way step by step, a card with distance, climb, time, grade and where to start, and a map of the trailhead. Needs the AnyPress Blocks plugin for the map. Part of the Byline kit; make one per route.",
 "route guide, trail, hike, directions, map, byline",
 sec("Route guide", N([cols([
   col(N([h("Walking to Hyalite Lake", 2, "xx-large"),
          p("This is the walk we send visitors on first. The trail climbs gently up a canyon past eleven named waterfalls, then opens out at a lake under the peak. It's busy on summer weekends and quiet the rest of the time.", "medium"),
          h("The way", 3, "large"),
          lst(["Start at the Hyalite Lake trailhead, at the end of the reservoir road", "Follow the creek past Grotto and Arch Falls", "Keep right at the junction with the Emerald Lake trail", "Climb the last switchbacks to the lake, and come back the same way"])]), "58%"),
   col(bcard([bcaps("Route facts", "primary"), bfact("Distance", "11 miles"), bfact("Climb", "1,800 ft"), bfact("Time", "5 to 6 hours"), bfact("Grade", "Moderate"), bfact("Best", "July to October"),
              btns([("Walk it with us", None, "/walks/")])]))], "xx-large", "wide", "top"),
   mapb("Hyalite Lake trailhead, Gallatin National Forest, MT", 45.4383, -110.9603, 11, "21/9")]), content="80rem"))

kit("byline-team", BK, "Byline team: the people who write it",
 "The editor and contributors with a portrait, their role and a line about them. Part of the Byline kit; use the real team.",
 "team, writers, editors, contributors, people, byline",
 sec("Team", N([bhead("The people", "Three of us, and our contributors"), grid([stackg([img("placeholder-tall.svg", f"Writer: {n}", "4/5"), h(n, 3, "x-large"), bcaps(r, "primary"), p(d, None, "secondary")]) for n, r, d in BTEAM], 3, "14rem", "x-large")])))

kit("byline-plans", BK, "Byline subscriptions: free, print and supporter",
 "Three ways to read, as cards: the free weekly email, the print edition and a supporter subscription, each with its price, what's included and a button. Part of the Byline kit; state the real prices.",
 "subscribe, subscription, pricing, plans, membership, print, byline",
 sec("Subscriptions", N([bhead("Subscribe", "Three ways to read"),
   grid([bcard([bcaps(lab, "primary"), h(name, 3, "x-large"), p(price, "xx-large", None, None, BSERIF, {"lineHeight": "1"}), lst(items), btns([(btn, style, href)])], cardstyle) for lab, name, price, items, btn, style, href, cardstyle in [
     ("Free", "The weekly email", "$0", ["One story every Thursday", "A free route guide to start", "Leave any time"], "Read the free stories", "outline", "/stories/", "section-tint"),
     ("Most readers", "Print and email", "$48 a year", ["Four printed issues a year", "Every route guide and the archive", "10% off guided walks"], "Subscribe", None, "/contact/", "section-card"),
     ("Supporter", "Keep it independent", "$96 a year", ["Everything in print and email", "Your name in each issue", "A free guided walk each year"], "Become a supporter", "outline", "/contact/", "section-tint")]], 3, "16rem", "large")])))

kit("byline-jobs", BK, "Byline write for us: what we look for and the open roles",
 "How to pitch a story, what the publication pays, the open roles and the application. Part of the Byline kit; keep the roles current and put the site's application form in the named Form group.",
 "write for us, contributors, pitch, careers, jobs, apply, byline",
 sec("Write for us", N([
   bhead("Write for us", "Send us an idea, not a finished piece"),
   grid([stackg([h(t, 3, "large"), p(d, None, "secondary")]) for t, d in [
     ("What we want", "First-person stories about walking, cooking and sleeping outside, and the people who do it."),
     ("What we pay", "$0.50 a word for stories, and $250 for a checked route guide."),
     ("How it works", "Pitch in a few lines. If we like it, we'll agree a length and a date."),
     ("Who we want", "New voices especially. You don't need to have written before.")]], 4, "13rem"),
   '<!-- wp:spacer {"height":"var:preset|spacing|large"} -->\n<div style="height:var(--wp--preset--spacing--large)" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->',
   h("Open roles", 2, "xx-large"),
   N([grp(N([row([h(t, 3, "large"), bcaps(when, "primary")], valign="center"), p(d, None, "secondary"), btns([("Apply for this", None, "#apply")])]), "section-tint", PAD_CARD, "small", {"type": "default"}) for t, when, d in [
     ("Contributing writer", "Freelance, paid per story", "Two stories a season about the walking, people and places of Montana."),
     ("Walk leader", "Part time, $28 an hour", "Lead our guided walks on weekends. Wilderness first aid required.")]]),
   grp(N([h("Apply or pitch", 2, "xx-large"), p("Tell us a little about you, and the story or role you have in mind. We reply to everyone within two weeks."),
          form("apply", "Email the editor", "mailto:jobs@example.com")]), "section-card", PAD_CARD, "small", {"type": "default"}, anchor="apply")])))

kit("byline-book-form", BK, "Byline book a walk: the form and what to bring",
 "A form to book a guided walk, beside what happens next and what to bring. Part of the Byline kit; put the site's form in the named Form group.",
 "book, booking, walk, event, form, byline",
 sec("Book", cols([
   col(bcard([h("Book a walk", 2, "xx-large"), p("Choose a walk and a date. We'll confirm by email within a day, with the meeting point and a kit list."),
              form("quote", "Call " + BPH, BTL, "Rather talk first? Call the office.")], "section-card"), "58%"),
   col(N([h("What happens next", 3, "large"),
          lst(["We confirm by email within a day", "You pay when you confirm", "We send the meeting point the week before"]),
          h("What to bring", 3, "large"), lst(["Boots that are already worn in", "A waterproof and a warm layer", "Water, and lunch unless it's included"])]))],
   "xx-large", "wide", "top"), "section-tint"))

kit("byline-contact-full", BK, "Byline contact: phone, email, office and form",
 "A contact section for a publication: the phone number, email, address and hours beside the contact form, then a map. Needs the AnyPress Blocks plugin for the map. Part of the Byline kit.",
 "contact, phone, email, office, map, form, byline",
 sec("Contact us", N([cols([
   col(N([h("Write, call or visit", 2, "xx-large"), p(f'<a href="{BTL}">' + T(BPH) + '</a>', "xx-large", None, None, BSERIF, None, raw=True, bind="phone_linked"),
          p('<a href="mailto:hello@example.com">hello@example.com</a>', None, None, None, None, None, raw=True, bind="email_linked"),
          p(BADDR, None, bind="address"), p(BHOURS, None, "secondary", bind="hours")]), "40%"),
   col(bcard([h("Send a note", 3, "large"), form("contact", "Call " + BPH, BTL, "We reply within two working days.")]))], "xx-large", "wide", "top"),
   mapb(BADDR, BLAT, BLON, 15, "21/9")])))

# The home page: topics now link to their pages; numbers, letters, the route of the month with a map and questions join.
kit_page("kit-magazine", "Home page: Byline kit, blog and magazine",
 "A complete home page for a blog, magazine, newsletter or writer in the Byline kit: the name between rules, the newest post large, six more in a grid, topics, the publication's numbers counting up, the route of the month with a map, letters from readers in a carousel, questions and a note from the writer. Posts appear on their own. Apply the Byline style for the look it was designed with.",
 "home, blog, magazine, newsletter, writer, publication, kit, byline",
 ["byline-masthead", "byline-lead", "byline-latest", "byline-topics", "byline-numbers", "byline-route-month", "byline-letters", "byline-faq-open", "byline-about"])

# ---------------------------------------------------------------- pages
def byline_page(slug, title, desc, kw, parts):
    write(slug, title, desc, "anypress/pages", kw, N(parts), "core/post-content", " * Post Types: page\n")

byline_page("byline-page-services", "Walks page: Byline kit",
 "A Walks page for a publication that runs guided walks or events: a heading, every walk with a link to its own page, letters from readers and questions. Byline kit.",
 "walks, guided walks, events, trips, byline",
 [bpage_hero("Guided walks", "Small groups, local guides and the routes we write about. Every walk ends with something good to eat.", "Walks", [("Book a walk", None, "/book-a-walk/"), ("Route guides", "outline", "/routes/")]),
  BODIES["byline-walks"], BODIES["byline-letters"], BODIES["byline-faq-open"]])

byline_page("byline-page-service", "Walk page: Byline kit (one walk)",
 "A page for one guided walk: a heading and a wide photo, the plan for the day, what's included, the price and dates, photos that open full screen, more walks and questions. Byline kit; make one per walk.",
 "walk, guided walk, event, trip, byline",
 [bpage_hero("Sunrise ridge walk", "Bridger Ridge · 6 miles · $95 a person · Saturdays, June to October", "Walks / Bridger Ridge", [("Book this walk", None, "/book-a-walk/")], "This walk: the ridge at sunrise"),
  BODIES["byline-walk-detail"], BODIES["byline-walks"], BODIES["byline-faq-open"]])

byline_page("byline-page-about", "About page: Byline kit",
 "An About page for a publication: a heading, the story beside a photo, the numbers counting up, the people who write it, letters from readers and the office with a map. Byline kit.",
 "about, about us, publication, story, team, byline",
 [bpage_hero("About Field Notes", "An independent magazine about walking, eating and sleeping outdoors, paid for by its readers.", "About"),
  sec("Story", cols([
    col(N([h("A notebook, then a magazine", 2, "xx-large"),
           p("Hanna Berg started Field Notes in 2016 as an email to forty friends about the walks she'd done that week. Today it reaches eighteen thousand readers, comes out in print four times a year and still has no adverts.", "large"),
           p("We walk every route we publish, cook every recipe on a trail first and pay every writer. Readers' subscriptions pay for all of it.", "medium")]), "52%", valign="center"),
    col(img("placeholder-wide.svg", "The office: a notebook and coffee on a desk", "4/3"))], "xx-large", "wide", "center")),
  BODIES["byline-numbers"], BODIES["byline-team"], BODIES["byline-letters"], BODIES["byline-contact-full"]])

byline_page("byline-page-reviews", "Letters page: Byline kit",
 "A Letters page for a publication: a heading, letters from readers as cards, the numbers counting up and how to subscribe. Byline kit; use real letters, with permission.",
 "letters, readers, testimonials, reviews, byline",
 [bpage_hero("Letters", "Eighteen thousand readers, and some of them write back. Here's what they say.", "Readers", [("Subscribe", None, BSUB)]),
  sec("All letters", grid([bletter(*r) for r in BLETTERS + [
    ("We took the cabin weekend for our anniversary. June's breakfast was the best meal of the year.", "Ben and Ade K.", "Walked with us"),
    ("I keep the print issues on the shelf by the door, for planning.", "Carol W.", "Print subscriber"),
    ("Honest about how hard each route is. That matters.", "Luis M.", "Reader in Helena")]], 3, "18rem", "medium"), "section-tint"),
  BODIES["byline-numbers"], BODIES["byline-plans"]])

byline_page("byline-page-areas", "Routes page: Byline kit",
 "A Routes page for a publication: a heading, every route guide with a link to its own page, the route of the month with a map and the guided walks. Byline kit.",
 "routes, trails, hikes, guides, byline",
 [bpage_hero("Route guides", "Every route walked, checked and written up by us, twice, in two seasons.", "Routes"),
  BODIES["byline-routes"], BODIES["byline-route-month"], BODIES["byline-walks"]])

byline_page("byline-page-area", "Route page: Byline kit (one route)",
 "A page for one route guide: a heading and a wide photo, what the walk is like, the way step by step, the facts, a map of the trailhead and more routes. Byline kit; make one per route.",
 "route, trail, hike, guide, map, byline",
 [bpage_hero("Hyalite Lake", "11 miles · 1,800 ft climb · Moderate. Eleven waterfalls on the way up to a lake under Hyalite Peak.", "Routes / Gallatin Range", [("All routes", "outline", "/routes/")], "Routes: the lake under Hyalite Peak"),
  BODIES["byline-route-detail"], BODIES["byline-routes"], BODIES["byline-letters"]])

byline_page("byline-page-offers", "Subscribe page: Byline kit",
 "A Subscribe page for a publication: a heading, the free, print and supporter subscriptions, the numbers counting up, letters from readers and questions. Byline kit; state the real prices.",
 "subscribe, subscription, pricing, plans, print, byline",
 [bpage_hero("Subscribe", "Field Notes has no adverts. Readers pay for everything, so every subscription keeps it going.", "Subscribe"),
  BODIES["byline-plans"], BODIES["byline-numbers"], BODIES["byline-letters"], BODIES["byline-faq-open"]])

byline_page("byline-page-join", "Book a walk page: Byline kit",
 "A Book a walk page: a heading, the booking form beside what happens next and what to bring, the walks and letters from readers. Byline kit; put the site's form in the named Form group.",
 "book, booking, walk, event, form, byline",
 [bpage_hero("Book a walk", "Pick a walk and a date. Groups are small, so book early for summer weekends.", "Book"),
  BODIES["byline-book-form"], BODIES["byline-walks"], BODIES["byline-letters"]])

byline_page("byline-page-faq", "Questions page: Byline kit",
 "A Questions page for a publication: answers that open and close, grouped into reading, walks and writing, and how to subscribe. Byline kit; answer the real questions.",
 "faq, questions, answers, subscribe, walks, byline",
 [bpage_hero("Questions", "Reading, walking with us and writing for us, answered plainly.", "Questions"),
  sec("Questions", N([N([h(group_t, 2, "xx-large"), accordion(qs)]) for group_t, qs in [
    ("Reading", [
      ("Is the email edition really free?", "Yes. One story every Thursday, free for good."),
      ("Do you ship the print edition abroad?", "Yes, to most countries, for $12 a year more.")]),
    ("Walks", [
      ("What if the weather is bad?", "We move the walk or refund you in full. We never walk a ridge in a storm."),
      ("Can I bring my dog?", "On the cooking walk and the map day, yes. Not on the ridge or the cabin weekend.")]),
    ("Writing", [
      ("Do you take finished stories?", "Rarely. Send us a few lines about the idea first."),
      ("How fast do you pay?", "Within two weeks of publishing.")])]]),
    content="56rem"),
  BODIES["byline-plans"]])

byline_page("byline-page-careers", "Write for us page: Byline kit",
 "A Write for us page: a heading, what the publication looks for and pays, the open roles, the application form and questions. Byline kit; keep the roles current and put the site's form in the named Form group.",
 "write for us, contributors, pitch, careers, jobs, byline",
 [bpage_hero("Write for us", "We pay every writer, and we'd especially like to hear from people who haven't written before.", "Write for us", [("Pitch or apply", None, "#apply")]),
  BODIES["byline-jobs"], BODIES["byline-faq-open"]])

byline_page("byline-page-contact", "Contact page: Byline kit",
 "A Contact page for a publication: a heading, the phone number, email, address and hours beside the contact form, a map and questions. Byline kit; put the site's contact form in the named Form group.",
 "contact, phone, email, office, byline",
 [bpage_hero("Contact", "Write to the editor, call about a subscription or a walk, or visit the office on Main Street.", "Contact"),
  BODIES["byline-contact-full"], BODIES["byline-faq-open"]])

byline_page("byline-page-thanks", "Thank-you page: Byline kit",
 "The page visitors see after sending a form: thanks, what happens next and when, and links to keep reading. Byline kit; send every form here.",
 "thank you, thanks, confirmation, form sent, byline",
 [sec("Thanks", N([bcaps("Message sent", "primary"), h("Thank you. We'll be in touch soon.", 1, "xxx-large", None, None, {"lineHeight": "1.05"}),
    p("We reply within two working days. Check your email for a copy of what you sent.", "large", "secondary"),
    btns([("Back to the home page", None, "/"), ("Read the latest stories", "outline", "/stories/")])]), None, ("xxx-large", "xxx-large", None, None), "56rem"),
  BODIES["byline-letters"]])

print("byline ok")
