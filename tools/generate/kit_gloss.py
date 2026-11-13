# Gloss (0.15.0): a whole website for a hair salon, barber, nail bar or beauty studio, written for a small salon. Run by
# kits.py after kit_parcel.py, so every helper in kits.py, kits_more.py, kit_ridge.py and the kits before it is in scope.
#
# A fashion page: a high-contrast serif, blush and oxblood, small spaced capitals on pill buttons. Pages link to each
# other by slug: /services/ and one page per service under it, /prices/, /book/, /team/ and one page per stylist under
# it, /about/, /reviews/, /offers/, /careers/, /faq/, /journal/, /contact/, /thank-you/. Forms are named groups, as in
# Ridge: "Form: quote" asks for an appointment, "Form: apply" is the job application.

G = "anypress/kit-salon"
GSERIF = "bodoni-moda"
GSANS = "jost"
GPH = "(217) 555-0133"
GTL = "tel:2175550133"
GBOOK = "/book/"
GADDR = "21 Elm Street, Springfield, IL 62701"
GLAT, GLON = 39.8003, -89.6489
GHOURS = "Tuesday to Friday, 9am to 8pm. Saturday, 9am to 5pm."

def gsmall(text, color="secondary"):
    return p(text, "small", color, None, GSANS, {"fontWeight": "500", "letterSpacing": "0.14em", "textTransform": "uppercase"})

def ghead(eb, title, link=None, size="xx-large"):
    left = stackg([gsmall(eb), h(title, 2, size)])
    return row([left, btns([(link[0], "outline", link[1])])] if link else [left], valign="bottom")

def g_buttons():
    """The header's button: Book online everywhere."""
    return '<!-- wp:buttons {"layout":{"type":"flex","flexWrap":"nowrap"}} -->\n<div class="wp-block-buttons"><!-- wp:button -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="' + GBOOK + '">' + T("Book online") + '</a></div>\n<!-- /wp:button --></div>\n<!-- /wp:buttons -->'

def gpage_hero(title, text, crumb=None, buttons=None, alt=None):
    words = N(([gsmall(crumb)] if crumb else []) + [h(title, 1, "xxx-large", None, None, {"lineHeight": "1"}), p(text, "large")] + ([btns(buttons)] if buttons else []))
    if not alt:
        return sec("Page hero", grp(words, gap="medium", layout={"type": "constrained", "contentSize": "48rem", "justifyContent": "left"}), "section-brand-soft", ("xx-large", "xx-large", None, None), "72rem")
    return sec("Page hero", cols([col(words, "55%", valign="center"), col(img("placeholder-tall.svg", alt, "4/5"))], "xx-large", "wide", "center"), "section-brand-soft", ("xx-large", "xx-large", None, None), "72rem")

def gprice(name, detail, price):
    """One level and its price on a line, with what it covers under it; never wraps in a narrow card."""
    return grp(N([grp(N([h(name, 3, "medium", None, GSANS, {"fontWeight": "400"}), p(price, "medium")]), layout={"type": "flex", "flexWrap": "nowrap", "justifyContent": "space-between", "verticalAlignment": "top"}),
                  p(detail, "small", "secondary")]), gap="x-small", layout={"type": "default"})

# ---------------------------------------------------------------- content
GSERV = [
    ("Cut and style", "cut-and-style", "A cut that suits your hair and the way you wear it, finished with a blow-dry."),
    ("Colour", "colour", "Root colour, all-over colour and grey blending, mixed for you."),
    ("Balayage", "balayage", "Hand-painted lightness that grows out softly, with no hard line."),
    ("Blow-dry and styling", "blow-dry", "Smooth, bouncy or waves, for a night out or a wedding morning."),
    ("Brows and lashes", "brows-and-lashes", "Brow shaping, tints and lash lifts with Bea."),
    ("Men's cuts", "mens-cuts", "Clipper work, scissor cuts and beard tidies."),
]
GTEAM = [("Nadia", "nadia", "Owner and colour director", "Balayage, grey blending and colour corrections."),
         ("Ollie", "ollie", "Senior stylist", "Short cuts, men's cuts and curly hair."),
         ("Bea", "bea", "Brows and lashes", "Brow shaping, tints and lash lifts."),
         ("Jess", "jess", "Stylist", "Curls cut dry, blow-dries and wedding hair.")]
