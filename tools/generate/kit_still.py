# Still (0.12.0): a whole website for a spa, massage practice, therapist or studio, written for a small massage
# practice with quiet rooms. Run by kits.py after kit_hearth.py, so every helper in kits.py, kits_more.py,
# kit_ridge.py and the kits before it is in scope.
#
# A quiet room: one light serif, sage on stone, square buttons and a lot of space. Pages link to each other by slug:
# /treatments/ and one page per treatment under it, /book/, /rooms/, /visiting/ and one page per nearby town under it,
# /about/, /reviews/, /gifts/, /work-with-us/, /faq/, /journal/, /contact/, /thank-you/. Forms are named groups, as in
# Ridge: "Form: quote" books a treatment, "Form: apply" is the job application.

SPHONE = "555 0170"
STEL = "tel:5550170"
SBOOK = "/book/"
SADDRESS = "3 Canal Street, Hebden Bridge"
SLAT, SLON = 53.7418, -2.0119
SLIGHT = {"lineHeight": "1.05", "fontWeight": "300"}

def ssmall(text):
    return p(text, "small", "secondary", None, None, {"letterSpacing": "0.06em", "textTransform": "uppercase"})

def stel(size="xx-large"):
    return p(f'<a href="{STEL}">' + T(SPHONE) + '</a>', size, None, None, None, SLIGHT, raw=True, bind="phone_linked")

def shead(eb, title, link=None, size="xx-large"):
    left = stackg([ssmall(eb), h(title, 2, size)])
    return row([left, btns([(link[0], "outline", link[1])])] if link else [left], valign="bottom")

def s_buttons():
    """The header's buttons: the phone number and Book on tablets and computers, just "Call" on phones."""
    book = f'<!-- wp:button {j({"metadata": {"blockVisibility": {"viewport": {"mobile": False}}}})} -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{SBOOK}">{T("Book")}</a></div>\n<!-- /wp:button -->'
    call = f'<!-- wp:button {j({"className": "is-style-outline", "metadata": {"blockVisibility": {"viewport": {"mobile": False}}, "bindings": button_bindings("phone")}})} -->\n<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="{STEL}">{T(SPHONE)}</a></div>\n<!-- /wp:button -->'
    short = f'<!-- wp:button {j({"metadata": {"blockVisibility": {"viewport": {"tablet": False, "desktop": False}}, "bindings": button_bindings("phone_link")}})} -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{STEL}">{T("Call")}</a></div>\n<!-- /wp:button -->'
    return '<!-- wp:buttons {"layout":{"type":"flex","flexWrap":"nowrap"}} -->\n<div class="wp-block-buttons">' + N([call, book, short]) + '</div>\n<!-- /wp:buttons -->'

def spage_hero(title, text, crumb=None, buttons=None, alt=None):
    words = N(([ssmall(crumb)] if crumb else []) + [h(title, 1, "xxx-large"), p(text, "large", "secondary")] + ([btns(buttons)] if buttons else []))
    if not alt:
        return sec("Page hero", grp(words, gap="medium", layout={"type": "constrained", "contentSize": "44rem", "justifyContent": "left"}), None, ("xxx-large", "x-large", None, None), "72rem")
    return sec("Page hero", cols([col(words, "48%", valign="center"), col(img("placeholder-tall.svg", alt, "4/5"))], "xx-large", "wide", "center"), None, ("xx-large", "x-large", None, None), "72rem")

def sprice(name, detail, price):
    """One length and its price on a line, with what it covers under it; never wraps in a narrow card."""
    return grp(N([grp(N([h(name, 3, "medium"), p(price, "medium")]), layout={"type": "flex", "flexWrap": "nowrap", "justifyContent": "space-between", "verticalAlignment": "top"}),
                  p(detail, "small", "secondary")]), gap="x-small", layout={"type": "default"})

