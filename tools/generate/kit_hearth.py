# Hearth (0.11.0): a whole website for a café, bakery or restaurant, written for a family bakery café. Run by kits.py
# after kit_launch.py, so every helper in kits.py, kits_more.py, kit_ridge.py and the kits before it is in scope.
#
# A printed menu: a soft serif for headings, olive and mustard on oat. Pages link to each other by slug: /menu/ and one
# page per part of the menu under it, /order/ (cake orders), /catering/, /markets/ and one page per market under it,
# /about/, /reviews/, /offers/, /jobs/, /faq/, /journal/, /contact/, /thank-you/. Forms are named groups, as in Ridge:
# "Form: quote" orders a cake, "Form: apply" is the job application.

HF = "young-serif"
HPHONE = "555 0198"
HTEL = "tel:5550198"
HORDER = "/order/"
HADDRESS = "14 Market Street, Springfield"
HLAT, HLON = 39.7990, -89.6440

def htel(size="xx-large"):
    return p(f'<a href="{HTEL}">' + T(HPHONE) + '</a>', size, None, None, HF, None, raw=True, bind="phone_linked")

def hhead(title, text=None, link=None, size="xxx-large"):
    left = stackg([h(title, 2, size)] + ([p(text, "medium", "secondary", None, None, {"fontStyle": "italic"})] if text else []))
    return row([left, btns([(link[0], "outline", link[1])])] if link else [left], valign="bottom")

def h_buttons():
    """The header's buttons: the phone number and Order a cake on tablets and computers, just "Call" on phones."""
    order = f'<!-- wp:button {j({"metadata": {"blockVisibility": {"viewport": {"mobile": False}}}})} -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{HORDER}">{T("Order a cake")}</a></div>\n<!-- /wp:button -->'
    call = f'<!-- wp:button {j({"className": "is-style-outline", "metadata": {"blockVisibility": {"viewport": {"mobile": False}}, "bindings": button_bindings("phone")}})} -->\n<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="{HTEL}">{T(HPHONE)}</a></div>\n<!-- /wp:button -->'
    short = f'<!-- wp:button {j({"metadata": {"blockVisibility": {"viewport": {"tablet": False, "desktop": False}}, "bindings": button_bindings("phone_link")}})} -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{HTEL}">{T("Call")}</a></div>\n<!-- /wp:button -->'
    return '<!-- wp:buttons {"layout":{"type":"flex","flexWrap":"nowrap"}} -->\n<div class="wp-block-buttons">' + N([call, order, short]) + '</div>\n<!-- /wp:buttons -->'

def hpage_hero(title, text, crumb=None, buttons=None, alt=None):
    words = N(([p(crumb, "small", "secondary", None, None, {"fontStyle": "italic"})] if crumb else []) + [h(title, 1, "xxx-large"), p(text, "large", "secondary")] + ([btns(buttons)] if buttons else []))
    if not alt:
        return sec("Page hero", grp(words, gap="medium", layout={"type": "constrained", "contentSize": "46rem", "justifyContent": "left"}), "section-tint", ("xx-large", "x-large", None, None), "72rem")
    return sec("Page hero", cols([col(words, "50%", valign="center"), col(img("placeholder-wide.svg", alt, "4/3"))], "x-large", "wide", "center"), "section-tint", ("xx-large", "x-large", None, None), "72rem")

# ---------------------------------------------------------------- content
PARTS = [
    ("Bread", "bread", "Sourdough, rye and the country loaf, out of the oven by 7am.", "Loaves of sourdough bread on a wooden board"),
    ("Pastries", "pastries", "Croissants, buns and tarts, laminated by hand the day before.", "Croissants on a baking tray"),
    ("Cakes", "cakes", "Cakes by the slice every day, and whole ones to order.", "A layered cake with cream and berries"),
    ("Breakfast", "breakfast", "Eggs, toast and granola until 11, with our own jam.", "Eggs and toast on a plate with coffee"),
    ("Lunch", "lunch", "Soup, tarts and sandwiches on the morning's bread.", "A bowl of soup with a slice of bread"),
    ("Coffee", "coffee", "Espresso from a roaster down the road, and tea from a family firm.", "A cup of coffee with latte art"),
]
MARKETS = [("Downtown Saturday market", "downtown"), ("Old Town Sunday market", "old-town"), ("Westside Wednesday market", "westside"), ("University farmers market", "university")]
HREVIEWS = [
    ("The rye is the best I've had outside my grandmother's kitchen. We drive in every Saturday for it.", "Anna K.", "Regular since 2004"),
    ("They made our wedding cake in eight days and it was perfect. Three tiers, lemon and elderflower.", "Jordan and Lee", "Wedding cake"),
    ("Get there before nine or the almond croissants are gone. Worth the alarm.", "Sam R.", "Saturday regular"),
    ("A proper lunch: soup, bread, a slab of tart and the nicest people behind the counter.", "Priya N.", "Works on Market Street"),
    ("They fed forty people at our office breakfast and remembered every allergy.", "Marcus T.", "Catering order"),
    ("Luca taught my son to shape a loaf on a quiet Tuesday. That's the kind of place it is.", "Elena P.", "Neighbour"),
]

