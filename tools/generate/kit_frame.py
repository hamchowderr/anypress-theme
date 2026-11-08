# Frame (0.17.0): a whole website for a photographer, designer, illustrator or architect, written for an architectural
# photographer. Run by kits.py after kit_rep.py, so every helper in kits.py, kits_more.py, kit_ridge.py and the kits
# before it is in scope.
#
# A gallery wall: lots of white space, a tight grotesque, small monospace labels and one strong blue. Pages link to
# each other by slug: /services/ and one page per service under it, /work/ and one page per project under it, /prints/,
# /commission/, /about/, /kind-words/, /assisting/, /faq/, /journal/, /contact/, /thank-you/. Forms are named groups,
# as in Ridge: "Form: quote" asks about a commission, "Form: apply" is the assistant application.

FK = "anypress/kit-portfolio"
FHEAD = "bricolage-grotesque"
FPH = "+351 21 555 0147"
FTL = "tel:+351215550147"
FASK = "/commission/"
FADDR = "Rua do Açúcar 54, 1950-009 Lisboa, Portugal"
FLAT, FLON = 38.7448, -9.1009
FHOURS = "Studio visits by appointment, Monday to Friday."

def fhead(label, title, link=None, size="xx-large"):
    left = stackg([mono(label), h(title, 2, size)])
    return row([left, btns([(link[0], "outline", link[1])])] if link else [left], valign="bottom")

def f_buttons():
    """The header's button: ask about a commission, everywhere."""
    return '<!-- wp:buttons {"layout":{"type":"flex","flexWrap":"nowrap"}} -->\n<div class="wp-block-buttons"><!-- wp:button -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="' + FASK + '">' + T("Commission") + '</a></div>\n<!-- /wp:button --></div>\n<!-- /wp:buttons -->'

def fpage_hero(title, text, crumb=None, buttons=None, alt=None):
    words = N(([mono(crumb)] if crumb else []) + [h(title, 1, "xxx-large", None, None, {"lineHeight": "1"}), p(text, "large", "secondary")] + ([btns(buttons)] if buttons else []))
    if not alt:
        return sec("Page hero", grp(words, gap="medium", layout={"type": "constrained", "contentSize": "52rem", "justifyContent": "left"}), None, ("xx-large", "x-large", None, None), "80rem")
    return N([sec("Page hero", grp(words, gap="medium", layout={"type": "constrained", "contentSize": "52rem", "justifyContent": "left"}), None, ("xx-large", "large", None, None), "80rem"),
              sec("Page photo", fwide(img("placeholder-wide.svg", alt, "21/9")), None, (None, "large", None, None), "80rem")])

def fwide(markup):
    """An image that fills its column even when the photo is narrower than the page."""
    return (markup.replace('"scale":"cover"}', '"scale":"cover","width":"100%"}', 1)
                  .replace('class="wp-block-image size-large"', 'class="wp-block-image size-large is-resized"', 1)
                  .replace('object-fit:cover"', 'object-fit:cover;width:100%;height:auto"', 1))

def ffact(label, value):
    """A label in monospace and its value on one line; never wraps in a narrow card."""
    return grp(N([mono(label), p(value)]), layout={"type": "flex", "flexWrap": "nowrap", "justifyContent": "space-between", "verticalAlignment": "top"}, gap="small")

def fcard(inner, style="section-tint", gap="medium"):
    return grp(N(inner), style, PAD_CARD, gap, {"type": "default"})