# ---------------------------------------------------------------- content
TREATS = [
    ("Deep tissue massage", "deep-tissue-massage", "60 or 90 minutes for tight shoulders, backs and legs.", "$85"),
    ("Hot stone massage", "hot-stone-massage", "75 minutes, slow and warm, for sleep.", "$100"),
    ("Pregnancy massage", "pregnancy-massage", "60 minutes on your side, from 14 weeks.", "$85"),
    ("Facials", "facials", "60 minutes with plain oils and warm cloths.", "$75"),
    ("Reflexology", "reflexology", "50 minutes of pressure on the feet.", "$65"),
    ("The quiet room", "quiet-room", "Two hours with tea, the bath and nothing to do.", "$40"),
]
STOWNS = [("Hebden Bridge", "hebden-bridge"), ("Todmorden", "todmorden"), ("Halifax", "halifax"), ("Burnley", "burnley")]
SREVIEWS = [
    ("I came in with a shoulder I couldn't lift and left with one I'd forgotten about. Sarah has the strongest hands in Yorkshire.", "Ruth A.", "Deep tissue massage"),
    ("The quiet room is the only place I don't check my phone. Two hours felt like a weekend.", "Tom W.", "The quiet room"),
    ("Booked at 30 weeks pregnant and finally slept through the night. Kind, careful and unhurried.", "Jess M.", "Pregnancy massage"),
    ("No music, no scented candles, no hard sell. Just a good massage in a warm room.", "Daniel K.", "Hot stone massage"),
    ("I bought my mum a voucher and she's been back every month since.", "Priya S.", "Gift voucher"),
    ("They asked about my back injury before I'd even mentioned it. That's when I knew I was in good hands.", "Mark L.", "Deep tissue massage"),
]

def sreview(text, name, note, size="medium"):
    return grp(N([p("“" + text + "”", size, None, None, None, {"lineHeight": "1.45"}), p(f"{name} · {note}", "small", "secondary")]), "section-card", PAD_CARD, "medium", {"type": "default"})

