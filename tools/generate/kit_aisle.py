# Aisle (0.23.0): a whole online shop on FluentCart, written for a small clothing brand. Run by kits.py after
# kit_branch.py, so every helper in kits.py, kits_more.py, kit_ridge.py and the kits before it is in scope.
#
# Clean and photo-led: a firm grotesk for headings and prices, a soft sans for reading, ink on warm white with moss
# green. Everything a shopper buys with is FluentCart's own: the product grids are its Products block, the product,
# category, cart, checkout, receipt and account pages are its own templates, and the header gets its search, account
# link and mini cart from the theme as soon as a product is published. The kit adds the pages around them, linked by
# slug: /shop/ (FluentCart's), /product-categories/<slug>/ for Tops, Bottoms, Outerwear, Accessories and Last few,
# /new-in/, /lookbook/, /gift-cards/, /help/ with /shipping/, /returns/, /size-guide/, /track-order/, /faq/ and
# /contact/ under it, /our-story/, /reviews/, /journal/ (the blog), /thank-you/. A link to one product is /item/<product slug>/, FluentCart's own address for it.
# Forms are named groups, as in Ridge.

AK = "anypress/kit-store"
AHEAD = "schibsted-grotesk"
AADDR = "2118 SE Division Street, Portland, OR 97202"
AHOURS = "Pick-ups Tuesday to Saturday, 11am to 5pm"
AMAIL = "hello@example.com"
ACATS = [
    ("Tops", "tops", "Hoodies, sweatshirts and tees", "A woman in a chunky knit jumper holding a camera"),
    ("Bottoms", "bottoms", "Jeans, shorts and leggings", "A woman in jeans and boots sitting on a wooden bench"),
    ("Outerwear", "outerwear", "Jackets for every season", "A man in a dark coat and scarf against a yellow wall"),
    ("Accessories", "accessories", "Caps, socks and gift cards", "A woman in a grey coat and red scarf holding a coffee cup"),
]

_ps = open(os.path.join(HERE, "patterns.py")).read()
exec(_ps[_ps.index("def products("): _ps.index('write("shop-products"')])  # FluentCart's Products block, as the theme writes it

variation("kit-aisle", "Aisle (clothing store)", PALS["aisle"], "manrope", AHEAD, "700", "-0.02em", "1.02",
    button("0", AHEAD, "700", None, "var:preset|font-size|base", "0.01em"), blocks=site_title(AHEAD, "800", None, "-0.03em"))

def alabel(text, color="secondary", size="small"):
    return p(text, size, color, None, None, {"fontWeight": "700", "letterSpacing": "0.1em", "textTransform": "uppercase"})

def ahead(label, title, link=None, size="xx-large"):
    left = stackg([alabel(label), h(title, 2, size)])
    return row([left, p(f'<a href="{link[1]}">' + T(link[0]) + " →</a>", "medium", None, None, None, {"fontWeight": "600"}, raw=True)] if link else [left], valign="bottom")

def apage_hero(title, text, crumb, buttons=None, alt=None):
    """A page's opening: the page's own photo full width, darkened toward the words (class anypress-scrim), as fashion
    shops open a collection. Kept short on pages that list products, so the first row of products still shows."""
    words = N([alabel(crumb, "base"), h(title, 1, "xxx-large"), p(text, "large")] + ([btns(buttons)] if buttons else []))
    return cover(grp(words, gap="medium", layout={"type": "constrained", "contentSize": "40rem", "justifyContent": "left"}),
                 "Page hero", "placeholder-wide.svg", 50, "30rem", "bottom left", ("xx-large", "x-large", "medium", "medium"), "80rem", alt=alt, cls="anypress-scrim")

AHELP_PILLS = [("Shipping", "/help/shipping/"), ("Returns", "/help/returns/"), ("Size guide", "/help/size-guide/"), ("Track an order", "/help/track-order/"),
         ("Questions", "/help/faq/"), ("Contact us", "/help/contact/")]

def ahelp_hero(title, text, crumb, here=None):
    """A help page's opening: the brand colour with stitching around its edge and thread rings behind it (class
    anypress-stitch), and a row of the other help pages, so every answer is one click from any help page."""
    words = N([alabel(crumb, "base"), h(title, 1, "xxx-large"), p(text, "large")])
    pills = btns([(label, "outline", href) for label, href in AHELP_PILLS if href != here])
    inner = grp(N([grp(words, gap="medium", layout={"type": "constrained", "contentSize": "44rem", "justifyContent": "left"}), pills]), gap="large")
    return grp(inner, "section-brand", ("xx-large", "xx-large", None, None), None, {"type": "constrained", "contentSize": "80rem"}, "section", "full", "Page hero").replace(
        '"className":"is-style-section-brand"', '"className":"is-style-section-brand anypress-stitch"').replace(
        'class="wp-block-group alignfull is-style-section-brand"', 'class="wp-block-group alignfull is-style-section-brand anypress-stitch"', 1)

def alinks(items):
    """A list of links, each in large type with an arrow."""
    lis = "\n\n".join(f'<!-- wp:list-item -->\n<li><a href="{href}">{T(label)}</a> →</li>\n<!-- /wp:list-item -->' for label, href in items)
    return '<!-- wp:list {"className":"is-style-no-bullets","fontSize":"large"} -->\n<ul class="wp-block-list is-style-no-bullets has-large-font-size">' + lis + '</ul>\n<!-- /wp:list -->'

def ashop(cid, per, order_by="ID", order="DESC", paginate=False):
    """FluentCart's Products block: per products, newest first unless told, with or without pages."""
    extra = {"per_page": per, "order_by": order_by, "order_type": order}
    if not paginate: extra["paginator"] = "numbers"
    return products(False, cid=cid, extra=extra, switcher=False, paginator=paginate)