GREVIEWS = [
    ("Nadia fixed a box-dye disaster in one visit and the colour still looks good three months later.", "Laura P.", "Colour with Nadia"),
    ("Ollie is the first person who has ever cut my curls dry. I finally have a shape that works.", "Marcus T.", "Curly cut with Ollie"),
    ("My brows were over-plucked for years. Bea had them looking full again in two visits.", "Hannah R.", "Brows with Bea"),
    ("Jess did my hair and my bridesmaids' on the wedding morning and kept us all calm.", "Sophie and Kate", "Wedding hair with Jess"),
    ("They tell you the price before they start, every time. No surprises at the desk.", "Dana M.", "Balayage"),
    ("Quick, sharp cut and a proper chat. Booked in for the next one before I left.", "Andre W.", "Men's cut"),
]

def greview(text, name, what, size="medium"):
    return grp(N([p("★★★★★", None, "primary"), p("“" + text + "”", size, None, None, None, {"lineHeight": "1.45"}),
                  gsmall(f"{name} · {what}")]), "section-card", PAD_CARD, "small", {"type": "default"})

# ---------------------------------------------------------------- sections
kit("gloss-topbar", G, "Gloss top bar: the new-client offer and the phone number",
 "A thin bar above the header with the new-client offer and a link to it, and the salon's phone number. Part of the Gloss kit; keep the offer current.",
 "top bar, announcement, offer, phone, header, gloss",
 grp(row([p(T("New clients: 20% off your first colour") + ' · <a href="/offers/">' + T("See offers") + '</a>', "small", None, None, None, None, raw=True),
          p(T("Call the salon") + f' <a href="{GTL}">' + T(GPH) + '</a>', "small", None, None, None, None, raw=True)], gap="small"),
     "section-dark", ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Top bar"))

GHEAD = grp(N([
    BODIES["gloss-topbar"],
    grp(row([
        row([dyn("site-logo", {"width": 36, "shouldSyncIcon": True}), dyn("site-title", {"level": 0, "fontSize": "x-large", "fontFamily": GSERIF, "style": {"typography": {"lineHeight": "1", "fontWeight": "600"}}})], "left", "small", False, "center"),
        row([dyn("navigation", {"overlayMenu": "mobile", "layout": {"type": "flex", "justifyContent": "right"}}), g_buttons()], "right", "medium", False, "center")], "space-between", "medium", False, "center"),
        None, ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Main bar").replace(
        '<!-- wp:group {', '<!-- wp:group {"backgroundColor":"base",', 1).replace('class="wp-block-group alignfull', 'class="wp-block-group alignfull has-base-background-color has-background', 1),
]), "sticky", None, "0", {"type": "default"}, align="full", name="Header")
write("gloss-header", "Gloss header: new-client offer, menu and a Book online button",
 "A site header for a salon, barber, nail bar or beauty studio that stays at the top while visitors scroll: a dark bar with the new-client offer and the phone number, then the logo, the menu (with dropdowns for services and the team) and a Book online button. Part of the Gloss kit; choose it for the header in the Site Editor.",
 "header", "header, menu, navigation, sticky, book, phone, salon, gloss", GHEAD, "core/template-part/header")

kit("gloss-numbers", G, "Gloss numbers: four figures that count up",
 "Four numbers that count up as they scroll into view (years open, clients, star rating, consultation minutes), each with a short line. Needs the AnyPress Blocks plugin. Part of the Gloss kit; use real figures only.",
 "numbers, statistics, counter, reviews, salon, gloss",
 sec("Numbers", grid([stackg([counter(n, "", "", "xxx-large", GSERIF, d).replace('"fontWeight":"900"', '"fontWeight":"500"'), p(lbl, None, "secondary")]) for n, d, lbl in
     [(14, 0, "years on Elm Street"), (3200, 0, "clients on our books"), (4.9, 1, "stars from 640 reviews"), (30, 0, "free minutes for a first colour chat")]], 4, "13rem", "x-large"), "section-brand-soft"))

kit("gloss-reviews", G, "Gloss reviews: a carousel of what clients say",
 "Clients in their own words, in a carousel, three at a time on a computer and one on a phone, with five stars, each client's name and what they had done. Needs the AnyPress Blocks plugin. Part of the Gloss kit; use real reviews, with permission.",
 "reviews, testimonials, clients, stars, carousel, gloss",
 sec("Reviews", N([ghead("Reviews", "4.9 stars from 640 clients", ("All reviews", "/reviews/")),
                   carousel([greview(*r) for r in GREVIEWS], 3, "Client reviews")])))

kit("gloss-faq-open", G, "Gloss questions: answers that open and close",
 "The questions people ask before booking a salon, as answers that open and close, beside a heading and a link to all questions. Part of the Gloss kit; answer the real questions.",
 "faq, questions, booking, colour, patch test, accordion, gloss",
 sec("Questions", cols([
   col(N([gsmall("Before you book"), h("Good to know", 2, "xx-large"), p("Something else? Call the salon and ask for Nadia.", None, "secondary"), btns([("All questions", "outline", "/faq/")])]), "36%"),
   col(accordion([
     ("Do I need a patch test?", "Yes, for any colour or lash tint if you're new to us or it's been six months. It takes five minutes, at least 48 hours before."),
     ("How do I know the price?", "Prices depend on length and the stylist's level. We confirm the price before we start, every time."),
     ("Can I come in for a consultation first?", "Yes. Colour consultations are free and take about 30 minutes."),
     ("What if I need to cancel?", "Please give us 24 hours' notice. Missed appointments may be charged half the price."),
     ("Do you do curly hair?", "Yes. Ollie and Jess cut curls dry, one by one, and teach you how to style them at home.")]))], "xx-large", "wide", "top")))

kit("gloss-visit", G, "Gloss visit: the salon's address and hours, with a map",
 "Where the salon is, with the address, opening hours and parking beside a map. Needs the AnyPress Blocks plugin for the map. Part of the Gloss kit.",
 "visit, location, address, hours, map, salon, gloss",
 sec("Visit", cols([
   col(N([gsmall("Find us"), h("On Elm Street, by the park", 2, "xx-large"), p(GADDR, "large", bind="address"),
          lst(["Tuesday to Friday, 9am to 8pm", "Saturday, 9am to 5pm", "Free parking behind the salon", "Step-free, with a basin that tilts back gently"])]), "40%"),
   col(mapb(GADDR, GLAT, GLON, 16, "4/3"))], "xx-large", "wide", "center")))

kit("gloss-signup", G, "Gloss signup: offers and free appointments by email",
 "A band asking visitors to join the email list for offers and last-minute free appointments, with the signup form beside it. Part of the Gloss kit; sits above the footer on every page.",
 "newsletter, signup, email, offers, appointments, gloss",
 sec("Signup", cols([
   col(N([h("Last-minute appointments, first", 2, "xx-large"), p("When someone cancels, the list hears first. Plus a seasonal offer or two. Unsubscribe any time.", None, "secondary")]), "55%", valign="center"),
   col(form("newsletter", "See the offers", "/offers/"), valign="center")], "x-large", "wide", "center"), "section-brand-soft", ("x-large", "x-large", None, None)))

GPOP = popup("offer", N([
    img("placeholder-wide.svg", "Pink roses on a pale table", "16/9"),
    grp(N([gsmall("New to the salon?"), h("20% off your first visit", 2, "xx-large"),
           p("Leave your email and we'll send a code for 20% off your first appointment, plus last-minute free times."),
           form("offer", "See the offers", "/offers/")]), None, (None, None, "large", "large"), "small", {"type": "default"})]),
    label="20% off your first visit")
kit("gloss-popup", G, "Gloss popup: 20% off the first visit",
 "A popup that opens five seconds into a first visit with a photo, a first-visit discount and one field for an email address; it closes with its button, Escape or a click outside and stays closed for two weeks. Needs the AnyPress Blocks plugin. Part of the Gloss kit; put it in the footer to show it on every page.",
 "popup, offer, discount, first visit, newsletter, email, modal, gloss", GPOP)

GFOOT = grp(N([
    BODIES["gloss-signup"],
    grp(N([cols([
        col(N([dyn("site-title", {"level": 0, "fontSize": "xx-large", "fontFamily": GSERIF, "style": {"typography": {"fontWeight": "600"}}}),
               p("Hair, colour and brows on Elm Street, Springfield, since 2012.", None, "main-accent"),
               p(f'<a href="{GTL}">' + T(GPH) + '</a>', "x-large", None, None, GSERIF, None, raw=True, bind="phone_linked"),
               social(["instagram", "facebook", "pinterest"])]), "34%"),
        col(flinks("Services", [(n, f"/services/{s}/") for n, s, _ in GSERV] + [("Prices", "/prices/")])),
        col(flinks("The salon", [("About us", "/about/"), ("Our team", "/team/"), ("Reviews", "/reviews/"), ("Offers", "/offers/"), ("Careers", "/careers/"), ("Questions", "/faq/"), ("Journal", "/journal/"), ("Contact", "/contact/")])),
        col(N([h("Visit", 3, "medium"), p(GADDR, None, "main-accent", bind="address"), p(GHOURS, None, "main-accent", bind="hours"),
               btns([("Book online", None, GBOOK)])]))], "large", "wide", "top"),
        sep(),
        row([p("© Elm Studio. Hair, colour and brows in Springfield.", "small", "main-accent"),
             p('<a href="/privacy-policy/">' + T("Privacy") + '</a> · <a href="/faq/">' + T("Cancellation policy") + '</a>', "small", "main-accent", None, None, None, raw=True)], gap="small")]),
        "section-dark", ("x-large", "large", None, None), "large", {"type": "constrained", "contentSize": "80rem"}, align="full", name="Footer columns"),
    GPOP,
]), None, None, "0", {"type": "default"}, align="full", name="Footer")
write("gloss-footer", "Gloss footer: offers by email, services and the first-visit popup",
 "A site footer for a salon, barber, nail bar or beauty studio: a band for the email list, then the phone number, service and salon links and the address and hours on dark, and the first-visit popup (needs the AnyPress Blocks plugin). Part of the Gloss kit; choose it for the footer in the Site Editor.",
 "footer", "footer, links, hours, newsletter, phone, popup, salon, gloss", GFOOT, "core/template-part/footer")

kit("gloss-service-detail", G, "Gloss service: what happens, how long and the price",
 "The body of a page for one service: what happens in the chair, what's included, how long it takes, a photo that opens full screen, and a card with the price by stylist level and a Book button. Part of the Gloss kit.",
 "service, details, price, booking, salon, gloss",
 sec("Service details", cols([
   col(N([h("In the chair", 2, "xx-large"),
          p("We start by talking about how you wear your hair and how much time you give it in the morning. Then a wash, a cut that works with your hair's natural fall, and a blow-dry so you can see the shape before you leave."),
          h("What's included", 3, "large"),
          lst(["A consultation, every time", "Wash with a scalp massage", "The cut, wet or dry", "A blow-dry and finish", "Tips for styling at home"]),
          zoom(img("placeholder-wide.svg", "This service: a stylist cutting a client's hair", "16/10"))]), "54%"),
   col(grp(N([gsmall("Prices"), gprice("Stylist", "Up to two years with us", "from $65"), gprice("Senior stylist", "Five years or more", "from $80"), gprice("Director", "Nadia, the owner", "from $95"),
              p("About an hour. We confirm the price before we start.", "small", "secondary"),
              btns([("Book this", None, GBOOK), ("Call", "outline", GTL)])]), "section-brand-soft", PAD_CARD, "medium", {"type": "default"}))], "xx-large", "wide", "top"), content="72rem"))

kit("gloss-stylists", G, "Gloss our team: every stylist, with a link to book them",
 "Every stylist with a portrait, their name, what they do and a link to their own page. Part of the Gloss kit; clients book a person, so show the real team.",
 "team, stylists, staff, people, book, gloss",
 sec("Our team", N([ghead("Our team", "Book the person, not just the time"), grid([stackg([img("placeholder-tall.svg", f"Our team: {n}", "3/4"), hlink(n, f"/team/{s}/", 3, "large"), gsmall(r, "primary"), p(d, None, "secondary")]) for n, s, r, d in GTEAM], 4, "13rem", "large")])))

kit("gloss-stylist", G, "Gloss stylist: what one stylist loves doing",
 "The body of a page for one stylist: what they love doing, their level and prices, what to book them for, and a quote from one of their clients. Part of the Gloss kit; make one per stylist.",
 "stylist, team member, profile, book, gloss",
 sec("Stylist", N([cols([
   col(N([gsmall("Colour director"), h("Nadia has been mixing colour on Elm Street since the day we opened", 2, "xx-large"),
          p("Nadia trained in Chicago and spent eight years colouring for photo shoots before opening the salon in 2012. She loves soft, lived-in colour and fixing the colour other people are scared of."),
          h("Book Nadia for", 3, "large"), lst(["Balayage and hand-painted colour", "Grey blending", "Colour corrections", "A big change you're nervous about"])]), "55%"),
   col(grp(N([gsmall("Prices with Nadia"), gprice("Cut and style", "About an hour", "from $95"), gprice("Balayage", "With toner and a cut", "from $210"),
              gprice("Colour consultation", "30 minutes", "Free"),
              btns([("Book with Nadia", None, GBOOK)])]), "section-brand-soft", PAD_CARD, "medium", {"type": "default"}))], "xx-large", "wide", "top"),
   greview("Nadia fixed a box-dye disaster in one visit and the colour still looks good three months later.", "Laura P.", "Colour with Nadia", "large")]), content="72rem"))

kit("gloss-offers", G, "Gloss offers: ways to save",
 "Three offers as cards with the saving in large type, who it's for and a button: new clients, bringing a friend and gift cards. Part of the Gloss kit; keep the offers current.",
 "offers, discounts, new client, refer a friend, gift card, gloss",
 sec("Offers", N([ghead("Ways to save", "Offers"), grid([grp(N([p(s, "xx-large", None, None, GSERIF, {"lineHeight": "1"}), h(t, 3, "large"), p(d, None, "secondary"), btns([(b, "outline", l)])]), st, PAD_CARD, "small", {"type": "default"}) for s, t, d, b, l, st in [
    ("20% off", "Your first visit", "New to the salon? 20% off your first colour or cut, with any stylist.", "Book now", GBOOK, "section-brand-soft"),
    ("$20 each", "Bring a friend", "Send a friend to us and you both get $20 off your next visit.", "Book together", GBOOK, "section-card"),
    ("Gift cards", "From $25", "For a cut, a colour or a brow shape. Sent by email or wrapped at the desk.", "Ask for a gift card", "/contact/", "section-brand-soft")]], 3, "16rem", "medium")])))

kit("gloss-jobs", G, "Gloss careers: why work here and the open roles",
 "Why people work at the salon, each open role with its pay, and the application. Part of the Gloss kit; keep the roles current and put the site's application form in the named Form group.",
 "careers, jobs, hiring, stylist, apprentice, apply, gloss",
 sec("Careers", N([
   ghead("Why work here", "A salon that trains its people"),
   grid([stackg([h(t, 3, "large"), p(d, None, "secondary")]) for t, d in [
     ("Education paid", "Two training days a year, and colour courses paid for."),
     ("Your own column", "Build your own clients, and we'll fill your book while you do."),
     ("Four-day weeks", "Most of the team works four days, with every Sunday and Monday off."),
     ("Fair pay", "Pay is on this page, plus commission on retail and tips that are yours.")]], 4, "13rem"),
   '<!-- wp:spacer {"height":"var:preset|spacing|large"} -->\n<div style="height:var(--wp--preset--spacing--large)" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->',
   h("Open roles", 2, "xx-large"),
   N([grp(N([row([h(t, 3, "large"), p(when, None, None, None, None, {"fontWeight": "500"})], valign="center"), p(d, None, "secondary"), btns([("Apply for this", None, "#apply")])]), "section-brand-soft", PAD_CARD, "small", {"type": "default"}) for t, when, d in [
     ("Stylist", "Full time, $22 an hour plus commission", "Two years on the floor or more, and a love of cutting. Colour training available."),
     ("Apprentice", "Full time, $16 an hour", "Learn the trade on the salon floor with Nadia and Ollie, and go to college one day a week."),
     ("Front desk", "Part time, $17 an hour", "Welcome clients, run the diary and keep the salon running smoothly.")]]),
   grp(N([h("Apply", 2, "xx-large"), p("Tell us a little about you and send a photo or two of your work. We reply to everyone within a week."),
          form("apply", "Email the salon", "mailto:jobs@example.com")]), "section-card", PAD_CARD, "small", {"type": "default"}, anchor="apply")])))

kit("gloss-book-form", G, "Gloss booking: the form and what to expect",
 "A form to ask for an appointment, beside what happens next and what to know before a first visit. Part of the Gloss kit; put the site's form in the named Form group.",
 "booking, appointment, book now, form, salon, gloss",
 sec("Book", cols([
   col(grp(N([h("Ask for an appointment", 2, "xx-large"), p("Tell us what you'd like and when suits you. We'll reply within a few hours with a time and the price."),
              form("quote", "Call " + GPH, GTL, "Rather talk now? Call the salon.")]), "section-card", PAD_CARD, "medium", {"type": "default"}), "58%"),
   col(N([h("What happens next", 3, "large"),
          lst(["We reply with a time and the price", "A reminder by text the day before", "Arrive ten minutes early for a drink"]),
          h("Before a first colour", 3, "large"), lst(["A patch test at least 48 hours before", "A photo of what you'd like helps", "Come with clean, dry hair"])]))],
   "xx-large", "wide", "top"), "section-brand-soft"))

kit("gloss-contact-full", G, "Gloss contact: phone, email, hours and form",
 "A contact section for a salon: the phone number, email, address and hours beside the contact form, then a map. Needs the AnyPress Blocks plugin for the map. Part of the Gloss kit.",
 "contact, phone, email, hours, map, form, gloss",
 sec("Contact us", N([cols([
   col(N([h("Call, write or drop in", 2, "xx-large"), p(f'<a href="{GTL}">' + T(GPH) + '</a>', "xx-large", None, None, GSERIF, None, raw=True, bind="phone_linked"),
          p('<a href="mailto:hello@example.com">hello@example.com</a>', None, None, None, None, None, raw=True, bind="email_linked"),
          p(GADDR, None, bind="address"), p(GHOURS, None, "secondary", bind="hours")]), "40%"),
   col(grp(N([h("Send a message", 3, "large"), form("contact", "Call " + GPH, GTL, "We reply the same day, Tuesday to Saturday.")]), "section-brand-soft", PAD_CARD, "medium", {"type": "default"}))], "xx-large", "wide", "top"),
   mapb(GADDR, GLAT, GLON, 16, "21/9")])))

# The home page: numbers, reviews and questions join the original sections.
kit_page("kit-salon", "Home page: Gloss kit, salon and beauty",
 "A complete home page for a hair salon, barber, nail bar or beauty studio in the Gloss kit: a big headline beside a photo, the price list, numbers that count up, the team, a gallery that opens full screen, reviews in a carousel, questions, the salon with a map and how to book. Apply the Gloss style for the look it was designed with.",
 "home, salon, hair, beauty, barber, nails, brows, kit, gloss",
 ["gloss-hero", "gloss-prices", "gloss-numbers", "gloss-team", "gloss-gallery", "gloss-reviews", "gloss-faq-open", "gloss-visit", "gloss-book"])

# ---------------------------------------------------------------- pages
def gloss_page(slug, title, desc, kw, parts):
    write(slug, title, desc, "anypress/pages", kw, N(parts), "core/post-content", " * Post Types: page\n")

gloss_page("gloss-page-services", "Services page: Gloss kit",
 "A Services page for a salon or beauty studio: a heading, every service with a photo and a link to its own page, the price list and reviews. Gloss kit.",
 "services, what we do, salon, hair, gloss",
 [gpage_hero("Services", "Cuts, colour, blow-dries, brows and men's cuts, with the price confirmed before we start.", "Services", [("Book online", None, GBOOK), ("See prices", "outline", "/prices/")]),
  sec("All services", grid([stackg([img("placeholder-tall.svg", f"Service: {n.lower()}", "4/5"), hlink(n, f"/services/{s}/", 3, "large"), p(d, None, "secondary")], "small") for n, s, d in GSERV], 3, "16rem", "x-large")),
  BODIES["gloss-reviews"], BODIES["gloss-book"]])

gloss_page("gloss-page-service", "Service page: Gloss kit (one service)",
 "A page for one service, such as a cut and style: a heading with a photo, what happens and the price by stylist, reviews, questions about it and how to book. Gloss kit; make one per service.",
 "service page, single service, salon, price, gloss",
 [gpage_hero("Cut and style", "A cut that suits your hair and the way you wear it, finished with a blow-dry.", "Services / Cut and style", [("Book online", None, GBOOK)], "Services: a stylist cutting long dark hair"),
  BODIES["gloss-service-detail"], BODIES["gloss-reviews"],
  sec("Questions", cols([col(N([gsmall("About this service"), h("Good to know", 2, "xx-large")]), "36%"), col(accordion([
    ("How long does it take?", "About an hour, including the consultation and blow-dry."),
    ("Should I come with clean hair?", "No need. We wash it first, every time."),
    ("Can I keep my length?", "Yes. Tell us what you want to keep and we'll show you before we cut."),
    ("How often should I come back?", "Every six to ten weeks for most cuts, sooner for short styles.")]))], "xx-large", "wide", "top")),
  BODIES["gloss-book"]])

gloss_page("gloss-page-about", "About page: Gloss kit",
 "An About page for a salon or beauty studio: a heading, the salon's story beside a photo, numbers that count up, the team, a gallery and the salon with a map. Gloss kit.",
 "about, about us, salon, story, team, gloss",
 [gpage_hero("About the salon", "Four people, six chairs and a promise that you'll know the price before we start.", "About"),
  sec("Story", cols([
    col(N([h("A salon where colour grows out beautifully", 2, "xx-large"),
           p("Nadia opened Elm Studio in 2012 after eight years colouring hair for photo shoots. She wanted a salon where people left with colour that still looked good in three months, not just three days.", "large"),
           p("Fourteen years on, the team is four, the chairs are by the window, and most new clients come because a friend sent them.")]), "50%", valign="center"),
    col(img("placeholder-tall.svg", "Inside the salon: red chairs and plants by a tall window", "4/5"))], "xx-large", "wide", "center")),
  BODIES["gloss-numbers"], BODIES["gloss-stylists"], BODIES["gloss-gallery"], BODIES["gloss-visit"]])

gloss_page("gloss-page-reviews", "Reviews page: Gloss kit",
 "A Reviews page for a salon: a heading, reviews as cards with stars, names and what each client had done, numbers that count up and how to book. Gloss kit; use real reviews, with permission.",
 "reviews, testimonials, clients, stars, gloss",
 [gpage_hero("Reviews", "4.9 stars from 640 clients. Here's what some of them say.", "Reviews", [("Book online", None, GBOOK)]),
  sec("All reviews", grid([greview(*r) for r in GREVIEWS + [
    ("I've had the same colour for six years and finally tried something new. Nadia talked me through it and I love it.", "Rachel H.", "Colour with Nadia"),
    ("Bea's lash lift lasted eight weeks. I've stopped wearing mascara.", "Mia C.", "Lash lift with Bea"),
    ("They even remembered how I like my coffee.", "Ruth S.", "Blow-dry with Jess")]], 3, "18rem", "medium"), "section-brand-soft"),
  BODIES["gloss-numbers"], BODIES["gloss-book"]])

gloss_page("gloss-page-areas", "Team page: Gloss kit",
 "A Team page for a salon: a heading, every stylist with a link to their own page, a gallery and reviews. Gloss kit.",
 "team, stylists, people, staff, gloss",
 [gpage_hero("Our team", "Book the person, not just the time. Each of us has the things we love doing most.", "Team"),
  BODIES["gloss-stylists"], BODIES["gloss-gallery"], BODIES["gloss-reviews"]])

gloss_page("gloss-page-area", "Stylist page: Gloss kit (one stylist)",
 "A page for one stylist: a heading with their portrait, what they love doing, their prices, a client's quote, reviews and how to book. Gloss kit; make one per stylist.",
 "stylist, team member, profile, gloss",
 [gpage_hero("Nadia", "Owner and colour director. Balayage, grey blending and colour corrections.", "Our team / Nadia", [("Book with Nadia", None, GBOOK)], "Our team: Nadia in the salon"),
  BODIES["gloss-stylist"], BODIES["gloss-gallery"], BODIES["gloss-book"]])

gloss_page("gloss-page-offers", "Offers page: Gloss kit",
 "An Offers page for a salon: a heading, ways to save, the price list, questions and how to book. Gloss kit; keep the offers current.",
 "offers, discounts, gift cards, gloss",
 [gpage_hero("Offers", "20% off your first visit, $20 off for you and a friend, and gift cards for anyone.", "Offers"),
  BODIES["gloss-offers"], BODIES["gloss-prices"], BODIES["gloss-faq-open"]])

gloss_page("gloss-page-join", "Book page: Gloss kit",
 "A Book page for a salon: a heading, the appointment form beside what happens next, the team and reviews. Gloss kit; put the site's form in the named Form group.",
 "book, booking, appointment, gloss",
 [gpage_hero("Book an appointment", "Tell us what you'd like and when suits you, and we'll reply with a time and the price.", "Book"),
  BODIES["gloss-book-form"], BODIES["gloss-stylists"], BODIES["gloss-reviews"]])

gloss_page("gloss-page-prices", "Prices page: Gloss kit",
 "A Prices page for a salon: a heading, the full price list, ways to save and how to book. Gloss kit; use the salon's real prices.",
 "prices, price list, menu, costs, gloss",
 [gpage_hero("Prices", "Prices depend on hair length and the stylist's level. We always confirm before we start.", "Prices", [("Book online", None, GBOOK)]),
  BODIES["gloss-prices"], BODIES["gloss-offers"], BODIES["gloss-book"]])

gloss_page("gloss-page-faq", "Questions page: Gloss kit",
 "A Questions page for a salon: answers that open and close, grouped into booking, colour and visiting, and how to book. Gloss kit; answer the real questions.",
 "faq, questions, answers, patch test, cancellation, gloss",
 [gpage_hero("Questions", "Booking, colour and visiting, answered plainly.", "FAQ"),
  sec("Questions", N([N([h(group_t, 2, "xx-large"), accordion(qs)]) for group_t, qs in [
    ("Booking", [
      ("What if I need to cancel?", "Please give us 24 hours' notice. Missed appointments may be charged half the price."),
      ("Can I book a particular stylist?", "Yes. Choose them when you book, or ask for whoever is free first.")]),
    ("Colour", [
      ("Do I need a patch test?", "Yes, for any colour or lash tint if you're new to us or it's been six months. It takes five minutes, at least 48 hours before."),
      ("Can you fix colour done elsewhere?", "Usually, yes. Book a free consultation with Nadia first.")]),
    ("Visiting", [
      ("Is there parking?", "Yes, free, behind the salon."),
      ("Can I bring my child?", "Children are welcome for their own cuts. For long colour appointments, it's best to come alone.")])]]),
    content="56rem"),
  BODIES["gloss-book"]])

gloss_page("gloss-page-careers", "Careers page: Gloss kit",
 "A Careers page for a salon: a heading, why people work there, the open roles with pay, the application form and the salon with a map. Gloss kit; keep the roles current and put the site's form in the named Form group.",
 "careers, jobs, hiring, stylist, apprentice, gloss",
 [gpage_hero("Careers", "A small salon that pays for your training and fills your column. Pay is on this page.", "Careers", [("See open roles", None, "#apply")]),
  BODIES["gloss-jobs"], BODIES["gloss-visit"]])

gloss_page("gloss-page-contact", "Contact page: Gloss kit",
 "A Contact page for a salon: a heading, the phone number, email, address and hours beside the contact form, a map and questions. Gloss kit; put the site's contact form in the named Form group.",
 "contact, phone, email, hours, gloss",
 [gpage_hero("Contact", "Call the salon, send a message or drop in on Elm Street.", "Contact"),
  BODIES["gloss-contact-full"], BODIES["gloss-faq-open"]])

gloss_page("gloss-page-thanks", "Thank-you page: Gloss kit",
 "The page visitors see after sending a form: thanks, what happens next and when, and links to keep browsing. Gloss kit; send every form here.",
 "thank you, thanks, confirmation, form sent, gloss",
 [sec("Thanks", N([gsmall("Message sent"), h("Thank you. We'll be in touch soon.", 1, "xxx-large"),
    p("We'll reply within a few hours, Tuesday to Saturday. Check your email for a copy of what you sent.", "large", "secondary"),
    btns([("Back to the home page", None, "/"), ("See our services", "outline", "/services/")])]), None, ("xxx-large", "xxx-large", None, None), "56rem"),
  BODIES["gloss-reviews"]])

print("gloss ok")
