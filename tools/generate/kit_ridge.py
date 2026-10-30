# Ridge as a whole website (0.5.0): the sections and pages a local trade's site needs beyond its home page, written for a
# plumbing and heating firm. Run by kits.py after kits_more.py, so every helper there is in scope.
#
# Pages link to each other by slug: /services/ and one page per service under it, /about/, /reviews/, /service-areas/
# and one page per town under it, /special-offers/, /get-a-quote/, /faq/, /careers/, /blog/, /contact/, /thank-you/.
# Forms are a named group ("Form: quote", "Form: contact", "Form: newsletter", "Form: apply") holding a button to the
# page that has the form: swap the group for the site's own form block.

# ---------------------------------------------------------------- AnyPress Blocks markup
def carousel(slides, per=3, label="", autoplay=0):
    a = {"perView": per}
    if autoplay: a["autoplay"] = autoplay
    if label: a["label"] = label
    return f'<!-- wp:anypress/carousel {j(a)} -->\n' + N(slides) + '\n<!-- /wp:anypress/carousel -->'

def counter(number, suffix="", prefix="", size="xxx-large", family="big-shoulders", decimals=0):
    a = {"number": number}
    if decimals: a["decimals"] = decimals
    if prefix: a["prefix"] = prefix
    if suffix: a["suffix"] = suffix
    a.update({"style": {"typography": {"fontWeight": "900", "lineHeight": "0.9"}}, "fontSize": size, "fontFamily": family})
    return f'<!-- wp:anypress/counter {j(a)} /-->'

def mapb(address, lat, lon, zoom=11, aspect="16/9", radius=None):
    a = {"address": address, "lat": lat, "lon": lon, "zoom": zoom, "aspect": aspect}
    if radius: a["style"] = {"border": {"radius": f"var:preset|border-radius|{radius}"}}
    return f'<!-- wp:anypress/map {j(a)} /-->'

def popup(pid, inner, delay=5, label="", days=14):
    a = {"popupId": pid, "trigger": "delay", "delay": delay, "showAgainDays": days, "size": "medium"}
    if label: a["label"] = label
    a["style"] = {"spacing": {"padding": {"top": "0", "bottom": "var:preset|spacing|large", "left": "0", "right": "0"}}}
    return f'<!-- wp:anypress/popup {j(a)} -->\n{inner}\n<!-- /wp:anypress/popup -->'

def accordion(items):
    out = []
    for q, ans in items:
        out.append('<!-- wp:accordion-item -->\n<div class="wp-block-accordion-item"><!-- wp:accordion-heading -->\n'
                   '<h3 class="wp-block-accordion-heading has-icon has-icon-right"><button type="button" class="wp-block-accordion-heading__toggle">'
                   f'<span class="wp-block-accordion-heading__toggle-title">{T(q)}</span><span class="wp-block-accordion-heading__toggle-icon" aria-hidden="true">+</span></button></h3>\n'
                   '<!-- /wp:accordion-heading -->\n\n<!-- wp:accordion-panel -->\n<div role="region" class="wp-block-accordion-panel">' + p(ans) + '</div>\n<!-- /wp:accordion-panel --></div>\n<!-- /wp:accordion-item -->')
    return '<!-- wp:accordion {"className":"is-style-divided"} -->\n<div role="group" class="wp-block-accordion is-style-divided">' + N(out) + '</div>\n<!-- /wp:accordion -->'

def form(kind, label, href, note=None):
    """Where a form goes: a named group with a button to the page that has the form. Swap it for the site's form block."""
    inner = ([p(note, None, "secondary")] if note else []) + [btns([(label, None, href) + (("phone",) if href.startswith("tel:") else ())])]
    return grp(N(inner), gap="small", layout={"type": "default"}, name=f"Form: {kind}")

def card(inner, style="section-card", pad=PAD_CARD):
    return grp(inner, style, pad, "small", {"type": "default"})

def hide_on(markup, *viewports):
    """Hides a block on phones ("mobile"), tablets or computers ("desktop"), with WordPress's own block visibility."""
    vis = {"blockVisibility": {"viewport": {v: False for v in viewports}}}
    name, _, attrs = markup[len("<!-- wp:"):].split("\n", 1)[0].rstrip(" ->/").partition(" ")
    a = json.loads(attrs) if attrs.strip().startswith("{") else {}
    a.setdefault("metadata", {}).update(vis)
    first, sep_, tail = markup.partition("\n")
    closing = " /-->" if first.endswith("/-->") else " -->"
    return f"<!-- wp:{name} {j(a)}{closing}" + sep_ + tail

def call_buttons():
    """The header's call button: the number in full on tablets and computers, just "Call" on phones."""
    full = f'<!-- wp:button {j({"metadata": {"blockVisibility": {"viewport": {"mobile": False}}, "bindings": button_bindings("phone")}})} -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{TEL}">{T("Call " + PHONE)}</a></div>\n<!-- /wp:button -->'
    short = f'<!-- wp:button {j({"metadata": {"blockVisibility": {"viewport": {"tablet": False, "desktop": False}}, "bindings": button_bindings("phone_link")}})} -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{TEL}">{T("Call")}</a></div>\n<!-- /wp:button -->'
    return '<!-- wp:buttons {"layout":{"type":"flex","flexWrap":"nowrap"}} -->\n<div class="wp-block-buttons">' + full + "\n\n" + short + '</div>\n<!-- /wp:buttons -->'

def link_p(text, href, size=None, typo=None):
    return p(f'<a href="{href}">' + T(text) + '</a>', size, None, None, None, typo, raw=True)