def areview(text, name, piece):
    return grp(N([p("★★★★★", None, "primary", None, None, {"letterSpacing": "0.1em"}), p("“" + text + "”", "medium", None, None, None, {"lineHeight": "1.45"}),
                  p(f"{name} · {piece}", "small", "secondary", None, None, {"fontWeight": "600"})]), "section-card", PAD_CARD, "small", {"type": "default"})

AREVIEWS = [
    ("Three years in and my hoodie still looks new. I've washed it more times than I can count.", "Priya S.", "Classic hoodie"),
    ("Measured my favourite hoodie like the size guide said and the large fits perfectly.", "Tom H.", "Fleece jacket"),
    ("Ordered at 1pm, it arrived the next day, with a handwritten note. Made my week.", "Dana K.", "Basic tee, two colours"),
    ("The size was off, so I asked for a swap and the new one arrived before I'd even posted the old one back.", "Leo M.", "Zipper hoodie"),
    ("Forest green in real life is exactly the colour in the photos. That never happens.", "Jen R.", "Modern sweatshirt"),
    ("A seam went after eight months. They fixed it for free and sent it back in a week.", "Marcus O.", "Casual hoodie"),
]

# ---------------------------------------------------------------- header and footer
kit("aisle-topbar", AK, "Aisle top bar: free shipping, returns and what's new",
 "A thin bar above the header with the shop's three promises (free shipping over a set amount, easy returns, same-day dispatch) and a link to what's new. Part of the Aisle kit; keep the numbers true to the shop's settings.",
 "top bar, announcement, free shipping, returns, header, aisle",
 grp(row([p(T("Free shipping over $75") + ' · ' + T("60-day returns") + ' · ' + T("Order by 2pm, sent today"), "small", None, None, None, None, raw=True),
          p('<a href="/new-in/">' + T("New this week: the winter collection") + ' →</a>', "small", None, None, None, {"fontWeight": "600"}, raw=True)], "center", "large"),
     "section-dark", ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Top bar"))

AHEADER = grp(N([
    BODIES["aisle-topbar"],
    grp(row([
        dyn("site-title", {"level": 0, "fontSize": "x-large", "style": {"typography": {"lineHeight": "1"}}}),
        dyn("navigation", {"overlayMenu": "mobile", "layout": {"type": "flex", "justifyContent": "right"}})], "space-between", "medium", False, "center"),
        None, ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Main bar").replace(
        '<!-- wp:group {', '<!-- wp:group {"backgroundColor":"base",', 1).replace('class="wp-block-group alignfull', 'class="wp-block-group alignfull has-base-background-color has-background', 1),
]), "sticky", None, "0", {"type": "default"}, align="full", name="Header")
write("aisle-header", "Aisle header: shop menu, search, account and cart",
 "A site header for an online clothing shop that stays at the top while visitors scroll: a dark bar with free shipping and returns, then the shop's name and the menu (with dropdowns for the categories and help). Once the shop has a published product, FluentCart's product search, account link and mini cart appear beside the menu. Part of the Aisle kit; choose it for the header in the Site Editor.",
 "header", "header, menu, navigation, sticky, shop, cart, search, account, ecommerce, aisle", AHEADER, "core/template-part/header")

kit("aisle-signup", AK, "Aisle signup: the newsletter, with 10% off",
 "A band asking visitors to join the shop's monthly letter for new colours first and 10% off the first order, with the signup form beside it. Part of the Aisle kit; sits above the footer on every page.",
 "newsletter, signup, email, discount, first order, aisle",
 sec("Signup", cols([
   col(N([h("New colours first, and 10% off", 2, "xx-large"), p("The Thread comes once a month: what's new, care tips and a look behind the seams. Join and we'll send a code for 10% off your first order.", "medium")]), "55%", valign="center"),
   col(form("newsletter", "See what's new", "/new-in/"), valign="center")], "large", "wide", "center"), "section-brand", ("x-large", "x-large", None, None)))

APOP = popup("offer", N([
    img("placeholder-wide.svg", "Neatly folded t-shirts in a stack of colours", "16/9"),
    grp(N([alabel("Welcome"), h("10% off your first order", 2, "xx-large"),
           p("Join The Thread for new colours first and care tips once a month. We'll email you a code for 10% off your first order."),
           form("offer", "See what's new", "/new-in/")]), None, (None, None, "large", "large"), "small", {"type": "default"})]),
    label="10% off your first order")
kit("aisle-popup", AK, "Aisle popup: 10% off the first order",
 "A popup that opens five seconds into a first visit with a photo, a first-order discount and one field for an email address; it closes with its button, Escape or a click outside and stays closed for two weeks. Needs the AnyPress Blocks plugin. Part of the Aisle kit; put it in the footer to show it on every page.",
 "popup, offer, discount, first order, newsletter, email, modal, aisle", APOP)

AFOOT = grp(N([
    BODIES["aisle-signup"],
    grp(N([cols([
        col(N([dyn("site-title", {"level": 0, "fontSize": "xx-large"}),
               p("Everyday clothes, made to last. Designed in Portland, made in two family mills, packed by hand.", None, "main-accent"),
               p(f'<a href="mailto:{AMAIL}">{AMAIL}</a>', None, None, None, None, None, raw=True, bind="email_linked"),
               social(["instagram", "pinterest", "facebook"])]), "34%"),
        col(flinks("Shop", [("Everything", "/shop/")] + [(n, f"/product-categories/{s}/") for n, s, *_ in ACATS] + [("New in", "/new-in/"), ("Last few", "/product-categories/last-few/"), ("Gift cards", "/gift-cards/")])),
        col(flinks("Help", [("Help centre", "/help/"), ("Shipping and delivery", "/help/shipping/"), ("Returns and exchanges", "/help/returns/"), ("Size guide", "/help/size-guide/"), ("Track your order", "/help/track-order/"), ("Questions", "/help/faq/"), ("Contact us", "/help/contact/")])),
        col(flinks("Thread & Co.", [("Our story", "/our-story/"), ("Lookbook", "/lookbook/"), ("Reviews", "/reviews/"), ("Journal", "/journal/"), ("Your account", "/account/")]))], "large", "wide", "top"),
        sep(),
        row([p("© Thread & Co. Prices in US dollars. Secure checkout: cards, Apple Pay and Google Pay.", "small", "main-accent"),
             p('<a href="/privacy-policy/">' + T("Privacy") + '</a> · <a href="/help/shipping/">' + T("Shipping") + '</a> · <a href="/help/returns/">' + T("Returns") + '</a>', "small", "main-accent", None, None, None, raw=True)], gap="small")]),
        "section-dark", ("x-large", "large", None, None), "large", {"type": "constrained", "contentSize": "80rem"}, align="full", name="Footer columns"),
]), None, None, "0", {"type": "default"}, align="full", name="Footer")
write("aisle-footer", "Aisle footer: newsletter, shop and help links",
 "A site footer for an online clothing shop: a band for the newsletter, then the shop's categories, every help page and the brand's own pages on dark, and how people pay. The first-order popup sits on the home page, so it never gets in the way at checkout. Part of the Aisle kit; choose it for the footer in the Site Editor.",
 "footer", "footer, links, shop, help, newsletter, ecommerce, aisle", AFOOT, "core/template-part/footer")

# ---------------------------------------------------------------- home sections
kit("aisle-hero", AK, "Aisle hero: a full-width photo with two ways in",
 "The first thing visitors see: a full-width photo of the clothes being worn, a short promise and two buttons, one to what's new and one to the whole shop. Part of the Aisle kit; use a real photo of the shop's own clothes.",
 "hero, banner, photo, new collection, shop, aisle",
 cover(N([alabel("The winter collection", "base"), h("Everyday clothes, made to last.", 1, "poster", None, None, {"lineHeight": "0.92"}),
          p("Hoodies, tees and jackets from two family mills, cut to fit and packed by hand. Free shipping over $75.", "large"),
          btns([("Shop new in", None, "/new-in/"), ("Shop everything", "outline", "/shop/")])]),
       "Hero", "placeholder-wide.svg", 40, "88vh", "bottom left", ("xx-large", "xx-large", "medium", "medium"), "80rem"))

kit("aisle-promises", AK, "Aisle promises: four reasons to buy here",
 "Four short promises in a row (free shipping, same-day dispatch, returns, repairs), each with its detail, right under the hero where shoppers look for them. Part of the Aisle kit; keep them true to the shop's settings.",
 "promises, shipping, returns, guarantee, trust, aisle",
 sec("Promises", grid([stackg([h(t, 3, "medium"), p(d, "small", "secondary")]) for t, d in [
    ("Free shipping over $75", "$8 below that, anywhere in the US. Canada, the UK and the EU at checkout."),
    ("Order by 2pm, sent today", "Packed by hand in Portland, Monday to Friday, in recycled paper mailers."),
    ("60 days to return", "Free returns in the US, or a size swap that leaves before yours comes back."),
    ("Free repairs for a year", "A seam goes or a zip breaks in the first year? We fix it.")]], 4, "13rem", "large"), "section-tint", ("large", "large", None, None)))

kit("aisle-categories", AK, "Aisle categories: four photo tiles",
 "The shop's four main categories as tall photos with the name and what's in each, each opening its FluentCart category page. Part of the Aisle kit; link each tile to the shop's own category.",
 "categories, collections, departments, shop by category, aisle",
 sec("Categories", N([ahead("Shop by category", "Find your next favourite", ("Shop everything", "/shop/")),
   grid([stackg([img("placeholder-tall.svg", alt, "3/4"), hlink(n, f"/product-categories/{s}/", 3, "large"), p(d, None, "secondary")], "small") for n, s, d, alt in ACATS], 4, "14rem", "medium")])))

kit("aisle-new-in", AK, "Aisle new in: the eight newest products",
 "The eight newest products as FluentCart product cards (photo, name, price, sale and sold-out badges, add to cart), under a heading with a link to everything new. Part of the Aisle kit; it fills itself from the shop.",
 "new in, new arrivals, latest, products, fluentcart, aisle",
 sec("New in", N([ahead("Just landed", "New in", ("See everything new", "/new-in/")), ashop("aisle-new-in", 8)])))

kit("aisle-look", AK, "Aisle shop the look: one outfit, piece by piece",
 "A large photo of an outfit beside the pieces in it, each linking to its product, with a button to the lookbook. Part of the Aisle kit; point each piece at the shop's own product.",
 "shop the look, outfit, lookbook, styling, aisle",
 sec("Shop the look", cols([
   col(img("placeholder-tall.svg", "A man in a beanie drinking coffee by a tent", "4/5"), "52%"),
   col(N([alabel("Shop the look"), h("Weekend, sorted", 2, "xx-large"),
          p("Tess styled this one for a night out at Trillium Lake: a hoodie you can live in, jeans that soften with every wash and a cap for when it drizzles.", "medium", "secondary"),
          alinks([("Classic zipper hoodie", "/item/classic-zipper-hoodie/"), ("Slim fit jeans", "/item/mens-slim-fit-jeans/"), ("Classic cap", "/item/classic-cap/")]),
          btns([("See the lookbook", "outline", "/lookbook/")])]), valign="center")], "xx-large", "wide", "center"), "section-tint"))

def aspot(name, title, label, head, text, points, photo, button, link, flip=False):
    words = col(N([alabel(label), h(head, 2, "xx-large"), p(text, "medium", "secondary"), lst(points),
                   btns([(button, None, link)])]), valign="center")
    pic = col(img("placeholder-tall.svg", photo, "4/5"), "52%")
    kit(name, AK, title,
        "One category in the spotlight: a large photo beside why it is worth a look, what makes it different and a button to the category. Part of the Aisle kit; use one for each category you want to push, alternating sides.",
        "category, spotlight, feature, collection, promotion, aisle",
        sec("Category spotlight", cols([words, pic] if flip else [pic, words], "xx-large", "wide", "center")))

aspot("aisle-spotlight", "Aisle category spotlight: outerwear, photo on the left", "The outerwear edit",
      "Built for the walk to work, and the weekend after",
      "Our jackets are cut a little longer and lined where it counts, so they keep the rain out on Monday and still look right on Saturday.",
      ["Water-resistant shells that breathe", "Pockets big enough for a phone and a book", "Free repairs on zips and seams for a year"],
      "A woman in a red checked jacket on a lake pier", "Shop outerwear", "/product-categories/outerwear/")
aspot("aisle-spotlight-2", "Aisle category spotlight: denim, photo on the right", "Denim that softens",
      "Jeans that get better every time you wash them",
      "Heavy cotton from a family mill, washed once before it reaches you. Pick your fit in the size guide and it stays that shape.",
      ["Slim, straight and relaxed fits", "Hemmed for free if you send us your length", "Made to wear for years, not one season"],
      "Close up of dark blue jeans", "Shop bottoms", "/product-categories/bottoms/", flip=True)

kit("aisle-story", AK, "Aisle story: who makes the clothes",
 "A short story of the brand beside a photo of the workroom, with three things it stands for and a link to the full story. Part of the Aisle kit; the owners' own words.",
 "about, story, brand, values, made to last, aisle",
 sec("Story", cols([
   col(N([alabel("Our story"), h("Started at a kitchen table, still packed by hand", 2, "xx-large"),
          p("Iris and Malik started Thread & Co. in 2020 with one hoodie and a promise: clothes that still look good after fifty washes. The fabric comes from two family mills we've visited ourselves.", "medium"),
          grid([stackg([h(t, 3, "medium"), p(d, "small", "secondary")]) for t, d in [
              ("Made to last", "Heavier fabric and better seams."), ("Fair all the way", "Mills that pay a fair wage."), ("No fake sales", "Fair prices all year.")]], 3, "9rem", "medium"),
          btns([("Read our story", "outline", "/our-story/")])]), "52%", valign="center"),
   col(img("placeholder-tall.svg", "A sewing machine stitching a piece of fabric", "4/5"))], "xx-large", "wide", "center")))

kit("aisle-reviews", AK, "Aisle reviews: what customers say, in a carousel",
 "Customers in their own words, in a carousel, three at a time on a computer and one on a phone, with stars, a name and what each bought, under the shop's overall rating. Needs the AnyPress Blocks plugin. Part of the Aisle kit; use real reviews, with permission.",
 "reviews, testimonials, customers, stars, rating, carousel, aisle",
 sec("Reviews", N([ahead("Rated 4.8 out of 5 from 1,200 reviews", "Worn, washed, and still loved", ("All reviews", "/reviews/")),
                   carousel([areview(*r) for r in AREVIEWS], 3, "Customer reviews")]), "section-tint"))

kit("aisle-club", AK, "Aisle club and gift cards: two easy ways to give",
 "Two cards side by side: a monthly subscription (a fresh pair of socks every month) and gift cards, each with its price and a button to its product. Part of the Aisle kit; point the buttons at the shop's own products.",
 "subscription, sock club, gift card, gifts, aisle",
 sec("Club and gifts", grid([grp(N([alabel(lbl, c), h(t, 2, "xx-large"), p(d, "medium"), p(price, "x-large", None, None, AHEAD, {"fontWeight": "700"}), btns([(b, None, href)])]), st, PAD_CARD, "small", {"type": "default"}) for lbl, c, t, d, price, b, href, st in [
    ("Every month", "primary", "The Sock club", "A fresh pair every month in a colour we pick for you. Skip a month or stop any time from your account.", "$12 a month", "Join the Sock club", "/item/sock-club/", "section-brand-soft"),
    ("For anyone", "secondary", "Gift cards", "Sent by email with your note, on the day you choose. Good for anything in the shop, and it never runs out.", "From $25", "Buy a gift card", "/gift-cards/", "section-card")]], 2, "18rem", "large")))

kit("aisle-journal", AK, "Aisle journal: the three latest posts",
 "The three latest posts from the journal with photo, title and date, and a link to all posts. Part of the Aisle kit.",
 "blog, journal, posts, style notes, care guides, aisle",
 sec("Journal", N([ahead("From the journal", "Style notes and care guides", ("All posts", "/journal/")),
   query(3, 0, 3, N([dyn("post-featured-image", {"isLink": True, "aspectRatio": "4/3"}), dyn("post-title", {"isLink": True, "level": 3, "fontSize": "large"}), dyn("post-date", {"fontSize": "small", "textColor": "secondary"})]), 31)])))

kit_page("kit-store", "Home page: Aisle kit, clothing store",
 "A complete home page for an online clothing shop on FluentCart in the Aisle kit: a full-width photo, four promises, categories with photos, the newest products, two category spotlights around a look to shop, reviews in a carousel, the brand's story, the subscription and gift cards, the journal, and a first-order popup. Apply the Aisle style for the look it was designed with.",
 "home, shop, store, clothing, fashion, ecommerce, fluentcart, products, kit, aisle",
 ["aisle-hero", "aisle-promises", "aisle-categories", "aisle-new-in", "aisle-spotlight", "aisle-look", "aisle-spotlight-2", "aisle-reviews", "aisle-story", "aisle-club", "aisle-journal", "aisle-popup"])

# ---------------------------------------------------------------- help sections
AHELP = [
    ("Shipping and delivery", "/help/shipping/", "What it costs, how long it takes and where we send."),
    ("Returns and exchanges", "/help/returns/", "60 days to send it back, or swap a size for free."),
    ("Size guide", "/help/size-guide/", "Measurements for every fit, and how to measure."),
    ("Track your order", "/help/track-order/", "Where your parcel is, from your account."),
    ("Questions", "/help/faq/", "Payment, care, repairs, gift cards and the Sock club."),
    ("Contact us", "/help/contact/", "A person replies the same working day."),
]
kit("aisle-help-grid", AK, "Aisle help: every help page as a card",
 "Every help page as a card with what it answers, so shoppers find the answer before they write in. Part of the Aisle kit.",
 "help, support, customer service, shipping, returns, size guide, aisle",
 sec("Help", grid([grp(N([hlink(t, href, 3, "large"), p(d, None, "secondary")]), "section-card", PAD_CARD, "small", {"type": "default"}) for t, href, d in AHELP], 3, "16rem", "medium")))

kit("aisle-shipping", AK, "Aisle shipping: what it costs and how long it takes",
 "The shop's delivery options in a table (cost and time for each), then sending abroad, with prices and VAT for the EU and UK, and when orders leave. Part of the Aisle kit; keep it the same as the shipping set up in FluentCart.",
 "shipping, delivery, costs, international, vat, eu, aisle",
 sec("Shipping", N([
   h("Delivery in the US", 2, "xx-large"),
   table(["Option", "Cost", "Arrives"], [
       ["Standard", "$8, free over $75", "3 to 5 working days"],
       ["Express", "$18", "1 to 2 working days"],
       ["Pick up in Portland", "Free", "Ready the next working day"]], "stripes"),
   p("Orders placed by 2pm Pacific, Monday to Friday, leave the same day. You'll get an email with tracking as soon as yours is on its way.", None, "secondary"),
   h("Sending abroad", 2, "xx-large"),
   table(["Where", "Cost", "Arrives", "Tax and duties"], [
       ["Canada", "$18", "5 to 8 working days", "Paid on delivery"],
       ["United Kingdom", "$22", "5 to 8 working days", "UK VAT added at checkout"],
       ["European Union", "$22", "5 to 10 working days", "Your country's VAT added at checkout, no surprise fees"]], "stripes"),
   p("For the EU and the UK the VAT is worked out for your country at checkout, so there's nothing more to pay at the door. Buying for a business? Add your VAT number at checkout and the VAT comes off.", None, "secondary")]), content="56rem"))

kit("aisle-returns", AK, "Aisle returns: how to send something back",
 "How to return or exchange in three numbered steps, then the rules in plain words: how long, what can come back, refunds and the 14-day right to cancel for EU customers, with a button to the cancellation form (FluentCart's Customer Rights add-on makes its page at /withdraw-from-contract/). Part of the Aisle kit; keep it the same as the shop's real policy.",
 "returns, exchanges, refunds, size swap, withdrawal, eu, aisle",
 sec("Returns", N([
   grid([stackg([p(n, "xxx-large", "primary", None, AHEAD, {"lineHeight": "1", "fontWeight": "700"}), h(t, 3, "large"), p(d, None, "secondary")]) for n, t, d in [
       ("1", "Tell us", "Open the order in your account and choose Return, or reply to your order email. Say if you'd like a refund or another size."),
       ("2", "Send it back", "Use the free label we email you (US), drop it at any post office and keep the receipt."),
       ("3", "Refund or swap", "Swaps leave as soon as you've posted yours. Refunds go back to your card within 3 to 5 days of it reaching us.")]], 3, "14rem", "large"),
   '<!-- wp:spacer {"height":"var:preset|spacing|large"} -->\n<div style="height:var(--wp--preset--spacing--large)" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->',
   cols([
     col(N([h("The rules, in plain words", 2, "xx-large"), lst([
         "60 days from delivery, for a refund or another size",
         "Unworn and unwashed, with the tags on",
         "Socks and Sock club pairs can't come back, for hygiene",
         "Last few pieces can be swapped but not refunded",
         "Something faulty? We pay the postage and fix or replace it"])]), "55%"),
     col(card(N([h("In the EU? 14 days to change your mind", 3, "large"),
                 p("Under EU law you can cancel any order within 14 days of receiving it, for any reason. Use the cancellation form, cancel from your account or email us, and we'll refund you, including the standard shipping, within 14 days of getting it back.", None),
                 btns([("Cancel an order", None, "/withdraw-from-contract/")])]), "section-brand-soft"))], "xx-large", "wide", "top")])))

kit("aisle-size-guide", AK, "Aisle size guide: tables and how to measure",
 "Size charts for tops and bottoms in inches, how to measure in three steps and what to do between sizes. Part of the Aisle kit; put the shop's own measurements here.",
 "size guide, sizes, measurements, fit, chart, aisle",
 sec("Size guide", N([
   cols([
     col(N([h("How to measure", 2, "xx-large"), lst([
         "Chest: under your arms, around the fullest part, tape level",
         "Waist: around your natural waist, where you bend",
         "Inside leg: from the top of the inside leg to the floor"]),
         p("Easier still: lay a top you love flat and measure armpit to armpit, then double it. Between sizes? Our fleece softens and gives a little, so take the smaller one for a close fit.", None, "secondary")]), "40%"),
     col(N([h("Tops", 3, "large"), table(["Size", "Chest (in)", "Length (in)", "Sleeve (in)"], [
         ["XS", "34–36", "26", "32"], ["S", "36–38", "27", "33"], ["M", "38–41", "28", "34"], ["L", "41–44", "29", "35"], ["XL", "44–47", "30", "36"], ["XXL", "47–50", "31", "36.5"]], "stripes"),
         h("Bottoms", 3, "large"), table(["Size", "Waist (in)", "Hip (in)", "Inside leg (in)"], [
         ["28", "28", "35", "30 / 32"], ["30", "30", "37", "30 / 32 / 34"], ["32", "32", "39", "30 / 32 / 34"], ["34", "34", "41", "30 / 32 / 34"], ["36", "36", "43", "32 / 34"]], "stripes")]))], "xx-large", "wide", "top")])))

kit("aisle-track", AK, "Aisle track your order: where to find it",
 "Where to see an order's progress (the customer's account, or the link in the shipping email), what each order status means and what to do if a parcel is late. Part of the Aisle kit.",
 "track order, order status, delivery, account, aisle",
 sec("Track", cols([
   col(N([h("Where's my order?", 2, "xx-large"),
          p("Every order, its status and its tracking link are in your account. Checked out as a guest? The tracking link is in your shipping email.", "medium"),
          btns([("Go to your account", None, "/account/"), ("Contact us", "outline", "/help/contact/")])]), "45%"),
   col(N([h("What the status means", 3, "large"), table(["Status", "What's happening"], [
       ["Processing", "We've got your order and we're packing it"],
       ["Shipped", "It's with the courier; the tracking link is in your email"],
       ["Completed", "It's been delivered"],
       ["On hold", "We need something from you, so check your email"]], "stripes"),
       p("Not arrived two days after the date in your tracking? Write to us with your order number and we'll chase it or send a new one.", None, "secondary")]))], "xx-large", "wide", "top")))

AFAQ = [
    ("Shipping", [
        ("How much is shipping?", "Free in the US on orders over $75, otherwise $8. Express is $18. Abroad, the price shows at checkout."),
        ("When will my order leave?", "Orders placed by 2pm Pacific on a working day leave the same day."),
        ("Do you ship to the EU and the UK?", "Yes. VAT for your country is added at checkout, so there's nothing to pay on delivery.")]),
    ("Returns and repairs", [
        ("How long do I have to return something?", "60 days from delivery. In the EU you also have 14 days to cancel for any reason."),
        ("Can I swap a size?", "Yes, for free. We send the new size as soon as you've posted the old one."),
        ("What's covered by free repairs?", "Seams, zips and cuffs on anything we make, for a year from delivery. Send us a photo first.")]),
    ("Payment", [
        ("How can I pay?", "Card, Apple Pay and Google Pay. The checkout is secure and we never see your card number."),
        ("Do you charge sales tax?", "We add sales tax where the law asks us to. It shows at checkout before you pay.")]),
    ("Gift cards and the Sock club", [
        ("How do gift cards work?", "They're sent by email on the day you choose, with your note. They're good for anything and they never run out."),
        ("Can I pause the Sock club?", "Yes. Skip a month or cancel any time from your account.")]),
]
kit("aisle-faq", AK, "Aisle questions: answers grouped by topic",
 "The questions shoppers ask, grouped into shipping, returns, payment, and gift cards and subscriptions, as answers that open and close. Part of the Aisle kit; put the shop's real policies here.",
 "faq, questions, shipping, returns, payment, gift cards, accordion, aisle",
 sec("Questions", N([N([h(t, 2, "x-large"), accordion(qs)]) for t, qs in AFAQ]), content="56rem"))

kit("aisle-faq-short", AK, "Aisle questions: before you order",
 "Four questions shoppers ask before they buy, as answers that open and close, beside a heading and a link to the help centre. Part of the Aisle kit.",
 "faq, questions, before you order, shipping, returns, sizes, accordion, aisle",
 sec("Questions", cols([
   col(N([alabel("Before you order"), h("Good to know", 2, "xx-large"), p("Can't find it? A person replies the same working day.", None, "secondary"), btns([("Help centre", "outline", "/help/")])]), "36%"),
   col(accordion([AFAQ[0][1][0], AFAQ[1][1][0], AFAQ[1][1][1], ("How do I find my size?", "Measure a top you love, flat, armpit to armpit, and compare it with the size guide. Between sizes, take the smaller one.")]))], "xx-large", "wide", "top")))

kit("aisle-contact", AK, "Aisle contact: email, studio and the contact form",
 "How to reach the shop (email, the studio for pick-ups and its hours, and a note to include the order number) beside the contact form. Part of the Aisle kit.",
 "contact, email, customer service, studio, form, aisle",
 sec("Contact us", cols([
   col(N([h("We're real people, in Portland", 2, "xx-large"),
          p(f'<a href="mailto:{AMAIL}">{AMAIL}</a>', "large", None, None, None, None, raw=True, bind="email_linked"),
          p("A person replies the same working day, Monday to Friday.", None, "secondary"),
          h("The studio", 3, "large"), p(AADDR, None, bind="address"), p(AHOURS, None, "secondary", bind="hours"),
          p("About an order? Put your order number in your message and we'll find it straight away.", None, "secondary")]), "40%"),
   col(card(N([h("Send a message", 3, "large"), form("contact", "Email us", f"mailto:{AMAIL}", "We'll reply by email.")]), "section-tint"))], "xx-large", "wide", "top")))

# ---------------------------------------------------------------- brand sections
ALOOKS = [("A woman in a navy coat walking through a pine forest", "Forest Park, Sunday"), ("A woman in a red checked jacket on a lake pier", "Trillium Lake"),
          ("A hiker in a red beanie looking out over the hills", "Up the gorge"), ("A woman in a black jacket holding a pink flower", "Saturday market"),
          ("A couple walking past a stone building", "Downtown"), ("A woman in a warm jumper holding a sparkler", "New Year's Eve")]
kit("aisle-lookbook", AK, "Aisle lookbook: the season's photos",
 "The season's photos in a grid, each opening full screen with a caption of where it was taken, then a button to shop what's new. Part of the Aisle kit; use the shop's own photos.",
 "lookbook, gallery, photos, styling, outfits, season, aisle",
 sec("Lookbook", N([grid([stackg([zoom(img("placeholder-tall.svg", alt, "4/5")), p(cap, "small", "secondary")], "small") for alt, cap in ALOOKS], 3, "16rem", "large"),
                    btns([("Shop new in", None, "/new-in/")], "center")])))

kit("aisle-team", AK, "Aisle the team: the people behind the shop",
 "The people who run the shop, each with their name, what they do and a line about them. Part of the Aisle kit; use real people's words, with permission.",
 "team, founders, people, about, aisle",
 sec("Team", N([ahead("Who we are", "Three of us, and two mills"), grid([grp(N([h(n, 3, "large"), alabel(r, "primary"), p(d, None, "secondary")]), "section-card", PAD_CARD, "small", {"type": "default"}) for n, r, d in [
    ("Iris Byrne", "Co-founder and designer", "Designs every piece and still packs orders on Tuesdays."),
    ("Malik Mensah", "Co-founder", "Looks after the mills, the money and the customer emails."),
    ("Tess Reid", "Stylist and photographer", "Shoots every photo against the same grey wall, so the colours you see are the colours you get.")]], 3, "16rem", "medium")])))

kit("aisle-numbers", AK, "Aisle numbers: four figures that count up",
 "Four numbers that count up as they scroll into view, each with a short line. Needs the AnyPress Blocks plugin. Part of the Aisle kit; use real figures only.",
 "numbers, statistics, counter, brand, aisle",
 sec("Numbers", grid([stackg([counter(n, sfx, "", "xxx-large", AHEAD, 0).replace('"fontWeight":"900"', '"fontWeight":"700"'), p(lbl, None, "secondary")]) for n, sfx, lbl in
     [(50, "+", "washes, and it still looks new"), (2, "", "family mills we've visited ourselves"), (38000, "", "orders packed by hand since 2020"), (60, "", "days to change your mind")]], 4, "13rem", "x-large"), "section-tint"))

kit("aisle-gift", AK, "Aisle gift cards: how they work",
 "How the shop's gift cards work, in three steps, beside the amounts and a button to buy one. Part of the Aisle kit; point the button at the shop's own gift card product.",
 "gift card, gift voucher, present, aisle",
 sec("Gift cards", cols([
   col(img("placeholder-wide.svg", "A woman in a reindeer jumper holding a wrapped present", "4/3"), "50%"),
   col(N([h("The easy present", 2, "xx-large"),
          lst(["Choose an amount, from $25 to $200", "Add your note and the day it should arrive", "We email it to them, ready to spend on anything"]),
          p("Gift cards never run out and can be used over several orders.", None, "secondary"),
          btns([("Buy a gift card", None, "/item/gift-card/")])]), valign="center")], "xx-large", "wide", "center")))

# ---------------------------------------------------------------- pages
def aisle_page(slug, title, desc, kw, parts):
    write(slug, title, desc, "anypress/pages", kw, N(parts), "core/post-content", " * Post Types: page\n")

aisle_page("aisle-page-new-in", "New in page: Aisle kit",
 "A New in page for an online shop: a heading, every product newest first as FluentCart product cards in pages, and the newsletter. Aisle kit.",
 "new in, new arrivals, latest, products, aisle",
 [apage_hero("New in", "Fresh from the mills this month: heavier fleece, forest green and oatmeal, and the zipper hoodie is back.", "Shop / New in", None, "A hand picking a striped top from a rail"),
  sec("Products", ashop("aisle-new-in-all", 12, paginate=True), None, ("large", "xx-large", None, None))])

aisle_page("aisle-page-lookbook", "Lookbook page: Aisle kit",
 "A Lookbook page for a clothing shop: a heading, the season's photos that open full screen, one look to shop piece by piece and the newest products. Aisle kit.",
 "lookbook, gallery, outfits, season, aisle",
 [apage_hero("The winter lookbook", "Shot around Portland on friends, customers and occasionally our parents. Click a photo to see it full size.", "Lookbook", None, "A woman in a checked scarf checking her watch"),
  BODIES["aisle-lookbook"], BODIES["aisle-look"], BODIES["aisle-new-in"]])

aisle_page("aisle-page-gift-cards", "Gift cards page: Aisle kit",
 "A Gift cards page for an online shop: a heading, how gift cards work with a button to buy one, the subscription beside it and questions. Aisle kit.",
 "gift cards, gifts, present, subscription, aisle",
 [apage_hero("Gift cards", "For the person who already has everything, or who'd rather choose. Sent by email, on the day you pick.", "Shop / Gift cards", [("Buy a gift card", None, "/item/gift-card/")], "A woman in a warm jumper holding a sparkler"),
  BODIES["aisle-gift"], BODIES["aisle-club"], sec("Questions", accordion(AFAQ[3][1] + [("Can I use a gift card and a discount code together?", "Yes. Add the code at checkout, then pay what's left with the gift card.")]), None, ("x-large", "xx-large", None, None), "56rem")])

aisle_page("aisle-page-help", "Help centre page: Aisle kit",
 "A Help centre page for an online shop: a heading, a card for every help page, the questions shoppers ask most and how to reach a person. Aisle kit.",
 "help, help centre, support, customer service, aisle",
 [ahelp_hero("How can we help?", "Answers about delivery, returns, sizes and your order. Can't find it? A person replies the same working day.", "Help"),
  BODIES["aisle-help-grid"], BODIES["aisle-faq-short"]])

for slug, title, crumb, text, body, kw in [
    ("shipping", "Shipping and delivery", "Help / Shipping", "What delivery costs, how long it takes and where we send. Free in the US on orders over $75.", "aisle-shipping", "shipping, delivery, international, vat"),
    ("returns", "Returns and exchanges", "Help / Returns", "60 days to send it back or swap a size, free in the US. Here's how.", "aisle-returns", "returns, exchanges, refunds, withdrawal"),
    ("size-guide", "Size guide", "Help / Size guide", "Measurements for every fit, and the two-minute trick that saves almost every return.", "aisle-size-guide", "size guide, sizes, fit, measurements"),
    ("track-order", "Track your order", "Help / Track your order", "Where your parcel is, and what to do if it's late.", "aisle-track", "track order, order status, delivery"),
    ("faq", "Questions", "Help / Questions", "Everything shoppers ask us, about delivery, returns, payment, gift cards and the Sock club.", "aisle-faq", "faq, questions, answers"),
    ("contact", "Contact us", "Help / Contact", "Write to us about an order, a size or anything else. A person replies the same working day.", "aisle-contact", "contact, email, customer service"),
]:
    aisle_page(f"aisle-page-{slug}", f"{title} page: Aisle kit",
     f"A {title} page for an online shop: a heading, " + {"shipping": "delivery options and costs, sending abroad with VAT for the EU and UK", "returns": "how to return in three steps and the rules, including the EU's 14 days to cancel", "size-guide": "how to measure and size charts for tops and bottoms", "track-order": "where to find an order and what each status means", "faq": "every question grouped by topic", "contact": "the email address, studio and hours beside the contact form"}[slug] + ", and links to the other help pages. Aisle kit.",
     kw + ", help, aisle", [ahelp_hero(title, text, crumb, f"/help/{slug}/"), BODIES[body]] + ([BODIES["aisle-help-grid"]] if slug != "faq" else [BODIES["aisle-contact"]]))

aisle_page("aisle-page-cancel", "Cancel an order page: Aisle kit",
 "The page where EU and UK shoppers cancel an order within 14 days: a heading, the cancellation form from FluentCart's free Customer Rights add-on, what happens next, and links to the other help pages. Aisle kit; needs the Customer Rights add-on (FluentCart, Settings, Features and addons). Put it on the page the add-on makes, Withdraw from contract.",
 "cancel order, withdrawal, eu, 14 days, right to cancel, customer rights, help, aisle",
 [ahelp_hero("Cancel an order", "Shopping from the EU or the UK? You have 14 days from delivery to cancel any order, no reason needed. Fill this in and we'll confirm by email straight away.", "Help / Cancel an order"),
  sec("Cancellation form", cols([
    col(N(['<!-- wp:shortcode -->\n[fluent_cart_withdrawal]\n<!-- /wp:shortcode -->']), "60%"),
    col(card(N([h("What happens next", 3, "large"), lst([
        "You get an email at once with what you sent and when",
        "We reply within one working day with a free return label",
        "Your refund, including the standard shipping, reaches your card within 14 days of the parcel getting back to us"]),
        p("Not in the EU or the UK? Our 60-day returns cover you. <a href=\"/help/returns/\">How returns work</a>", None, "secondary", raw=True)]), "section-brand-soft"))], "xx-large", "wide", "top"), None, ("x-large", "xx-large", None, None)),
  BODIES["aisle-help-grid"]])

aisle_page("aisle-page-about", "Our story page: Aisle kit",
 "An Our story page for a clothing brand: a heading with a photo, the story, numbers that count up, what the brand stands for, the team and the newest products. Aisle kit.",
 "about, our story, brand, team, values, aisle",
 [apage_hero("Our story", "One hoodie, a kitchen table and a promise: clothes that still look good after fifty washes.", "Our story", None, "Clothes hanging on a rail in a bright shop"),
  sec("Story", cols([
    col(N([h("Why we started", 2, "xx-large"),
           p("In 2020 Iris was on her fourth hoodie in two years, each one bobbled and shapeless after a few months. Malik had spent ten years buying fabric for big brands and knew it didn't have to be that way.", "large"),
           p("So they made one hoodie, properly: heavier fleece, flat seams and cuffs that hold their shape. It sold out in a week. Five years on, there are three of us, two family mills and everything we make is still packed by hand in Portland.")]), "55%", valign="center"),
    col(img("placeholder-tall.svg", "Hands at an old sewing machine with a spool of thread", "4/5"))], "xx-large", "wide", "center")),
  BODIES["aisle-numbers"], BODIES["aisle-team"], BODIES["aisle-new-in"]])

aisle_page("aisle-page-reviews", "Reviews page: Aisle kit",
 "A Reviews page for an online shop: a heading with the overall rating, reviews as cards with stars, names and what each person bought, the promises and the newest products. Aisle kit; use real reviews, with permission.",
 "reviews, testimonials, customers, rating, aisle",
 [apage_hero("Reviews", "Rated 4.8 out of 5 from more than 1,200 reviews. Every product page has its own reviews too.", "Reviews", [("Shop everything", None, "/shop/")], "A couple walking past a stone building"),
  sec("All reviews", grid([areview(*r) for r in AREVIEWS + [
    ("Bought the Sock club for my dad. He now talks about socks. Thank you, I think.", "Hannah L.", "Sock club"),
    ("Sent a gift card to my sister in Berlin. The VAT was all sorted at checkout, nothing extra to pay.", "Paul D.", "Gift card"),
    ("The fleece jacket is warm enough for Portland winters and doesn't look like a sleeping bag.", "Aisha B.", "Fleece jacket")]], 3, "18rem", "medium"), "section-tint"),
  BODIES["aisle-promises"], BODIES["aisle-new-in"]])

aisle_page("aisle-page-thanks", "Thank-you page: Aisle kit",
 "The page visitors see after sending a form: thanks, when to expect a reply and the newest products. Aisle kit; send every form here.",
 "thank you, thanks, confirmation, form sent, aisle",
 [sec("Thanks", N([alabel("Message sent"), h("Thanks. We'll reply the same working day.", 1, "xxx-large"),
    p("Check your email for a copy of what you sent. In the meantime, here's what just landed.", "large", "secondary"),
    btns([("Back to the home page", None, "/"), ("Shop new in", "outline", "/new-in/")])]), None, ("xxx-large", "x-large", None, None), "56rem"),
  BODIES["aisle-new-in"]])

print("aisle ok")
