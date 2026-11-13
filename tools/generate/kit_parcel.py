# Parcel (0.14.0): a whole website for an online shop or maker, written for a small pottery studio. Run by kits.py
# after kit_ledger.py, so every helper in kits.py, kits_more.py, kit_ridge.py and the kits before it is in scope.
#
# A catalogue page: a narrow serif for names, a plain sans for everything else, clay and cream. Pages link to each
# other by slug: /shop/ and one page per collection under it, /order/, /stockists/ and one page per stockist under it,
# /about/, /reviews/, /offers/, /jobs/, /help/, /journal/, /contact/, /thank-you/. Forms are named groups, as in
# Ridge: "Form: quote" orders a piece or a set, "Form: apply" is the job application.

P = "anypress/kit-shop"
PSERIF = "instrument-serif"
PORDER = "/order/"
PADDR = "191 Lyman Street, Studio 4, Asheville, NC 28801"
PLAT, PLON = 35.5868, -82.5671
PHOURS = "Wednesday to Sunday, 10am to 5pm"
PPH = "(828) 555-0147"
PTL = "tel:8285550147"

def psmall(text, color="secondary"):
    return p(text, "small", color, None, None, {"fontWeight": "600", "letterSpacing": "0.08em", "textTransform": "uppercase"})

def phead(eb, title, link=None, size="xx-large"):
    left = stackg([psmall(eb), h(title, 2, size)])
    return row([left, btns([(link[0], "outline", link[1])])] if link else [left], valign="bottom")

def p_buttons():
    """The header's buttons: Order a set and Shop on tablets and computers, just Shop on phones."""
    order = f'<!-- wp:button {j({"className": "is-style-outline", "metadata": {"blockVisibility": {"viewport": {"mobile": False}}}})} -->\n<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="{PORDER}">{T("Order a set")}</a></div>\n<!-- /wp:button -->'
    shop = f'<!-- wp:button -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/shop/">{T("Shop")}</a></div>\n<!-- /wp:button -->'
    return '<!-- wp:buttons {"layout":{"type":"flex","flexWrap":"nowrap"}} -->\n<div class="wp-block-buttons">' + N([order, shop]) + '</div>\n<!-- /wp:buttons -->'

def ppage_hero(title, text, crumb=None, buttons=None, alt=None):
    words = N(([psmall(crumb)] if crumb else []) + [h(title, 1, "xxx-large"), p(text, "large")] + ([btns(buttons)] if buttons else []))
    if not alt:
        return sec("Page hero", grp(words, gap="medium", layout={"type": "constrained", "contentSize": "48rem", "justifyContent": "left"}), "section-tint", ("xx-large", "xx-large", None, None), "72rem")
    return sec("Page hero", cols([col(words, "50%", valign="center"), col(img("placeholder-wide.svg", alt, "4/3"))], "xx-large", "wide", "center"), "section-tint", ("xx-large", "xx-large", None, None), "72rem")

# ---------------------------------------------------------------- content
PCOL = [
    ("Cups and mugs", "cups-and-mugs", "Mugs, cups and tumblers for every hand and every hot drink."),
    ("Bowls", "bowls", "Breakfast bowls, noodle bowls and big bowls for the middle of the table."),
    ("Plates", "plates", "Side plates and dinner plates in glazes that go together."),
    ("Vases", "vases", "Bud vases and moon vases for one stem or an armful."),
    ("Bottles", "bottles", "Bottles for oil, water or a single branch."),
]
PSTOCK = [("Asheville", "asheville"), ("Durham", "durham"), ("Charleston", "charleston"), ("Atlanta", "atlanta")]
PREVIEWS = [
    ("My mug is the first thing I reach for every morning. Two years in and it still looks new.", "Rosa M.", "Everyday mug"),
    ("Packed so well I almost didn't want to open it. Not one chip, all the way to Oregon.", "Tom H.", "Set of four dinner plates"),
    ("I ordered a set of eight for our wedding table. June called me to talk through the glaze.", "Aisha and Dev", "A set made to order"),
    ("The moon vase is even nicer in person. It holds one stem from the garden perfectly.", "Clare B.", "Moon vase"),
    ("We use the breakfast bowls for everything, and they've been through the dishwasher hundreds of times.", "Marcus L.", "Breakfast bowls"),
    ("Bought one at the Durham shop and came straight home to order three more online.", "Jen K.", "Ridged tumblers"),
]