CAPS_T = {"textTransform": "uppercase", "fontWeight": "800", "letterSpacing": "0.02em"}
PHONE = "555 0142"
TEL = "tel:5550142"

# ---------------------------------------------------------------- shared content
SERVICES = [
    ("Emergency plumbing", "emergency-plumbing", "Burst pipes, overflowing toilets and no hot water, any hour of any day.", "From $180", "A flooded kitchen floor after a burst pipe under the sink"),
    ("Leaks and burst pipes", "leak-repair", "Found with a thermal camera, fixed, and photographed so you can see it is done.", "From $150", "Water dripping from a chrome tap over a white basin"),
    ("Drain cleaning", "drain-cleaning", "Blocked sinks, showers, toilets and main lines cleared, with a camera check.", "From $120", "A kitchen sink with water running from two taps"),
    ("Water heaters", "water-heaters", "Tank and tankless heaters repaired or replaced, and the old one taken away.", "From $950", "A new water heater fitted in a utility room"),
    ("Boilers and heating", "heating", "Boilers and furnaces serviced, repaired or replaced, with a yearly plan.", "From $110", "A heating unit on a roof under a clear sky"),
    ("Bathrooms and kitchens", "bathrooms-and-kitchens", "New sinks, showers, tubs and toilets fitted, and whole rooms re-plumbed.", "Free quote", "A tiled bathroom with a white bathtub"),
]
TOWNS = [("Springfield", "springfield", 39.7817, -89.6501), ("Chatham", "chatham", 39.6761, -89.7043), ("Rochester", "rochester", 39.7495, -89.5318),
         ("Sherman", "sherman", 39.8936, -89.6048), ("Riverton", "riverton", 39.8445, -89.5390), ("Auburn", "auburn", 39.5917, -89.7462),
         ("Petersburg", "petersburg", 40.0117, -89.8482), ("New Berlin", "new-berlin", 39.7253, -89.9101)]
REVIEWS = [
    ("They found a leak two other plumbers missed, fixed it the same afternoon and sent photos of every step.", "Dana R.", "Springfield"),
    ("Water heater died on a Sunday night. Mike was here by nine the next morning and we had hot water by lunch.", "Jo M.", "Chatham"),
    ("Booked online, got a text when they were on the way, and the price did not change.", "Carlos T.", "Rochester"),
    ("Cleared a main line that had backed up twice this year and showed us the camera footage of the roots.", "Priya S.", "Sherman"),
    ("Tidy, polite and they put dust sheets down before touching anything.", "Sam K.", "Riverton"),
    ("Our boiler service was quick, and they talked us out of a replacement we didn't need.", "Linda H.", "Auburn"),
]

def svc_card(name, slug, text, price, alt):
    return card(N([img("placeholder-wide.svg", alt, "4/3"), h(name, 3, "large"), p(text, None, "secondary"),
                   row([p(price, "medium", None, None, "big-shoulders", {"fontWeight": "800"}), link_p("Details", f"/services/{slug}/", None, {"fontWeight": "700"})], valign="center")]),
                pad=("medium", "medium", "medium", "medium"))

def review_card(text, name, town, size="medium"):
    return card(N([p("★★★★★", "medium", "primary"), p(text, size), p(f"{name}, {town}", "small", "secondary", None, None, {"fontWeight": "700"})]), "section-tint")

def page_hero(title, text, crumb=None, buttons=None):
    trail = [p(crumb, "small", None, None, "big-shoulders", CAPS_T)] if crumb else []
    return sec("Page hero", N(trail + [h(title, 1, "xxx-large"), p(text, "medium")] + ([btns(buttons)] if buttons else [])),
               "section-second-brand", ("xx-large", "x-large", None, None), "80rem")

