# Keystone (0.18.0): a whole website for an estate agent, realtor or property manager, written for a small agency.
# Run by kits.py after kit_frame.py, so every helper in kits.py, kits_more.py, kit_ridge.py and the kits before it is
# in scope.
#
# A brochure: forest green and brass, a sharp display serif, small monospace labels. Pages link to each other by slug:
# /homes/ and one page per home under it, /towns/ and one page per town under it, /rentals/, /selling/, /valuation/,
# /about/, /reviews/, /join-us/, /faq/, /market-notes/, /contact/, /thank-you/. Forms are named groups, as in Ridge:
# "Form: quote" asks for a free valuation, "Form: apply" is the job application.

KK = "anypress/kit-real-estate"
KSERIF = "gloock"
KPH = "(845) 555-0117"
KTL = "tel:8455550117"
KVAL = "/valuation/"
KADDR = "38 East Market Street, Rhinebeck, NY 12572"
KLAT, KLON = 41.9268, -73.9124
KHOURS = "Monday to Saturday, 9am to 6pm. Sundays by appointment."

def khead(label, title, link=None, size="xx-large"):
    left = stackg([mono(label, "primary"), h(title, 2, size)])
    return row([left, btns([(link[0], "outline", link[1])])] if link else [left], valign="bottom")

def k_buttons():
    """The header's button: the free valuation, everywhere."""
    return '<!-- wp:buttons {"layout":{"type":"flex","flexWrap":"nowrap"}} -->\n<div class="wp-block-buttons"><!-- wp:button -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="' + KVAL + '">' + T("Valuation") + '</a></div>\n<!-- /wp:button --></div>\n<!-- /wp:buttons -->'

def kwide(markup):
    """An image that fills its column even when the photo is narrower than the page."""
    return (markup.replace('"scale":"cover"}', '"scale":"cover","width":"100%"}', 1)
                  .replace('class="wp-block-image size-large"', 'class="wp-block-image size-large is-resized"', 1)
                  .replace('object-fit:cover"', 'object-fit:cover;width:100%;height:auto"', 1))

def kpage_hero(title, text, crumb=None, buttons=None, alt=None):
    words = N(([mono(crumb, "primary")] if crumb else []) + [h(title, 1, "xxx-large", None, None, {"lineHeight": "1.05"}), p(text, "large")] + ([btns(buttons)] if buttons else []))
    head = sec("Page hero", grp(words, gap="medium", layout={"type": "constrained", "contentSize": "52rem", "justifyContent": "left"}), "section-tint", ("xx-large", "x-large", None, None), "80rem")
    if not alt:
        return head
    return N([head, sec("Page photo", kwide(img("placeholder-wide.svg", alt, "21/9")), "section-tint", (None, "x-large", None, None), "80rem")])

def kfact(label, value):
    """A label in monospace and its value on one line; never wraps in a narrow card."""
    return grp(N([mono(label), p(value)]), layout={"type": "flex", "flexWrap": "nowrap", "justifyContent": "space-between", "verticalAlignment": "top"}, gap="small")

def kcard(inner, style="section-tint", gap="medium"):
    return grp(N(inner), style, PAD_CARD, gap, {"type": "default"})

# ---------------------------------------------------------------- content
KHOMES = [
    ("12 Orchard Lane", "12-orchard-lane", "Rhinebeck", "Just listed", "$485,000", "3 bed · 2 bath · 1,850 sq ft"),
    ("4 Mill Road", "4-mill-road", "Kingston", "Open house Sunday", "$629,000", "4 bed · 3 bath · 2,400 sq ft"),
    ("The Old Rectory", "the-old-rectory", "Hudson", "Price reduced", "$1,150,000", "5 bed · 4 bath · 3,900 sq ft"),
    ("27 Tinker Street", "27-tinker-street", "Woodstock", "New price", "$549,000", "3 bed · 2 bath · 1,700 sq ft"),
    ("9 River View Drive", "9-river-view-drive", "Saugerties", "Just listed", "$415,000", "3 bed · 1 bath · 1,400 sq ft"),
    ("2 Church Street", "2-church-street", "Rhinebeck", "Under offer", "$725,000", "4 bed · 3 bath · 2,600 sq ft"),
]
KTOWNS = [("Rhinebeck", "rhinebeck", "A village of old inns, a Sunday market and the county fair."),
          ("Kingston", "kingston", "The old state capital, with a busy uptown and a waterfront."),
          ("Hudson", "hudson", "Antique shops, restaurants and the Amtrak station on Warren Street."),
          ("Woodstock", "woodstock", "Artists, music and walks in the Catskills from your door.")]
