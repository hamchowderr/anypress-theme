# Circuit (0.6.0): a whole website for an electrician. Run by kits.py after kit_ridge.py, so every helper in kits.py,
# kits_more.py and kit_ridge.py (carousel, counter, mapb, popup, accordion, form, card, hide_on, link_p, zoom) is in scope.
#
# Bright and tidy where Ridge is loud: one grotesk in sentence case, deep electric blue with a yellow spark, rounded
# cards and pill buttons, photos with soft corners. Pages link to each other by slug: /services/ and one page per
# service under it, /about/, /reviews/, /service-areas/ and one page per town under it, /special-offers/,
# /book-a-visit/, /faq/, /careers/, /blog/, /contact/, /thank-you/. Forms are named groups, as in Ridge.

C = "anypress/kit-electrical"
CF = "schibsted-grotesk"
CPHONE = "555 0187"
CTEL = "tel:5550187"
BOOK = "/book-a-visit/"

# Circuit: electricians. A clean service van: deep electric blue, a yellow spark, one grotesk, pill buttons.
variation("kit-circuit", "Circuit (electricians)", PALS["circuit"], "instrument-sans", CF, "700", "-0.03em", "1.05",
    button("var:preset|border-radius|full", "instrument-sans", "600"),
    blocks={**site_title(CF, "800", None, "-0.03em"), "core/image": {"border": {"radius": "var:preset|border-radius|lg"}}})

EYEBROW_T = {"textTransform": "uppercase", "letterSpacing": "0.12em", "fontWeight": "700"}
def eyebrow(text, color="primary"):
    return p(text, "x-small", color, None, None, EYEBROW_T)

def cimg(alt, ratio="4/3", file="placeholder-wide.svg"):
    return img(file, alt, ratio, "lg")

def ccard(inner, style="section-card", pad=PAD_CARD):
    return grp(inner, style, pad, "small", {"type": "default"}, radius="lg")

def tel_link(size="xx-large", text=CPHONE):
    return p(f'<a href="{CTEL}">' + T(text) + '</a>', size, None, None, CF, {"fontWeight": "800", "lineHeight": "1"}, raw=True, bind="phone_linked" if text == CPHONE else None)

def c_call_buttons():
    """The header's buttons: Book a visit and the number on tablets and computers, just "Call" on phones."""
    book = f'<!-- wp:button {j({"metadata": {"blockVisibility": {"viewport": {"mobile": False}}}})} -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{BOOK}">{T("Book a visit")}</a></div>\n<!-- /wp:button -->'
    call = f'<!-- wp:button {j({"className": "is-style-outline", "metadata": {"blockVisibility": {"viewport": {"mobile": False}}, "bindings": button_bindings("phone")}})} -->\n<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="{CTEL}">{T(CPHONE)}</a></div>\n<!-- /wp:button -->'
    short = f'<!-- wp:button {j({"metadata": {"blockVisibility": {"viewport": {"tablet": False, "desktop": False}}, "bindings": button_bindings("phone_link")}})} -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{CTEL}">{T("Call")}</a></div>\n<!-- /wp:button -->'
    return '<!-- wp:buttons {"layout":{"type":"flex","flexWrap":"nowrap"}} -->\n<div class="wp-block-buttons">' + N([call, book, short]) + '</div>\n<!-- /wp:buttons -->'

def checks(items, color="primary"):
    """Short promises with a tick, in a row that wraps."""
    return row([p('<strong>✓</strong> ' + T(t), None, None, None, None, {"fontWeight": "600"}, raw=True) for t in items], "left", "large")

def csec(name, inner, style=None, pad=("xx-large", "xx-large", None, None), content="80rem"):
    return sec(name, inner, style, pad, content)

def head_row(eb, title, link=None, size="xx-large"):
    left = stackg([eyebrow(eb), h(title, 2, size)])
    return row([left, btns([(link[0], "outline", link[1])])] if link else [left], valign="bottom")

# ---------------------------------------------------------------- content
CSERVICES = [
    ("Panel upgrades", "panel-upgrades", "Old fuse boxes and full panels replaced with modern breakers, permits and inspection included.", "From $1,850", "A breaker panel with neatly labelled switches"),
    ("EV chargers", "ev-chargers", "Level 2 home chargers fitted in a day, on their own circuit, with the rebate paperwork done for you.", "From $950", "Rows of breakers in an electrical distribution board"),
    ("Lighting", "lighting", "Recessed, pendant, under-cabinet and outdoor lighting, planned with you and fitted cleanly.", "From $180", "A modern black pendant light glowing over a room"),
    ("Rewiring", "rewiring", "Knob-and-tube and aluminium wiring replaced room by room, with the walls patched before we leave.", "Free quote", "Exposed wires and a bare bulb in an unfinished room"),
    ("Repairs and fault finding", "repairs", "Tripping breakers, dead outlets and flickering lights traced to the cause and fixed the same day.", "From $129", "A screwdriver on a wooden workbench"),
    ("Generators and surge protection", "generators", "Standby generators, transfer switches and whole-home surge protection, so a storm doesn't stop the house.", "From $395", "A row of power outlets on a white panel with indicator lights"),
]
CTOWNS = [("Columbus", "columbus", 39.9612, -82.9988), ("Westerville", "westerville", 40.1262, -82.9291), ("Dublin", "dublin", 40.0992, -83.1141),
          ("Worthington", "worthington", 40.0931, -83.0180), ("Hilliard", "hilliard", 40.0334, -83.1582), ("Grove City", "grove-city", 39.8815, -83.0930),
          ("Gahanna", "gahanna", 40.0192, -82.8793), ("Upper Arlington", "upper-arlington", 39.9945, -83.0624)]