def preview(text, name, piece, size="medium"):
    return grp(N([p("★★★★★", None, "primary"), p("“" + text + "”", size, None, None, None, {"lineHeight": "1.4"}),
                  p(f"{name} · {piece}", "small", "secondary", None, None, {"fontWeight": "600"})]), "section-card", PAD_CARD, "small", {"type": "default"})

def pproduct(alt, name, price, note):
    return stackg([zoom(img("placeholder-square.svg", alt, "1")), stackg([h(name, 3, "medium"), p(price), p(note, "small", "secondary")], "x-small"),
                   btns([("Order", "outline", PORDER)])])

# ---------------------------------------------------------------- sections
kit("parcel-topbar", P, "Parcel top bar: free shipping and the next sale",
 "A thin bar above the header with the free shipping line, a link to the next sale and the studio's phone number. Part of the Parcel kit; keep the sale current.",
 "top bar, announcement, shipping, sale, phone, header, parcel",
 grp(row([p(T("Free shipping on orders over $60") + ' · <a href="/offers/">' + T("Seconds sale, first weekend of every month") + '</a>', "small", None, None, None, None, raw=True),
          p(T("Questions? Call the studio") + f' <a href="{PTL}">' + T(PPH) + '</a>', "small", None, None, None, None, raw=True)], gap="small"),
     "section-second-brand", ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Top bar"))

PHEAD = grp(N([
    BODIES["parcel-topbar"],
    grp(row([
        row([dyn("site-logo", {"width": 36, "shouldSyncIcon": True}), dyn("site-title", {"level": 0, "fontSize": "x-large", "fontFamily": PSERIF, "style": {"typography": {"lineHeight": "1"}}})], "left", "small", False, "center"),
        row([dyn("navigation", {"overlayMenu": "mobile", "layout": {"type": "flex", "justifyContent": "right"}}), p_buttons()], "right", "medium", False, "center")], "space-between", "medium", False, "center"),
        None, ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Main bar").replace(
        '<!-- wp:group {', '<!-- wp:group {"backgroundColor":"base",', 1).replace('class="wp-block-group alignfull', 'class="wp-block-group alignfull has-base-background-color has-background', 1),
]), "sticky", None, "0", {"type": "default"}, align="full", name="Header")
write("parcel-header", "Parcel header: free shipping, menu and a Shop button",
 "A site header for an online shop or maker that stays at the top while visitors scroll: a bar with free shipping and the next sale, then the logo, the menu (with dropdowns for the collections and stockists), an Order a set button and a Shop button. Part of the Parcel kit; choose it for the header in the Site Editor.",
 "header", "header, menu, navigation, sticky, shop, shipping, ecommerce, parcel", PHEAD, "core/template-part/header")

kit("parcel-numbers", P, "Parcel numbers: four figures that count up",
 "Four numbers that count up as they scroll into view (pieces sent out, years at the wheel, firings, shops), each with a short line. Needs the AnyPress Blocks plugin. Part of the Parcel kit; use real figures only.",
 "numbers, statistics, counter, maker, shop, parcel",
 sec("Numbers", grid([stackg([counter(n, "", "", "xxx-large", PSERIF, 0).replace('"fontWeight":"900"', '"fontWeight":"400"'), p(lbl, None, "secondary")]) for n, lbl in
     [(12000, "pieces packed and sent since 2016"), (10, "years at the wheel"), (2, "firings for every piece"), (14, "shops and cafés that stock us")]], 4, "13rem", "x-large"), "section-tint"))

kit("parcel-making", P, "Parcel how it's made: four steps",
 "How every piece is made, in four numbered steps from the wheel to the second firing. Part of the Parcel kit; one sentence each.",
 "process, how it's made, handmade, steps, craft, parcel",
 sec("How it's made", N([phead("How it's made", "Four times through our hands"), grid([stackg([p(n, "xx-large", "primary", None, PSERIF, {"lineHeight": "1"}), sep(), h(t, 3, "large"), p(d, None, "secondary")]) for n, t, d in [
    ("01", "Thrown", "Each piece starts as a ball of clay on the wheel, in our studio by the river."),
    ("02", "Trimmed", "A day later, leather hard, it's trimmed by hand and gets its handle or foot."),
    ("03", "Fired once", "A slow first firing turns clay into something we can glaze."),
    ("04", "Glazed and fired again", "Dipped by hand, then fired to 2,300°F. Tough enough for every day.")]], 4, "13rem", "x-large")])))

kit("parcel-reviews", P, "Parcel reviews: a carousel of what buyers say",
 "Buyers in their own words, in a carousel, three at a time on a computer and one on a phone, with five stars, each buyer's name and what they bought. Needs the AnyPress Blocks plugin. Part of the Parcel kit; use real reviews, with permission.",
 "reviews, testimonials, customers, stars, carousel, parcel",
 sec("Reviews", N([phead("Reviews", "Loved in kitchens from here to Oregon", ("All reviews", "/reviews/")),
                   carousel([preview(*r) for r in PREVIEWS], 3, "Customer reviews")]), "section-tint"))

kit("parcel-faq-open", P, "Parcel questions: shipping, returns and care",
 "The questions shoppers ask before they buy, about shipping, returns and care, as answers that open and close, beside a heading and a link to all questions. Part of the Parcel kit; put the shop's real policies here.",
 "faq, questions, shipping, returns, care, accordion, parcel",
 sec("Questions", cols([
   col(N([psmall("Good to know"), h("Shipping, returns and care", 2, "xx-large"), p("Something else? Send us a note and June or Ellie will reply the same day.", None, "secondary"), btns([("All questions", "outline", "/help/")])]), "36%"),
   col(accordion([
     ("How long does shipping take?", "We pack orders in two working days. Most arrive three to five days after that, anywhere in the US."),
     ("What if something arrives broken?", "Send us a photo within a week and we'll send a new one or refund you, whichever you'd like."),
     ("Can I return a piece?", "Yes, within 30 days if it's unused. We'll send a free return label."),
     ("Is it safe in the dishwasher?", "Yes. Everything is fired to 2,300°F and is safe in the dishwasher and the microwave."),
     ("Do you ship outside the US?", "To Canada and the UK, yes. Shipping is worked out at checkout.")]))], "xx-large", "wide", "top")))

kit("parcel-studio", P, "Parcel studio shop: where to visit, with a map",
 "The studio shop's address, opening days and what's there, beside a map. Needs the AnyPress Blocks plugin for the map. Part of the Parcel kit.",
 "studio, shop, visit, location, address, map, parcel",
 sec("Studio shop", cols([
   col(N([psmall("Visit the studio"), h("Come and see the wheel", 2, "xx-large"), p(PADDR, "large", bind="address"),
          lst([PHOURS, "Seconds at half price on the back shelf", "Watch us throw on Saturday mornings"])]), "40%"),
   col(mapb(PADDR, PLAT, PLON, 15, "4/3"))], "xx-large", "wide", "center")))

kit("parcel-signup", P, "Parcel signup: new pieces first, by email",
 "A band asking visitors to join the email list to hear about new pieces and sales first, with the signup form beside it. Part of the Parcel kit; sits above the footer on every page.",
 "newsletter, signup, email, new pieces, sale, parcel",
 sec("Signup", cols([
   col(N([h("Hear about new pieces first", 2, "xx-large"), p("One email when a new batch comes out of the kiln, usually twice a month. The seconds sale dates too.", None, "secondary")]), "55%", valign="center"),
   col(form("newsletter", "See the offers", "/offers/"), valign="center")], "x-large", "wide", "center"), "section-brand-soft", ("x-large", "x-large", None, None)))

PPOP = popup("offer", N([
    img("placeholder-wide.svg", "A mug of coffee beside a vase of flowers", "16/9"),
    grp(N([psmall("Welcome"), h("10% off your first order", 2, "xx-large"),
           p("Join the list for new pieces and sale dates, and we'll send a code for 10% off your first order."),
           form("offer", "See the offers", "/offers/")]), None, (None, None, "large", "large"), "small", {"type": "default"})]),
    label="10% off your first order")
kit("parcel-popup", P, "Parcel popup: 10% off the first order",
 "A popup that opens five seconds into a first visit with a photo, a first-order discount and one field for an email address; it closes with its button, Escape or a click outside and stays closed for two weeks. Needs the AnyPress Blocks plugin. Part of the Parcel kit; put it in the footer to show it on every page.",
 "popup, offer, discount, first order, newsletter, email, modal, parcel", PPOP)

PFOOT = grp(N([
    BODIES["parcel-signup"],
    grp(N([cols([
        col(N([dyn("site-title", {"level": 0, "fontSize": "xx-large", "fontFamily": PSERIF}),
               p("Stoneware thrown by hand in small batches, in our Asheville studio by the river.", None, "main-accent"),
               p('<a href="mailto:hello@example.com">hello@example.com</a>', None, None, None, None, None, raw=True, bind="email_linked"),
               social(["instagram", "pinterest", "facebook"])]), "34%"),
        col(flinks("Shop", [(n, f"/shop/{s}/") for n, s, _ in PCOL] + [("Order a set", PORDER), ("Offers", "/offers/")])),
        col(flinks("The studio", [("Our story", "/about/"), ("Reviews", "/reviews/"), ("Stockists", "/stockists/"), ("Work with us", "/jobs/"), ("Shipping and returns", "/help/"), ("Journal", "/journal/"), ("Contact", "/contact/")])),
        col(N([h("Studio shop", 3, "medium"), p(PADDR, None, "main-accent", bind="address"), p(PHOURS, None, "main-accent", bind="hours"),
               btns([("Shop online", None, "/shop/")])]))], "large", "wide", "top"),
        sep(),
        row([p("© Park Clay. Handmade in Asheville, North Carolina.", "small", "main-accent"),
             p('<a href="/privacy-policy/">' + T("Privacy") + '</a> · <a href="/help/">' + T("Shipping and returns") + '</a>', "small", "main-accent", None, None, None, raw=True)], gap="small")]),
        "section-dark", ("x-large", "large", None, None), "large", {"type": "constrained", "contentSize": "80rem"}, align="full", name="Footer columns"),
    PPOP,
]), None, None, "0", {"type": "default"}, align="full", name="Footer")
write("parcel-footer", "Parcel footer: new pieces by email, the collections and the first-order popup",
 "A site footer for an online shop or maker: a band for the email list, then the shop's links, the studio and its address on dark, and the first-order popup (needs the AnyPress Blocks plugin). Part of the Parcel kit; choose it for the footer in the Site Editor.",
 "footer", "footer, links, shop, newsletter, studio, popup, ecommerce, parcel", PFOOT, "core/template-part/footer")

kit("parcel-collection", P, "Parcel collection: the pieces, how they're made and a set to order",
 "The body of a page for one collection: three pieces with photos that open full screen, prices and an Order button, then what the pieces are like, how to care for them and a card for ordering a set. Part of the Parcel kit; when the shop's products are set up, the shop's own product blocks can replace the pieces.",
 "collection, products, category, shop, prices, parcel",
 sec("Collection", N([
   grid([pproduct("Cups and mugs: a grey speckled mug on a wooden table", "Everyday mug", "$34", "Holds 12 oz, in speckled grey"),
         pproduct("Cups and mugs: a white cup with a matching saucer", "Crackle cup and saucer", "$38", "Crackle white glaze"),
         pproduct("Cups and mugs: a tumbler with blue brush marks", "Ridged tumbler", "$24", "Set of three, $64")], 3, "16rem", "large"),
   '<!-- wp:spacer {"height":"var:preset|spacing|large"} -->\n<div style="height:var(--wp--preset--spacing--large)" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->',
   cols([
     col(N([h("About these pieces", 2, "xx-large"),
            p("Every mug is thrown on the wheel, trimmed by hand and fired twice, the second time to 2,300°F, so it's tough enough for the dishwasher and for every morning for years."),
            lst(["Stoneware, fired to 2,300°F", "Safe in the dishwasher and microwave", "Each one a little different", "Packed and sent in two working days", "More in the studio shop"])]), "54%"),
     col(grp(N([psmall("Made to order"), h("A matching set", 3, "large"),
                p("Four or more to match, for your kitchen or a gift. Made, fired and sent in three to four weeks."),
                p("From $120 for four", "x-large", "primary", None, PSERIF, {"lineHeight": "1.1"}),
                btns([("Order a set", None, PORDER)])]), "section-brand-soft", PAD_CARD, "small", {"type": "default"}))], "xx-large", "wide", "top")]), content="72rem"))

kit("parcel-stockists", P, "Parcel stockists: shops and markets that carry the work",
 "The shops and markets where the work can be seen and bought, as cards with what's there and a link to each one's page. Part of the Parcel kit.",
 "stockists, where to buy, shops, markets, retailers, parcel",
 sec("Stockists", N([phead("Where to buy", "See it before you buy it"), grid([grp(N([h(n, 3, "large"), p(d, None, "secondary"), link_p(f"Where to buy in {n} →", f"/stockists/{s}/", None, {"fontWeight": "600"})]), "section-card", PAD_CARD, "small", {"type": "default"}) for (n, s), d in zip(PSTOCK, [
    "Our own studio shop in the River Arts District, with seconds on the back shelf.",
    "Bull City Goods on West Main Street, with mugs and bowls all year.",
    "Tidewater Home on King Street, with vases and bottles.",
    "Our stall at the Little Five Points makers market, first Saturday of the month."])], 4, "13rem", "medium")]), "section-tint"))

kit("parcel-stockist", P, "Parcel stockist: one shop or market, with a map",
 "The body of a page for one shop or market that carries the work: its address and opening times, what's on its shelves and a map. Needs the AnyPress Blocks plugin for the map. Part of the Parcel kit; make one per stockist.",
 "stockist, shop, market, address, map, parcel",
 sec("Stockist", cols([
   col(N([psmall("The studio shop"), h("Park Clay, River Arts District", 2, "xx-large"), p(PADDR, "large"),
          h("Opening times", 3, "large"), p(PHOURS),
          h("On the shelves", 3, "large"), lst(["Every collection, including pieces not online", "Seconds at half price", "Gift wrapping while you wait"])]), "40%"),
   col(mapb(PADDR, PLAT, PLON, 15, "4/3"))], "xx-large", "wide", "top")))

kit("parcel-offers", P, "Parcel offers: ways to save",
 "Three offers as cards with the saving in large type, who it's for and a button: the monthly seconds sale, free shipping and gift cards. Part of the Parcel kit; keep the offers current.",
 "offers, sale, discount, shipping, gift card, parcel",
 sec("Offers", N([phead("Ways to save", "Offers"), grid([grp(N([p(s, "xx-large", None, None, PSERIF, {"lineHeight": "1"}), h(t, 3, "large"), p(d, None, "secondary"), btns([(b, "outline", l)])]), st, PAD_CARD, "small", {"type": "default"}) for s, t, d, b, l, st in [
    ("Up to 40% off", "Seconds sale", "Pieces with a small glaze mark, at the studio shop the first weekend of every month.", "Visit the studio", "/stockists/asheville/", "section-brand-soft"),
    ("Free shipping", "Orders over $60", "Anywhere in the US, packed in paper and card with no plastic.", "Shop now", "/shop/", "section-card"),
    ("Gift cards", "From $25", "Let them choose. Sent by email with a note from you, or wrapped at the studio.", "Order a gift card", PORDER, "section-brand-soft")]], 3, "16rem", "medium")])))

kit("parcel-team", P, "Parcel the studio: the people who make and pack",
 "The people at the studio, each with a photo, their name, what they do and a line about them. Part of the Parcel kit; use real photos, with permission.",
 "team, makers, studio, people, about, parcel",
 sec("Team", N([phead("The studio", "The three of us"), grid([stackg([img("placeholder-tall.svg", alt, "4/5"), h(n, 3, "large"), psmall(r, "primary"), p(d, None, "secondary")]) for n, r, d, alt in [
    ("June Park", "Potter and owner", "Throws every piece. Started with one wheel in a garage in 2016.", "The studio: June Park"),
    ("Ellie Novak", "Shop and shipping", "Packs every order and runs the studio shop. Answers your emails too.", "The studio: Ellie Novak"),
    ("Marcus Reid", "Glazes and kiln", "Mixes the glazes and fires the kiln twice a week, often at night.", "The studio: Marcus Reid")]], 3, "16rem", "large")])))

kit("parcel-jobs", P, "Parcel work with us: why work here and the open roles",
 "Why people work at the studio, each open role with its hours and pay, and the application. Part of the Parcel kit; keep the roles current and put the site's application form in the named Form group.",
 "careers, jobs, hiring, studio, apply, parcel",
 sec("Work with us", N([
   phead("Why work here", "A small studio by the river"),
   grid([stackg([h(t, 3, "large"), p(d, None, "secondary")]) for t, d in [
     ("Learn the wheel", "Everyone gets studio time and lessons from June, whatever their job."),
     ("Steady hours", "Set days, agreed in advance, and no late nights except for the kiln."),
     ("Pieces to keep", "A staff discount, and the first pick of the seconds."),
     ("Paid fairly", "Pay is on this page, and goes up every year you stay.")]], 4, "13rem"),
   '<!-- wp:spacer {"height":"var:preset|spacing|large"} -->\n<div style="height:var(--wp--preset--spacing--large)" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->',
   h("Open roles", 2, "xx-large"),
   N([grp(N([row([h(t, 3, "large"), p(when, None, None, None, None, {"fontWeight": "600"})], valign="center"), p(d, None, "secondary"), btns([("Apply for this", None, "#apply")])]), "section-tint", PAD_CARD, "small", {"type": "default"}) for t, when, d in [
     ("Studio assistant", "Full time, $19 an hour", "Wedge clay, trim pieces and help load the kiln. Some clay experience helps."),
     ("Packing and shipping", "Three days a week, $17 an hour", "Pack every order safely, mostly in the mornings. Careful hands needed."),
     ("Saturday shop", "Saturdays, $17 an hour", "Run the studio shop on our busiest day and talk to visitors about the work.")]]),
   grp(N([h("Apply", 2, "xx-large"), p("Tell us a little about you and which role you'd like. We reply to everyone within a week."),
          form("apply", "Email the studio", "mailto:jobs@example.com")]), "section-card", PAD_CARD, "small", {"type": "default"}, anchor="apply")])))

kit("parcel-order-form", P, "Parcel order: the form and what happens next",
 "A form to order a piece, a matching set or a gift card, beside what happens after sending it and how long it takes. Part of the Parcel kit; put the site's form in the named Form group.",
 "order, custom order, set, commission, gift card, form, parcel",
 sec("Order", cols([
   col(grp(N([h("Order a piece or a set", 2, "xx-large"), p("Tell us what you'd like and when you need it. We'll reply within a day with the price, the shipping and a date."),
              form("quote", "Shop online", "/shop/", "Rather choose from what's ready? Shop online.")]), "section-card", PAD_CARD, "medium", {"type": "default"}), "58%"),
   col(N([h("What happens next", 3, "large"),
          lst(["We reply within a day with a price and a date", "You pay by card from a link in the email", "We make, fire and pack it, and send the tracking"]),
          h("How long it takes", 3, "large"), lst(["Pieces in stock: two working days", "Sets made to order: three to four weeks", "Gift cards: the same day, by email"])]))],
   "xx-large", "wide", "top"), "section-tint"))

kit("parcel-contact-full", P, "Parcel contact: email, studio, hours and form",
 "A contact section for a shop or maker: the email address, studio address and hours beside the contact form, then a map. Needs the AnyPress Blocks plugin for the map. Part of the Parcel kit.",
 "contact, email, studio, hours, map, form, parcel",
 sec("Contact us", N([cols([
   col(N([h("Write to the studio", 2, "xx-large"),
          p('<a href="mailto:hello@example.com">hello@example.com</a>', "large", None, None, None, None, raw=True, bind="email_linked"),
          p(PADDR, None, bind="address"), p(PHOURS, None, "secondary", bind="hours"),
          p("For an order already on its way, include your order number and we'll find it.", None, "secondary")]), "40%"),
   col(grp(N([h("Send a message", 3, "large"), form("contact", "Shop online", "/shop/", "We reply the same day, Wednesday to Sunday.")]), "section-tint", PAD_CARD, "medium", {"type": "default"}))], "xx-large", "wide", "top"),
   mapb(PADDR, PLAT, PLON, 15, "21/9")])))

# The home page: numbers, reviews, questions and the studio shop join the original sections.
kit_page("kit-shop", "Home page: Parcel kit, online shop",
 "A complete home page for an online shop or maker in the Parcel kit: a product photo beside the collection, three promises, collections, best sellers, the maker's story, numbers that count up, reviews in a carousel, questions and the studio shop with a map. Apply the Parcel style for the look it was designed with.",
 "home, shop, store, ecommerce, products, maker, handmade, kit, parcel",
 ["parcel-hero", "parcel-promise", "parcel-categories", "parcel-products", "parcel-story", "parcel-numbers", "parcel-reviews", "parcel-faq-open", "parcel-studio"])

# ---------------------------------------------------------------- pages
def parcel_page(slug, title, desc, kw, parts):
    write(slug, title, desc, "anypress/pages", kw, N(parts), "core/post-content", " * Post Types: page\n")

parcel_page("parcel-page-services", "Shop page: Parcel kit",
 "A Shop page for an online shop or maker: a heading, every collection with a photo and a link to its own page, best sellers, how it's made and reviews. Parcel kit.",
 "shop, collections, products, catalogue, parcel",
 [ppage_hero("Shop", "Everything we make, thrown by hand in small batches. Free shipping on orders over $60.", "Shop", [("Order a set", "outline", PORDER)]),
  sec("Collections", grid([stackg([img("placeholder-tall.svg", f"Shop: {n.lower()}", "4/5"), hlink(n, f"/shop/{s}/", 3, "large"), p(d, None, "secondary")], "small") for n, s, d in PCOL], 3, "16rem", "x-large")),
  BODIES["parcel-products"], BODIES["parcel-making"], BODIES["parcel-reviews"]])

parcel_page("parcel-page-service", "Collection page: Parcel kit (one collection)",
 "A page for one collection, such as cups and mugs: a heading with a photo, the pieces with prices, what they're like and a set to order, reviews and questions. Parcel kit; make one per collection.",
 "collection, category, products, shop, parcel",
 [ppage_hero("Cups and mugs", "Mugs, cups and tumblers for every hand and every hot drink.", "Shop / Cups and mugs", [("Order a set", None, PORDER)], "The collection: a mug of tea on a wooden table"),
  BODIES["parcel-collection"], BODIES["parcel-reviews"],
  sec("Questions", cols([col(N([psmall("About these pieces"), h("Good to know", 2, "xx-large")]), "36%"), col(accordion([
    ("How big are the mugs?", "The everyday mug holds 12 oz, the cup 8 oz and the tumbler 10 oz. Each one varies a little."),
    ("Are they safe for hot drinks?", "Yes. The handles stay cool and the glaze is safe for food, the dishwasher and the microwave."),
    ("Can I order a set to match?", "Yes. Four or more to match, made in three to four weeks."),
    ("Why does mine look a little different?", "Every piece is thrown and glazed by hand, so no two are quite the same. That's the point.")]))], "xx-large", "wide", "top"))])

parcel_page("parcel-page-about", "Our story page: Parcel kit",
 "An Our story page for a shop or maker: a heading, the maker's story beside a photo, numbers that count up, the people at the studio, how it's made and the studio shop with a map. Parcel kit.",
 "about, our story, maker, studio, team, parcel",
 [ppage_hero("Our story", "One potter, one wheel in a garage, and ten years later a studio by the river and three of us making every piece.", "Our story"),
  sec("Story", cols([
    col(N([h("It started with one wheel in a garage", 2, "xx-large"),
           p("June Park bought a second-hand wheel in 2016 and taught herself to throw in the evenings after work. The first mugs went to friends. Then friends of friends asked for them.", "large"),
           p("Ten years on, the studio is in the River Arts District, Ellie and Marcus have joined, and every piece still goes through June's hands at least four times before it reaches you.")]), "50%", valign="center"),
    col(img("placeholder-tall.svg", "Our story: clay-covered hands holding a freshly thrown mug", "4/5"))], "xx-large", "wide", "center")),
  BODIES["parcel-numbers"], BODIES["parcel-team"], BODIES["parcel-making"], BODIES["parcel-studio"]])

parcel_page("parcel-page-reviews", "Reviews page: Parcel kit",
 "A Reviews page for a shop or maker: a heading, reviews as cards with stars, names and what each person bought, numbers that count up and best sellers. Parcel kit; use real reviews, with permission.",
 "reviews, testimonials, customers, stars, parcel",
 [ppage_hero("Reviews", "Rated 4.9 out of 5 by more than 800 buyers. Here's what some of them say.", "Reviews", [("Shop the collection", None, "/shop/")]),
  sec("All reviews", grid([preview(*r) for r in PREVIEWS + [
    ("The bottle sits on our kitchen windowsill with one branch in it, and everyone who visits asks about it.", "Nina S.", "Gourd bottle"),
    ("I sent a gift card to my sister and she chose a bowl I'd never have picked. She loves it.", "Paul D.", "Gift card"),
    ("Watched June throwing at the studio on a Saturday and left with four plates. Worth the drive.", "Hannah and Lee", "Dinner plates")]], 3, "18rem", "medium"), "section-tint"),
  BODIES["parcel-numbers"], BODIES["parcel-products"]])

parcel_page("parcel-page-areas", "Stockists page: Parcel kit",
 "A Stockists page for a shop or maker: a heading, a card for each shop or market that carries the work, linking to its own page, the studio shop with a map and reviews. Parcel kit.",
 "stockists, where to buy, shops, markets, parcel",
 [ppage_hero("Where to buy", "Online any time, at our studio shop in Asheville, and at three shops and a market across the South.", "Stockists"),
  BODIES["parcel-stockists"], BODIES["parcel-studio"], BODIES["parcel-reviews"]])

parcel_page("parcel-page-area", "Stockist page: Parcel kit (one shop or market)",
 "A page for one shop or market that carries the work: a heading with a photo, its address, opening times and what's there, with a map, the collections and reviews. Parcel kit; make one per stockist.",
 "stockist, shop, market, where to buy, parcel",
 [ppage_hero("Where to buy in Asheville", "Our own studio shop, open five days a week, with pieces you won't find online.", "Stockists / Asheville", [("Shop online", None, "/shop/")], "Where to buy: shelves of handmade plates and bowls"),
  BODIES["parcel-stockist"], BODIES["parcel-categories"], BODIES["parcel-reviews"]])

parcel_page("parcel-page-offers", "Offers page: Parcel kit",
 "An Offers page for a shop or maker: a heading, ways to save, best sellers, questions and the email list. Parcel kit; keep the offers current.",
 "offers, sale, discounts, gift cards, parcel",
 [ppage_hero("Offers", "Seconds every month, free shipping over $60 and gift cards for anyone who's hard to buy for.", "Offers"),
  BODIES["parcel-offers"], BODIES["parcel-products"], BODIES["parcel-faq-open"]])

parcel_page("parcel-page-join", "Order page: Parcel kit",
 "An Order page for a shop or maker: a heading, the order form beside what happens next, how it's made and reviews. Parcel kit; put the site's form in the named Form group.",
 "order, custom order, set, commission, gift card, parcel",
 [ppage_hero("Order a piece or a set", "A matching set for your table, a piece for a gift or a gift card. Tell us what you'd like.", "Order"),
  BODIES["parcel-order-form"], BODIES["parcel-making"], BODIES["parcel-reviews"]])

parcel_page("parcel-page-faq", "Shipping and returns page: Parcel kit",
 "A Shipping and returns page for a shop or maker: answers that open and close, grouped into shipping, returns and care, and the studio's contact details. Parcel kit; put the shop's real policies here.",
 "faq, questions, shipping, returns, care, parcel",
 [ppage_hero("Shipping and returns", "How we pack and send, what to do if something breaks, and how to look after your pieces.", "Help"),
  sec("Questions", N([N([h(group_t, 2, "xx-large"), accordion(qs)]) for group_t, qs in [
    ("Shipping", [
      ("How long does shipping take?", "We pack orders in two working days. Most arrive three to five days after that, anywhere in the US."),
      ("How much is shipping?", "Free on orders over $60. Below that it's a flat $8 in the US."),
      ("Do you ship outside the US?", "To Canada and the UK, yes. Shipping is worked out at checkout.")]),
    ("Returns and breakages", [
      ("What if something arrives broken?", "Send us a photo within a week and we'll send a new one or refund you, whichever you'd like."),
      ("Can I return a piece?", "Yes, within 30 days if it's unused. We'll send a free return label.")]),
    ("Care", [
      ("Is it safe in the dishwasher?", "Yes. Everything is fired to 2,300°F and is safe in the dishwasher and the microwave."),
      ("Can it go in the oven?", "Bowls and plates can go in a warm oven. Avoid sudden changes, like from the fridge to a hot oven.")])]]),
    content="56rem"),
  BODIES["parcel-contact-full"]])

parcel_page("parcel-page-careers", "Work with us page: Parcel kit",
 "A Work with us page for a shop or maker: a heading, why people work there, the open roles with pay, the application form and the studio with a map. Parcel kit; keep the roles current and put the site's form in the named Form group.",
 "careers, jobs, hiring, studio, parcel",
 [ppage_hero("Work with us", "A small studio that teaches everyone the wheel. Pay is on this page.", "Work with us", [("See open roles", None, "#apply")]),
  BODIES["parcel-jobs"], BODIES["parcel-studio"]])

parcel_page("parcel-page-contact", "Contact page: Parcel kit",
 "A Contact page for a shop or maker: a heading, the email address, studio and hours beside the contact form, a map and questions. Parcel kit; put the site's contact form in the named Form group.",
 "contact, email, studio, parcel",
 [ppage_hero("Contact", "Send a note, ask about an order or come and see us at the studio.", "Contact"),
  BODIES["parcel-contact-full"], BODIES["parcel-faq-open"]])

parcel_page("parcel-page-thanks", "Thank-you page: Parcel kit",
 "The page visitors see after sending a form: thanks, what happens next and when, and links to keep shopping. Parcel kit; send every form here.",
 "thank you, thanks, confirmation, form sent, parcel",
 [sec("Thanks", N([psmall("Message sent"), h("Thank you. We'll be in touch soon.", 1, "xxx-large"),
    p("We'll reply within a day, Wednesday to Sunday. Check your email for a copy of what you sent.", "large", "secondary"),
    btns([("Back to the home page", None, "/"), ("Keep shopping", "outline", "/shop/")])]), None, ("xxx-large", "xxx-large", None, None), "56rem"),
  BODIES["parcel-products"]])

print("parcel ok")