KTEAM = [("Claire Hollis", "Broker and owner", "Grew up in Rhinebeck and has sold homes here since 2003."),
         ("Ana Mensah", "Licensed agent", "Kingston and Saugerties, first-time buyers and rentals.")]
KREVIEWS = [
    ("Claire priced our house honestly, and it sold in nine days for more than we asked.", "Laura and Ben T.", "Sold in Rhinebeck"),
    ("Ana found us a rental in two weeks, from three hours away, and sent videos of every room.", "Marcus D.", "Rented in Kingston"),
    ("They answer the phone. That sounds small until you've tried other agents.", "Joan F.", "Bought in Hudson"),
    ("Claire told us which repairs mattered and which didn't. It saved us thousands.", "Sam and Priya K.", "Sold in Woodstock"),
    ("First home, no idea what we were doing. Ana walked us through every step.", "Ella W.", "Bought in Saugerties"),
    ("Our tenants are happy and we never hear about a dripping tap. That's the point.", "Robert M.", "Rental owner"),
]

def kreview(text, name, what, size="medium"):
    return grp(N([p("★★★★★", None, "primary"), p("“" + text + "”", size, None, None, None, {"lineHeight": "1.45"}), mono(f"{name} · {what}")]),
               "section-card", PAD_CARD, "small", {"type": "default"})