# ---------------------------------------------------------------- content
FSERV = [
    ("Architecture", "architecture", "Finished buildings for architects, for competitions, awards and books."),
    ("Interiors", "interiors", "Homes, hotels and shops, lit to look the way they feel to be in."),
    ("People and places", "people-and-places", "Buildings in use: the people who live, work and wait in them."),
    ("Editorial", "editorial", "Stories for magazines and newspapers about cities and how we live in them."),
]
FWORK = [
    ("Casa Moreira", "casa-moreira", "A spiral stair in a Porto townhouse", "2025"),
    ("Azul", "azul", "Social housing in Setúbal", "2025"),
    ("Marvila studios", "marvila-studios", "Artists' studios in an old warehouse", "2024"),
    ("Tower One", "tower-one", "A glass tower for Atelier Sul", "2023"),
    ("Mercado Novo", "mercado-novo", "A market hall brought back to life", "2022"),
]
FWORDS = [
    ("Ines shot our tower over three weeks and waited for the light. The photos won us the competition.", "Rita Sousa", "Atelier Sul"),
    ("She notices the things we spent months on: a handrail, a shadow, a join in the stone.", "Pedro Moreira", "Casa Moreira"),
    ("The people in her photos make the buildings feel lived in. Our tenants loved seeing themselves.", "Joana Reis", "Habitar Setúbal"),
    ("Fast, calm and easy to work with on a tight magazine deadline.", "Tomás Neves", "Revista Linha"),
    ("We still use her photos of the market hall, four years on.", "Helena Costa", "Câmara de Vila Nova"),
    ("She printed one for our office and it's the first thing visitors ask about.", "Ana Ferro", "Studio Ferro"),
]

def fword(text, name, org, size="medium"):
    return grp(N([p("“" + text + "”", size, None, None, None, {"lineHeight": "1.45"}), mono(f"{name}, {org}")]), "section-card", PAD_CARD, "small", {"type": "default"})