def hreview(text, name, note, size="medium"):
    return card(N([p("“" + text + "”", size, None, None, HF, {"lineHeight": "1.4"}), p(f"{name}, {note}", "small", "secondary", None, None, {"fontWeight": "700"})]), "section-card")

# ---------------------------------------------------------------- sections
kit("hearth-topbar", H, "Hearth top bar: today's bake and the phone number",
 "A thin bar above the header with a line about today's bake and a link to order, and the phone number. Part of the Hearth kit; keep the line current.",
 "top bar, announcement, today, phone, header, hearth",
 grp(row([p(T("Fresh loaves from 7am, Tuesday to Sunday") + ' · <a href="/order/">' + T("Order a cake") + '</a>', "small", None, None, None, None, raw=True),
          hide_on(p(T("Call the bakery") + f' <a href="{HTEL}">' + T(HPHONE) + '</a>', "small", None, None, None, None, raw=True), "mobile")], gap="small"),
     "section-brand", ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Top bar"))

HHEADER = grp(N([
    BODIES["hearth-topbar"],
    grp(row([
        row([dyn("site-logo", {"width": 40, "shouldSyncIcon": True}), dyn("site-title", {"level": 0, "fontSize": "large", "fontFamily": HF, "style": {"typography": {"lineHeight": "1"}}})], "left", "small", False, "center"),
        row([dyn("navigation", {"overlayMenu": "mobile", "layout": {"type": "flex", "justifyContent": "right"}}),
             h_buttons()], "right", "medium", False, "center")], "space-between", "medium", False, "center"),
        None, ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Main bar").replace(
        '<!-- wp:group {', '<!-- wp:group {"backgroundColor":"base",', 1).replace('class="wp-block-group alignfull', 'class="wp-block-group alignfull has-base-background-color has-background', 1),
]), "sticky", None, "0", {"type": "default"}, align="full", name="Header")
write("hearth-header", "Hearth header: today's bake, menu and an order button",
 "A site header for a café, bakery or restaurant that stays at the top while visitors scroll: a bar with today's bake and the phone number, then the logo, the menu (with dropdowns for the menu and the place), the phone number and an Order a cake button. Part of the Hearth kit; choose it for the header in the Site Editor.",
 "header", "header, menu, navigation, sticky, order, phone, bakery, cafe, hearth", HHEADER, "core/template-part/header")

kit("hearth-numbers", H, "Hearth numbers: four figures that count up",
 "Four big numbers that count up as they scroll into view (loaves a day, hours of rising, generations, miles to the mill), each with a short line. Needs the AnyPress Blocks plugin. Part of the Hearth kit; use real figures only.",
 "numbers, statistics, counter, bakery, history, hearth",
 sec("Numbers", grid([stackg([counter(n, suf, "", "xx-large", HF, 0), p(lbl, "medium", "secondary", None, None, {"fontStyle": "italic"})]) for n, suf, lbl in
     [(400, "", "loaves out of the oven every morning"), (36, "", "hours for every sourdough to rise"), (3, "", "generations at the same oven"), (40, "", "miles to the mill our flour comes from")]], 4, "14rem", "x-large"), "section-brand-soft"))

kit("hearth-reviews", H, "Hearth reviews: a carousel of kind words",
 "What regulars say, in a carousel, three at a time on a computer and one on a phone, with each person's name and a note. Needs the AnyPress Blocks plugin. Part of the Hearth kit; use real reviews, with permission.",
 "reviews, testimonials, quotes, regulars, carousel, hearth",
 sec("Reviews", N([hhead("Kind words", "From the people in the queue", ("All reviews", "/reviews/")),
                   carousel([hreview(*r) for r in HREVIEWS], 3, "Reviews")])))

kit("hearth-oven", H, "Hearth from the oven: photos that open full screen",
 "Photos of the food in a carousel, each opening full screen when clicked, with a line saying what it is. Needs the AnyPress Blocks plugin. Part of the Hearth kit; use the owner's own photos.",
 "gallery, photos, food, carousel, lightbox, bakery, hearth",
 sec("From the oven", N([hhead("From the oven", "This morning's bake, more or less"), carousel([stackg([zoom(img("placeholder-square.svg", alt, "1")), p(cap, None, "secondary", None, None, {"fontStyle": "italic"})]) for alt, cap in [
    ("From the oven: country loaves cooling on a rack", "Country loaves, cooling"),
    ("From the oven: a tray of croissants", "Croissants, laminated by hand"),
    ("From the oven: a baker shaping dough on a floured bench", "Shaping the rye at 4am"),
    ("From the oven: a slice of cake with berries", "Cake of the day"),
    ("From the oven: coffee being poured at the counter", "The first coffee of the day")]], 3, "Photos from the bakery", 6)]), "section-tint"))

kit("hearth-map", H, "Hearth find us: the address beside a map",
 "Where the place is, with the address, how to get there and parking beside a map. Needs the AnyPress Blocks plugin for the map. Part of the Hearth kit.",
 "location, address, map, directions, parking, visit, hearth",
 sec("Find us", cols([
   col(N([h("Find the bakery", 2, "xxx-large"), p(HADDRESS, "large", None, None, HF, None, bind="address"),
          lst(["Two minutes' walk from the station", "Free parking behind the shop after 9am", "Step-free, with room for prams"], "medium")]), "40%"),
   col(mapb(HADDRESS + ", IL", HLAT, HLON, 16, "4/3"))], "x-large", "wide", "center")))

kit("hearth-faq-open", H, "Hearth questions: answers that open and close",
 "The questions people ask at the counter, as answers that open and close, beside a heading and a link to all questions. Part of the Hearth kit; answer the real questions.",
 "faq, questions, answers, accordion, allergies, hearth",
 sec("Questions", cols([
   col(N([h("Asked at the counter", 2, "xxx-large"), p("Can't see yours? Call the bakery and ask for Maria.", "medium", "secondary", None, None, {"fontStyle": "italic"}), btns([("All questions", "outline", "/faq/")])]), "36%"),
   col(accordion([
     ("Do you have gluten-free bread?", "We bake a gluten-free loaf on Fridays and Saturdays, in a separate tin. Our kitchen uses flour all day, so we can't promise it is free of traces."),
     ("Can I reserve a loaf?", "Yes. Call by 5pm the day before and we'll keep it behind the counter until noon."),
     ("How much notice do you need for a cake?", "Three days for most cakes, and four weeks for wedding cakes."),
     ("Do you have seats?", "Twenty inside and eight in the courtyard when it's warm. We don't take bookings for breakfast or lunch."),
     ("Are dogs welcome?", "In the courtyard, always, with a bowl of water by the door.")]))], "x-large", "wide", "top")))

kit("hearth-signup", H, "Hearth signup: the weekly bake list",
 "A band asking visitors to join a weekly email with the weekend bake and news, with the signup form beside it. Part of the Hearth kit; sits above the footer on every page.",
 "newsletter, signup, email, weekly, specials, hearth",
 sec("Signup", cols([
   col(N([h("The weekend bake, every Thursday", 2, "xx-large"), p("What's coming out of the oven on Saturday and Sunday, the soup of the week and the odd recipe. One short email, no more.", "medium", "secondary")]), "55%", valign="center"),
   col(form("newsletter", "Read the journal", "/journal/"), valign="center")], "large", "wide", "center"), "section-brand-soft", ("x-large", "x-large", None, None)))

HPOPUP = popup("offer", N([
    img("placeholder-wide.svg", "A cup of coffee and a pastry on a café table", "16/9"),
    grp(N([p("First time here?", "small", "secondary", None, None, {"fontStyle": "italic"}), h("Your first coffee is on us", 2, "xx-large"),
           p("Leave your email and we'll send a card for a free coffee with any pastry, plus the weekend bake list every Thursday."),
           form("offer", "See the menu", "/menu/")]), None, (None, None, "large", "large"), "small", {"type": "default"})]),
    label="A free coffee")
kit("hearth-popup", H, "Hearth popup: a free first coffee",
 "A popup that opens five seconds into a first visit with a photo, an offer of a free first coffee and one field for an email address; it closes with its button, Escape or a click outside and stays closed for two weeks. Needs the AnyPress Blocks plugin. Part of the Hearth kit; put it in the footer to show it on every page.",
 "popup, offer, coffee, discount, newsletter, email, modal, hearth", HPOPUP)

HFOOTER = grp(N([
    BODIES["hearth-signup"],
    grp(N([cols([
        col(N([dyn("site-title", {"level": 0, "fontSize": "x-large", "fontFamily": HF}),
               p("Bread, coffee and a long lunch, baked on site every morning since 1989.", None, "main-accent"),
               htel("xx-large"), social(["instagram", "facebook", "google"])]), "34%"),
        col(flinks("The menu", [(n, f"/menu/{s}/") for n, s, *_ in PARTS] + [("Order a cake", "/order/"), ("Catering", "/catering/")])),
        col(flinks("The bakery", [("Our story", "/about/"), ("Markets", "/markets/"), ("Reviews", "/reviews/"), ("Offers", "/offers/"), ("Work with us", "/jobs/"), ("Journal", "/journal/"), ("Questions", "/faq/"), ("Visit", "/contact/")])),
        col(N([h("Opening hours", 3, "medium"), p("Tuesday to Friday, 7am to 3pm<br>Saturday and Sunday, 8am to 3pm<br>Closed Monday", None, "main-accent", raw=True, bind="hours"),
               p(HADDRESS, None, "main-accent", bind="address"), btns([("Order a cake", None, HORDER)])]))], "large", "wide", "top"),
        sep(),
        row([p("© Ferro Bakery. Made by hand in Springfield.", "small", "main-accent"),
             p('<a href="/privacy-policy/">' + T("Privacy") + '</a> · <a href="/contact/">' + T("Visit") + '</a>', "small", "main-accent", None, None, None, raw=True)], gap="small")]),
        "section-dark", ("x-large", "large", None, None), "large", {"type": "constrained", "contentSize": "80rem"}, align="full", name="Footer columns"),
    HPOPUP,
]), None, None, "0", {"type": "default"}, align="full", name="Footer")
write("hearth-footer", "Hearth footer: weekly bake list, menu links and the free coffee",
 "A site footer for a café, bakery or restaurant: a band for the weekly email, then the phone number, menu and bakery links and the opening hours on dark, and the free coffee popup (needs the AnyPress Blocks plugin). Part of the Hearth kit; choose it for the footer in the Site Editor.",
 "footer", "footer, links, opening hours, newsletter, phone, popup, bakery, cafe, hearth", HFOOTER, "core/template-part/footer")

kit("hearth-menu-part", H, "Hearth menu part: one part of the menu with prices",
 "The body of a page for one part of the menu, such as bread: every item with a dotted line to its price and a line about it, a photo that opens full screen, and a card on ordering ahead. Part of the Hearth kit.",
 "menu, prices, bread, dishes, order ahead, hearth",
 sec("Menu", cols([
   col(N([h("On the counter", 2, "xx-large"), p("Baked here every morning. What's on the shelf by 7am is what there is, so come early on Saturdays.", "medium", "secondary", None, None, {"fontStyle": "italic"}),
          grp(N([item(*i) for i in [
            ("Country loaf", "White and wholemeal, 36 hours from start to oven.", "$8.00"),
            ("Dark rye", "Seeded, dense, keeps a week in a cloth bag.", "$9.00"),
            ("Baguette", "Out of the oven at 7am and again at noon.", "$3.50"),
            ("Olive and rosemary", "Saturdays only, until it's gone.", "$9.50"),
            ("Sandwich loaf", "Soft, sliced if you ask, for the school week.", "$6.50")]]), gap="medium", layout={"type": "default"}),
          zoom(img("placeholder-wide.svg", "On the counter: sourdough loaves on wooden shelves", "16/10"))]), "60%"),
   col(card(N([h("Order ahead", 3, "x-large"), p("Call by 5pm and we'll keep your order behind the counter until noon the next day. Bigger orders need two days."),
               htel("x-large"), btns([("Order a cake", None, HORDER), ("Catering", "outline", "/catering/")])]), "section-brand-soft", PAD_CARD))], "x-large", "wide", "top"), content="72rem"))

kit("hearth-markets", H, "Hearth markets: where else to find the bread",
 "The markets and stalls where the place sells, as cards with the day and time and a link to each one's page. Part of the Hearth kit; keep the days current.",
 "markets, stalls, farmers market, locations, where to buy, hearth",
 sec("Markets", N([hhead("At the markets", "Four stalls a week, the same bread as the shop"), grid([card(N([p(when, "small", "secondary", None, None, {"fontStyle": "italic"}), h(n, 3, "large"), p(d), link_p("Find the stall →", f"/markets/{s}/", None, {"fontWeight": "700"})]), "section-card") for (n, s), when, d in zip(MARKETS, [
    "Saturdays, 8am to 1pm", "Sundays, 9am to 1pm", "Wednesdays, 3pm to 7pm", "Thursdays, 11am to 2pm"], [
    "Our biggest stall, under the clock on Main Square, with every loaf and the full pastry table.",
    "Bread, buns and coffee from the van, by the fountain on Church Lane.",
    "An after-work stall with bread, cake and the next day's sandwich loaves.",
    "Lunch for students and staff: soup, sandwiches and slices of tart."])], 4, "14rem", "medium")]), "section-tint"))

kit("hearth-market", H, "Hearth market: one stall, when and where",
 "The body of a page for one market stall: when it runs, where to find it and what's on the table, beside a map. Needs the AnyPress Blocks plugin for the map. Part of the Hearth kit; make one per market.",
 "market, stall, farmers market, location, map, hearth",
 sec("Market", cols([
   col(N([h("Under the clock on Main Square", 2, "xx-large"), p("Saturdays, 8am to 1pm, all year except the two weeks after Christmas.", "large", None, None, HF),
          p("Look for the olive awning by the clock. Luca runs it with two of the bakers, and there's coffee from the van from 8.", "medium"),
          lst(["Every loaf from the shop", "The full pastry table", "Whole cakes to order, picked up here", "Cards and cash"], "medium"),
          btns([("Order for pickup here", None, HORDER)])]), "42%"),
   col(mapb("Main Square, Springfield, IL", 39.8017, -89.6436, 16, "4/3"))], "x-large", "wide", "top")))

kit("hearth-offers", H, "Hearth offers: the loyalty card, a bread club and gift cards",
 "Three offers as cards with the deal in large type, who it's for and a button: a loyalty card, a weekly bread subscription and gift cards. Part of the Hearth kit; keep the offers current.",
 "offers, loyalty, subscription, gift cards, deals, hearth",
 sec("Offers", N([hhead("Little extras", "For regulars and the people they love"), grid([card(N([p(s, "xx-large", None, None, HF), h(t, 3, "large"), p(d), btns([(b, None, l)])]), st, PAD_CARD) for s, t, d, b, l, st in [
    ("10th free", "The loyalty card", "A stamp for every coffee or loaf. The tenth is on us. Ask for a card at the counter.", "Visit the bakery", "/contact/", "section-brand-soft"),
    ("$30 a month", "The bread club", "A loaf of your choice every week, kept for you until 2pm, with a pastry on the first Saturday.", "Join the club", "/contact/", "section-card"),
    ("Any amount", "Gift cards", "For a birthday breakfast or a cake they choose themselves. Buy them at the counter or by phone.", "Call the bakery", HTEL, "section-brand-soft")]], 3, "16rem", "medium")])))

kit("hearth-catering", H, "Hearth catering: breakfasts, lunches and parties",
 "Three catering packages as cards with what's in them and the price per person, and a line on how to order. Part of the Hearth kit; match it to the real menu.",
 "catering, events, office breakfast, party, packages, hearth",
 sec("Catering", N([hhead("Feeding a crowd", "For offices, parties and the morning after a wedding"), grid([card(N([h(t, 3, "x-large"), p(price, "large", None, None, HF), lst(items), p(note, None, "secondary", None, None, {"fontStyle": "italic"})]), st, PAD_CARD) for t, price, items, note, st in [
    ("Office breakfast", "$9 a person", ["Croissants and buns", "Fruit and yoghurt", "Coffee and tea urns"], "From 10 people, delivered by 8am.", "section-card"),
    ("Working lunch", "$15 a person", ["Sandwiches on the morning's bread", "A slice of tart and a salad", "Cake to finish"], "From 10 people, delivered by noon.", "section-brand-soft"),
    ("Party table", "$22 a person", ["Loaves, cheeses and our pickles", "Savoury tarts and rolls", "A whole cake of your choice"], "From 20 people, set up and cleared away.", "section-card")]], 3, "16rem", "medium"),
   p("Order at least three days ahead. Call the bakery or use the order form, and we'll send a quote the same day.", "medium", None, "center"),
   btns([("Ask for a quote", None, HORDER)], "center")]), "section-tint"))

kit("hearth-jobs", H, "Hearth jobs: why work here and the open roles",
 "Why people work at the place, each open role with its hours and pay, and the application. Part of the Hearth kit; keep the roles current and put the site's application form in the named Form group.",
 "careers, jobs, hiring, baker, barista, apply, hearth",
 sec("Careers", N([
   hhead("Why work here", "A family kitchen, not a factory"),
   grid([stackg([h(t, 3, "large"), p(d, None, "secondary")]) for t, d in [
     ("Done by 3pm", "The shop closes at three and nobody works past five."),
     ("Mondays off", "Every Monday, for everyone, all year."),
     ("Bread to take home", "A loaf and whatever's left on the shelf, every day."),
     ("Learn the trade", "Maria and Luca teach every baker the whole process, from mixing to the oven.")]], 4, "13rem"),
   '<!-- wp:spacer {"height":"var:preset|spacing|large"} -->\n<div style="height:var(--wp--preset--spacing--large)" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->',
   h("Open roles", 2, "xx-large"),
   N([card(N([row([h(t, 3, "large"), p(when, None, None, None, None, {"fontWeight": "700"})], valign="center"), p(d, None, "secondary"), btns([("Apply for this", None, "#apply")])]), "section-tint") for t, when, d in [
     ("Early baker", "4am to noon, $21 an hour", "Mix, shape and bake the morning's bread with Luca. We'll teach you; you bring the early start."),
     ("Barista", "7am to 3pm, $17 an hour plus tips", "Run the coffee machine on the busiest counter in town, Wednesday to Sunday."),
     ("Counter and café", "Weekends, $16 an hour plus tips", "Serve, wrap, chat and keep the café tidy on Saturdays and Sundays.")]]),
   grp(N([h("Apply", 2, "xx-large"), p("Tell us who you are, the role you'd like and when you could start. We reply to everyone within a week."),
          form("apply", "Email the bakery", "mailto:jobs@example.com")]), "section-card", PAD_CARD, "small", {"type": "default"}, anchor="apply")])))

kit("hearth-order-form", H, "Hearth order: a cake or a big order",
 "A form to order a cake or a big order, beside how ordering works and a card about the cakes. Part of the Hearth kit; put the site's form in the named Form group.",
 "order, cake order, custom cake, catering, form, hearth",
 sec("Order", cols([
   col(card(N([h("Tell us what you'd like", 2, "xx-large"), p("Choose what you'd like, the day you need it and any writing on top. We'll call or email within a day to confirm the price."),
               form("quote", "Call " + HPHONE, HTEL, "In a hurry? Call the bakery.")]), "section-card", PAD_CARD), "58%"),
   col(N([h("How ordering works", 3, "x-large"),
          lst(["Three days' notice for most cakes", "Four weeks for wedding cakes, with a tasting first", "Pay when you pick up, or on delivery", "Delivery in Springfield for $8"], "medium"),
          card(N([h("Cakes we love making", 3, "large"), p("Lemon and elderflower, chocolate and hazelnut, carrot with brown butter, and Maria's plum cake in the autumn."), btns([("See the cakes", "outline", "/menu/cakes/")])]), "section-brand-soft")]))],
   "x-large", "wide", "top"), "section-tint"))

kit("hearth-contact", H, "Hearth contact: the phone, hours and address",
 "A contact section for a café or bakery: the phone number, email, address and opening hours beside the contact form, then a map. Needs the AnyPress Blocks plugin for the map. Part of the Hearth kit.",
 "contact, visit, phone, email, hours, address, map, form, hearth",
 sec("Contact", N([cols([
   col(N([h("Come by or call", 2, "xx-large"), htel("xxx-large"),
          p('<a href="mailto:hello@example.com">hello@example.com</a>', "medium", None, None, None, None, raw=True, bind="email_linked"),
          p(HADDRESS, "medium", bind="address"), p("Tuesday to Friday, 7am to 3pm<br>Saturday and Sunday, 8am to 3pm<br>Closed Monday", None, "secondary", raw=True, bind="hours")]), "42%"),
   col(card(N([h("Send a message", 3, "x-large"), form("contact", "Call " + HPHONE, HTEL, "We read messages after the shop closes and reply the same day.")]), "section-tint", PAD_CARD))], "x-large", "wide", "top"),
   mapb(HADDRESS + ", IL", HLAT, HLON, 16, "21/9")])))

# The home page: numbers, reviews, questions and a map join the original sections.
kit_page("kit-food", "Home page: Hearth kit, food and drink",
 "A complete home page for a café, bakery or restaurant in the Hearth kit: a menu card over a food photo, the menu with dotted leaders, numbers that count up, four favourites on coloured tiles, the story beside a photo, reviews in a carousel, questions, a map and the practical details. Apply the Hearth style for the look it was designed with.",
 "home, restaurant, cafe, bakery, food, menu, kit, hearth",
 ["hearth-hero", "hearth-menu", "hearth-numbers", "hearth-specimens", "hearth-story", "hearth-reviews", "hearth-faq-open", "hearth-map", "hearth-visit"])

# ---------------------------------------------------------------- pages
def hearth_page(slug, title, desc, kw, parts):
    write(slug, title, desc, "anypress/pages", kw, N(parts), "core/post-content", " * Post Types: page\n")

hearth_page("hearth-page-services", "Menu page: Hearth kit",
 "A Menu page for a café or bakery: a heading, the full menu with dotted leaders, every part of the menu with a link to its own page, photos from the oven and the practical details. Hearth kit.",
 "menu, food, dishes, prices, bakery, cafe, hearth",
 [hpage_hero("The menu", "Everything is made here, most of it before the sun is up. Prices include tax.", "Menu", [("Order a cake", None, HORDER), ("Catering", "outline", "/catering/")]),
  BODIES["hearth-menu"],
  sec("All of it", grid([stackg([sep(), h(n, 3, "large"), p(d, None, "secondary"), link_p(f"See the {n.lower()} →", f"/menu/{s}/", None, {"fontWeight": "700"})], "small") for n, s, d, _ in PARTS], 3, "16rem", "x-large")),
  BODIES["hearth-oven"], BODIES["hearth-visit"]])

hearth_page("hearth-page-service", "Menu part page: Hearth kit (one part of the menu)",
 "A page for one part of the menu, such as bread: a heading with a photo, every item with its price, ordering ahead, photos from the oven, reviews, questions and the practical details. Hearth kit; make one per part of the menu.",
 "menu page, bread, pastries, cakes, prices, hearth",
 [hpage_hero("Bread", "Sourdough, rye and the country loaf, out of the oven by 7am.", "Menu / Bread", [("Order ahead", None, HTEL), ("Order a cake", "outline", HORDER)], "Inside the bakery: loaves of sourdough bread on a wooden board"),
  BODIES["hearth-menu-part"], BODIES["hearth-oven"], BODIES["hearth-reviews"],
  sec("Questions", cols([col(h("About the bread", 2, "xx-large"), "36%"), col(accordion([
    ("How long does it keep?", "Three days in a cloth bag, a week for the rye. It freezes well, sliced."),
    ("Is the sourdough vegan?", "Yes. Flour, water and salt, nothing else."),
    ("Can I order bread for a party?", "Yes, with two days' notice. Twenty loaves or more come with a small discount."),
    ("Do you slice it?", "Yes, ask at the counter. We'd rather you slice it at home, though.")]))], "x-large", "wide", "top")),
  BODIES["hearth-visit"]])

hearth_page("hearth-page-about", "About page: Hearth kit",
 "An About page for a café or bakery: a heading, the story beside a photo, numbers that count up, photos from the oven and a map. Hearth kit.",
 "about, our story, family, history, bakers, hearth",
 [hpage_hero("Our story", "One oven, a grandmother's recipes and a queue that started in 1989.", "About"),
  sec("Story", cols([
    col(N([h("Three generations, one way of doing it", 2, "xxx-large"),
           p("Maria Ferro opened the bakery on Market Street in 1989 with one oven, a mixer bought second-hand and her grandmother's recipes for rye and plum cake.", "large"),
           p("Her son Luca grew up sweeping the floor and now runs the early shift. The oven is new, the recipes aren't. Every loaf still rises for 36 hours, and the flour still comes from the same mill forty miles away."),
           p("The café came later, when people wouldn't leave. Now there are twenty seats, eight more in the courtyard, and a long lunch most days.")]), "50%", valign="center"),
    col(img("placeholder-tall.svg", "Inside the bakery: the café with its wooden tables", "4/5"))], "x-large", "wide", "center")),
  BODIES["hearth-numbers"], BODIES["hearth-oven"], BODIES["hearth-map"]])

hearth_page("hearth-page-reviews", "Reviews page: Hearth kit",
 "A Reviews page for a café or bakery: a heading, reviews as cards with names and a note, numbers that count up and the practical details. Hearth kit; use real reviews, with permission.",
 "reviews, testimonials, kind words, regulars, hearth",
 [hpage_hero("Kind words", "From regulars, wedding couples and the office down the road.", "Reviews", [("Order a cake", None, HORDER)]),
  sec("All reviews", grid([hreview(*r) for r in HREVIEWS + [
    ("The plum cake in October is the reason I look forward to autumn.", "Ben C.", "Regular"),
    ("Kind to kids, kind to dogs and the coffee is excellent.", "Hannah L.", "Courtyard regular"),
    ("They remembered my order after one visit. Small-town bakery at its best.", "Omar S.", "New in town")]], 3, "18rem", "medium"), "section-tint"),
  BODIES["hearth-numbers"], BODIES["hearth-visit"]])

hearth_page("hearth-page-areas", "Markets page: Hearth kit",
 "A Markets page for a bakery or food business: a heading, a card for each market stall linking to its own page, a map of the shop and the practical details. Hearth kit.",
 "markets, stalls, farmers markets, where to buy, hearth",
 [hpage_hero("At the markets", "Can't get to Market Street? Find the same bread at four stalls around town.", "Markets"),
  BODIES["hearth-markets"], BODIES["hearth-map"]])

hearth_page("hearth-page-area", "Market page: Hearth kit (one stall)",
 "A page for one market stall: a heading, when and where with a map, photos from the oven, reviews and the practical details. Hearth kit; make one per market.",
 "market, stall, farmers market, location, hearth",
 [hpage_hero("Downtown Saturday market", "Every loaf from the shop and the full pastry table, under the clock on Main Square.", "Markets / Downtown", [("Order for pickup", None, HORDER)]),
  BODIES["hearth-market"], BODIES["hearth-oven"], BODIES["hearth-reviews"]])

hearth_page("hearth-page-offers", "Offers page: Hearth kit",
 "An Offers page for a café or bakery: a heading, the loyalty card, bread club and gift cards, questions and the practical details. Hearth kit; keep the offers current.",
 "offers, loyalty card, subscription, gift cards, hearth",
 [hpage_hero("Offers", "A free tenth coffee, a loaf kept for you every week and cakes as gifts.", "Offers"),
  BODIES["hearth-offers"], BODIES["hearth-faq-open"], BODIES["hearth-visit"]])

hearth_page("hearth-page-join", "Order page: Hearth kit",
 "An Order page for a café or bakery: a heading, the order form beside how ordering works, catering packages and reviews. Hearth kit; put the site's form in the named Form group.",
 "order, cake order, custom cake, pre-order, hearth",
 [hpage_hero("Order a cake", "Birthdays, weddings, Friday at the office. Tell us what you'd like and when.", "Order"),
  BODIES["hearth-order-form"], BODIES["hearth-catering"], BODIES["hearth-reviews"]])

hearth_page("hearth-page-catering", "Catering page: Hearth kit",
 "A Catering page for a café or bakery: a heading, catering packages with prices, reviews and the order form. Hearth kit.",
 "catering, events, office, party, hearth",
 [hpage_hero("Catering", "Breakfasts, working lunches and party tables, baked the same morning and delivered in Springfield.", "Catering", [("Ask for a quote", None, HORDER)]),
  BODIES["hearth-catering"], BODIES["hearth-reviews"], BODIES["hearth-visit"]])

hearth_page("hearth-page-faq", "Questions page: Hearth kit",
 "A Questions page for a café or bakery: answers that open and close, grouped into visiting, food and allergies, and orders, and the practical details. Hearth kit; answer the real questions.",
 "faq, questions, answers, allergies, orders, hearth",
 [hpage_hero("Questions and answers", "Opening times, allergies, orders and dogs: the things people ask at the counter.", "FAQ"),
  sec("Questions", N([N([h(group_t, 2, "xx-large"), accordion(qs)]) for group_t, qs in [
    ("Visiting", [
      ("Do you take bookings?", "Not for breakfast or lunch. For groups of eight or more, call and we'll do our best."),
      ("Are dogs welcome?", "In the courtyard, always, with a bowl of water by the door."),
      ("Is there parking?", "Free parking behind the shop after 9am, and a bike rack by the door.")]),
    ("Food and allergies", [
      ("Do you have gluten-free bread?", "On Fridays and Saturdays, in a separate tin. Our kitchen uses flour all day, so we can't promise it is free of traces."),
      ("What's vegan?", "The sourdough, the rye, the baguette and the soup on most days. Ask at the counter.")]),
    ("Orders", [
      ("How much notice do you need for a cake?", "Three days for most cakes, and four weeks for wedding cakes."),
      ("Do you deliver?", "Cakes and catering in Springfield for $8. Bread is pick-up only.")])]]),
    content="56rem"),
  BODIES["hearth-visit"]])

hearth_page("hearth-page-careers", "Jobs page: Hearth kit",
 "A Jobs page for a café or bakery: a heading, why people work there, the open roles with hours and pay, the application form and a map. Hearth kit; keep the roles current and put the site's form in the named Form group.",
 "jobs, careers, hiring, baker, barista, hearth",
 [hpage_hero("Work with us", "Early starts, early finishes and bread to take home. Pay is on this page.", "Jobs", [("See open roles", None, "#apply")]),
  BODIES["hearth-jobs"], BODIES["hearth-map"]])

hearth_page("hearth-page-contact", "Visit page: Hearth kit",
 "A Visit and contact page for a café or bakery: a heading, the phone number, email, address and hours beside the contact form, a map, and the practical details. Hearth kit; put the site's contact form in the named Form group.",
 "contact, visit, hours, address, phone, hearth",
 [hpage_hero("Visit and contact", "Come by, call the bakery or send a message. Orders by phone until 5pm.", "Visit"),
  BODIES["hearth-contact"], BODIES["hearth-faq-open"]])

hearth_page("hearth-page-thanks", "Thank-you page: Hearth kit",
 "The page visitors see after sending a form: thanks, what happens next and when, and links to keep reading. Hearth kit; send every form here.",
 "thank you, thanks, confirmation, form sent, hearth",
 [sec("Thanks", N([p("Message sent", "small", "secondary", None, None, {"fontStyle": "italic"}), h("Thank you. We'll be in touch soon.", 1, "xxx-large"),
    p("Someone from the bakery will call or email within a day, usually after the shop closes at three. Check your email for a copy of what you sent.", "large", "secondary"),
    btns([("Back to the home page", None, "/"), ("See the menu", "outline", "/menu/")])]), None, ("xxx-large", "xxx-large", None, None), "56rem"),
  BODIES["hearth-reviews"]])

print("hearth ok")