# ---------------------------------------------------------------- sections
kit("keystone-topbar", KK, "Keystone top bar: the free valuation and the phone number",
 "A thin bar above the header with the free valuation offer and a link to it, and the office phone number. Part of the Keystone kit.",
 "top bar, announcement, valuation, phone, header, keystone",
 grp(row([p(T("Thinking of selling? Free valuation in writing") + f' · <a href="{KVAL}">' + T("Book one") + '</a>', "small", None, None, None, None, raw=True),
          p(T("Call the office") + f' <a href="{KTL}">' + T(KPH) + '</a>', "small", None, None, None, None, raw=True)], gap="small"),
     "section-brand", ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Top bar"))

KHEADER = grp(N([
    BODIES["keystone-topbar"],
    grp(row([
        row([dyn("site-logo", {"width": 36, "shouldSyncIcon": True}), dyn("site-title", {"level": 0, "fontSize": "large", "fontFamily": KSERIF, "style": {"typography": {"lineHeight": "1"}}})], "left", "small", False, "center"),
        row([dyn("navigation", {"overlayMenu": "mobile", "layout": {"type": "flex", "justifyContent": "right"}}), k_buttons()], "right", "medium", False, "center")], "space-between", "medium", False, "center"),
        None, ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Main bar").replace(
        '<!-- wp:group {', '<!-- wp:group {"backgroundColor":"base",', 1).replace('class="wp-block-group alignfull', 'class="wp-block-group alignfull has-base-background-color has-background', 1),
]), "sticky", None, "0", {"type": "default"}, align="full", name="Header")
write("keystone-header", "Keystone header: valuation offer, menu and a Valuation button",
 "A site header for an estate agent, realtor or property manager that stays at the top while visitors scroll: a bar with the free valuation and the phone number, then the logo, the menu (with dropdowns for homes and towns) and a Valuation button. Part of the Keystone kit; choose it for the header in the Site Editor.",
 "header", "header, menu, navigation, sticky, valuation, phone, real estate, keystone", KHEADER, "core/template-part/header")

# The record, now as numbers that count up.
kit("keystone-numbers", KK, "Keystone numbers: the agency's record",
 "Four numbers that count up as they scroll into view, showing the agency's record (homes sold, days on the market, asking price achieved, reviews). Needs the AnyPress Blocks plugin. Part of the Keystone kit; use real, current figures.",
 "numbers, statistics, record, proof, results, counter, keystone",
 sec("Record", grid([stackg([counter(n, sfx, "", "xxx-large", KSERIF, d).replace('"fontWeight":"900"', '"fontWeight":"400"'), p(lbl, None, "secondary")], "x-small") for n, sfx, d, lbl in
     [(340, "", 0, "homes sold since 2019"), (21, " days", 0, "on the market, on average"), (98, "%", 0, "of asking price achieved"), (4.9, " / 5", 1, "from 210 reviews")]], 4, "12rem", "large"),
   "section-tint", ("x-large", "x-large", None, None)))

kit("keystone-reviews", KK, "Keystone reviews: a carousel of what clients say",
 "Buyers, sellers and landlords in their own words, in a carousel, three at a time on a computer and one on a phone, with five stars and what each client did. Needs the AnyPress Blocks plugin. Part of the Keystone kit; use real reviews, with permission.",
 "reviews, testimonials, clients, stars, carousel, keystone",
 sec("Reviews", N([khead("Reviews", "4.9 from 210 buyers and sellers", ("All reviews", "/reviews/")),
                   carousel([kreview(*r) for r in KREVIEWS], 3, "Client reviews")])))

kit("keystone-faq-open", KK, "Keystone questions: answers that open and close",
 "The questions buyers and sellers ask first, as answers that open and close, beside a heading and a link to all questions. Part of the Keystone kit; answer the real questions.",
 "faq, questions, buying, selling, fees, accordion, keystone",
 sec("Questions", cols([
   col(N([mono("Before you call", "primary"), h("Good to know", 2, "xx-large"), p("Something else? Call the office and ask for Claire.", None, "secondary"), btns([("All questions", "outline", "/faq/")])]), "36%"),
   col(accordion([
     ("What do you charge to sell?", "5% of the sale price, shared with the buyer's agent, and nothing at all if your home doesn't sell."),
     ("How long will it take to sell?", "Homes we price well sell in about three weeks here. We'll tell you honestly if yours might take longer."),
     ("Do I pay you to help me buy?", "No. As a buyer, our fee is paid by the seller."),
     ("Do you manage rentals?", "Yes, about sixty homes across the valley, from finding tenants to fixing the boiler."),
     ("Is the valuation really free?", "Yes. Claire visits, writes it up within two days, and there's no obligation.")]))], "xx-large", "wide", "top")))

kit("keystone-visit", KK, "Keystone office: the address and hours, with a map",
 "Where the office is, with the address, opening hours and parking beside a map. Needs the AnyPress Blocks plugin for the map. Part of the Keystone kit.",
 "office, visit, location, address, hours, map, keystone",
 sec("Office", cols([
   col(N([mono("The office", "primary"), h("On East Market Street", 2, "xx-large"), p(KADDR, "large", bind="address"),
          lst(["Monday to Saturday, 9am to 6pm", "Sundays by appointment", "Parking behind the building", "Listings in the window, day and night"])]), "40%"),
   col(mapb(KADDR, KLAT, KLON, 15, "4/3"))], "xx-large", "wide", "center")))

kit("keystone-signup", KK, "Keystone signup: new homes by email",
 "A band asking visitors to join the email list for new listings before they reach the big websites, with the signup form beside it. Part of the Keystone kit; sits above the footer on every page.",
 "newsletter, signup, email, new listings, alerts, keystone",
 sec("Signup", cols([
   col(N([h("New homes, a day early", 2, "xx-large"), p("New listings by email the day before they reach the big property websites. Once a week at most. Unsubscribe any time.", None, "secondary")]), "55%", valign="center"),
   col(form("newsletter", "See homes for sale", "/homes/"), valign="center")], "x-large", "wide", "center"), "section-tint", ("x-large", "x-large", None, None)))

KPOP = popup("offer", N([
    img("placeholder-wide.svg", "A stone house with a green lawn", "16/9"),
    grp(N([mono("Thinking of selling?", "primary"), h("What is your home worth today?", 2, "xx-large"),
           p("Leave your email and we'll send this month's prices for your town, and book a free valuation if you'd like one."),
           form("offer", "Book a valuation", KVAL)]), None, (None, None, "large", "large"), "small", {"type": "default"})]),
    label="What is your home worth today?")
kit("keystone-popup", KK, "Keystone popup: what your home is worth",
 "A popup that opens five seconds into a first visit with a photo, an offer of local prices and a free valuation, and one field for an email address; it closes with its button, Escape or a click outside and stays closed for two weeks. Needs the AnyPress Blocks plugin. Part of the Keystone kit; put it in the footer to show it on every page.",
 "popup, valuation, offer, newsletter, email, modal, keystone", KPOP)

KFOOT = grp(N([
    BODIES["keystone-signup"],
    grp(N([cols([
        col(N([dyn("site-title", {"level": 0, "fontSize": "x-large", "fontFamily": KSERIF, "style": {"typography": {"lineHeight": "1"}}}),
               p("Homes bought, sold and rented in the Hudson Valley since 2003.", None, "main-accent"),
               p(f'<a href="{KTL}">' + T(KPH) + '</a>', "x-large", None, None, KSERIF, None, raw=True, bind="phone_linked"),
               social(["instagram", "facebook", "youtube"])]), "34%"),
        col(flinks("Homes", [("Homes for sale", "/homes/"), ("Rentals", "/rentals/"), ("Selling", "/selling/"), ("Free valuation", KVAL)] + [(n, f"/towns/{s}/") for n, s, _ in KTOWNS])),
        col(flinks("The agency", [("About us", "/about/"), ("Reviews", "/reviews/"), ("Join us", "/join-us/"), ("Questions", "/faq/"), ("Market notes", "/market-notes/"), ("Contact", "/contact/")])),
        col(N([h("Visit", 3, "medium"), p(KADDR, None, "main-accent", bind="address"), p(KHOURS, None, "main-accent", bind="hours"),
               btns([("Valuation", None, KVAL)])]))], "large", "wide", "top"),
        sep(),
        row([p("© Hollis & Co. Licensed real estate broker, New York. Equal housing opportunity.", "small", "main-accent"),
             p('<a href="/privacy-policy/">' + T("Privacy") + '</a> · <a href="/faq/">' + T("Fair housing") + '</a>', "small", "main-accent", None, None, None, raw=True)], gap="small")]),
        "section-dark", ("x-large", "large", None, None), "large", {"type": "constrained", "contentSize": "80rem"}, align="full", name="Footer columns"),
    KPOP,
]), None, None, "0", {"type": "default"}, align="full", name="Footer")
write("keystone-footer", "Keystone footer: new homes by email, links and the valuation popup",
 "A site footer for an estate agent, realtor or property manager: a band for the email list, then the phone number, home and agency links and the office address on dark, and the valuation popup (needs the AnyPress Blocks plugin). Part of the Keystone kit; choose it for the footer in the Site Editor.",
 "footer", "footer, links, office, newsletter, phone, popup, real estate, keystone", KFOOT, "core/template-part/footer")

kit("keystone-home-detail", KK, "Keystone home: the description, the facts and the photos",
 "The body of a page for one home: what makes it special, its features, a card with the price and facts and a button to book a viewing, then four photos that open full screen. Part of the Keystone kit; make one per listing.",
 "listing, property, home for sale, details, viewing, gallery, keystone",
 sec("Home details", N([cols([
   col(N([h("A bright farmhouse on a quiet lane", 2, "xx-large"),
          p("Built in 1920 and lovingly updated, this farmhouse sits at the end of a quiet lane, a ten-minute walk from the village. The kitchen opens onto a deep porch, the living room has the original fireplace, and the half-acre garden backs onto an old apple orchard.", "medium"),
          h("What you'll love", 3, "large"),
          lst(["The wraparound porch", "Original wide-plank floors", "A kitchen redone in 2022", "Half an acre, backing onto an orchard", "Walk to the village and the farmers' market"])]), "58%"),
   col(kcard([mono("At a glance", "primary"), p("$485,000", "xx-large", None, None, KSERIF, {"lineHeight": "1.05"}), kfact("Bedrooms", "3"), kfact("Bathrooms", "2"), kfact("Size", "1,850 sq ft"), kfact("Land", "0.5 acres"), kfact("Taxes", "$7,900 a year"),
              btns([("Book a viewing", None, "/contact/"), ("Call", "outline", KTL)])]))], "xx-large", "wide", "top"),
   grid([zoom(img("placeholder-wide.svg", a, "4/3")) for a in ["This home: the living room", "This home: the kitchen", "This home: a bedroom", "This home: the porch"]], 2, "18rem", "medium")]), content="80rem"))

kit("keystone-all-homes", KK, "Keystone homes for sale: every listing",
 "Every home for sale as a card with a photo that opens full screen, its status, price, address (linking to its own page) and the facts. Part of the Keystone kit; remove a home when it sells.",
 "listings, homes for sale, properties, all homes, keystone",
 sec("Homes for sale", N([khead("For sale", "Homes for sale now", ("Sell with us", "/selling/")),
   grid([listing("placeholder-wide.svg", f"Home for sale: {n}", st, pr, f"{n}, {t}", fa, f"/homes/{s}/") for n, s, t, st, pr, fa in KHOMES], 3, "16rem", "large")])))

kit("keystone-towns", KK, "Keystone towns: where we sell",
 "The towns the agency covers, each with a photo, a line about it and a link to its own guide. Part of the Keystone kit; list the towns you really know.",
 "towns, areas, neighborhoods, communities, guides, keystone",
 sec("Towns", N([khead("Where we sell", "Know the town before you move"), grid([stackg([img("placeholder-wide.svg", f"Town: {n}", "4/3"), hlink(n, f"/towns/{s}/", 3, "x-large"), p(d, None, "secondary")]) for n, s, d in KTOWNS], 4, "13rem", "large")])))

kit("keystone-town", KK, "Keystone town guide: living there, prices and commutes",
 "The body of a page for one town: what it's like to live there, a card with prices, commute and schools, and the places locals love. Part of the Keystone kit; make one per town.",
 "town guide, neighborhood, area, community, living, keystone",
 sec("Town guide", cols([
   col(N([h("Living in Rhinebeck", 2, "xx-large"),
          p("Rhinebeck is a village of old inns, bookshops and a Sunday farmers' market, with the Hudson a short drive west. Most homes are within a walk of the village, and the county fair arrives every August.", "medium"),
          h("What locals love", 3, "large"), lst(["The Sunday farmers' market", "Upstate Films, the little cinema", "Walks at Poets' Walk park", "The Dutchess County Fair"])]), "58%"),
   col(kcard([mono("Rhinebeck in numbers", "primary"), kfact("Typical home", "$575,000"), kfact("To New York City", "2 hours by train"), kfact("Schools", "Rhinebeck Central"), kfact("Homes we sold", "64 since 2019"),
              btns([("Homes in Rhinebeck", None, "/homes/")])]))], "xx-large", "wide", "top"), content="80rem"))

kit("keystone-team", KK, "Keystone team: the agents, with how to reach them",
 "Every agent with a portrait, their role, a line about them and direct contact details. Part of the Keystone kit; use the real team.",
 "team, agents, realtors, staff, people, keystone",
 sec("Team", N([khead("The team", "Two agents, one phone that gets answered"), grid([stackg([img("placeholder-tall.svg", f"Agent: {n}", "4/5"), h(n, 3, "x-large"), mono(r, "primary"), p(d, None, "secondary")]) for n, r, d in KTEAM], 2, "16rem", "x-large")]), content="56rem"))

kit("keystone-sell", KK, "Keystone selling: how we sell, step by step",
 "How the agency sells a home, in four numbered steps, beside a card with the fee and what it includes. Part of the Keystone kit; state the real fee.",
 "selling, sell your home, fees, process, steps, keystone",
 sec("Selling", cols([
   col(N([khead("Selling with us", "Four steps from valuation to keys"),
          grid([stackg([p(n, "xx-large", "primary", None, KSERIF, {"lineHeight": "1"}), h(t, 3, "large"), p(d, None, "secondary")]) for n, t, d in [
            ("1", "A free valuation", "Claire visits, looks at what's sold nearby and gives you a price in writing."),
            ("2", "Photos and a floor plan", "Professional photos, a floor plan and a short film, all included."),
            ("3", "Viewings we host", "We show every buyer around ourselves, evenings and weekends too."),
            ("4", "Offer to keys", "We handle the offers, the inspection and the lawyers until you hand over the keys.")]], 2, "14rem", "large")]), "60%"),
   col(kcard([mono("Our fee", "primary"), p("5%", "xxx-large", None, None, KSERIF, {"lineHeight": "1"}), p("of the sale price, shared with the buyer's agent. Nothing at all if your home doesn't sell."),
              lst(["Photos, floor plan and film", "Every viewing hosted", "Listed on every major website", "No upfront costs"]),
              btns([("Book a free valuation", None, KVAL)])]))], "xx-large", "wide", "top")))

kit("keystone-rentals", KK, "Keystone rentals: homes to rent and property management",
 "Homes to rent as cards with a photo, monthly rent, address and facts, beside what the agency does for landlords and its fee. Part of the Keystone kit; keep the rentals current.",
 "rentals, to rent, lettings, landlords, property management, keystone",
 sec("Rentals", N([khead("To rent", "Homes to rent now"),
   grid([listing("placeholder-wide.svg", a, st, pr, ad, fa, "/contact/") for a, st, pr, ad, fa in [
     ("Rental: an apartment with a big window", "Available now", "$2,100 a month", "Apartment 3, 41 Wall Street, Kingston", "2 bed · 1 bath · 900 sq ft"),
     ("Rental: a cottage by the river", "Available March 1", "$2,650 a month", "8 Ferry Road, Saugerties", "2 bed · 1 bath · 1,100 sq ft"),
     ("Rental: a family house with a garden", "Available April 1", "$3,200 a month", "15 Elm Street, Rhinebeck", "3 bed · 2 bath · 1,600 sq ft")]], 3, "16rem", "large"),
   kcard([cols([col(N([h("For landlords", 2, "xx-large"), p("We find and check tenants, collect the rent, handle repairs with local trades we trust, and send you a statement every month.", "medium")]), "60%"),
                col(N([kfact("Tenant finding", "One month's rent"), kfact("Full management", "8% of the rent"), btns([("Talk to Ana", None, "/contact/")])]))], "x-large", "wide", "center")])])))

kit("keystone-jobs", KK, "Keystone careers: why join and the open roles",
 "Why agents and staff work at the agency, each open role with its pay, and the application. Part of the Keystone kit; keep the roles current and put the site's application form in the named Form group.",
 "careers, jobs, hiring, agent, realtor, apply, keystone",
 sec("Join us", N([
   khead("Join us", "A small agency that shares its leads"),
   grid([stackg([h(t, 3, "large"), p(d, None, "secondary")]) for t, d in [
     ("Shared leads", "Every enquiry is shared fairly, not kept by whoever answered the phone."),
     ("A good split", "Agents keep 70% of their commission from day one."),
     ("Paid licensing", "We pay for your licensing course and your first year of fees."),
     ("Weekends off", "We take turns, so you get most weekends with your family.")]], 4, "13rem"),
   '<!-- wp:spacer {"height":"var:preset|spacing|large"} -->\n<div style="height:var(--wp--preset--spacing--large)" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->',
   h("Open roles", 2, "xx-large"),
   N([grp(N([row([h(t, 3, "large"), mono(when, "primary")], valign="center"), p(d, None, "secondary"), btns([("Apply for this", None, "#apply")])]), "section-tint", PAD_CARD, "small", {"type": "default"}) for t, when, d in [
     ("Licensed agent", "Full time, commission plus a $2,000 monthly draw", "A New York licence or the will to get one, and a car. We'll teach you the valley."),
     ("Office manager", "Full time, $24 an hour", "Run the diary, the listings and the office. Real estate experience helps.")]]),
   grp(N([h("Apply", 2, "xx-large"), p("Tell us a little about you and why real estate. We reply to everyone within a week."),
          form("apply", "Email the office", "mailto:jobs@example.com")]), "section-card", PAD_CARD, "small", {"type": "default"}, anchor="apply")])))

kit("keystone-valuation-form", KK, "Keystone valuation: the form and what happens next",
 "A form to book a free valuation, beside what happens next and what helps to have ready. Part of the Keystone kit; put the site's form in the named Form group.",
 "valuation, appraisal, sell, form, keystone",
 sec("Valuation", cols([
   col(kcard([h("Book a free valuation", 2, "xx-large"), p("Tell us about your home and when suits you. Claire will call to book a visit, and send the price in writing within two days of it."),
              form("quote", "Call " + KPH, KTL, "Rather talk now? Call the office.")], "section-card"), "58%"),
   col(N([h("What happens next", 3, "large"),
          lst(["Claire calls to book a time", "A visit of about an hour", "A written price within two days"]),
          h("Helpful to have ready", 3, "large"), lst(["Any work done, and when", "Your tax bill", "When you'd like to move"])]))],
   "xx-large", "wide", "top"), "section-tint"))

kit("keystone-contact-full", KK, "Keystone contact: phone, email, office and form",
 "A contact section for an agency: the phone number, email, address and hours beside the contact form, then a map. Needs the AnyPress Blocks plugin for the map. Part of the Keystone kit.",
 "contact, phone, email, office, map, form, keystone",
 sec("Contact us", N([cols([
   col(N([h("Call, write or drop in", 2, "xx-large"), p(f'<a href="{KTL}">' + T(KPH) + '</a>', "xx-large", None, None, KSERIF, None, raw=True, bind="phone_linked"),
          p('<a href="mailto:hello@example.com">hello@example.com</a>', None, None, None, None, None, raw=True, bind="email_linked"),
          p(KADDR, None, bind="address"), p(KHOURS, None, "secondary", bind="hours")]), "40%"),
   col(kcard([h("Send a message", 3, "large"), form("contact", "Call " + KPH, KTL, "We reply the same day, Monday to Saturday.")]))], "xx-large", "wide", "top"),
   mapb(KADDR, KLAT, KLON, 15, "21/9")])))

# The home page: the record now counts up; reviews, questions and the office with a map join the original sections.
kit_page("kit-real-estate", "Home page: Keystone kit, real estate",
 "A complete home page for an estate agent, realtor or property manager in the Keystone kit: a home photo with buy, sell and rent, three listings whose photos open full screen, a featured home, the agency's record counting up, the agent, reviews in a carousel, questions, the office with a map and a free valuation. Apply the Keystone style for the look it was designed with.",
 "home, real estate, realtor, estate agent, property, homes for sale, rentals, kit, keystone",
 ["keystone-hero", "keystone-listings", "keystone-feature", "keystone-numbers", "keystone-agent", "keystone-reviews", "keystone-faq-open", "keystone-visit", "keystone-valuation"])

# ---------------------------------------------------------------- pages
def keystone_page(slug, title, desc, kw, parts):
    write(slug, title, desc, "anypress/pages", kw, N(parts), "core/post-content", " * Post Types: page\n")

keystone_page("keystone-page-services", "Homes for sale page: Keystone kit",
 "A Homes for sale page for an agency: a heading, every listing with a link to its own page, the towns, reviews and a free valuation. Keystone kit.",
 "homes for sale, listings, properties, buy, keystone",
 [kpage_hero("Homes for sale", "Every home we're selling now, from village houses to farmhouses with land.", "Buy", [("Book a viewing", None, "/contact/"), ("Rentals", "outline", "/rentals/")]),
  BODIES["keystone-all-homes"], BODIES["keystone-towns"], BODIES["keystone-reviews"], BODIES["keystone-valuation"]])

keystone_page("keystone-page-service", "Home for sale page: Keystone kit (one home)",
 "A page for one home for sale: a heading and a wide photo, the description, the price and facts, photos that open full screen, the agent, questions and more homes. Keystone kit; make one per listing.",
 "listing, property, home for sale, single home, keystone",
 [kpage_hero("12 Orchard Lane", "Rhinebeck · $485,000 · 3 bed, 2 bath, 1,850 sq ft", "Homes for sale / Rhinebeck", [("Book a viewing", None, "/contact/")], "This home: the farmhouse from the lane"),
  BODIES["keystone-home-detail"], BODIES["keystone-agent"], BODIES["keystone-listings"]])

keystone_page("keystone-page-about", "About page: Keystone kit",
 "An About page for an agency: a heading, the agency's story beside a photo, the record counting up, the team, reviews and the office with a map. Keystone kit.",
 "about, about us, agency, story, team, keystone",
 [kpage_hero("About us", "A small agency that answers the phone and has sold homes in the valley since 2003.", "About"),
  sec("Story", cols([
    col(N([h("Twenty-two years, one valley", 2, "xx-large"),
           p("Claire Hollis sold her first house in Rhinebeck in 2003, from a desk in her kitchen. Today the office is on East Market Street, there are two agents, and we still show every home ourselves.", "large"),
           p("We only sell where we live. That means we know which roads flood, which schools are good and what the house next door sold for.", "medium")]), "52%", valign="center"),
    col(img("placeholder-wide.svg", "Inside the office: a long table by a brick wall", "4/3"))], "xx-large", "wide", "center")),
  BODIES["keystone-numbers"], BODIES["keystone-team"], BODIES["keystone-reviews"], BODIES["keystone-visit"]])

keystone_page("keystone-page-reviews", "Reviews page: Keystone kit",
 "A Reviews page for an agency: a heading, reviews from buyers, sellers and landlords as cards, the record counting up and a free valuation. Keystone kit; use real reviews, with permission.",
 "reviews, testimonials, clients, stars, keystone",
 [kpage_hero("Reviews", "4.9 from 210 buyers, sellers and landlords. Here's what some of them say.", "Reviews", [("Book a free valuation", None, KVAL)]),
  sec("All reviews", grid([kreview(*r) for r in KREVIEWS + [
    ("We'd been told our house needed a new roof to sell. Claire said it didn't, and she was right.", "Helen P.", "Sold in Hudson"),
    ("Ana sent us a video of the house at night so we could see the street lights. Who does that?", "Chris and Dee L.", "Bought in Kingston"),
    ("Honest, patient and always on time.", "Mary O.", "Sold in Rhinebeck")]], 3, "18rem", "medium"), "section-tint"),
  BODIES["keystone-numbers"], BODIES["keystone-valuation"]])

keystone_page("keystone-page-areas", "Towns page: Keystone kit",
 "A Towns page for an agency: a heading, every town with a link to its own guide, the listings and reviews. Keystone kit.",
 "towns, areas, neighborhoods, communities, keystone",
 [kpage_hero("Towns", "We only sell where we live. Here's what each town is like.", "Towns"),
  BODIES["keystone-towns"], BODIES["keystone-listings"], BODIES["keystone-reviews"]])

keystone_page("keystone-page-area", "Town page: Keystone kit (one town)",
 "A page for one town: a heading and a wide photo, what it's like to live there with prices and commutes, homes for sale, the agent and a free valuation. Keystone kit; make one per town.",
 "town, neighborhood, area guide, community, keystone",
 [kpage_hero("Rhinebeck", "A village of old inns, a Sunday market and the county fair.", "Towns / Rhinebeck", [("Homes for sale", None, "/homes/")], "Towns: the main street in Rhinebeck"),
  BODIES["keystone-town"], BODIES["keystone-listings"], BODIES["keystone-agent"], BODIES["keystone-valuation"]])

keystone_page("keystone-page-offers", "Selling page: Keystone kit",
 "A Selling page for an agency: a heading, how the agency sells in four steps with the fee, the record counting up, reviews, questions and a free valuation. Keystone kit; state the real fee.",
 "selling, sell your home, fees, valuation, keystone",
 [kpage_hero("Selling", "A fair price, honest advice and every viewing hosted by us. No sale, no fee.", "Sell", [("Book a free valuation", None, KVAL)]),
  BODIES["keystone-sell"], BODIES["keystone-numbers"], BODIES["keystone-reviews"], BODIES["keystone-faq-open"]])

keystone_page("keystone-page-join", "Valuation page: Keystone kit",
 "A Valuation page for an agency: a heading, the form to book a free valuation beside what happens next, the record counting up and reviews. Keystone kit; put the site's form in the named Form group.",
 "valuation, appraisal, home value, sell, keystone",
 [kpage_hero("Free valuation", "What your home is worth, in writing, within two days of a visit. Free, with no obligation.", "Valuation"),
  BODIES["keystone-valuation-form"], BODIES["keystone-numbers"], BODIES["keystone-reviews"]])

keystone_page("keystone-page-rentals", "Rentals page: Keystone kit",
 "A Rentals page for an agency: a heading, homes to rent with prices, what the agency does for landlords, questions and the office with a map. Keystone kit; keep the rentals current.",
 "rentals, to rent, lettings, landlords, property management, keystone",
 [kpage_hero("Rentals", "Homes to rent across the valley, and full management for landlords.", "Rent", [("Talk to Ana", None, "/contact/")]),
  BODIES["keystone-rentals"], BODIES["keystone-faq-open"], BODIES["keystone-visit"]])

keystone_page("keystone-page-faq", "Questions page: Keystone kit",
 "A Questions page for an agency: answers that open and close, grouped into buying, selling and renting, and a free valuation. Keystone kit; answer the real questions.",
 "faq, questions, answers, buying, selling, renting, keystone",
 [kpage_hero("Questions", "Buying, selling and renting, answered plainly.", "Questions"),
  sec("Questions", N([N([h(group_t, 2, "xx-large"), accordion(qs)]) for group_t, qs in [
    ("Buying", [
      ("Do I pay you to help me buy?", "No. As a buyer, our fee is paid by the seller."),
      ("Can you help me get a mortgage?", "We'll introduce you to two local lenders we trust. You choose.")]),
    ("Selling", [
      ("What do you charge to sell?", "5% of the sale price, shared with the buyer's agent, and nothing at all if your home doesn't sell."),
      ("Do I need to fix things before selling?", "Usually not. Claire will tell you which repairs pay for themselves and which don't.")]),
    ("Renting", [
      ("What do I need to rent a home?", "Proof of income, references and a deposit of one month's rent."),
      ("Do you accept pets?", "Many of our landlords do. Ask about each home.")])]]),
    content="56rem"),
  BODIES["keystone-valuation"]])

keystone_page("keystone-page-careers", "Join us page: Keystone kit",
 "A Join us page for an agency: a heading, why people work there, the open roles with pay, the application form and the office with a map. Keystone kit; keep the roles current and put the site's form in the named Form group.",
 "careers, jobs, hiring, agent, realtor, keystone",
 [kpage_hero("Join us", "A small agency that shares its leads, pays your licensing and gives you weekends.", "Join us", [("See open roles", None, "#apply")]),
  BODIES["keystone-jobs"], BODIES["keystone-visit"]])

keystone_page("keystone-page-contact", "Contact page: Keystone kit",
 "A Contact page for an agency: a heading, the phone number, email, address and hours beside the contact form, a map and questions. Keystone kit; put the site's contact form in the named Form group.",
 "contact, phone, email, office, keystone",
 [kpage_hero("Contact", "Call the office, send a message or drop in on East Market Street.", "Contact"),
  BODIES["keystone-contact-full"], BODIES["keystone-faq-open"]])

keystone_page("keystone-page-thanks", "Thank-you page: Keystone kit",
 "The page visitors see after sending a form: thanks, what happens next and when, and links to keep browsing. Keystone kit; send every form here.",
 "thank you, thanks, confirmation, form sent, keystone",
 [sec("Thanks", N([mono("Message sent", "primary"), h("Thank you. We'll be in touch soon.", 1, "xxx-large", None, None, {"lineHeight": "1.05"}),
    p("We reply the same day, Monday to Saturday. Check your email for a copy of what you sent.", "large", "secondary"),
    btns([("Back to the home page", None, "/"), ("See homes for sale", "outline", "/homes/")])]), None, ("xxx-large", "xxx-large", None, None), "56rem"),
  BODIES["keystone-reviews"]])

print("keystone ok")