CREVIEWS = [
    ("Our breakers kept tripping for months. Ana found a failing outlet behind the fridge in twenty minutes and fixed it on the spot.", "Megan P.", "Westerville"),
    ("They fitted our EV charger in a morning, dealt with the permit and even filled in the utility rebate form.", "Raj D.", "Dublin"),
    ("Clear price before they started, boots off at the door, and the new lights look exactly like the plan.", "Kelly O.", "Worthington"),
    ("Rewired a 1940s house without wrecking it. The walls were patched so well you can't tell.", "Tom B.", "Upper Arlington"),
    ("Power went out in a storm on a Saturday. They were here within two hours and had us back on before dark.", "Lucia M.", "Hilliard"),
    ("Honest advice: they told us our panel had years left in it and saved us two thousand dollars.", "Dan S.", "Gahanna"),
]

def csvc_card(name, slug, text, price, alt):
    return ccard(N([cimg(alt, "3/2"), h(name, 3, "large"), p(text, None, "secondary"),
                    row([p(price, None, None, None, None, {"fontWeight": "700"}), link_p("Learn more →", f"/services/{slug}/", None, {"fontWeight": "700"})], valign="center")]),
                 "section-card", ("medium", "medium", "medium", "medium"))

def creview_card(text, name, town, size="medium"):
    return ccard(N([p("★★★★★", "medium", "primary"), p("“" + text + "”", size), p(f"{name}, {town}", "small", "secondary", None, None, {"fontWeight": "700"})]), "section-tint")

def cpage_hero(title, text, crumb=None, buttons=None, alt=None):
    words = N(([eyebrow(crumb, "primary-alt")] if crumb else []) + [h(title, 1, "xxx-large"), p(text, "medium")] + ([btns(buttons)] if buttons else []))
    if not alt:
        return sec("Page hero", words, "section-brand", ("xx-large", "x-large", None, None), "80rem")
    return sec("Page hero", cols([col(words, "58%", valign="center"), col(cimg(alt, "4/3"))], "x-large", "wide", "center"), "section-brand", ("xx-large", "x-large", None, None), "80rem")

def cinitials(name, style):
    letters = "".join(w[0] for w in name.split()[:2])
    return grp(p(letters, "xxx-large", None, "center", CF, {"fontWeight": "800", "lineHeight": "1"}), style, ("x-large", "x-large", None, None), layout={"type": "default"}, radius="lg")