# ---------------------------------------------------------------- sections
kit("frame-topbar", FK, "Frame top bar: when you're free and the phone number",
 "A thin bar above the header with the date commissions open and a link to ask, and the studio's phone number. Part of the Frame kit; keep the date current.",
 "top bar, announcement, availability, phone, header, frame",
 grp(row([p(T("Taking commissions from March") + f' · <a href="{FASK}">' + T("Ask about dates") + '</a>', "small", None, None, None, None, raw=True),
          p(T("Call the studio") + f' <a href="{FTL}">' + T(FPH) + '</a>', "small", None, None, None, None, raw=True)], gap="small"),
     "section-brand", ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Top bar"))

FHEADER = grp(N([
    BODIES["frame-topbar"],
    grp(row([
        row([dyn("site-logo", {"width": 36, "shouldSyncIcon": True}), dyn("site-title", {"level": 0, "fontSize": "large", "fontFamily": FHEAD, "style": {"typography": {"lineHeight": "1", "fontWeight": "700", "letterSpacing": "-0.02em"}}})], "left", "small", False, "center"),
        row([dyn("navigation", {"overlayMenu": "mobile", "layout": {"type": "flex", "justifyContent": "right"}}), f_buttons()], "right", "medium", False, "center")], "space-between", "medium", False, "center"),
        None, ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Main bar").replace(
        '<!-- wp:group {', '<!-- wp:group {"backgroundColor":"base",', 1).replace('class="wp-block-group alignfull', 'class="wp-block-group alignfull has-base-background-color has-background', 1),
]), "sticky", None, "0", {"type": "default"}, align="full", name="Header")
write("frame-header", "Frame header: availability, menu and a Commission button",
 "A site header for a photographer, designer, illustrator or architect that stays at the top while visitors scroll: a bar with when commissions open and the phone number, then the name, the menu (with dropdowns for services and work) and a Commission button. Part of the Frame kit; choose it for the header in the Site Editor.",
 "header", "header, menu, navigation, sticky, commission, phone, portfolio, frame", FHEADER, "core/template-part/header")

kit("frame-numbers", FK, "Frame numbers: four figures that count up",
 "Four numbers that count up as they scroll into view (years working, buildings, clients, books), each with a short line in monospace. Needs the AnyPress Blocks plugin. Part of the Frame kit; use real figures only.",
 "numbers, statistics, counter, experience, frame",
 sec("Numbers", grid([stackg([counter(n, "", "", "xxx-large", FHEAD, 0).replace('"fontWeight":"900"', '"fontWeight":"700"'), mono(lbl)]) for n, lbl in
     [(12, "years behind the camera"), (140, "buildings photographed"), (38, "architects and studios"), (9, "books with my photos")]], 4, "13rem", "x-large"), "section-tint"))

kit("frame-words", FK, "Frame kind words: a carousel of what clients say",
 "Clients in their own words, in a carousel, three at a time on a computer and one on a phone, each with the person's name and studio in monospace. Needs the AnyPress Blocks plugin. Part of the Frame kit; use real quotes, with permission.",
 "reviews, testimonials, clients, kind words, carousel, frame",
 sec("Kind words", N([fhead("Kind words", "What clients say", ("All kind words", "/kind-words/")),
                      carousel([fword(*r) for r in FWORDS], 3, "Kind words from clients")])))

kit("frame-faq-open", FK, "Frame questions: answers that open and close",
 "The questions clients ask before a commission, as answers that open and close, beside a heading and a link to all questions. Part of the Frame kit; answer the real questions.",
 "faq, questions, commission, pricing, licensing, accordion, frame",
 sec("Questions", cols([
   col(N([mono("Before you ask"), h("Good to know", 2, "xx-large"), p("Something else? Write or call the studio.", None, "secondary"), btns([("All questions", "outline", "/faq/")])]), "36%"),
   col(accordion([
     ("How much does a shoot cost?", "Most architecture shoots are one or two days, from €1,200 a day with editing. I send a fixed quote before we start."),
     ("How soon can you come?", "I'm booked about six weeks ahead. Tell me your deadline and I'll say honestly if I can meet it."),
     ("Do you travel?", "Yes, across Portugal and Spain, and further for the right project. Travel is added at cost."),
     ("Who owns the photos?", "I do, and you get a licence to use them for what we agree: press, awards, your website and print."),
     ("How do I get the photos?", "As a private online gallery to download, usually within two weeks of the shoot.")]))], "xx-large", "wide", "top")))

kit("frame-visit", FK, "Frame studio: the address and visiting hours, with a map",
 "Where the studio is, with the address, visiting hours and how to get there beside a map. Needs the AnyPress Blocks plugin for the map. Part of the Frame kit.",
 "studio, visit, location, address, map, frame",
 sec("Studio", cols([
   col(N([mono("The studio"), h("In Marvila, by the river", 2, "xx-large"), p(FADDR, "large", bind="address"),
          lst(["Visits by appointment, Monday to Friday", "Prints to see in person on the wall", "Two minutes from Marvila station", "Step-free, ground floor"])]), "40%"),
   col(mapb(FADDR, FLAT, FLON, 15, "4/3"))], "xx-large", "wide", "center")))

kit("frame-signup", FK, "Frame signup: new work by email",
 "A band asking visitors to join the email list for new work and print releases, with the signup form beside it. Part of the Frame kit; sits above the footer on every page.",
 "newsletter, signup, email, new work, prints, frame",
 sec("Signup", cols([
   col(N([h("New work, four times a year", 2, "xx-large"), p("A short letter with new projects and the next print release, before anyone else. Unsubscribe any time.", None, "secondary")]), "55%", valign="center"),
   col(form("newsletter", "See the prints", "/prints/"), valign="center")], "x-large", "wide", "center"), "section-tint", ("x-large", "x-large", None, None)))

FPOP = popup("offer", N([
    img("placeholder-wide.svg", "A white spiral stair seen from below", "16/9"),
    grp(N([mono("Print release"), h("10% off your first print", 2, "xx-large"),
           p("Leave your email and I'll send a code for 10% off any print, and tell you first when the next edition comes out."),
           form("offer", "See the prints", "/prints/")]), None, (None, None, "large", "large"), "small", {"type": "default"})]),
    label="10% off your first print")
kit("frame-popup", FK, "Frame popup: 10% off a first print",
 "A popup that opens five seconds into a first visit with a photo, a first-print discount and one field for an email address; it closes with its button, Escape or a click outside and stays closed for two weeks. Needs the AnyPress Blocks plugin. Part of the Frame kit; put it in the footer to show it on every page.",
 "popup, offer, prints, discount, newsletter, email, modal, frame", FPOP)

FFOOT = grp(N([
    BODIES["frame-signup"],
    grp(N([cols([
        col(N([dyn("site-title", {"level": 0, "fontSize": "x-large", "fontFamily": FHEAD, "style": {"typography": {"lineHeight": "1", "fontWeight": "700", "letterSpacing": "-0.02em"}}}),
               p("Architecture and interiors photographed in Lisbon, Porto and wherever the work is.", None, "main-accent"),
               p(f'<a href="{FTL}">' + T(FPH) + '</a>', "large", None, None, FHEAD, None, raw=True, bind="phone_linked"),
               social(["instagram", "behance", "linkedin"])]), "34%"),
        col(flinks("Services", [(n, f"/services/{s}/") for n, s, _ in FSERV] + [("Prints", "/prints/")])),
        col(flinks("Studio", [("Work", "/work/"), ("About", "/about/"), ("Kind words", "/kind-words/"), ("Assisting", "/assisting/"), ("Questions", "/faq/"), ("Journal", "/journal/"), ("Contact", "/contact/")])),
        col(N([h("Visit", 3, "medium"), p(FADDR, None, "main-accent", bind="address"), p(FHOURS, None, "main-accent", bind="hours"),
               btns([("Commission", None, FASK)])]))], "large", "wide", "top"),
        sep(),
        row([p("© Ines Duarte. Photographs may not be used without a licence.", "small", "main-accent"),
             p('<a href="/privacy-policy/">' + T("Privacy") + '</a> · <a href="/faq/">' + T("Licensing") + '</a>', "small", "main-accent", None, None, None, raw=True)], gap="small")]),
        "section-dark", ("x-large", "large", None, None), "large", {"type": "constrained", "contentSize": "80rem"}, align="full", name="Footer columns"),
    FPOP,
]), None, None, "0", {"type": "default"}, align="full", name="Footer")
write("frame-footer", "Frame footer: new work by email, services and the print popup",
 "A site footer for a photographer, designer, illustrator or architect: a band for the email list, then the phone number, service and studio links and the studio address on dark, and the first-print popup (needs the AnyPress Blocks plugin). Part of the Frame kit; choose it for the footer in the Site Editor.",
 "footer", "footer, links, studio, newsletter, phone, popup, portfolio, frame", FFOOT, "core/template-part/footer")

kit("frame-service-detail", FK, "Frame service: what's included, how it works and the price",
 "The body of a page for one service: how a shoot goes, what's included, two photos that open full screen, and a card with the price, time on site and delivery and an Ask button. Part of the Frame kit.",
 "service, details, price, commission, frame",
 sec("Service details", cols([
   col(N([h("How a shoot goes", 2, "xx-large"),
          p("I visit the building first, alone, to see how the light moves through it over a day. Then we agree a shot list together, and I come back on the right days to shoot it: sometimes early, sometimes late, sometimes in the rain.", "medium"),
          h("What's included", 3, "large"),
          lst(["A first visit and a shot list", "One or two days on site", "Twenty to forty finished photos", "A licence for press, awards and your website", "Prints at cost for your office"]),
          grid([zoom(img("placeholder-wide.svg", a, "4/3")) for a in ["This service: a white concrete building against a blue sky", "This service: a stair seen from above"]], 2, "14rem", "small")]), "56%"),
   col(fcard([mono("At a glance"), ffact("Price", "From €1,200 a day"), ffact("On site", "One or two days"), ffact("Photos", "Twenty to forty"), ffact("Delivery", "Within two weeks"),
              p("Fixed quote before we start.", "small", "secondary"),
              btns([("Ask about dates", None, FASK), ("Call", "outline", FTL)])]))], "xx-large", "wide", "top"), content="80rem"))

kit("frame-project-list", FK, "Frame work: every project, with a link to its page",
 "Every project as a large photo with its name, a line about it and the year, each linking to its own page. Part of the Frame kit; show the work you want more of.",
 "work, projects, portfolio, case studies, frame",
 sec("Work", N([fhead("Selected work", "Projects"), grid([stackg([img("placeholder-wide.svg", f"Project: {n}", "4/3"), hlink(n, f"/work/{s}/", 3, "x-large"), p(d, None, "secondary"), mono(y)]) for n, s, d, y in FWORK], 2, "20rem", "x-large")])))

kit("frame-project-body", FK, "Frame project: the brief, the details and the photos",
 "The body of a page for one project: the brief and how it was shot beside the client, year and role in monospace, then four photos that open full screen and a client's words. Part of the Frame kit; make one per project.",
 "project, case study, gallery, client, frame",
 sec("Project", N([cols([
   col(N([h("Three weeks for the right grey day", 2, "xx-large"),
          p("Atelier Sul wanted Tower One shown as it really is: a glass building that changes colour with the weather. We shot it on eleven days over three weeks and chose the light, not the angle, for each photo. The set went into the competition entry and later a book.", "medium")]), "60%"),
   col(fcard([mono("Project"), ffact("Client", "Atelier Sul"), ffact("Year", "2023"), ffact("Role", "Photography"), ffact("Used in", "Competition, book")]))], "xx-large", "wide", "top"),
   grid([zoom(img("placeholder-wide.svg", a, r)) for a, r in [("Tower One: the glass tower against a blue sky", "4/3"), ("Tower One: looking up between two glass walls", "4/3"),
                                                             ("Tower One: the facade on a grey day", "4/3"), ("Tower One: the glass in the evening", "4/3")]], 2, "18rem", "medium"),
   fword("Ines shot our tower over three weeks and waited for the light. The photos won us the competition.", "Rita Sousa", "Atelier Sul", "large")]), content="80rem"))

kit("frame-prints", FK, "Frame prints: editions for sale",
 "Prints for sale as cards with a photo, the title, the edition size and price, and a button to ask for one. Part of the Frame kit; keep the editions and prices current.",
 "prints, shop, editions, art, buy, frame",
 sec("Prints", N([fhead("Prints", "Signed editions"), p("Archival prints on cotton rag paper, signed and numbered, in editions of 25. Framed or unframed, sent across Europe.", "medium", "secondary"),
   grid([stackg([zoom(img("placeholder-tall.svg", f"Print: {t}", "4/5")), h(t, 3, "large"), ffact("Edition", ed), ffact("Price", pr), btns([("Ask for this print", "outline", "/contact/")])]) for t, ed, pr in [
     ("Spiral, Porto", "8 of 25 left", "€240"), ("Blue wall, Setúbal", "12 of 25 left", "€240"), ("White stair, Marvila", "3 of 25 left", "€320")]], 3, "15rem", "large")])))

kit("frame-jobs", FK, "Frame assisting: working with the studio",
 "What it's like to assist the studio, each open role with its pay, and the application. Part of the Frame kit; keep the roles current and put the site's application form in the named Form group.",
 "careers, jobs, assistant, internship, apply, frame",
 sec("Assisting", N([
   fhead("Assisting", "Work with the studio"),
   grid([stackg([h(t, 3, "large"), p(d, None, "secondary")]) for t, d in [
     ("Paid, always", "Every day on site is paid, including travel days."),
     ("Real shoots", "You'll carry, light and shoot alongside me, not make coffee."),
     ("Your own work", "Use the studio and its printer for your own projects."),
     ("Credit", "Your name on every set you work on.")]], 4, "13rem"),
   '<!-- wp:spacer {"height":"var:preset|spacing|large"} -->\n<div style="height:var(--wp--preset--spacing--large)" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->',
   h("Open roles", 2, "xx-large"),
   N([grp(N([row([h(t, 3, "large"), mono(when, "primary")], valign="center"), p(d, None, "secondary"), btns([("Apply for this", None, "#apply")])]), "section-tint", PAD_CARD, "small", {"type": "default"}) for t, when, d in [
     ("Shoot assistant", "Freelance, €180 a day", "A driving licence, a strong back and some photography of your own. Light and camera experience helps."),
     ("Studio intern", "Six months, €900 a month", "Editing, printing, the archive and the website, three days a week. For a recent graduate.")]]),
   grp(N([h("Apply", 2, "xx-large"), p("Tell me a little about you and send a link to your own photos. I reply to everyone within two weeks."),
          form("apply", "Email the studio", "mailto:jobs@example.com")]), "section-card", PAD_CARD, "small", {"type": "default"}, anchor="apply")])))

kit("frame-commission-form", FK, "Frame commission: the form and what happens next",
 "A form to ask about a commission, beside what happens next and what helps to send. Part of the Frame kit; put the site's form in the named Form group.",
 "commission, quote, booking, hire, form, frame",
 sec("Commission", cols([
   col(fcard([h("Tell me about the project", 2, "xx-large"), p("What it is, where it is and when you need the photos. I'll reply within two days with dates and a fixed quote."),
              form("quote", "Call " + FPH, FTL, "Rather talk first? Call the studio.")], "section-card"), "58%"),
   col(N([h("What happens next", 3, "large"),
          lst(["I reply with dates and a fixed quote", "A first visit to see the light", "We agree a shot list, then shoot"]),
          h("Helpful to send", 3, "large"), lst(["Drawings or a few phone photos", "Where the photos will be used", "Any deadline, such as an award"])]))],
   "xx-large", "wide", "top"), "section-tint"))

kit("frame-contact-full", FK, "Frame contact: phone, email, studio and form",
 "A contact section for a studio: the phone number, email, address and visiting hours beside the contact form, then a map. Needs the AnyPress Blocks plugin for the map. Part of the Frame kit.",
 "contact, phone, email, studio, map, form, frame",
 sec("Contact us", N([cols([
   col(N([h("Write, call or visit", 2, "xx-large"), p(f'<a href="{FTL}">' + T(FPH) + '</a>', "x-large", None, None, FHEAD, None, raw=True, bind="phone_linked"),
          p('<a href="mailto:hello@example.com">hello@example.com</a>', None, None, None, None, None, raw=True, bind="email_linked"),
          p(FADDR, None, bind="address"), p(FHOURS, None, "secondary", bind="hours")]), "40%"),
   col(fcard([h("Send a message", 3, "large"), form("contact", "Call " + FPH, FTL, "I reply within two days.")]))], "xx-large", "wide", "top"),
   mapb(FADDR, FLAT, FLON, 15, "21/9")])))

# The home page: numbers, kind words, questions and the studio with a map join the original sections.
kit_page("kit-portfolio", "Home page: Frame kit, creative portfolio",
 "A complete home page for a photographer, designer, illustrator, architect or artist in the Frame kit: one big sentence, selected work in staggered columns that opens full screen, one project in depth, numbers that count up, clients, kind words in a carousel, questions, the studio with a map and a huge email address. Apply the Frame style for the look it was designed with.",
 "home, portfolio, photographer, designer, illustrator, architect, artist, creative, kit, frame",
 ["frame-hero", "frame-work", "frame-project", "frame-numbers", "frame-clients", "frame-words", "frame-faq-open", "frame-visit", "frame-contact"])

# ---------------------------------------------------------------- pages
def frame_page(slug, title, desc, kw, parts):
    write(slug, title, desc, "anypress/pages", kw, N(parts), "core/post-content", " * Post Types: page\n")

frame_page("frame-page-services", "Services page: Frame kit",
 "A Services page for a photographer or studio: a heading, every service with a photo and a link to its own page, clients, kind words and how to commission. Frame kit.",
 "services, what I do, photography, commission, frame",
 [fpage_hero("Services", "Architecture, interiors, people in places and editorial stories, each shot slowly and with the light.", "Services", [("Ask about a commission", None, FASK), ("See the work", "outline", "/work/")]),
  sec("All services", grid([stackg([img("placeholder-wide.svg", f"Service: {n.lower()}", "4/3"), hlink(n, f"/services/{s}/", 3, "x-large"), p(d, None, "secondary")], "small") for n, s, d in FSERV], 2, "20rem", "x-large")),
  BODIES["frame-clients"], BODIES["frame-words"], BODIES["frame-contact"]])

frame_page("frame-page-service", "Service page: Frame kit (one service)",
 "A page for one service, such as architecture: a heading and a wide photo, how a shoot goes, what's included and the price, kind words, questions about it and how to commission. Frame kit; make one per service.",
 "service page, single service, photography, price, frame",
 [fpage_hero("Architecture", "Finished buildings for architects, for competitions, awards and books.", "Services / Architecture", [("Ask about dates", None, FASK)], "Services: a concrete building rising into a pale sky"),
  BODIES["frame-service-detail"], BODIES["frame-words"],
  sec("Questions", cols([col(N([mono("About this service"), h("Good to know", 2, "xx-large")]), "36%"), col(accordion([
    ("Can you shoot before the building is finished?", "Yes, for progress sets. The final set is best once the landscaping is in."),
    ("Do you need the building empty?", "For some photos, yes. For others, people make the place. We plan it together."),
    ("Do you use drones?", "Yes, where it's allowed and it adds something. Permits are included in the quote."),
    ("Can we use the photos for awards?", "Yes. Award entries are always part of the licence.")]))], "xx-large", "wide", "top")),
  BODIES["frame-contact"]])

frame_page("frame-page-about", "About page: Frame kit",
 "An About page for a photographer or studio: a heading, the story beside a portrait, numbers that count up, clients, kind words and the studio with a map. Frame kit.",
 "about, about me, photographer, story, studio, frame",
 [fpage_hero("About", "I photograph buildings and the people who use them, from a studio in Marvila.", "About"),
  sec("Story", cols([
    col(N([h("Twelve years of waiting for the light", 2, "xx-large"),
           p("I trained as an architect in Porto and spent three years drawing buildings before I realised I'd rather photograph them. Since 2014 I've worked for architects, magazines and city councils across Portugal and Spain.", "large"),
           p("I work slowly. I visit every building alone first, and come back when the light is right, even if that means waiting a week.", "medium")]), "52%", valign="center"),
    col(img("placeholder-wide.svg", "Ines Duarte with her camera", "4/3"))], "xx-large", "wide", "center")),
  BODIES["frame-numbers"], BODIES["frame-clients"], BODIES["frame-words"], BODIES["frame-visit"]])

frame_page("frame-page-reviews", "Kind words page: Frame kit",
 "A Kind words page for a photographer or studio: a heading, quotes from clients as cards, numbers that count up and how to commission. Frame kit; use real quotes, with permission.",
 "reviews, testimonials, kind words, clients, frame",
 [fpage_hero("Kind words", "From the architects, editors and councils I've worked for.", "Kind words", [("Ask about a commission", None, FASK)]),
  sec("All kind words", grid([fword(*r) for r in FWORDS + [
    ("She sent the gallery a day early, with a note about the three photos she liked best. She was right.", "Marta Lopes", "Norte Weekly"),
    ("Our book wouldn't look the way it does without her.", "Luís Ferreira", "Oficina Azul"),
    ("Calm on site, even with forty people and a deadline.", "Sara Matos", "Lisbon Design Week")]], 3, "18rem", "medium"), "section-tint"),
  BODIES["frame-numbers"], BODIES["frame-contact"]])

frame_page("frame-page-areas", "Work page: Frame kit",
 "A Work page for a photographer or studio: a heading, every project with a photo and a link to its own page, clients and kind words. Frame kit.",
 "work, projects, portfolio, case studies, frame",
 [fpage_hero("Work", "Five recent projects. Ask to see more, or the full set from any of them.", "Work"),
  BODIES["frame-project-list"], BODIES["frame-clients"], BODIES["frame-words"]])

frame_page("frame-page-area", "Project page: Frame kit (one project)",
 "A page for one project: a heading and a wide photo, the brief and the details, four photos that open full screen, a client's words, more work and how to commission. Frame kit; make one per project.",
 "project, case study, single project, gallery, frame",
 [fpage_hero("Tower One", "A glass tower for Atelier Sul, shot on eleven days over three weeks.", "Work / Tower One", None, "Tower One: the glass tower seen from below"),
  BODIES["frame-project-body"], BODIES["frame-contact"]])

frame_page("frame-page-offers", "Prints page: Frame kit",
 "A Prints page for a photographer: a heading, the editions for sale with prices, questions and the studio where prints can be seen. Frame kit; keep the editions current.",
 "prints, shop, editions, buy, frame",
 [fpage_hero("Prints", "Signed editions of 25 on cotton rag paper, framed or unframed.", "Prints", [("Ask for a print", None, "/contact/")]),
  BODIES["frame-prints"],
  sec("Print questions", cols([col(N([mono("About the prints"), h("Good to know", 2, "xx-large")]), "36%"), col(accordion([
    ("How are they printed?", "With pigment inks on cotton rag paper, in the studio, by me."),
    ("Can I see one first?", "Yes. Visit the studio by appointment and see them on the wall."),
    ("Do you ship?", "Across Europe, flat in a rigid box, or framed by courier."),
    ("Can I order a larger size?", "Yes, up to 120 cm wide. Ask for a price.")]))], "xx-large", "wide", "top")),
  BODIES["frame-visit"]])

frame_page("frame-page-join", "Commission page: Frame kit",
 "A Commission page for a photographer or studio: a heading, the form beside what happens next, the services and kind words. Frame kit; put the site's form in the named Form group.",
 "commission, quote, booking, hire, frame",
 [fpage_hero("Commission", "Tell me about the building and when you need the photos. I'll reply with dates and a fixed quote.", "Commission"),
  BODIES["frame-commission-form"], BODIES["frame-words"], BODIES["frame-faq-open"]])

frame_page("frame-page-faq", "Questions page: Frame kit",
 "A Questions page for a photographer: answers that open and close, grouped into commissions, licensing and prints, and how to get in touch. Frame kit; answer the real questions.",
 "faq, questions, answers, licensing, commission, frame",
 [fpage_hero("Questions", "Commissions, licensing and prints, answered plainly.", "Questions"),
  sec("Questions", N([N([h(group_t, 2, "xx-large"), accordion(qs)]) for group_t, qs in [
    ("Commissions", [
      ("How much does a shoot cost?", "Most architecture shoots are one or two days, from €1,200 a day with editing. I send a fixed quote before we start."),
      ("How soon can you come?", "I'm booked about six weeks ahead. Tell me your deadline and I'll say honestly if I can meet it.")]),
    ("Licensing", [
      ("Who owns the photos?", "I do, and you get a licence to use them for what we agree: press, awards, your website and print."),
      ("Can the builder or engineer use them too?", "Yes, with their own licence at a reduced price. Just ask.")]),
    ("Prints", [
      ("How are prints made?", "With pigment inks on cotton rag paper, in the studio."),
      ("Can I return a print?", "Unframed prints, yes, within 14 days.")])]]),
    content="56rem"),
  BODIES["frame-contact"]])

frame_page("frame-page-careers", "Assisting page: Frame kit",
 "An Assisting page for a photographer or studio: a heading, what it's like to work there, the open roles with pay, the application form and the studio with a map. Frame kit; keep the roles current and put the site's form in the named Form group.",
 "careers, jobs, assistant, internship, frame",
 [fpage_hero("Assisting", "Paid days on real shoots, the studio for your own work, and your name on every set.", "Assisting", [("See open roles", None, "#apply")]),
  BODIES["frame-jobs"], BODIES["frame-visit"]])

frame_page("frame-page-contact", "Contact page: Frame kit",
 "A Contact page for a photographer or studio: a heading, the phone number, email, address and visiting hours beside the contact form, a map and questions. Frame kit; put the site's contact form in the named Form group.",
 "contact, phone, email, studio, frame",
 [fpage_hero("Contact", "Write, call, or visit the studio in Marvila by appointment.", "Contact"),
  BODIES["frame-contact-full"], BODIES["frame-faq-open"]])

frame_page("frame-page-thanks", "Thank-you page: Frame kit",
 "The page visitors see after sending a form: thanks, what happens next and when, and links to keep browsing. Frame kit; send every form here.",
 "thank you, thanks, confirmation, form sent, frame",
 [sec("Thanks", N([mono("Message sent"), h("Thank you. I'll be in touch soon.", 1, "xxx-large", None, None, {"lineHeight": "1"}),
    p("I reply within two days, Monday to Friday. Check your email for a copy of what you sent.", "large", "secondary"),
    btns([("Back to the home page", None, "/"), ("See the work", "outline", "/work/")])]), None, ("xxx-large", "xxx-large", None, None), "56rem"),
  BODIES["frame-words"]])

print("frame ok")