# ---------------------------------------------------------------- sections
kit("ridge-topbar", R, "Ridge top bar: emergency line and hours",
 "A thin dark bar above the header with the emergency phone number, the opening hours and a link to the quote page. Part of the Ridge kit; use the owner's real number.",
 "top bar, emergency, phone, hours, announcement, header, ridge",
 grp(row([p('<strong>' + T("24/7 emergency line:") + '</strong> <a href="' + TEL + '">' + T(PHONE) + '</a>', "small", None, None, None, None, raw=True),
          hide_on(p(T("Office: 7am to 7pm, seven days") + ' · <a href="/get-a-quote/">' + T("Free quotes") + '</a>', "small", None, None, None, None, raw=True), "mobile")], gap="small"),
     "section-dark", ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Top bar"))

HEADER = grp(N([
    BODIES["ridge-topbar"],
    grp(row([
        row([dyn("site-logo", {"width": 48, "shouldSyncIcon": True}), dyn("site-title", {"level": 0, "fontSize": "medium", "style": {"typography": {"lineHeight": "1"}}})], "left", "small", False, "center"),
        row([dyn("navigation", {"overlayMenu": "mobile", "layout": {"type": "flex", "justifyContent": "right"}, "style": {"typography": {"fontWeight": "700", "textTransform": "uppercase"}}, "fontFamily": "big-shoulders", "fontSize": "medium"}),
             call_buttons()], "right", "medium", False, "center")], "space-between", "medium", False, "center"),
        None, ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Main bar").replace(
        '<!-- wp:group {', '<!-- wp:group {"backgroundColor":"base",', 1).replace('class="wp-block-group alignfull', 'class="wp-block-group alignfull has-base-background-color has-background', 1),
]), "sticky", None, "0", {"type": "default"}, align="full", name="Header")
write("ridge-header", "Ridge header: emergency bar, menu and a call button",
 "A site header for a trade that stays at the top while visitors scroll: a dark bar with the emergency number and hours, then the logo, the menu (with dropdowns for services and areas) and a Call button that phones the business. Part of the Ridge kit; choose it for the header in the Site Editor.",
 "header", "header, menu, navigation, sticky, phone, call, emergency, ridge", HEADER, "core/template-part/header")

def flinks(title, items):
    lis = "\n\n".join(f'<!-- wp:list-item -->\n<li><a href="{href}">{T(label)}</a></li>\n<!-- /wp:list-item -->' for label, href in items)
    return N([h(title, 3, "medium"), '<!-- wp:list {"className":"is-style-no-bullets"} -->\n<ul class="wp-block-list is-style-no-bullets">' + lis + '</ul>\n<!-- /wp:list -->'])
kit("ridge-signup", R, "Ridge signup: offers by email",
 "A band asking visitors to join the email list for seasonal checks and offers, with the signup form beside it. Part of the Ridge kit; sits above the footer on every page.",
 "newsletter, signup, email, offers, subscribe, ridge",
 sec("Signup", cols([
   col(N([h("Get $50 off your next job", 2, "xx-large"), p("Join the list for seasonal checks, offers and the odd useful tip. Two emails a month at most.", "medium")]), "55%", valign="center"),
   col(form("newsletter", "Join the list", "/special-offers/"), valign="center")], "large", "wide", "center"), "section-second-brand", ("x-large", "x-large", None, None)))

POPUP = popup("offer", N([
    img("placeholder-wide.svg", "A plumber's hands tightening a pipe fitting with a wrench", "16/9"),
    grp(N([p("New customers", "small", "primary", None, "big-shoulders", CAPS_T), h("$50 off your first job", 2, "xx-large"),
           p("Leave your email and we'll send the code. One email, no calls."),
           form("offer", "See this month's offers", "/special-offers/")]), None, (None, None, "large", "large"), "small", {"type": "default"})]),
    label="Offer for new customers")
kit("ridge-popup", R, "Ridge popup: $50 off for new customers",
 "A popup that opens five seconds into a first visit with a photo, the offer and one field for an email address; it closes with its button, Escape or a click outside and stays closed for two weeks. Needs the AnyPress Blocks plugin. Part of the Ridge kit; put it in the footer to show it on every page.",
 "popup, offer, discount, newsletter, email, modal, ridge", POPUP)

FOOTER = grp(N([
    BODIES["ridge-signup"],
    grp(N([cols([
        col(N([dyn("site-title", {"level": 0, "fontSize": "x-large"}),
               p("Plumbing and heating for homes and small businesses across the county since 2001. Licensed, insured, and on call day and night.", None, "main-accent"),
               p(f'<a href="{TEL}">' + T(PHONE) + '</a>', "xx-large", None, None, "big-shoulders", {"fontWeight": "900", "lineHeight": "1"}, raw=True, bind="phone_linked"),
               social(["facebook", "instagram", "google"])]), "34%"),
        col(flinks("Services", [(n, f"/services/{s}/") for n, s, *_ in SERVICES])),
        col(flinks("Company", [("About us", "/about/"), ("Reviews", "/reviews/"), ("Service areas", "/service-areas/"), ("Special offers", "/special-offers/"), ("Careers", "/careers/"), ("Blog", "/blog/"), ("FAQ", "/faq/")])),
        col(N([h("Visit or call", 3, "medium"), p("2140 Wabash Avenue, Springfield", None, "main-accent", bind="address"), p("Office: 7am to 7pm, seven days", None, "main-accent", bind="hours"), p("Emergencies: day and night", None, "main-accent"),
               btns([("Get a free quote", None, "/get-a-quote/")])]))], "large", "wide", "top"),
        sep(),
        row([p("© Clearwater Plumbing & Heating. Master plumber licence 48213.", "small", "main-accent"),
             p('<a href="/privacy-policy/">' + T("Privacy") + '</a> · <a href="/contact/">' + T("Contact") + '</a>', "small", "main-accent", None, None, None, raw=True)], gap="small")]),
        "section-dark", ("x-large", "large", None, None), "large", {"type": "constrained", "contentSize": "80rem"}, align="full", name="Footer columns"),
    POPUP,
]), None, None, "0", {"type": "default"}, align="full", name="Footer")
write("ridge-footer", "Ridge footer: signup band, links, phone and the offer popup",
 "A site footer for a trade: a band for joining the email list, then the phone number, services, company pages, address and hours on dark, and the new-customer offer popup (needs the AnyPress Blocks plugin). Part of the Ridge kit; choose it for the footer in the Site Editor.",
 "footer", "footer, links, newsletter, signup, phone, address, hours, popup, ridge", FOOTER, "core/template-part/footer")

kit("ridge-numbers", R, "Ridge numbers: four figures that count up",
 "Four big numbers that count up as they scroll into view (years, jobs, reviews, response time), each with a short label, on the dark style. Needs the AnyPress Blocks plugin. Part of the Ridge kit; use the owner's real figures.",
 "numbers, statistics, counter, proof, years, jobs, ridge",
 sec("Numbers", grid([stackg([counter(n, suf, "", decimals=d), p(lbl, "medium", "main-accent")]) for n, suf, d, lbl in
     [(25, "", 0, "years in the county"), (18400, "+", 0, "jobs done"), (4.9, "★", 1, "from 1,200 reviews"), (60, " min", 0, "average emergency arrival")]], 4, "12rem"),
     "section-dark", ("x-large", "x-large", None, None)))
kit("ridge-service-cards", R, "Ridge services: cards with photos, prices and links",
 "Every service as a card with a photo, one line about it, a starting price and a link to its own page, three across. Part of the Ridge kit; each link goes to /services/<service>/.",
 "services, cards, prices, photos, links, trades, ridge",
 sec("Services", N([row([h("What we fix", 2, "xxx-large"), btns([("All services", "outline", "/services/")])], valign="bottom"),
                    grid([svc_card(*s) for s in SERVICES], 3, "18rem")])))

kit("ridge-steps", R, "Ridge steps: how a job works",
 "Three numbered steps from first call to finished job, in big numerals, so visitors know what happens next. Part of the Ridge kit.",
 "how it works, steps, process, booking, ridge",
 sec("How it works", N([h("How it works", 2, "xxx-large"), grid([stackg([p(n, "poster", "primary", None, "big-shoulders", {"fontWeight": "900", "lineHeight": "0.9"}), h(t, 3, "x-large"), p(d, "medium", "secondary")]) for n, t, d in [
    ("01", "Call or book online", "Tell us what's wrong. We give you a price range on the phone and a time that suits you."),
    ("02", "We arrive on time", "You get a text with the plumber's name and photo when they're on the way. Dust sheets go down first."),
    ("03", "Fixed, and guaranteed", "We show you what we did, take the old parts away and guarantee the work for a year.")]], 3, "16rem", "x-large")]),
    "section-tint"))

kit("ridge-reviews-carousel", R, "Ridge reviews: a carousel of five-star reviews",
 "Customer reviews in a carousel, three at a time on a computer and one on a phone, with the rating and the customer's name and town. Needs the AnyPress Blocks plugin. Part of the Ridge kit; use real reviews.",
 "reviews, testimonials, carousel, slider, stars, customers, ridge",
 sec("Reviews", N([row([h("4.9 from 1,200 reviews", 2, "xxx-large"), btns([("Read them all", "outline", "/reviews/")])], valign="bottom"),
                   carousel([review_card(*r) for r in REVIEWS], 3, "Customer reviews")])))

def zoom(markup):
    """An image that opens full screen when clicked (core lightbox)."""
    return markup.replace("<!-- wp:image {", '<!-- wp:image {"lightbox":{"enabled":true},', 1)

kit("ridge-jobs", R, "Ridge recent jobs: photos in a carousel",
 "Photos of recent jobs in a carousel, each with a short caption of what was done and where. Needs the AnyPress Blocks plugin. Part of the Ridge kit; use the owner's own photos.",
 "projects, jobs, gallery, photos, carousel, portfolio, ridge",
 sec("Recent jobs", N([h("Recent jobs", 2, "xxx-large"), carousel([stackg([zoom(img("placeholder-tall.svg", alt, "3/4")), p(cap, None, "secondary")]) for alt, cap in [
    ("A plumber fitting a new dishwasher under a kitchen counter", "New dishwasher plumbed in, Chatham"),
    ("A tiled bathroom with a white bathtub", "Bathroom re-plumbed and a new tub fitted, Springfield"),
    ("A kitchen sink with water running from two taps", "Double sink and new taps, Rochester"),
    ("A heating unit on a roof under a clear sky", "Rooftop heating unit serviced, Sherman"),
    ("Water dripping from a chrome tap over a white basin", "Dripping tap and basin waste, Riverton")]], 3, "Recent jobs", 6)]), "section-tint"))

kit("ridge-faq", R, "Ridge questions: answers that open and close",
 "The questions people ask before booking a trade, as answers that open and close, beside a heading and a call button. Part of the Ridge kit; answer with the owner's real prices and policies.",
 "faq, questions, answers, accordion, prices, ridge",
 sec("Questions", cols([
   col(N([h("Questions people ask", 2, "xxx-large"), p("Can't see yours? Call and ask: you'll talk to a plumber, not a call center.", "medium", "secondary"), btns([("All questions", "outline", "/faq/")])]), "36%"),
   col(accordion([
     ("Do you charge a call-out fee?", "No. You pay for the job, at the price we agree before we start. Emergency visits after 7pm add a flat $80."),
     ("How soon can you come?", "Most repairs the same or next day. For emergencies we aim to be there within the hour, day or night."),
     ("Do you give written quotes?", "Yes, free and in writing, with photos of what we found. The price doesn't change unless you change the job."),
     ("Are you licensed and insured?", "Yes. Master plumber licence 48213 and $2 million liability insurance. We'll send copies if you'd like them."),
     ("Is the work guaranteed?", "Every repair is guaranteed for a year, parts and labour. New water heaters and boilers carry the maker's warranty too.")]))], "x-large", "wide", "top")))

def initials(name, style):
    letters = "".join(w[0] for w in name.split()[:2])
    return grp(p(letters, "poster", None, "center", "big-shoulders", {"fontWeight": "900", "lineHeight": "1"}), style, ("x-large", "x-large", None, None), layout={"type": "default"})
kit("ridge-team", R, "Ridge team: the people who come to your door",
 "The team as cards with each person's initials on a coloured panel, their name, job and years with the business, so customers know who is coming. Part of the Ridge kit; swap the initials for a photo of each person when there is one.",
 "team, staff, people, plumbers, about, ridge",
 sec("Team", N([h("Who comes to your door", 2, "xxx-large"), p("Every plumber is ours: employed, trained and background-checked. No subcontractors.", "medium", "secondary"),
   grid([card(N([initials(n, st), h(n, 3, "large"), p(r, None, "secondary")]), "section-tint", ("medium", "medium", "medium", "medium")) for n, r, st in [
     ("Mike Alvarez", "Owner and master plumber, 25 years", "section-brand"),
     ("Tasha Greene", "Heating engineer, 12 years", "section-dark"),
     ("Devon Price", "Plumber, 6 years", "section-second-brand"),
     ("Rosa Lin", "Office manager, 9 years", "section-card")]], 4, "13rem", "medium")])))

kit("ridge-offers", R, "Ridge offers: three coupons",
 "Current offers as three coupon cards with the saving in huge type, what it covers and a button to claim it, then the small print. Part of the Ridge kit; keep the dates and terms current.",
 "offers, coupons, discounts, deals, specials, ridge",
 sec("Offers", N([grid([card(N([p(s, "poster", None, None, "big-shoulders", {"fontWeight": "900", "lineHeight": "0.9"}), h(t, 3, "x-large"), p(d), btns([("Claim this offer", None, "/get-a-quote/")])]), st, PAD_CARD) for s, t, d, st in [
    ("$50 off", "Your first job with us", "Any repair or install over $250. Mention the offer when you book.", "section-brand"),
    ("$89", "Boiler or furnace service", "A full yearly service and safety check. Normally $129.", "section-second-brand"),
    ("10% off", "Seniors and veterans", "On every job, every time. Just tell us when you call.", "section-dark")]], 3, "16rem", "medium"),
    p("One offer per job. Not for emergency call-outs after 7pm. Offers run to the end of the month and are renewed each month.", "small", "secondary")])))

kit("ridge-service-detail", R, "Ridge service: what's included and the price",
 "The body of one service page: what the service covers in plain words, a list of what's included, and a price box with the starting price and buttons to book or call. Part of the Ridge kit.",
 "service, details, included, price, book, ridge",
 sec("Service details", cols([
   col(N([h("What we do", 2, "xx-large"),
          p("A slow drain is usually a build-up you can't see: grease, hair, soap, or roots in the main line. We find what's causing it before we clear it, so it stays clear."),
          lst(["A camera check of the pipe before and after", "Clearing with a cable or high-pressure water jet", "Sinks, tubs, showers, toilets, floor drains and main lines", "Advice on keeping it clear, and a 90-day no-return guarantee", "Clean-up before we leave"], "medium"),
          img("placeholder-wide.svg", "Photo of the service: a kitchen sink with water running from two taps", "16/9")]), "60%"),
   col(card(N([p("Drain cleaning", "small", None, None, "big-shoulders", CAPS_T), p("From $120", "poster", None, None, "big-shoulders", {"fontWeight": "900", "lineHeight": "0.9"}),
               p("Most sink and shower drains. Main lines from $280. The price is agreed before we start."),
               btns([("Book online", None, "/get-a-quote/"), ("Call " + PHONE, "outline", TEL, "phone")])]), "section-second-brand", PAD_CARD))], "x-large", "wide", "top")))

kit("ridge-areas-map", R, "Ridge areas: a map and the towns served",
 "Where the business works: a map of the area and every town served as a link to its own page, with a line on travel outside the area. Needs the AnyPress Blocks plugin for the map. Part of the Ridge kit.",
 "service areas, map, towns, locations, coverage, ridge",
 sec("Areas served", cols([
   col(N([h("Where we work", 2, "xxx-large"), p("Every town within 25 miles of Springfield, with no travel charge. Outside that, call and ask: we often say yes.", "medium", "secondary"),
          '<!-- wp:list {"className":"is-style-no-bullets","fontFamily":"big-shoulders","fontSize":"x-large","style":{"typography":{"lineHeight":"1.15","textTransform":"uppercase","fontWeight":"800"}}} -->\n'
          '<ul class="wp-block-list is-style-no-bullets has-big-shoulders-font-family has-x-large-font-size" style="line-height:1.15;text-transform:uppercase;font-weight:800">'
          + "\n\n".join(f'<!-- wp:list-item -->\n<li><a href="/service-areas/{s}/">{T(t)}</a></li>\n<!-- /wp:list-item -->' for t, s, *_ in TOWNS) + '</ul>\n<!-- /wp:list -->']), "36%"),
   col(mapb("Springfield, Illinois", 39.7817, -89.6501, 10, "4/3"))], "x-large", "wide", "top")))

kit("ridge-careers", R, "Ridge careers: why work here and open jobs",
 "A careers section for a trade: four reasons to join, then each open job with its pay, hours and what it needs, and a button to apply. Part of the Ridge kit; keep the jobs current.",
 "careers, jobs, hiring, vacancies, apprentice, work with us, ridge",
 sec("Careers", N([
   h("Why plumbers stay", 2, "xxx-large"),
   grid([stackg([h(t, 3, "large"), p(d, None, "secondary")]) for t, d in [
     ("Paid well, paid weekly", "Above union scale, overtime at time and a half, and a bonus on every five-star review."),
     ("A van and tools", "A new van you can take home, and a full set of tools we replace when they wear out."),
     ("Home for dinner", "Four-day weeks on rotation, and on-call shared fairly, one week in five."),
     ("Training paid for", "Apprentices through to master licence, with the exam fees and study time paid.")]], 4, "13rem"),
   '<!-- wp:spacer {"height":"var:preset|spacing|large"} -->\n<div style="height:var(--wp--preset--spacing--large)" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->',
   h("Open jobs", 2, "xx-large"),
   N([card(N([row([h(t, 3, "x-large"), p(pay, "medium", None, None, "big-shoulders", {"fontWeight": "800"})], valign="center"), p(d, None, "secondary"), btns([("Apply for this job", None, "#apply")])]), "section-tint") for t, pay, d in [
     ("Service plumber", "$32 to $42 an hour", "Journeyman licence and three years on residential service. Clean driving record."),
     ("Heating engineer", "$34 to $45 an hour", "Boiler and furnace service and installs. Gas certification required."),
     ("Apprentice plumber", "$19 an hour to start", "No experience needed. Reliable, careful and happy to learn. We pay for school.")]]),
   grp(N([h("Apply", 2, "xx-large"), p("Send your name, phone, the job you want and a few lines about you. Rosa replies to every application within two working days."),
          form("apply", "Email your application", "mailto:jobs@example.com")]), "section-card", PAD_CARD, "small", {"type": "default"}, anchor="apply")])))

kit("ridge-quote", R, "Ridge quote: the form and what happens next",
 "A quote request section: the form on one side, and on the other what happens after sending it, the phone number for anything urgent and the guarantee. Part of the Ridge kit.",
 "quote, estimate, form, book, request, ridge",
 sec("Quote", cols([
   col(card(N([h("Ask for a free quote", 2, "xx-large"), p("Tell us what's wrong and when suits you. Photos help: you can add them to the form."),
               form("quote", "Call " + PHONE, TEL, "Prefer to talk? Call us instead.")]), "section-card", PAD_CARD), "58%"),
   col(N([h("What happens next", 3, "x-large"),
          lst(["We reply within two working hours, 7am to 7pm.", "You get a price range, or we book a free visit to look.", "You choose a time. We text when we're on the way."], "medium"),
          card(N([p("Water everywhere?", "large", None, None, "big-shoulders", CAPS_T), p("Don't fill in a form. Turn off the water at the stop valve and call us now."),
                  p(f'<a href="{TEL}">' + T(PHONE) + '</a>', "xxx-large", None, None, "big-shoulders", {"fontWeight": "900", "lineHeight": "1"}, raw=True, bind="phone_linked")]), "section-brand")]))],
   "x-large", "wide", "top"), "section-tint"))

kit("ridge-contact", R, "Ridge contact: details, form and map",
 "A contact section for a trade: phone, email, address and hours beside the contact form, then a map of the office with directions. Needs the AnyPress Blocks plugin for the map. Part of the Ridge kit.",
 "contact, phone, email, address, hours, map, form, ridge",
 sec("Contact", N([cols([
   col(N([h("Call, write or visit", 2, "xxx-large"),
          p(f'<a href="{TEL}">' + T(PHONE) + '</a>', "xxx-large", None, None, "big-shoulders", {"fontWeight": "900", "lineHeight": "1"}, raw=True, bind="phone_linked"),
          p('<a href="mailto:hello@example.com">hello@example.com</a>', "medium", None, None, None, None, raw=True, bind="email_linked"),
          p("2140 Wabash Avenue, Springfield", "medium", bind="address"), p("Office: 7am to 7pm, seven days. Emergencies: day and night.", None, "secondary")]), "42%"),
   col(card(N([h("Send a message", 3, "x-large"), form("contact", "Call " + PHONE, TEL, "We reply within two working hours.")]), "section-tint", PAD_CARD))], "x-large", "wide", "top"),
   mapb("2140 Wabash Avenue, Springfield, Illinois", 39.7817, -89.6501, 13, "21/9")])))

kit("ridge-news", R, "Ridge blog: the latest three posts",
 "The three latest blog posts as cards with a photo, the title and the date, and a link to the blog. Part of the Ridge kit.",
 "blog, news, posts, tips, articles, latest, ridge",
 sec("Blog", N([row([h("Tips from the van", 2, "xxx-large"), btns([("All posts", "outline", "/blog/")])], valign="bottom"),
   query(3, 0, 3, N([dyn("post-featured-image", {"isLink": True, "aspectRatio": "4/3"}), dyn("post-title", {"isLink": True, "level": 3, "fontSize": "large"}), dyn("post-date", {"fontSize": "small", "textColor": "secondary"})]), 31)])))

# ---------------------------------------------------------------- pages
def ridge_page(slug, title, desc, kw, parts):
    write(slug, title, desc, "anypress/pages", kw, N(parts), "core/post-content", " * Post Types: page\n")

kit_page("kit-home-services", "Home page: Ridge kit, home services",
 "A complete home page for a plumber, electrician, roofer or other trade in the Ridge kit: a loud hero with the phone number, proof on coloured panels, numbers that count up, services with photos, prices and links, how it works, recent jobs and reviews in carousels, areas served with a map, common questions, the latest tips and a huge phone number to close. Apply the Ridge style for the look it was designed with.",
 "home, trades, plumber, electrician, roofer, cleaner, landscaper, hvac, kit, ridge",
 ["ridge-hero", "ridge-proof", "ridge-numbers", "ridge-service-cards", "ridge-steps", "ridge-photo", "ridge-reviews-carousel", "ridge-areas-map", "ridge-faq", "ridge-news", "ridge-call"])

ridge_page("ridge-page-services", "Services page: Ridge kit",
 "A Services page for a trade: a page heading, every service as a card linking to its own page, how a job works, the guarantee panels, common questions and the phone number. Ridge kit.",
 "services, all services, prices, trades, ridge",
 [page_hero("Plumbing and heating services", "Repairs, replacements and new installs for homes and small businesses. Fixed prices, agreed before we start.", "Services", [("Get a free quote", None, "/get-a-quote/"), ("Call " + PHONE, "outline", TEL, "phone")]),
  BODIES["ridge-service-cards"], BODIES["ridge-steps"], BODIES["ridge-proof"], BODIES["ridge-faq"], BODIES["ridge-call"]])

ridge_page("ridge-page-service", "Service page: Ridge kit (one service)",
 "A page for one service, such as drain cleaning: a heading, what's included and the price, how it works, recent jobs, reviews, questions about this service and the phone number. Ridge kit; make one per service under Services.",
 "service page, drain cleaning, water heater, repair, single service, ridge",
 [page_hero("Drain cleaning", "Blocked sink, shower, toilet or main line? Cleared today in most cases, with a camera check so it stays clear.", "Services / Drain cleaning", [("Book online", None, "/get-a-quote/"), ("Call " + PHONE, "outline", TEL, "phone")]),
  BODIES["ridge-service-detail"], BODIES["ridge-steps"], BODIES["ridge-jobs"], BODIES["ridge-reviews-carousel"],
  sec("Questions", cols([col(h("About drain cleaning", 2, "xxx-large"), "36%"), col(accordion([
    ("Will chemical drain cleaner fix it?", "Sometimes for a while, but it eats old pipes and rarely shifts a real block. We'd rather you didn't: it also burns whoever opens the pipe next."),
    ("How long does it take?", "Most sink and shower drains take under an hour. A main line with roots can take two or three."),
    ("What if it blocks again?", "If the same drain blocks within 90 days, we come back and clear it free."),
    ("Do you dig up the yard?", "Almost never. The camera shows us where the problem is, and most lines clear from inside or from the cleanout.")]))], "x-large", "wide", "top")),
  BODIES["ridge-call"]])

ridge_page("ridge-page-about", "About page: Ridge kit",
 "An About page for a trade: a heading, the story of the business with a photo, numbers that count up, the team, why customers trust it, reviews and the phone number. Ridge kit.",
 "about, about us, story, team, history, family business, ridge",
 [page_hero("Family-run since 2001", "Mike Alvarez started with one van and a pager. Twenty-five years on, his team looks after 6,000 homes across the county.", "About us"),
  sec("Story", cols([
    col(N([h("One van, one rule", 2, "xxx-large"),
           p("Mike's rule from day one: fix it properly, tell people the truth, and leave the house cleaner than you found it.", "large"),
           p("We're still a family firm. Mike still answers the phone some evenings, Rosa has run the office for nine years, and every plumber who comes to your door is someone we trained ourselves."),
           p("We don't upsell, we don't use subcontractors, and if a repair will do, we won't sell you a replacement.")]), "50%", valign="center"),
    col(img("placeholder-tall.svg", "Construction workers standing in front of a big work truck", "4/5"))], "x-large", "wide", "center")),
  BODIES["ridge-numbers"], BODIES["ridge-team"], BODIES["ridge-proof"], BODIES["ridge-reviews-carousel"], BODIES["ridge-call"]])

ridge_page("ridge-page-reviews", "Reviews page: Ridge kit",
 "A Reviews page for a trade: the overall rating, the reviews as cards with names and towns, and the phone number. Ridge kit; use real reviews and say where they come from.",
 "reviews, testimonials, ratings, customers, stars, ridge",
 [page_hero("4.9 stars from 1,200 reviews", "What customers say on Google and Facebook. We read every one, and reply to every one.", "Reviews", [("Leave a review", "outline", "/contact/")]),
  sec("All reviews", grid([review_card(*r) for r in REVIEWS + [
    ("Fixed our outside tap before the frost and checked the rest of the house for free.", "Greg W.", "Petersburg"),
    ("Honest price on a new water heater, fitted the same day, old one hauled away.", "Maria F.", "New Berlin"),
    ("Third time we've used them. Always on time, always the price they said.", "Ahmed B.", "Springfield")]], 3, "18rem", "medium")),
  BODIES["ridge-numbers"], BODIES["ridge-call"]])

ridge_page("ridge-page-areas", "Service areas page: Ridge kit",
 "A Service areas page for a trade: a heading, a map with every town served as a link to its own page, a card for each main town, and the phone number. Ridge kit.",
 "service areas, locations, towns, map, coverage, ridge",
 [page_hero("Where we work", "Springfield and every town within 25 miles, with no travel charge.", "Service areas"),
  BODIES["ridge-areas-map"],
  sec("Towns", grid([card(N([h(t, 3, "x-large"), p(f"Plumbing and heating in {t}: repairs, drains, water heaters and boilers.", None, "secondary"), link_p(f"Plumber in {t}", f"/service-areas/{s}/", None, {"fontWeight": "700"})]), "section-card") for t, s, *_ in TOWNS], 4, "13rem", "medium"), "section-tint"),
  BODIES["ridge-call"]])

ridge_page("ridge-page-area", "Town page: Ridge kit (one service area)",
 "A page for one town served, such as Chatham: a heading, a few lines about working there with a map, the services, reviews from that town and the phone number. Ridge kit; make one per main town under Service areas, with real local details.",
 "service area page, town, city, local, plumber near me, ridge",
 [page_hero("Plumber in Chatham", "Fifteen minutes from our yard, so most Chatham jobs get a same-day visit. Emergencies within the hour.", "Service areas / Chatham", [("Get a free quote", None, "/get-a-quote/"), ("Call " + PHONE, "outline", TEL, "phone")]),
  sec("Local", cols([
    col(N([h("Plumbing and heating in Chatham", 2, "xx-large"),
           p("We've worked in Chatham since 2001, from the older homes near the center to the newer subdivisions. Hard water is common here, so we see a lot of tired water heaters and scaled-up taps."),
           lst(["Same-day repairs most weekdays", "No travel charge", "Water softener and heater advice for hard water"], "medium")]), "50%"),
    col(mapb("Chatham, Illinois", 39.6761, -89.7043, 13, "4/3"))], "x-large", "wide", "top")),
  BODIES["ridge-service-cards"], BODIES["ridge-reviews-carousel"], BODIES["ridge-call"]])

ridge_page("ridge-page-offers", "Special offers page: Ridge kit",
 "A Special offers page for a trade: a heading, the current offers as coupons with their terms, and the phone number. Ridge kit; keep the offers current.",
 "offers, coupons, specials, deals, discounts, ridge",
 [page_hero("Special offers", "This month's savings. Mention the offer when you book and we'll take it off the bill.", "Special offers"),
  BODIES["ridge-offers"], BODIES["ridge-signup"], BODIES["ridge-call"]])

ridge_page("ridge-page-quote", "Quote page: Ridge kit",
 "A Get a quote page for a trade: a heading, the quote form with what happens next and the emergency number beside it, how a job works, and the guarantee. Ridge kit; put the site's quote form in the named Form group.",
 "quote, free quote, estimate, book, booking, form, ridge",
 [page_hero("Get a free quote", "Free and in writing, with photos. The price doesn't change unless the job does.", "Get a quote"),
  BODIES["ridge-quote"], BODIES["ridge-steps"], BODIES["ridge-proof"]])

ridge_page("ridge-page-faq", "Questions page: Ridge kit",
 "A Questions page for a trade: answers that open and close, grouped into prices, booking, emergencies and guarantees, and the phone number. Ridge kit; answer with the owner's real policies.",
 "faq, questions, answers, help, prices, ridge",
 [page_hero("Questions and answers", "Straight answers about prices, booking, emergencies and our guarantee.", "FAQ"),
  sec("Questions", N([N([h(group_t, 2, "xx-large"), accordion(qs)]) for group_t, qs in [
    ("Prices and paying", [
      ("Do you charge a call-out fee?", "No. You pay for the job, at the price we agree before we start. Emergency visits after 7pm add a flat $80."),
      ("Do you charge by the hour?", "No, by the job. You know the price before we pick up a tool."),
      ("How can I pay?", "Card, bank transfer or check, when the job is done. For installs over $2,000 we take a 20% deposit."),
      ("Do you offer finance?", "Yes, on water heaters, boilers and bathrooms over $1,500: 12 months interest-free, subject to approval.")]),
    ("Booking and arrival", [
      ("How soon can you come?", "Most repairs the same or next day. For emergencies we aim to be there within the hour, day or night."),
      ("Can I book online?", "Yes, on the Get a quote page. We call back within two working hours to fix a time."),
      ("Will I know who's coming?", "Yes. You get a text with the plumber's name and photo when they're on the way."),
      ("Do I need to be home?", "Someone over 18 needs to let us in and sign off the job. A neighbor or key safe is fine.")]),
    ("Emergencies", [
      ("What counts as an emergency?", "Water you can't stop, no heat in winter, no water at all, a sewage backup, or a gas smell (call the gas company first)."),
      ("What should I do while I wait?", "Turn off the water at the stop valve, usually under the kitchen sink or where the pipe comes into the house. Switch off the water heater if it's leaking."),
      ("Do you work weekends and holidays?", "Yes. Emergencies every day of the year. Regular jobs Saturday and Sunday too.")]),
    ("Guarantees", [
      ("Is the work guaranteed?", "Every repair is guaranteed for a year, parts and labour. New water heaters and boilers carry the maker's warranty too."),
      ("What if a drain blocks again?", "If the same drain blocks within 90 days, we come back and clear it free."),
      ("Are you licensed and insured?", "Yes. Master plumber licence 48213 and $2 million liability insurance.")])]]),
    content="56rem"),
  BODIES["ridge-call"]])

ridge_page("ridge-page-careers", "Careers page: Ridge kit",
 "A Careers page for a trade: a heading, why people stay, the open jobs with pay and a button to apply, the team and the application. Ridge kit; keep the jobs current and put the site's application form in the named Form group.",
 "careers, jobs, hiring, work with us, apprentice, vacancies, ridge",
 [page_hero("Work with us", "We're hiring plumbers, heating engineers and apprentices. Good pay, a new van and home for dinner.", "Careers", [("See open jobs", None, "#apply")]),
  BODIES["ridge-careers"], BODIES["ridge-team"]])

ridge_page("ridge-page-contact", "Contact page: Ridge kit",
 "A Contact page for a trade: a heading, the phone number, email, address and hours beside the contact form, a map of the office, and the areas served. Ridge kit; put the site's contact form in the named Form group.",
 "contact, contact us, phone, email, address, map, hours, ridge",
 [page_hero("Contact us", "Call for anything urgent. For everything else, send a message and we'll reply within two working hours.", "Contact"),
  BODIES["ridge-contact"], BODIES["ridge-call"]])

ridge_page("ridge-page-thanks", "Thank-you page: Ridge kit",
 "The page visitors see after sending a form: thanks, what happens next and when, the emergency number, and links to keep reading. Ridge kit; send every form here.",
 "thank you, thanks, confirmation, form sent, ridge",
 [sec("Thanks", N([p("Message sent", "medium", None, None, "big-shoulders", CAPS_T), h("Thanks. We'll call you back soon.", 1, "xxx-large"),
    p("Rosa or one of the team will reply within two working hours, 7am to 7pm. Check your email for a copy of what you sent.", "large"),
    p('Water everywhere? Don\'t wait: call <a href="' + TEL + '">' + T(PHONE) + '</a> now.', "medium", None, None, None, None, raw=True),
    btns([("Back to the home page", None, "/"), ("Read our tips", "outline", "/blog/")])]), "section-second-brand", ("xxx-large", "xxx-large", None, None), "56rem"),
  BODIES["ridge-reviews-carousel"]])

print("ridge ok")