# ---------------------------------------------------------------- sections
kit("circuit-topbar", C, "Circuit top bar: same-day service and the phone number",
 "A thin dark bar above the header with the business's promise, the opening hours and the phone number. Part of the Circuit kit (electricians); use the owner's real number.",
 "top bar, phone, hours, announcement, header, electrician, circuit",
 grp(row([p(T("Same-day service across Columbus") + ' · ' + T("Licensed and insured"), "small", None, None, None, None, raw=True),
          hide_on(p(T("Mon to Sat, 7am to 7pm · Emergencies 24/7:") + f' <a href="{CTEL}">' + T(CPHONE) + '</a>', "small", None, None, None, None, raw=True), "mobile")], gap="small"),
     "section-dark", ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Top bar"))

CHEADER = grp(N([
    BODIES["circuit-topbar"],
    grp(row([
        row([dyn("site-logo", {"width": 44, "shouldSyncIcon": True}), dyn("site-title", {"level": 0, "fontSize": "medium", "style": {"typography": {"lineHeight": "1"}}})], "left", "small", False, "center"),
        row([dyn("navigation", {"overlayMenu": "mobile", "layout": {"type": "flex", "justifyContent": "right"}, "style": {"typography": {"fontWeight": "600"}}}),
             c_call_buttons()], "right", "medium", False, "center")], "space-between", "medium", False, "center"),
        None, ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Main bar").replace(
        '<!-- wp:group {', '<!-- wp:group {"backgroundColor":"base",', 1).replace('class="wp-block-group alignfull', 'class="wp-block-group alignfull has-base-background-color has-background', 1),
]), "sticky", None, "0", {"type": "default"}, align="full", name="Header")
write("circuit-header", "Circuit header: menu, phone and a Book a visit button",
 "A site header for an electrician that stays at the top while visitors scroll: a dark bar with the promise and hours, then the logo, the menu (with dropdowns for services and areas), the phone number and a Book a visit button. Part of the Circuit kit; choose it for the header in the Site Editor.",
 "header", "header, menu, navigation, sticky, phone, book, electrician, circuit", CHEADER, "core/template-part/header")

kit("circuit-hero", C, "Circuit hero: a promise over a photo of the work",
 "Opening section for an electrician: a full-width photo with a dark overlay, a short label, a clear promise, one sentence, Book a visit and Call buttons, and three ticks people look for (licensed, same day, guarantee). Part of the Circuit kit (electricians).",
 "hero, electrician, electrical, cover, photo, book, phone, circuit",
 cover(grp(N([eyebrow("Electricians in Columbus since 2009", "primary-alt"),
              h("Safe, tidy electrical work, done right the first time", 1, "xxx-large"),
              p("Licensed electricians for homes and small businesses: repairs, panel upgrades, EV chargers and lighting. Clear prices before we start.", "medium"),
              btns([("Book a visit", None, BOOK), ("Call " + CPHONE, "outline", CTEL, "phone")]),
              checks(["Licensed and insured", "Same-day repairs", "2-year guarantee"])]), None, None, "medium", {"type": "constrained", "contentSize": "52rem", "justifyContent": "left"}).replace(
              '<!-- wp:group {', '<!-- wp:group {"textColor":"base",', 1).replace('class="wp-block-group', 'class="wp-block-group has-base-color has-text-color', 1),
   "Hero", "placeholder-wide.svg", 70, "88vh", "center left", ("xx-large", "xx-large", "medium", "medium")))

kit("circuit-intro", C, "Circuit intro: who we are and four reasons to call",
 "An introduction for an electrician: a short statement of who they are, four reasons to choose them with one line each, and a photo of the team at work. Part of the Circuit kit; state only what the owner can back up.",
 "about, intro, why us, features, trust, electrician, circuit",
 csec("Intro", cols([
   col(N([eyebrow("About Brightline"), h("A team of licensed electricians who turn up, explain, and leave the place spotless", 2, "xx-large"),
          grid([stackg([h(t, 3, "medium"), p(d, None, "secondary")]) for t, d in [
            ("On time, or the call-out is free", "We give a two-hour window and text when we're on the way."),
            ("Licensed and insured", "Every electrician is state-licensed, background-checked and ours."),
            ("Prices before we start", "A fixed price for the job, in writing. No surprises on the bill."),
            ("Guaranteed for two years", "Parts and labour, on every job we do.")]], 2, "14rem", "large"),
          btns([("More about us", "outline", "/about/")])]), "56%", valign="center"),
   col(cimg("An electrician in a hard hat at work on a street", "4/5", "placeholder-tall.svg"))], "xx-large", "wide", "center")))

kit("circuit-service-cards", C, "Circuit services: six cards with photos and prices",
 "Every service as a card with a rounded photo, one line about it, a starting price and a link to its own page, three across. Part of the Circuit kit; each link goes to /services/<service>/.",
 "services, cards, prices, photos, links, electrician, circuit",
 csec("Services", N([head_row("What we do", "Electrical work for homes and small businesses", ("All services", "/services/")),
                     grid([csvc_card(*s) for s in CSERVICES], 3, "18rem")]), "section-tint"))

kit("circuit-numbers", C, "Circuit numbers: four figures that count up",
 "Four numbers that count up as they scroll into view (years, jobs, rating, arrival time) on the brand colour. Needs the AnyPress Blocks plugin. Part of the Circuit kit; use the owner's real figures.",
 "numbers, statistics, counter, proof, electrician, circuit",
 csec("Numbers", grid([stackg([counter(n, suf, "", "xx-large", CF, d), p(lbl, "medium")]) for n, suf, d, lbl in
     [(17, " yrs", 0, "keeping Columbus switched on"), (9200, "+", 0, "jobs finished"), (4.9, "★", 1, "from 860 reviews"), (2, " hrs", 0, "to an emergency, on average")]], 4, "12rem"),
     "section-brand", ("x-large", "x-large", None, None)))

kit("circuit-why", C, "Circuit why us: four promises on cards",
 "Why customers choose this electrician: a heading and sentence beside four rounded cards (fast response, upfront prices, licensed team, clean work). Part of the Circuit kit.",
 "why us, promises, benefits, trust, electrician, circuit",
 csec("Why us", cols([
   col(N([eyebrow("Why Brightline"), h("Not just electricians. Problem solvers.", 2, "xx-large"),
          p("Most calls start with a mystery: a breaker that won't stay on, lights that flicker, an outlet that's warm. We find the cause, fix it, and tell you how to stop it happening again.", "medium", "secondary"),
          btns([("Book a visit", None, BOOK)])]), "40%", valign="center"),
   col(grid([ccard(N([p(icon, "x-large", "primary"), h(t, 3, "large"), p(d, None, "secondary")]), "section-card") for icon, t, d in [
     ("↯", "Fast response", "Same-day repairs most weekdays, and an electrician on call every night."),
     ("$", "Upfront prices", "A fixed price in writing before we start. It doesn't change."),
     ("✓", "Licensed team", "State-licensed electricians, employed by us. No subcontractors."),
     ("◎", "Clean, careful work", "Shoe covers, dust sheets, and every bit of mess taken away.")]], 2, "14rem", "medium"))], "xx-large", "wide", "center"), "section-tint"))

kit("circuit-steps", C, "Circuit steps: how a visit works",
 "Three numbered steps from booking to finished job, each in a rounded card, so visitors know what happens next. Part of the Circuit kit.",
 "how it works, steps, process, booking, electrician, circuit",
 csec("How it works", N([eyebrow("How it works"), h("Three steps to a job well done", 2, "xx-large"),
   grid([ccard(N([p(n, "xx-large", "primary", None, CF, {"fontWeight": "800"}), h(t, 3, "large"), p(d, None, "secondary")]), "section-tint") for n, t, d in [
     ("1", "Book a visit", "Online or by phone. Tell us what's wrong and we'll give you a two-hour window."),
     ("2", "We find the cause", "Your electrician tests, explains what they found and gives you a fixed price."),
     ("3", "Fixed and guaranteed", "We fix it, test it, clean up and guarantee the work for two years.")]], 3, "16rem", "medium")])))

kit("circuit-reviews-carousel", C, "Circuit reviews: a carousel of customer reviews",
 "Customer reviews in a carousel on rounded cards, three at a time on a computer and one on a phone, with stars, the customer's name and town. Needs the AnyPress Blocks plugin. Part of the Circuit kit; use real reviews.",
 "reviews, testimonials, carousel, slider, stars, customers, electrician, circuit",
 csec("Reviews", N([head_row("Reviews", "Trusted by 860 homeowners and businesses", ("All reviews", "/reviews/")),
                    carousel([creview_card(*r) for r in CREVIEWS], 3, "Customer reviews")])))

kit("circuit-jobs", C, "Circuit recent work: photos in a carousel",
 "Photos of recent jobs in a carousel, each opening full screen when clicked, with a caption of what was done and where. Needs the AnyPress Blocks plugin. Part of the Circuit kit; use the owner's own photos.",
 "projects, jobs, gallery, photos, carousel, portfolio, lightbox, electrician, circuit",
 csec("Recent work", N([eyebrow("Recent work"), h("Fresh from the van", 2, "xx-large"), carousel([stackg([zoom(cimg(alt, "3/4", "placeholder-tall.svg")), p(cap, None, "secondary")]) for alt, cap in [
    ("A modern ceiling light fitting with spotlights", "Kitchen spotlights and a new fitting, Dublin"),
    ("Globe pendant lights glowing over a room", "Pendants over an island, Worthington"),
    ("Recessed lights in a dark ceiling around a pendant", "Recessed lighting throughout, Upper Arlington"),
    ("Solar panels on the roof of a modern building", "Solar tie-in and a new panel, Hilliard"),
    ("A glowing LED wall light in a wooden frame", "LED wall lights in a hallway, Gahanna")]], 3, "Recent work", 6)]), "section-tint"))

kit("circuit-team", C, "Circuit team: the electricians who come to your door",
 "The team as rounded cards with each person's initials on a coloured panel, their name and role, so customers know who is coming. Part of the Circuit kit; swap the initials for a photo of each person when there is one.",
 "team, staff, people, electricians, about, circuit",
 csec("Team", N([eyebrow("Our team"), h("Meet the people who come to your door", 2, "xx-large"),
   grid([ccard(N([cinitials(n, st), h(n, 3, "large"), p(r, None, "secondary")]), "section-tint", ("medium", "medium", "medium", "medium")) for n, r, st in [
     ("Ana Ruiz", "Owner and master electrician", "section-brand"),
     ("Marcus Hill", "Senior electrician, 14 years", "section-dark"),
     ("Jade Okafor", "Electrician, EV and solar", "section-second-brand"),
     ("Ben Carter", "Apprentice, year three", "section-brand-soft")]], 4, "13rem", "medium")])))

kit("circuit-cta", C, "Circuit call to action: book today, on yellow",
 "A bright band that asks visitors to book: a big question, one sentence, Book a visit and Call buttons, beside a photo. Part of the Circuit kit; place it between sections or before the footer.",
 "call to action, book, phone, banner, electrician, circuit",
 csec("Book", cols([
   col(N([h("Need an electrician today?", 2, "xxx-large"), p("Book a two-hour window online, or call and talk to a real person. Same-day repairs most weekdays.", "medium"),
          btns([("Book a visit", None, BOOK), ("Call " + CPHONE, "outline", CTEL, "phone")])]), "55%", valign="center"),
   col(cimg("A white light fitting with a round bulb on a brick wall", "4/3"))], "x-large", "wide", "center"), "section-second-brand", ("x-large", "x-large", None, None)))

kit("circuit-faq", C, "Circuit questions: answers that open and close",
 "The questions people ask before booking an electrician, as answers that open and close, beside a heading and a button to all questions. Part of the Circuit kit; answer with the owner's real prices and policies.",
 "faq, questions, answers, accordion, prices, electrician, circuit",
 csec("Questions", cols([
   col(N([eyebrow("Questions"), h("Got questions? Here are straight answers.", 2, "xx-large"), btns([("All questions", "outline", "/faq/")])]), "36%"),
   col(accordion([
     ("Do you charge a call-out fee?", "A flat $79 diagnostic visit, which comes off the bill if you go ahead with the repair."),
     ("Do you do 24/7 emergencies?", "Yes. For loss of power, burning smells, sparking or water near electrics, call any time, day or night."),
     ("How much does a typical repair cost?", "Most outlet, switch and breaker repairs are $129 to $350. We give you the price before we start."),
     ("Are your electricians licensed?", "Yes. Every electrician is state-licensed, insured and employed by us. License EL-47215."),
     ("How soon can you come?", "Same day for most repairs booked before noon, and the next day for everything else.")]))], "x-large", "wide", "top")))

kit("circuit-areas-map", C, "Circuit areas: a map and the towns served",
 "Where the electrician works: a map of the area beside every town served as a link to its own page, and a line on travel outside the area. Needs the AnyPress Blocks plugin for the map. Part of the Circuit kit.",
 "service areas, map, towns, locations, coverage, electrician, circuit",
 csec("Areas served", cols([
   col(N([eyebrow("Service areas"), h("Across Columbus and the suburbs", 2, "xx-large"), p("No travel charge anywhere inside the I-270 loop and the towns around it. Further out? Call and ask.", "medium", "secondary"),
          grid([link_p(t, f"/service-areas/{s}/", "medium", {"fontWeight": "600"}) for t, s, *_ in CTOWNS], 2, "10rem", "small")]), "40%"),
   col(mapb("Columbus, Ohio", 39.9612, -82.9988, 10, "4/3", "lg"))], "x-large", "wide", "top")))

def cflinks(title, items):
    lis = "\n\n".join(f'<!-- wp:list-item -->\n<li><a href="{href}">{T(label)}</a></li>\n<!-- /wp:list-item -->' for label, href in items)
    return N([h(title, 3, "medium"), '<!-- wp:list {"className":"is-style-no-bullets"} -->\n<ul class="wp-block-list is-style-no-bullets">' + lis + '</ul>\n<!-- /wp:list -->'])

kit("circuit-signup", C, "Circuit signup: the safety checklist by email",
 "A band asking visitors to join the email list for a free home electrical safety checklist and seasonal offers, with the signup form beside it. Part of the Circuit kit; sits above the footer on every page.",
 "newsletter, signup, email, offers, subscribe, electrician, circuit",
 csec("Signup", cols([
   col(N([h("Get our free home safety checklist", 2, "xx-large"), p("Ten things to check in ten minutes, plus seasonal offers. One email a month, at most.", "medium")]), "55%", valign="center"),
   col(form("newsletter", "Send me the checklist", "/special-offers/"), valign="center")], "large", "wide", "center"), "section-tint", ("x-large", "x-large", None, None)))

CPOPUP = popup("offer", N([
    cimg("Globe pendant lights with a soft yellow glow", "16/9"),
    grp(N([eyebrow("New customers"), h("$40 off your first visit", 2, "xx-large"),
           p("Leave your email and we'll send the code. One email, no calls."),
           form("offer", "See this month's offers", "/special-offers/")]), None, (None, None, "large", "large"), "small", {"type": "default"})]),
    label="Offer for new customers")
kit("circuit-popup", C, "Circuit popup: $40 off for new customers",
 "A popup that opens five seconds into a first visit with a photo, the offer and one field for an email address; it closes with its button, Escape or a click outside and stays closed for two weeks. Needs the AnyPress Blocks plugin. Part of the Circuit kit; put it in the footer to show it on every page.",
 "popup, offer, discount, newsletter, email, modal, electrician, circuit", CPOPUP)

CFOOTER = grp(N([
    BODIES["circuit-signup"],
    grp(N([cols([
        col(N([dyn("site-title", {"level": 0, "fontSize": "x-large"}),
               p("Licensed electricians for homes and small businesses in Columbus and the suburbs since 2009.", None, "main-accent"),
               tel_link("xx-large"),
               p('<a href="mailto:hello@example.com">hello@example.com</a>', None, None, None, None, None, raw=True, bind="email_linked"),
               social(["facebook", "instagram", "google"])]), "34%"),
        col(cflinks("Services", [(n, f"/services/{s}/") for n, s, *_ in CSERVICES])),
        col(cflinks("Company", [("About us", "/about/"), ("Reviews", "/reviews/"), ("Service areas", "/service-areas/"), ("Special offers", "/special-offers/"), ("Careers", "/careers/"), ("Blog", "/blog/"), ("Questions", "/faq/")])),
        col(N([h("Visit or call", 3, "medium"), p("880 King Avenue, Columbus", None, "main-accent", bind="address"), p("Mon to Sat, 7am to 7pm", None, "main-accent", bind="hours"), p("Emergencies 24/7", None, "main-accent"),
               btns([("Book a visit", None, BOOK)])]))], "large", "wide", "top"),
        sep(),
        row([p("© Brightline Electric. State electrical contractor license EL-47215.", "small", "main-accent"),
             p('<a href="/privacy-policy/">' + T("Privacy") + '</a> · <a href="/contact/">' + T("Contact") + '</a>', "small", "main-accent", None, None, None, raw=True)], gap="small")]),
        "section-dark", ("x-large", "large", None, None), "large", {"type": "constrained", "contentSize": "80rem"}, align="full", name="Footer columns"),
    CPOPUP,
]), None, None, "0", {"type": "default"}, align="full", name="Footer")
write("circuit-footer", "Circuit footer: safety checklist signup, links, phone and the offer popup",
 "A site footer for an electrician: a band for joining the email list, then the phone number, services, company pages, address and hours on dark, and the new-customer offer popup (needs the AnyPress Blocks plugin). Part of the Circuit kit; choose it for the footer in the Site Editor.",
 "footer", "footer, links, newsletter, signup, phone, address, hours, popup, electrician, circuit", CFOOTER, "core/template-part/footer")

kit("circuit-offers", C, "Circuit offers: three coupons",
 "Current offers as three rounded coupon cards with the saving in big type, what it covers and a button to claim it, then the small print. Part of the Circuit kit; keep the dates and terms current.",
 "offers, coupons, discounts, deals, specials, electrician, circuit",
 csec("Offers", N([grid([ccard(N([p(s, "xxx-large", None, None, CF, {"fontWeight": "800", "lineHeight": "1"}), h(t, 3, "large"), p(d), btns([("Claim this offer", None, BOOK)])]), st, PAD_CARD) for s, t, d, st in [
    ("$40 off", "Your first visit", "Any repair or install over $200. Mention the offer when you book.", "section-brand"),
    ("$99", "Home safety inspection", "A full check of your panel, outlets, smoke alarms and grounding. Normally $149.", "section-second-brand"),
    ("$200 off", "EV charger installs", "Level 2 charger fitted and tested, on top of any utility rebate.", "section-dark")]], 3, "16rem", "medium"),
    p("One offer per job. Not for emergency call-outs. Offers run to the end of the month and are renewed each month.", "small", "secondary")])))

kit("circuit-service-detail", C, "Circuit service: what's included and the price",
 "The body of one service page: what the service covers in plain words, a list of what's included, a photo, and a rounded price card with the starting price and buttons to book or call. Part of the Circuit kit.",
 "service, details, included, price, book, electrician, circuit",
 csec("Service details", cols([
   col(N([h("What's included", 2, "xx-large"),
          p("A home charger needs its own circuit, the right breaker and a panel that can take the load. We check all three before we quote, so the price is the price."),
          lst(["A load check of your panel and supply", "A dedicated 240-volt circuit and breaker", "Fitting and testing your charger, any brand", "The permit and inspection", "Help with your utility's rebate paperwork"], "medium"),
          cimg("Photo of the service: rows of breakers in an electrical distribution board", "16/9")]), "60%"),
   col(ccard(N([eyebrow("EV chargers"), p("From $950", "xxx-large", None, None, CF, {"fontWeight": "800", "lineHeight": "1"}),
               p("Most garage installs, with the charger supplied by you. Long cable runs or a panel upgrade are quoted first."),
               btns([("Book a visit", None, BOOK), ("Call " + CPHONE, "outline", CTEL, "phone")])]), "section-tint", PAD_CARD))], "x-large", "wide", "top")))

kit("circuit-careers", C, "Circuit careers: why work here and open jobs",
 "A careers section for an electrician: four reasons to join, then each open job on a rounded card with its pay and what it needs, and the application. Part of the Circuit kit; keep the jobs current.",
 "careers, jobs, hiring, vacancies, apprentice, work with us, electrician, circuit",
 csec("Careers", N([
   eyebrow("Careers"), h("Why electricians stay", 2, "xx-large"),
   grid([stackg([h(t, 3, "large"), p(d, None, "secondary")]) for t, d in [
     ("Top pay, paid weekly", "Above scale, overtime at time and a half, and a bonus for every five-star review."),
     ("Your own van", "A new, stocked van you take home, and the tools to do the job properly."),
     ("Evenings back", "Four ten-hour days on rotation, and on-call shared fairly."),
     ("Training paid for", "Apprentice to master license, with the school, exams and study time paid.")]], 4, "13rem"),
   '<!-- wp:spacer {"height":"var:preset|spacing|large"} -->\n<div style="height:var(--wp--preset--spacing--large)" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->',
   h("Open jobs", 2, "xx-large"),
   N([ccard(N([row([h(t, 3, "x-large"), p(pay, "medium", None, None, None, {"fontWeight": "700"})], valign="center"), p(d, None, "secondary"), btns([("Apply for this job", None, "#apply")])]), "section-tint") for t, pay, d in [
     ("Service electrician", "$34 to $46 an hour", "Journeyman license and three years of residential service work. Clean driving record."),
     ("EV and solar installer", "$32 to $42 an hour", "Charger and solar tie-in installs. We'll train you on the brands we fit."),
     ("Apprentice electrician", "$20 an hour to start", "No experience needed. Careful, reliable and keen to learn. We pay for school.")]]),
   grp(N([h("Apply", 2, "xx-large"), p("Send your name, phone, the job you want and a few lines about you. Ana replies to every application within two working days."),
          form("apply", "Email your application", "mailto:jobs@example.com")]), "section-card", PAD_CARD, "small", {"type": "default"}, anchor="apply", radius="lg")])))

kit("circuit-quote", C, "Circuit booking: the form and what happens next",
 "A booking section: the booking form on a rounded card on one side, and on the other what happens after sending it and what to do in an emergency. Part of the Circuit kit; put the site's booking form in the named Form group.",
 "book, booking, appointment, quote, form, request, electrician, circuit",
 csec("Booking", cols([
   col(ccard(N([h("Book a visit", 2, "xx-large"), p("Tell us what's wrong and pick a day. We'll call to confirm a two-hour window."),
                form("quote", "Call " + CPHONE, CTEL, "Prefer to talk? Call us instead.")]), "section-card", PAD_CARD), "58%"),
   col(N([h("What happens next", 3, "x-large"),
          lst(["We call or text within an hour, 7am to 7pm.", "You get a two-hour arrival window.", "Your electrician texts when they're on the way."], "medium"),
          ccard(N([h("Sparks, smoke or a burning smell?", 3, "large"), p("Don't book online. Switch off the main breaker if it's safe, then call us now."),
                   tel_link("xx-large")]), "section-second-brand")]))],
   "x-large", "wide", "top"), "section-tint"))

kit("circuit-contact", C, "Circuit contact: details, form and map",
 "A contact section for an electrician: phone, email, address and hours beside the contact form on a rounded card, then a map of the office with directions. Needs the AnyPress Blocks plugin for the map. Part of the Circuit kit.",
 "contact, phone, email, address, hours, map, form, electrician, circuit",
 csec("Contact", N([cols([
   col(N([eyebrow("Get in touch"), h("Call, write or drop by", 2, "xx-large"), tel_link("xxx-large"),
          p('<a href="mailto:hello@example.com">hello@example.com</a>', "medium", None, None, None, None, raw=True, bind="email_linked"),
          p("880 King Avenue, Columbus", "medium", bind="address"), p("Mon to Sat, 7am to 7pm. Emergencies 24/7.", None, "secondary")]), "42%"),
   col(ccard(N([h("Send a message", 3, "x-large"), form("contact", "Call " + CPHONE, CTEL, "We reply within two working hours.")]), "section-tint", PAD_CARD))], "x-large", "wide", "top"),
   mapb("880 King Avenue, Columbus, Ohio", 39.9937, -83.0219, 14, "21/9", "lg")])))

kit("circuit-news", C, "Circuit blog: the latest three posts",
 "The three latest blog posts as cards with a rounded photo, the title and the date, and a link to the blog. Part of the Circuit kit.",
 "blog, news, posts, tips, articles, latest, electrician, circuit",
 csec("Blog", N([head_row("From the blog", "Tips to keep your home safe", ("All posts", "/blog/")),
   query(3, 0, 3, N([dyn("post-featured-image", {"isLink": True, "aspectRatio": "3/2", "style": {"border": {"radius": "var:preset|border-radius|lg"}}}),
                     dyn("post-title", {"isLink": True, "level": 3, "fontSize": "large"}), dyn("post-date", {"fontSize": "small", "textColor": "secondary"})]), 41)])))

# ---------------------------------------------------------------- pages
def circuit_page(slug, title, desc, kw, parts):
    write(slug, title, desc, "anypress/pages", kw, N(parts), "core/post-content", " * Post Types: page\n")

kit_page("kit-home-electrical", "Home page: Circuit kit, electricians",
 "A complete home page for an electrician in the Circuit kit: a photo hero with the promise and booking buttons, who they are, services with photos and prices, numbers that count up, why customers choose them, how a visit works, reviews in a carousel, the team, a bright booking band, service areas with a map, common questions and the latest tips. Apply the Circuit style for the look it was designed with.",
 "home, electrician, electrical contractor, ev charger, lighting, trades, kit, circuit",
 ["circuit-hero", "circuit-intro", "circuit-service-cards", "circuit-numbers", "circuit-why", "circuit-steps", "circuit-reviews-carousel", "circuit-team", "circuit-cta", "circuit-areas-map", "circuit-faq", "circuit-news"])

circuit_page("circuit-page-services", "Services page: Circuit kit",
 "A Services page for an electrician: a page heading, every service as a card linking to its own page, how a visit works, why customers choose them, common questions and a booking band. Circuit kit.",
 "services, all services, prices, electrician, circuit",
 [cpage_hero("Electrical services", "Repairs, upgrades and new installs for homes and small businesses, at a fixed price agreed before we start.", "Services", [("Book a visit", None, BOOK), ("Call " + CPHONE, "outline", CTEL, "phone")]),
  BODIES["circuit-service-cards"], BODIES["circuit-steps"], BODIES["circuit-why"], BODIES["circuit-faq"], BODIES["circuit-cta"]])

circuit_page("circuit-page-service", "Service page: Circuit kit (one service)",
 "A page for one service, such as EV charger installation: a heading with a photo, what's included and the price, how a visit works, recent work, reviews, questions about this service and a booking band. Circuit kit; make one per service under Services.",
 "service page, ev charger, panel upgrade, lighting, single service, electrician, circuit",
 [cpage_hero("EV charger installation", "A Level 2 home charger on its own circuit, fitted in a day, with the permit and rebate paperwork done for you.", "Services / EV chargers", [("Book a visit", None, BOOK), ("Call " + CPHONE, "outline", CTEL, "phone")], "Photo of the service: a house with solar panels on the roof"),
  BODIES["circuit-service-detail"], BODIES["circuit-steps"], BODIES["circuit-jobs"], BODIES["circuit-reviews-carousel"],
  csec("Questions", cols([col(N([eyebrow("Questions"), h("About EV chargers", 2, "xx-large")]), "36%"), col(accordion([
    ("Do I need a panel upgrade?", "Often not. Most 200-amp panels have room for a 40-amp charger circuit. We check the load first and only suggest an upgrade if you need one."),
    ("How long does it take?", "Most garage installs take four to six hours. Longer runs to a driveway can take a day."),
    ("Which chargers do you fit?", "Any brand with a UL listing: Tesla, ChargePoint, Emporia, Wallbox and the rest."),
    ("Can you help with the rebate?", "Yes. We fill in the utility's form and send the inspection certificate they ask for.")]))], "x-large", "wide", "top")),
  BODIES["circuit-cta"]])

circuit_page("circuit-page-about", "About page: Circuit kit",
 "An About page for an electrician: a heading with a photo, the story of the business, numbers that count up, the team, why customers choose them, reviews and a booking band. Circuit kit.",
 "about, about us, story, team, history, family business, electrician, circuit",
 [cpage_hero("Bright ideas, safe wiring", "Ana Ruiz started Brightline in 2009 with one van and a rule: do it right, explain it plainly, and leave it clean.", "About us", None, "Construction workers standing in front of a big work truck"),
  csec("Story", cols([
    col(N([eyebrow("Our story"), h("From one van to a team of twelve", 2, "xx-large"),
           p("Ana spent ten years wiring hospitals and offices before starting on her own. Homeowners kept telling her the same thing: electricians turned up late, spoke in jargon and left a mess.", "large"),
           p("So Brightline does the opposite. We give you a window and keep to it, we show you what we found, and we put the price in writing before we pick up a tool."),
           p("Today we're twelve electricians and apprentices, every one employed and trained by us.")]), "55%", valign="center"),
    col(cimg("Two pendant lights with soft shades glowing over a room", "4/5", "placeholder-tall.svg"))], "x-large", "wide", "center")),
  BODIES["circuit-numbers"], BODIES["circuit-team"], BODIES["circuit-why"], BODIES["circuit-reviews-carousel"], BODIES["circuit-cta"]])

circuit_page("circuit-page-reviews", "Reviews page: Circuit kit",
 "A Reviews page for an electrician: the overall rating, the reviews as rounded cards with names and towns, numbers that count up and a booking band. Circuit kit; use real reviews and say where they come from.",
 "reviews, testimonials, ratings, customers, stars, electrician, circuit",
 [cpage_hero("4.9 stars from 860 reviews", "What customers say on Google and Facebook. We read every review, and reply to every one.", "Reviews", [("Leave a review", "outline", "/contact/")]),
  csec("All reviews", grid([creview_card(*r) for r in CREVIEWS + [
    ("Replaced every outlet in our kitchen with USB ones and added under-cabinet lights. Neat as anything.", "Sara L.", "Grove City"),
    ("They spotted scorched wiring in our attic during an inspection. Probably saved the house.", "Mike R.", "Columbus"),
    ("Booked online at 9am, fixed by 2pm. That simple.", "Hannah W.", "Westerville")]], 3, "18rem", "medium")),
  BODIES["circuit-numbers"], BODIES["circuit-cta"]])

circuit_page("circuit-page-areas", "Service areas page: Circuit kit",
 "A Service areas page for an electrician: a heading, a map with every town served as a link to its own page, a card for each town and a booking band. Circuit kit.",
 "service areas, locations, towns, map, coverage, electrician, circuit",
 [cpage_hero("Where we work", "Columbus and every suburb inside and around the I-270 loop, with no travel charge.", "Service areas"),
  BODIES["circuit-areas-map"],
  csec("Towns", grid([ccard(N([h(t, 3, "large"), p(f"Electrical repairs, upgrades, EV chargers and lighting in {t}.", None, "secondary"), link_p(f"Electrician in {t} →", f"/service-areas/{s}/", None, {"fontWeight": "700"})]), "section-card") for t, s, *_ in CTOWNS], 4, "13rem", "medium"), "section-tint"),
  BODIES["circuit-cta"]])

circuit_page("circuit-page-area", "Town page: Circuit kit (one service area)",
 "A page for one town served, such as Westerville: a heading, a few lines about working there with a map, the services, reviews and a booking band. Circuit kit; make one per main town under Service areas, with real local details.",
 "service area page, town, city, local, electrician near me, circuit",
 [cpage_hero("Electrician in Westerville", "Twenty minutes from our shop, so most Westerville repairs get a same-day visit.", "Service areas / Westerville", [("Book a visit", None, BOOK), ("Call " + CPHONE, "outline", CTEL, "phone")]),
  csec("Local", cols([
    col(N([h("Electrical work in Westerville", 2, "xx-large"),
           p("We've worked in Westerville since 2009, from the older homes near Uptown to the newer streets out east. Many houses here still have their original 1970s panels, so we fit a lot of upgrades and EV chargers."),
           lst(["Same-day repairs most weekdays", "No travel charge", "Panel checks for homes built before 1985"], "medium")]), "50%"),
    col(mapb("Westerville, Ohio", 40.1262, -82.9291, 13, "4/3", "lg"))], "x-large", "wide", "top")),
  BODIES["circuit-service-cards"], BODIES["circuit-reviews-carousel"], BODIES["circuit-cta"]])

circuit_page("circuit-page-offers", "Special offers page: Circuit kit",
 "A Special offers page for an electrician: a heading, the current offers as coupons with their terms and a booking band (the footer carries the email signup). Circuit kit; keep the offers current.",
 "offers, coupons, specials, deals, discounts, electrician, circuit",
 [cpage_hero("Special offers", "This month's savings. Mention the offer when you book and we'll take it off the bill.", "Special offers"),
  BODIES["circuit-offers"], BODIES["circuit-cta"]])

circuit_page("circuit-page-book", "Book a visit page: Circuit kit",
 "A Book a visit page for an electrician: a heading, the booking form with what happens next and the emergency number beside it, how a visit works and why customers choose them. Circuit kit; put the site's booking form in the named Form group.",
 "book, booking, appointment, quote, estimate, form, electrician, circuit",
 [cpage_hero("Book a visit", "Pick a day, tell us what's wrong, and we'll confirm a two-hour window.", "Book a visit"),
  BODIES["circuit-quote"], BODIES["circuit-steps"], BODIES["circuit-why"]])

circuit_page("circuit-page-faq", "Questions page: Circuit kit",
 "A Questions page for an electrician: answers that open and close, grouped into prices, booking, safety and guarantees, and a booking band. Circuit kit; answer with the owner's real policies.",
 "faq, questions, answers, help, prices, safety, electrician, circuit",
 [cpage_hero("Questions and answers", "Straight answers about prices, booking, safety and our guarantee.", "Questions"),
  csec("Questions", N([N([h(group_t, 2, "xx-large"), accordion(qs)]) for group_t, qs in [
    ("Prices and paying", [
      ("Do you charge a call-out fee?", "A flat $79 diagnostic visit, which comes off the bill if you go ahead with the repair."),
      ("Do you charge by the hour?", "No, by the job. You get a fixed price in writing before we start."),
      ("How can I pay?", "Card, bank transfer or check when the job is done. For jobs over $2,500 we take a 25% deposit."),
      ("Do you offer finance?", "Yes, on panel upgrades, generators and rewiring over $1,500: 12 months interest-free, subject to approval.")]),
    ("Booking and arrival", [
      ("How soon can you come?", "Same day for most repairs booked before noon, and the next day for everything else."),
      ("Can I book online?", "Yes, on the Book a visit page. We call or text within an hour to confirm a window."),
      ("Will I know who's coming?", "Yes. You get a text with the electrician's name and photo when they're on the way."),
      ("Do I need to be home?", "Someone over 18 needs to let us in and sign off the job. A neighbor or key safe is fine.")]),
    ("Safety", [
      ("What counts as an emergency?", "A burning smell, sparks, smoke, a hot outlet, water near electrics, or no power when your neighbors have it."),
      ("What should I do while I wait?", "If it's safe, switch off the main breaker. Don't touch anything wet or scorched, and keep everyone away from it."),
      ("Is my old panel dangerous?", "Some brands, such as Federal Pacific and Zinsco, are known to fail. We'll check yours free with any visit.")]),
    ("Guarantees", [
      ("Is the work guaranteed?", "Every job is guaranteed for two years, parts and labour. New fittings also carry the maker's warranty."),
      ("Do you pull permits?", "Yes, for every job that needs one, and we're there for the inspection."),
      ("Are you licensed and insured?", "Yes. State electrical contractor license EL-47215 and $2 million liability insurance.")])]]),
    content="56rem"),
  BODIES["circuit-cta"]])

circuit_page("circuit-page-careers", "Careers page: Circuit kit",
 "A Careers page for an electrician: a heading, why people stay, the open jobs with pay and a button to apply, the team and the application. Circuit kit; keep the jobs current and put the site's application form in the named Form group.",
 "careers, jobs, hiring, work with us, apprentice, vacancies, electrician, circuit",
 [cpage_hero("Work with us", "We're hiring electricians, EV installers and apprentices. Top pay, your own van and your evenings back.", "Careers", [("See open jobs", None, "#apply")]),
  BODIES["circuit-careers"], BODIES["circuit-team"]])

circuit_page("circuit-page-contact", "Contact page: Circuit kit",
 "A Contact page for an electrician: a heading, the phone number, email, address and hours beside the contact form, a map of the office and a booking band. Circuit kit; put the site's contact form in the named Form group.",
 "contact, contact us, phone, email, address, map, hours, electrician, circuit",
 [cpage_hero("Contact us", "Call for anything urgent. For everything else, send a message and we'll reply within two working hours.", "Contact"),
  BODIES["circuit-contact"], BODIES["circuit-cta"]])

circuit_page("circuit-page-thanks", "Thank-you page: Circuit kit",
 "The page visitors see after sending a form: thanks, what happens next and when, the emergency number, and links to keep reading. Circuit kit; send every form here.",
 "thank you, thanks, confirmation, form sent, electrician, circuit",
 [csec("Thanks", N([eyebrow("Message sent", "primary-alt"), h("Thanks. We'll be in touch within the hour.", 1, "xxx-large"),
    p("Someone from the office will call or text to confirm, 7am to 7pm. Check your email for a copy of what you sent.", "large"),
    p('Sparks or a burning smell? Don\'t wait: call <a href="' + CTEL + '">' + T(CPHONE) + '</a> now.', "medium", None, None, None, None, raw=True),
    btns([("Back to the home page", None, "/"), ("Read our tips", "outline", "/blog/")])]), "section-brand", ("xxx-large", "xxx-large", None, None), "56rem"),
  BODIES["circuit-reviews-carousel"]])

print("circuit ok")