# ---------------------------------------------------------------- sections
kit("still-topbar", W, "Still top bar: opening hours and the phone number",
 "A thin quiet bar above the header with the opening hours and a link to gift vouchers, and the phone number. Part of the Still kit.",
 "top bar, announcement, hours, phone, header, still",
 grp(row([p(T("Open Tuesday to Sunday") + ' · <a href="/gifts/">' + T("Gift vouchers") + '</a>', "small", None, None, None, None, raw=True),
          hide_on(p(T("Call") + f' <a href="{STEL}">' + T(SPHONE) + '</a>', "small", None, None, None, None, raw=True), "mobile")], gap="small"),
     "section-tint", ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Top bar"))

SHEADER = grp(N([
    BODIES["still-topbar"],
    grp(row([
        row([dyn("site-logo", {"width": 36, "shouldSyncIcon": True}), dyn("site-title", {"level": 0, "fontSize": "large", "style": {"typography": {"lineHeight": "1", "fontWeight": "400"}}})], "left", "small", False, "center"),
        row([dyn("navigation", {"overlayMenu": "mobile", "layout": {"type": "flex", "justifyContent": "right"}}),
             s_buttons()], "right", "medium", False, "center")], "space-between", "medium", False, "center"),
        None, ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Main bar").replace(
        '<!-- wp:group {', '<!-- wp:group {"backgroundColor":"base",', 1).replace('class="wp-block-group alignfull', 'class="wp-block-group alignfull has-base-background-color has-background', 1),
]), "sticky", None, "0", {"type": "default"}, align="full", name="Header")
write("still-header", "Still header: hours, menu and a Book button",
 "A site header for a spa, massage practice or studio that stays at the top while visitors scroll: a quiet bar with the opening hours and the phone number, then the logo, the menu (with dropdowns for treatments and the place), the phone number and a Book button. Part of the Still kit; choose it for the header in the Site Editor.",
 "header", "header, menu, navigation, sticky, booking, phone, spa, massage, still", SHEADER, "core/template-part/header")

kit("still-numbers", W, "Still numbers: four quiet figures that count up",
 "Four light numbers that count up as they scroll into view (years open, therapists, minutes between bookings, regulars), each with a short line. Needs the AnyPress Blocks plugin. Part of the Still kit; use real figures only.",
 "numbers, statistics, counter, about, still",
 sec("Numbers", grid([stackg([counter(n, suf, "", "xx-large", "newsreader", 0).replace('"fontWeight":"900"', '"fontWeight":"300"'), p(lbl, None, "secondary")]) for n, suf, lbl in
     [(12, "", "years in the old mill"), (4, "", "therapists, all fully qualified"), (15, "", "minutes between every booking"), (900, "+", "people who come back each year")]], 4, "13rem", "x-large")))

kit("still-reviews", W, "Still kind words: a carousel of reviews",
 "What clients say, in a carousel, two at a time on a computer and one on a phone, with each person's name and treatment. Needs the AnyPress Blocks plugin. Part of the Still kit; use real reviews, with permission.",
 "reviews, testimonials, quotes, clients, carousel, still",
 sec("Reviews", N([shead("Kind words", "What people say after", ("All reviews", "/reviews/")),
                   carousel([sreview(*r) for r in SREVIEWS], 2, "Reviews")]), "section-tint"))

kit("still-rooms-gallery", W, "Still rooms: photos that open full screen",
 "Photos of the rooms in a carousel, each opening full screen when clicked, with a short caption. Needs the AnyPress Blocks plugin. Part of the Still kit; use the owner's own photos.",
 "gallery, photos, rooms, interior, carousel, lightbox, still",
 sec("Rooms", N([shead("The rooms", "Warm, low-lit and quiet", ("See the rooms", "/rooms/")), carousel([stackg([zoom(img("placeholder-tall.svg", alt, "3/4")), p(cap, "small", "secondary")]) for alt, cap in [
    ("The rooms: a massage table with folded towels", "Room one, by the canal"),
    ("The rooms: warm stones laid out on a cloth", "Stones warming for the next booking"),
    ("The rooms: a deep bath by a window", "The bath in the quiet room"),
    ("The rooms: a pot of tea and two cups", "Tea, after"),
    ("The rooms: green plants on a windowsill", "The garden room, open in summer")]], 3, "Photos of the rooms", 0)])))

kit("still-map", W, "Still finding us: the address beside a map",
 "How to find the place, with the address, parking and the nearest station beside a map. Needs the AnyPress Blocks plugin for the map. Part of the Still kit.",
 "location, address, map, directions, parking, still",
 sec("Finding us", cols([
   col(N([ssmall("Finding us"), h("In the old mill, by the canal", 2, "xx-large"), p(SADDRESS, "large", bind="address"),
          lst(["Ground floor, step-free from the canal path", "Park on Station Road, two minutes' walk", "Eight minutes from the train station"])]), "40%"),
   col(mapb(SADDRESS + ", UK", SLAT, SLON, 16, "4/3"))], "xx-large", "wide", "center")))

kit("still-faq-open", W, "Still questions: answers that open and close",
 "The questions people ask before their first visit, as answers that open and close, beside a short heading. Part of the Still kit; answer the real questions.",
 "faq, questions, answers, accordion, first visit, still",
 sec("Questions", cols([
   col(N([ssmall("Before you come"), h("First time?", 2, "xx-large"), p("Anything else, call and ask. We'd rather you asked.", None, "secondary"), btns([("All questions", "outline", "/faq/")])]), "34%"),
   col(accordion([
     ("What should I wear?", "Whatever is comfortable. You'll undress to your comfort level and stay covered with towels the whole time."),
     ("When should I arrive?", "Ten minutes early, so you can fill in a short form and have some water."),
     ("Can I come if I'm pregnant?", "Yes, from 14 weeks, for a pregnancy massage. Tell us when you book."),
     ("What if I need to cancel?", "Give us a day's notice and there's no charge. Later than that, we charge half."),
     ("Is it quiet?", "Very. No music unless you ask for it, and phones stay in a basket by the door.")]))], "xx-large", "wide", "top")))

kit("still-signup", W, "Still signup: a quiet letter, once a season",
 "A band asking visitors to join a seasonal email with new treatments and quiet times to book, with the signup form beside it. Part of the Still kit; sits above the footer on every page.",
 "newsletter, signup, email, seasonal, still",
 sec("Signup", cols([
   col(N([h("A short letter, four times a year", 2, "xx-large"), p("New treatments, the quiet weekday hours and the odd offer for people on the list. Nothing more.", None, "secondary")]), "55%", valign="center"),
   col(form("newsletter", "Read the journal", "/journal/"), valign="center")], "x-large", "wide", "center"), "section-brand-soft", ("x-large", "x-large", None, None)))

SPOPUP = popup("offer", N([
    img("placeholder-wide.svg", "A massage room with towels and a plant", "16/9"),
    grp(N([ssmall("Your first visit"), h("Twenty minutes extra, on us", 2, "xx-large"),
           p("Leave your email and we'll send a code for twenty extra minutes on your first massage, and our short letter four times a year."),
           form("offer", "See the treatments", "/treatments/")]), None, (None, None, "large", "large"), "small", {"type": "default"})]),
    label="Twenty minutes extra")
kit("still-popup", W, "Still popup: twenty minutes extra on a first visit",
 "A popup that opens five seconds into a first visit with a calm photo, an offer of extra time on a first massage and one field for an email address; it closes with its button, Escape or a click outside and stays closed for two weeks. Needs the AnyPress Blocks plugin. Part of the Still kit; put it in the footer to show it on every page.",
 "popup, offer, first visit, discount, newsletter, email, modal, still", SPOPUP)

SFOOTER = grp(N([
    BODIES["still-signup"],
    grp(N([cols([
        col(N([dyn("site-title", {"level": 0, "fontSize": "x-large", "style": {"typography": {"fontWeight": "300"}}}),
               p("Massage and quiet rooms in the old mill, Hebden Bridge.", None, "main-accent"),
               stel("xx-large"), social(["instagram", "facebook", "google"])]), "34%"),
        col(flinks("Treatments", [(n, f"/treatments/{s}/") for n, s, *_ in TREATS] + [("Book", SBOOK)])),
        col(flinks("The place", [("About us", "/about/"), ("The rooms", "/rooms/"), ("Kind words", "/reviews/"), ("Gift vouchers", "/gifts/"), ("Coming from nearby", "/visiting/"), ("Work with us", "/work-with-us/"), ("Journal", "/journal/"), ("Questions", "/faq/"), ("Contact", "/contact/")])),
        col(N([h("Hours", 3, "medium"), p("Tuesday to Saturday, 10am to 8pm<br>Sunday, 10am to 4pm<br>Closed Monday", None, "main-accent", raw=True, bind="hours"),
               p(SADDRESS, None, "main-accent", bind="address"), btns([("Book a treatment", None, SBOOK)])]))], "large", "wide", "top"),
        sep(),
        row([p("© Still Water. Fully qualified and insured therapists.", "small", "main-accent"),
             p('<a href="/privacy-policy/">' + T("Privacy") + '</a> · <a href="/contact/">' + T("Contact") + '</a>', "small", "main-accent", None, None, None, raw=True)], gap="small")]),
        "section-dark", ("x-large", "large", None, None), "large", {"type": "constrained", "contentSize": "80rem"}, align="full", name="Footer columns"),
    SPOPUP,
]), None, None, "0", {"type": "default"}, align="full", name="Footer")
write("still-footer", "Still footer: seasonal letter, treatments and the first visit offer",
 "A site footer for a spa, massage practice or studio: a band for the seasonal email, then the phone number, treatment and place links and the opening hours on dark, and the first visit offer popup (needs the AnyPress Blocks plugin). Part of the Still kit; choose it for the footer in the Site Editor.",
 "footer", "footer, links, opening hours, newsletter, phone, popup, spa, massage, still", SFOOTER, "core/template-part/footer")

kit("still-treatment-detail", W, "Still treatment: what happens, who it's for and the price",
 "The body of a page for one treatment: what happens in plain words, who it helps, a photo that opens full screen, and a card with the lengths and prices and a Book button. Part of the Still kit.",
 "treatment, massage, details, price, booking, still",
 sec("Treatment", cols([
   col(N([h("What happens", 2, "xx-large"),
          p("We start with ten minutes of questions about where it hurts and how you sleep. Then slow, firm pressure on the knots in your back, shoulders and legs, as deep as you want and no deeper."),
          h("Who it's for", 3, "large"),
          lst(["Desk workers with tight shoulders and necks", "Runners, climbers and walkers", "Anyone who carries stress in their back", "Not for the first weeks after an injury"]),
          zoom(img("placeholder-wide.svg", "This treatment: a therapist working on a client's back", "16/10"))]), "54%"),
   col(grp(N([ssmall("Lengths and prices"), sprice("60 minutes", "Back, shoulders and legs", "$85"), sprice("90 minutes", "The whole body, unhurried", "$120"),
              p("Fifteen minutes before and after are yours, at no charge.", "small", "secondary"),
              btns([("Book this", None, SBOOK), ("Call " + SPHONE, "outline", STEL)])]), "section-brand-soft", PAD_CARD, "medium", {"type": "default"}))], "xx-large", "wide", "top"), content="72rem"))

kit("still-towns", W, "Still nearby: the towns people come from",
 "The towns nearby, as cards with how long it takes to get here and a link to each one's page. Part of the Still kit; for practices that draw people from around the area.",
 "nearby, towns, area, directions, visiting, still",
 sec("Nearby", N([shead("Coming from nearby", "Worth the short trip"), grid([grp(N([h(n, 3, "large"), p(d, None, "secondary"), link_p(f"From {n} →", f"/visiting/{s}/")]), "section-card", PAD_CARD, "small", {"type": "default"}) for (n, s), d in zip(STOWNS, [
    "Five minutes' walk from the town centre, along the canal.", "Twelve minutes on the train, or twenty by bike along the towpath.",
    "Twenty-five minutes on the train, or half an hour by car.", "Thirty minutes over the tops by car, with parking on Station Road."])], 4, "13rem", "medium")]), "section-tint"))

kit("still-town", W, "Still nearby town: how to get here, with a map",
 "The body of a page for one nearby town: how to get here from it, how long it takes and what people from there book, beside a map. Needs the AnyPress Blocks plugin for the map. Part of the Still kit; make one per town.",
 "town, area, directions, map, nearby, still",
 sec("Town", cols([
   col(N([h("A walk along the canal", 2, "xx-large"),
          p("From the town centre, follow the canal path east for five minutes. The old mill is on your right, with our door on the canal side.", "large"),
          lst(["Five minutes on foot", "Step-free all the way", "Bike racks by the door"]),
          p("Most people from Hebden Bridge come on a weekday evening, after work, for a deep tissue massage or the quiet room.", None, "secondary"),
          btns([("Book a treatment", None, SBOOK)])]), "42%"),
   col(mapb("Hebden Bridge, UK", 53.7424, -2.0137, 14, "4/3"))], "xx-large", "wide", "top")))

kit("still-gifts", W, "Still gifts: vouchers and quiet offers",
 "Three offers as plain cards with the deal, who it's for and a button: gift vouchers, a series of five and quiet weekday mornings. Part of the Still kit; keep the offers current.",
 "gift vouchers, offers, series, discount, still",
 sec("Gifts", N([shead("Gifts and offers", "For you, or someone who needs it"), grid([grp(N([p(s, "xx-large", None, None, None, SLIGHT), h(t, 3, "large"), p(d, None, "secondary"), btns([(b, "outline", l)])]), st, PAD_CARD, "small", {"type": "default"}) for s, t, d, b, l, st in [
    ("Any amount", "Gift vouchers", "Sent by email straight away, or in a card by post. Good for a year, for any treatment.", "Call to buy one", STEL, "section-card"),
    ("Five for four", "A series of five", "Book five massages of the same length and the fifth is free. Use them within six months.", "Book a series", SBOOK, "section-brand-soft"),
    ("20% off", "Quiet mornings", "Tuesday to Thursday, before noon, every treatment is 20% less.", "Book a morning", SBOOK, "section-card")]], 3, "16rem", "medium")])))

kit("still-team", W, "Still therapists: who you'll see",
 "The therapists, each with a photo, their name, what they do and how long they've done it. Part of the Still kit; use real photos, with permission.",
 "team, therapists, staff, about, people, still",
 sec("Team", N([shead("The therapists", "Four of us, all fully qualified"), grid([stackg([img("placeholder-tall.svg", alt, "3/4"), h(n, 3, "large"), p(d, None, "secondary")]) for n, d, alt in [
    ("Sarah", "Deep tissue and sports massage. Founded Still Water in 2014.", "A therapist: Sarah, smiling"),
    ("Amir", "Hot stones and reflexology, twenty years at the table.", "A therapist: Amir"),
    ("Holly", "Pregnancy massage and facials, and a midwife before that.", "A therapist: Holly"),
    ("Grace", "Massage and the quiet room, and the one who makes the tea.", "A therapist: Grace")]], 4, "13rem", "large")])))

kit("still-jobs", W, "Still work with us: why work here and the open roles",
 "Why people work at the place, each open role with its hours and pay, and the application. Part of the Still kit; keep the roles current and put the site's application form in the named Form group.",
 "careers, jobs, hiring, therapist, apply, still",
 sec("Careers", N([
   shead("Why work here", "Fewer bookings, done properly"),
   grid([stackg([h(t, 3, "large"), p(d, None, "secondary")]) for t, d in [
     ("Fifteen minutes between", "Every booking has a gap after it, so nobody runs from room to room."),
     ("Five a day at most", "No back-to-back days of eight massages."),
     ("Paid training", "A week a year of courses, paid, on top of holidays."),
     ("Treatments for you", "A free treatment from a colleague every month.")]], 4, "13rem"),
   '<!-- wp:spacer {"height":"var:preset|spacing|large"} -->\n<div style="height:var(--wp--preset--spacing--large)" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->',
   h("Open roles", 2, "xx-large"),
   N([grp(N([row([h(t, 3, "large"), p(when, None, "secondary")], valign="center"), p(d, None, "secondary"), btns([("Apply for this", None, "#apply")])]), "section-tint", PAD_CARD, "small", {"type": "default"}) for t, when, d in [
     ("Massage therapist", "Four days a week, $32 an hour", "Deep tissue and relaxation massage, with time to learn hot stones from Amir. Level 4 or above."),
     ("Facialist", "Three days a week, $28 an hour", "Facials with plain oils, and a say in which products we use."),
     ("Front desk", "Saturdays and Sundays, $17 an hour", "Welcome people, make the tea, keep the diary and the rooms calm.")]]),
   grp(N([h("Apply", 2, "xx-large"), p("Tell us about you, the role and your qualifications. We reply to everyone within a week."),
          form("apply", "Email us", "mailto:jobs@example.com")]), "section-card", PAD_CARD, "small", {"type": "default"}, anchor="apply")])))

kit("still-book-form", W, "Still book: ask for a time",
 "A form to ask for a booking, beside what to expect on a first visit and the cancellation terms. Part of the Still kit; put the site's form in the named Form group.",
 "booking, book, appointment, form, still",
 sec("Book", cols([
   col(grp(N([h("Ask for a time", 2, "xx-large"), p("Choose a treatment and a day. We'll reply within a few hours with a time and a confirmation."),
              form("quote", "Call " + SPHONE, STEL, "Rather talk? Call us.")]), "section-card", PAD_CARD, "medium", {"type": "default"}), "58%"),
   col(N([h("Your first visit", 3, "large"),
          lst(["Arrive ten minutes early", "A short form about your health", "Tea and water before and after", "Pay by card after your treatment"]),
          h("Cancelling", 3, "large"), p("Free with a day's notice. Later than that, we charge half the price.", None, "secondary")]))],
   "xx-large", "wide", "top"), "section-tint"))

kit("still-contact", W, "Still contact: the phone, hours and address",
 "A contact section for a spa or massage practice: the phone number, email, address and opening hours beside the contact form, then a map. Needs the AnyPress Blocks plugin for the map. Part of the Still kit.",
 "contact, phone, email, hours, address, map, form, still",
 sec("Contact", N([cols([
   col(N([h("Call, write or come by", 2, "xx-large"), stel("xxx-large"),
          p('<a href="mailto:hello@example.com">hello@example.com</a>', None, None, None, None, None, raw=True, bind="email_linked"),
          p(SADDRESS, None, bind="address"), p("Tuesday to Saturday, 10am to 8pm<br>Sunday, 10am to 4pm<br>Closed Monday", None, "secondary", raw=True, bind="hours")]), "40%"),
   col(grp(N([h("Send a message", 3, "large"), form("contact", "Call " + SPHONE, STEL, "We answer messages between treatments, the same day.")]), "section-tint", PAD_CARD, "medium", {"type": "default"}))], "xx-large", "wide", "top"),
   mapb(SADDRESS + ", UK", SLAT, SLON, 16, "21/9")])))

# The home page: numbers, kind words, the rooms, questions and a map join the original sections.
kit_page("kit-wellness", "Home page: Still kit, wellness",
 "A complete home page for a spa, massage therapist, yoga studio or clinic in the Still kit: a full-screen photo with the name along the bottom, a short welcome, two photos, treatments as a plain list, numbers that count up, the rooms in a carousel, kind words, questions, a map and the practical details. Apply the Still style for the look it was designed with.",
 "home, spa, massage, wellness, therapy, yoga, clinic, kit, still",
 ["still-hero", "still-intro", "still-photos", "still-treatments", "still-numbers", "still-rooms-gallery", "still-reviews", "still-faq-open", "still-map", "still-practical"])

# ---------------------------------------------------------------- pages
def still_page(slug, title, desc, kw, parts):
    write(slug, title, desc, "anypress/pages", kw, N(parts), "core/post-content", " * Post Types: page\n")

still_page("still-page-services", "Treatments page: Still kit",
 "A Treatments page for a spa or massage practice: a heading, every treatment with its price and a link to its own page, the rooms, kind words and the practical details. Still kit.",
 "treatments, services, prices, massage, still",
 [spage_hero("Treatments", "Massage, facials and quiet time, booked with space around them so nobody rushes you.", "Treatments", [("Book", None, SBOOK)]),
  sec("All treatments", grid([stackg([sep(), h(n, 3, "large"), p(d, None, "secondary"), p("From " + pr, None, None, None, None, SLIGHT), link_p("About this treatment →", f"/treatments/{s}/")], "small") for n, s, d, pr in TREATS], 3, "16rem", "x-large")),
  BODIES["still-rooms-gallery"], BODIES["still-reviews"], BODIES["still-practical"]])

still_page("still-page-service", "Treatment page: Still kit (one treatment)",
 "A page for one treatment, such as deep tissue massage: a heading with a photo, what happens, who it's for, the prices, kind words, questions about it and the practical details. Still kit; make one per treatment.",
 "treatment page, massage, single service, price, still",
 [spage_hero("Deep tissue massage", "Slow, firm pressure on the knots in your back, shoulders and legs, as deep as you want and no deeper.", "Treatments / Deep tissue massage", [("Book this", None, SBOOK)], "Inside the treatment: a massage on the upper back"),
  BODIES["still-treatment-detail"], BODIES["still-reviews"],
  sec("Questions", cols([col(N([ssmall("About this treatment"), h("Good to know", 2, "xx-large")]), "34%"), col(accordion([
    ("Will it hurt?", "It can be firm, but never more than you want. Say so and we'll ease off straight away."),
    ("How often should I come?", "Once a month keeps most people loose. Weekly for a few weeks if something's badly stuck."),
    ("Will I be sore after?", "A little, for a day. Drink water and take a warm bath that evening."),
    ("Can I claim it on insurance?", "Many health plans cover massage from a qualified therapist. We'll give you a receipt.")]))], "xx-large", "wide", "top")),
  BODIES["still-practical"]])

still_page("still-page-about", "About page: Still kit",
 "An About page for a spa or massage practice: a heading, the story beside a photo, numbers that count up, the therapists and a map. Still kit.",
 "about, our story, therapists, team, still",
 [spage_hero("About Still Water", "Four therapists, three rooms and one rule: nobody is rushed.", "About"),
  sec("Story", cols([
    col(N([h("Started with one room", 2, "xx-large"),
           p("Sarah opened Still Water in 2014 in a single room of the old mill, after ten years of massage in busy hotel spas where every booking ran into the next.", "large"),
           p("She wanted the opposite: fewer people, more time, no music unless you ask, and fifteen minutes after every treatment that belong to you. Twelve years on there are three rooms, four of us, and the rule hasn't changed.")]), "50%", valign="center"),
    col(img("placeholder-tall.svg", "Inside the mill: a calm room with a chair and soft light", "4/5"))], "xx-large", "wide", "center")),
  BODIES["still-numbers"], BODIES["still-team"], BODIES["still-map"]])

still_page("still-page-reviews", "Kind words page: Still kit",
 "A Reviews page for a spa or massage practice: a heading, reviews as cards with names and treatments, numbers that count up and the practical details. Still kit; use real reviews, with permission.",
 "reviews, testimonials, kind words, clients, still",
 [spage_hero("Kind words", "From regulars, first-timers and the people they bought vouchers for.", "Reviews", [("Book", None, SBOOK)]),
  sec("All reviews", grid([sreview(*r) for r in SREVIEWS + [
    ("I've had massages all over the world. This is the one I'd come back for.", "Helen B.", "Hot stone massage"),
    ("Reflexology with Amir is the calmest hour of my month.", "Joe F.", "Reflexology"),
    ("My skin hasn't looked this good since my twenties, and nobody tried to sell me a cream.", "Anna C.", "Facial")]], 2, "20rem", "medium")),
  BODIES["still-numbers"], BODIES["still-practical"]])

still_page("still-page-areas", "Coming from nearby page: Still kit",
 "A page for the towns people come from: a heading, a card for each town linking to its own page, a map and the practical details. Still kit.",
 "nearby, towns, area, visiting, directions, still",
 [spage_hero("Coming from nearby", "People come from all along the valley. Here's how to get to us from each town.", "Visiting"),
  BODIES["still-towns"], BODIES["still-map"], BODIES["still-practical"]])

still_page("still-page-area", "Nearby town page: Still kit (one town)",
 "A page for one nearby town: a heading, how to get here with a map, kind words and the practical details. Still kit; make one per town.",
 "town, area, directions, map, nearby, still",
 [spage_hero("Massage near Hebden Bridge", "Five minutes' walk along the canal from the town centre.", "Visiting / Hebden Bridge", [("Book", None, SBOOK)]),
  BODIES["still-town"], BODIES["still-reviews"], BODIES["still-practical"]])

still_page("still-page-offers", "Gifts page: Still kit",
 "A Gifts and offers page for a spa or massage practice: a heading, gift vouchers, a series and quiet mornings, questions and the practical details. Still kit; keep the offers current.",
 "gift vouchers, offers, gifts, discount, still",
 [spage_hero("Gifts and offers", "A voucher for someone who needs an hour, and a few ways to come more often for less.", "Gifts"),
  BODIES["still-gifts"], BODIES["still-faq-open"], BODIES["still-practical"]])

still_page("still-page-join", "Book page: Still kit",
 "A Book page for a spa or massage practice: a heading, the booking form beside what to expect, the treatments and kind words. Still kit; put the site's form in the named Form group.",
 "book, booking, appointment, still",
 [spage_hero("Book a treatment", "Ask for a day and a treatment, and we'll reply with a time within a few hours.", "Book"),
  BODIES["still-book-form"], BODIES["still-treatments"], BODIES["still-reviews"]])

still_page("still-page-rooms", "Rooms page: Still kit",
 "A page about the rooms: a heading, two photos, the rooms in a carousel, the welcome and the practical details. Still kit.",
 "rooms, interior, photos, space, still",
 [spage_hero("The rooms", "Three treatment rooms and a quiet room with a bath, on the ground floor of the old mill.", "Rooms"),
  BODIES["still-photos"], BODIES["still-rooms-gallery"], BODIES["still-intro"], BODIES["still-practical"]])

still_page("still-page-faq", "Questions page: Still kit",
 "A Questions page for a spa or massage practice: answers that open and close, grouped into your first visit, treatments, and booking and paying, and the practical details. Still kit; answer the real questions.",
 "faq, questions, answers, first visit, booking, still",
 [spage_hero("Questions", "What to wear, when to arrive, and what happens if you need to cancel.", "FAQ"),
  sec("Questions", N([N([h(group_t, 2, "xx-large"), accordion(qs)]) for group_t, qs in [
    ("Your first visit", [
      ("What should I wear?", "Whatever is comfortable. You'll undress to your comfort level and stay covered with towels the whole time."),
      ("When should I arrive?", "Ten minutes early, so you can fill in a short form and have some water."),
      ("Is it quiet?", "Very. No music unless you ask for it, and phones stay in a basket by the door.")]),
    ("Treatments", [
      ("Can I come if I'm pregnant?", "Yes, from 14 weeks, for a pregnancy massage. Tell us when you book."),
      ("Can I choose a man or a woman?", "Yes. Say when you book and we'll make it work.")]),
    ("Booking and paying", [
      ("What if I need to cancel?", "Give us a day's notice and there's no charge. Later than that, we charge half."),
      ("How do I pay?", "By card after your treatment, or with a voucher.")])]]),
    content="52rem"),
  BODIES["still-practical"]])

still_page("still-page-careers", "Work with us page: Still kit",
 "A Work with us page for a spa or massage practice: a heading, why people work there, the open roles with hours and pay, the application form and a map. Still kit; keep the roles current and put the site's form in the named Form group.",
 "jobs, careers, hiring, therapist, still",
 [spage_hero("Work with us", "Fewer bookings, more time with each person, and pay on this page.", "Jobs", [("See open roles", None, "#apply")]),
  BODIES["still-jobs"], BODIES["still-map"]])

still_page("still-page-contact", "Contact page: Still kit",
 "A Contact page for a spa or massage practice: a heading, the phone number, email, address and hours beside the contact form, a map, and questions. Still kit; put the site's contact form in the named Form group.",
 "contact, phone, address, hours, still",
 [spage_hero("Contact", "Call, write or come by. We answer between treatments, the same day.", "Contact"),
  BODIES["still-contact"], BODIES["still-faq-open"]])

still_page("still-page-thanks", "Thank-you page: Still kit",
 "The page visitors see after sending a form: thanks, what happens next and when, and links to keep reading. Still kit; send every form here.",
 "thank you, thanks, confirmation, form sent, still",
 [sec("Thanks", N([ssmall("Message sent"), h("Thank you. We'll be in touch soon.", 1, "xxx-large"),
    p("We'll reply within a few hours, between treatments. Check your email for a copy of what you sent.", "large", "secondary"),
    btns([("Back to the home page", None, "/"), ("See the treatments", "outline", "/treatments/")])]), None, ("xxx-large", "xxx-large", None, None), "52rem"),
  BODIES["still-reviews"]])

print("still ok")
