# Commons (0.7.0): a whole website for a chamber of commerce, association, club or church, written for a chamber. Run by
# kits.py after kit_circuit.py, so every helper in kits.py, kits_more.py and kit_ridge.py is in scope.
#
# Civic and calm: a serif for headings, navy with a brick red, square cards and plain rules. Pages link to each other
# by slug: /programs/ and one page per program under it, /events/, /about/, /member-stories/, /directory/ and one page
# per business category under it, /member-deals/, /join/, /faq/, /volunteer/, /news/, /contact/, /thank-you/. Forms
# are named groups, as in Ridge: "Form: quote" is the membership application, "Form: apply" the volunteer form.

K = "anypress/kit-community"
SF = "crimson-pro"
MPHONE = "555 0164"
MTEL = "tel:5550164"
JOIN = "/join/"
ADDRESS = "100 Main Street, Springfield"
SERIF_T = {"fontWeight": "600", "lineHeight": "1"}
EYE_T = {"textTransform": "uppercase", "letterSpacing": "0.1em", "fontWeight": "700"}

def meye(text, color="primary-alt"):
    return p(text, "x-small", color, None, None, EYE_T)

def mimg(alt, ratio="3/2", file="placeholder-wide.svg"):
    return img(file, alt, ratio)

def mtel(size="xx-large"):
    return p(f'<a href="{MTEL}">' + T(MPHONE) + '</a>', size, None, None, SF, SERIF_T, raw=True, bind="phone_linked")

def mhead(eb, title, link=None, size="xx-large"):
    left = stackg([meye(eb), h(title, 2, size)])
    return row([left, btns([(link[0], "outline", link[1])])] if link else [left], valign="bottom")

def m_buttons():
    """The header's buttons: Join and the number on tablets and computers, just "Call" on phones."""
    join = f'<!-- wp:button {j({"metadata": {"blockVisibility": {"viewport": {"mobile": False}}}})} -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{JOIN}">{T("Join the chamber")}</a></div>\n<!-- /wp:button -->'
    call = f'<!-- wp:button {j({"className": "is-style-outline", "metadata": {"blockVisibility": {"viewport": {"mobile": False}}, "bindings": button_bindings("phone")}})} -->\n<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="{MTEL}">{T(MPHONE)}</a></div>\n<!-- /wp:button -->'
    short = f'<!-- wp:button {j({"metadata": {"blockVisibility": {"viewport": {"tablet": False, "desktop": False}}, "bindings": button_bindings("phone_link")}})} -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{MTEL}">{T("Call")}</a></div>\n<!-- /wp:button -->'
    return '<!-- wp:buttons {"layout":{"type":"flex","flexWrap":"nowrap"}} -->\n<div class="wp-block-buttons">' + N([call, join, short]) + '</div>\n<!-- /wp:buttons -->'

def mpage_hero(title, text, crumb=None, buttons=None, alt=None):
    words = N(([meye(crumb, "main-accent")] if crumb else []) + [h(title, 1, "xxx-large"), p(text, "medium")] + ([btns(buttons)] if buttons else []))
    if not alt:
        return sec("Page hero", words, "section-brand", ("xx-large", "x-large", None, None), "80rem")
    return sec("Page hero", cols([col(words, "58%", valign="center"), col(mimg(alt, "4/3"))], "x-large", "wide", "center"), "section-brand", ("xx-large", "x-large", None, None), "80rem")

# ---------------------------------------------------------------- content
PROGRAMS = [
    ("Business breakfasts", "business-breakfasts", "A speaker, a hot breakfast and forty other owners, on the second Thursday of every month.", "Free for members", "Members talking over coffee at a business breakfast"),
    ("Mentoring", "mentoring", "New business owners matched with someone who has done it before, for six months of monthly meetings.", "Free for members", "Two colleagues talking across a desk with a laptop"),
    ("Leadership Springfield", "leadership", "Ten months of sessions with the people who run the town, for the next generation of local leaders.", "$450 a place", "A speaker addressing a seated audience in a hall"),
    ("Workshops", "workshops", "Practical lunchtime sessions on hiring, marketing, money and the law, in person and online.", "From $15", "People taking notes at a workshop around a long table"),
    ("Speaking up for business", "advocacy", "We take members' views to the city council and county board, on parking, permits, taxes and planning.", "Included", "A city hall building with a flag outside"),
    ("Young professionals", "young-professionals", "Socials, talks and volunteering for people under 35 who work or own a business in town.", "Free for members", "A group of young people laughing at an evening event"),
]
CATEGORIES = [("Food and drink", "food-and-drink", 39.8017, -89.6436), ("Shops", "shops", 39.7990, -89.6500), ("Trades and building", "trades-and-building", 39.7817, -89.6501),
              ("Professional services", "professional-services", 39.8003, -89.6489), ("Health and wellbeing", "health-and-wellbeing", 39.7890, -89.6620),
              ("Arts and leisure", "arts-and-leisure", 39.8010, -89.6460), ("Property", "property", 39.7700, -89.6800), ("Nonprofits", "nonprofits", 39.7950, -89.6550)]
STORIES = [
    ("I met my accountant, my banker and half my customers at the breakfasts. Best $240 I spend all year.", "Maria Lopez", "Lopez Flowers"),
    ("My mentor had run a shop on Main Street for thirty years. She saved me from two very expensive mistakes.", "Kwame Asante", "Asante Coffee"),
    ("The chamber got the council to rethink the parking plan. Every shop on our block noticed.", "Jen Hart", "Hart & Home"),
    ("Leadership Springfield introduced me to people I'd never have met. Three of them are now clients.", "Chris Novak", "Novak Law"),
    ("We posted one job on the members' board and had a great hire within a week.", "Ray Ellison", "Ellison Builders"),
    ("As a new business in town, the welcome visit and the directory listing made us feel part of it.", "Aisha Khan", "Khan Dental"),
]
EVENTS = [("14", "Mar", "Business breakfast: hiring your first employee", "7:30am to 9am", "The Grand Hotel"),
          ("21", "Mar", "Main Street clean-up", "10am to 1pm", "Meet at the town hall"),
          ("04", "Apr", "Members' evening and awards", "6pm to 9pm", "Riverside Brewery"),
          ("18", "Apr", "Workshop: getting found on Google", "12pm to 1pm", "Online"),
          ("09", "May", "Business breakfast: the new downtown plan", "7:30am to 9am", "The Grand Hotel"),
          ("16", "May", "Young professionals: rooftop social", "5:30pm to 8pm", "The Lincoln Rooftop")]

def program_card(name, slug, text, price, alt):
    return card(N([mimg(alt, "3/2"), h(name, 3, "large"), p(text, None, "secondary"),
                   row([p(price, None, None, None, None, {"fontWeight": "700"}), link_p("Learn more →", f"/programs/{slug}/", None, {"fontWeight": "700"})], valign="center")]),
                "section-card", ("medium", "medium", "medium", "medium"))

def story_card(text, name, biz, size="medium"):
    return card(N([p("“" + text + "”", size, None, None, SF, {"lineHeight": "1.35"}), p(f"{name}, {biz}", "small", "secondary", None, None, {"fontWeight": "700"})]), "section-tint")

# ---------------------------------------------------------------- sections
kit("commons-topbar", K, "Commons top bar: the next event and the phone number",
 "A thin dark bar above the header with the next event and a link to the calendar, the office hours and the phone number. Part of the Commons kit; keep the event current.",
 "top bar, announcement, next event, phone, hours, header, commons",
 grp(row([p(T("Next breakfast: Thursday 14 March, The Grand Hotel") + ' · <a href="/events/">' + T("All events") + '</a>', "small", None, None, None, None, raw=True),
          hide_on(p(T("Office: Mon to Fri, 9am to 5pm") + f' · <a href="{MTEL}">' + T(MPHONE) + '</a>', "small", None, None, None, None, raw=True), "mobile")], gap="small"),
     "section-dark", ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Top bar"))

MHEADER = grp(N([
    BODIES["commons-topbar"],
    grp(row([
        row([dyn("site-logo", {"width": 44, "shouldSyncIcon": True}), dyn("site-title", {"level": 0, "fontSize": "medium", "fontFamily": SF, "style": {"typography": {"lineHeight": "1", "fontWeight": "600"}}})], "left", "small", False, "center"),
        row([dyn("navigation", {"overlayMenu": "mobile", "layout": {"type": "flex", "justifyContent": "right"}, "style": {"typography": {"fontWeight": "600"}}}),
             m_buttons()], "right", "medium", False, "center")], "space-between", "medium", False, "center"),
        None, ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Main bar").replace(
        '<!-- wp:group {', '<!-- wp:group {"backgroundColor":"base",', 1).replace('class="wp-block-group alignfull', 'class="wp-block-group alignfull has-base-background-color has-background', 1),
]), "sticky", None, "0", {"type": "default"}, align="full", name="Header")
write("commons-header", "Commons header: next event, menu and a Join button",
 "A site header for a chamber, association or church that stays at the top while visitors scroll: a dark bar with the next event and the office number, then the logo, the menu (with dropdowns for programs, the directory and about), the phone number and a Join button. Part of the Commons kit; choose it for the header in the Site Editor.",
 "header", "header, menu, navigation, sticky, join, phone, chamber, association, commons", MHEADER, "core/template-part/header")

kit("commons-numbers", K, "Commons numbers: four figures that count up",
 "Four big numbers that count up as they scroll into view (members, years, events a year, money raised), each with a short label, on the brand colour. Needs the AnyPress Blocks plugin. Part of the Commons kit; use the group's real figures.",
 "numbers, statistics, counter, members, impact, commons",
 sec("Numbers", grid([stackg([counter(n, suf, pre, "xxx-large", SF, d), p(lbl, "medium", "main-accent")]) for n, suf, pre, d, lbl in
     [(412, "", "", 0, "member businesses"), (96, " years", "", 0, "speaking up for Springfield"), (48, "", "", 0, "events a year"), (38, "k", "$", 0, "in scholarships last year")]], 4, "12rem"),
     "section-brand", ("x-large", "x-large", None, None)))

kit("commons-programs", K, "Commons programs: cards with photos and links",
 "Every program as a card with a photo, one line about it, who it's for or what it costs and a link to its own page, three across. Part of the Commons kit; each link goes to /programs/<program>/.",
 "programs, services, benefits, cards, photos, links, membership, commons",
 sec("Programs", N([mhead("What members get", "Programs for every stage of a business", ("All programs", "/programs/")),
                    grid([program_card(*x) for x in PROGRAMS], 3, "18rem", "medium")]), "section-tint"))

kit("commons-steps", K, "Commons steps: how to join",
 "Three numbered steps from first visit to member, in big serif numerals, so people know what joining involves. Part of the Commons kit.",
 "how to join, steps, process, membership, commons",
 sec("How to join", N([mhead("How to join", "Three steps, and you're in"), grid([stackg([p(n, "xxx-large", "primary-alt", None, SF, SERIF_T), h(t, 3, "large"), p(d, None, "secondary")]) for n, t, d in [
    ("1", "Come as our guest", "Your first breakfast is free. Meet members, hear the speaker and see if it's for you."),
    ("2", "Choose a level", "Apply online in five minutes. We'll call to welcome you and answer any questions."),
    ("3", "Get listed and get going", "Your business goes in the directory, and we introduce you to members you should know.")]], 3, "16rem", "x-large")])))

kit("commons-stories", K, "Commons member stories: a carousel of quotes",
 "Members in their own words, in a carousel, three at a time on a computer and one on a phone, with each member's name and business. Needs the AnyPress Blocks plugin. Part of the Commons kit; use real quotes, with permission.",
 "testimonials, member stories, quotes, carousel, slider, members, commons",
 sec("Member stories", N([mhead("Member stories", "Why 412 businesses belong", ("All stories", "/member-stories/")),
                          carousel([story_card(*s) for s in STORIES], 3, "Member stories")])))

kit("commons-gallery", K, "Commons gallery: photos from recent events",
 "Photos from recent events in a carousel, each opening full screen when clicked, with a caption of the event and date. Needs the AnyPress Blocks plugin. Part of the Commons kit; use the group's own photos.",
 "gallery, photos, events, carousel, community, commons",
 sec("Gallery", N([mhead("From recent events", "Members together"), carousel([stackg([zoom(img("placeholder-tall.svg", alt, "4/5")), p(cap, None, "secondary")]) for alt, cap in [
    ("A crowd at a summer street fair on Main Street", "Summer street fair, July"),
    ("Members talking over coffee at a business breakfast", "Business breakfast, February"),
    ("A ribbon being cut outside a new shop", "Ribbon cutting at Khan Dental, January"),
    ("Volunteers in matching shirts picking up litter", "Main Street clean-up, October"),
    ("A speaker addressing a seated audience in a hall", "Annual meeting, December")]], 3, "Photos from recent events", 6)]), "section-tint"))

kit("commons-directory-map", K, "Commons directory: a map and every category",
 "Where to find members: every category of the member directory as a link to its own page, beside a map of the town. Needs the AnyPress Blocks plugin for the map. Part of the Commons kit.",
 "directory, members, businesses, categories, map, find, commons",
 sec("Directory", cols([
   col(N([meye("Member directory"), h("Find a member business", 2, "xx-large"), p("Shop local: 412 member businesses in Springfield and the villages around it.", "medium", "secondary"),
          '<!-- wp:list {"className":"is-style-no-bullets","fontSize":"large","style":{"typography":{"lineHeight":"1.6","fontWeight":"600"}}} -->\n'
          '<ul class="wp-block-list is-style-no-bullets has-large-font-size" style="line-height:1.6;font-weight:600">'
          + "\n\n".join(f'<!-- wp:list-item -->\n<li><a href="/directory/{s}/">{T(t)}</a></li>\n<!-- /wp:list-item -->' for t, s, *_ in CATEGORIES) + '</ul>\n<!-- /wp:list -->']), "38%"),
   col(mapb("Springfield, Illinois", 39.7990, -89.6440, 13, "4/3"))], "x-large", "wide", "top")))

kit("commons-faq", K, "Commons questions: answers that open and close",
 "The questions people ask before joining, as answers that open and close, beside a heading and a link to all questions. Part of the Commons kit; answer with the group's real dues and rules.",
 "faq, questions, answers, accordion, membership, commons",
 sec("Questions", cols([
   col(N([meye("Questions"), h("Before you join", 2, "xx-large"), p("Can't see yours? Call the office: you'll talk to Joe or Priya, not a machine.", "medium", "secondary"), btns([("All questions", "outline", "/faq/")])]), "36%"),
   col(accordion([
     ("Who can join?", "Any business, nonprofit or person who works in or near Springfield. You don't need a shop front."),
     ("How much does it cost?", "From $60 a year for individuals and $240 for most small businesses. See the levels on the Join page."),
     ("Can I come to an event first?", "Yes. Your first breakfast is free, and most workshops are open to guests."),
     ("Is it worth it for a one-person business?", "Most of our members have fewer than ten staff. The breakfasts and the directory alone usually pay for it."),
     ("Can I leave?", "Yes, any time. Membership runs for a year and doesn't renew without asking you.")]))], "x-large", "wide", "top")))

kit("commons-call", K, "Commons closing band: join or call",
 "A closing band on the second brand colour asking visitors to join, with the Join button and the office phone number. Part of the Commons kit; ends most pages.",
 "call to action, join, phone, contact, closing, commons",
 sec("Join us", cols([
   col(N([h("Join 412 local businesses", 2, "xxx-large"), p("Membership from $60 a year. Your first breakfast is on us.", "large")]), "60%", valign="center"),
   col(N([btns([("Join the chamber", None, JOIN)]), p("Or call the office", None, "main-accent"), mtel("xx-large")]), valign="center")], "x-large", "wide", "center"), "section-second-brand", ("x-large", "x-large", None, None)))

kit("commons-signup", K, "Commons signup: the weekly email",
 "A band asking visitors to join the weekly email of events and news, with the signup form beside it. Part of the Commons kit; sits above the footer on every page.",
 "newsletter, signup, email, events, subscribe, commons",
 sec("Signup", cols([
   col(N([h("The week in Springfield business", 2, "xx-large"), p("Events, openings and news from members, every Monday morning. Free for anyone.", "medium", "secondary")]), "55%", valign="center"),
   col(form("newsletter", "Get the weekly email", "/events/"), valign="center")], "large", "wide", "center"), "section-tint", ("x-large", "x-large", None, None)))

MPOPUP = popup("offer", N([
    img("placeholder-wide.svg", "Members talking over coffee at a business breakfast", "16/9"),
    grp(N([meye("New to the chamber?"), h("Your first breakfast is on us", 2, "xx-large"),
           p("Leave your email and we'll send a guest pass for the next business breakfast. One email, no calls."),
           form("offer", "See upcoming events", "/events/")]), None, (None, None, "large", "large"), "small", {"type": "default"})]),
    label="A free breakfast for guests")
kit("commons-popup", K, "Commons popup: a free breakfast for guests",
 "A popup that opens five seconds into a first visit with a photo, a guest offer and one field for an email address; it closes with its button, Escape or a click outside and stays closed for two weeks. Needs the AnyPress Blocks plugin. Part of the Commons kit; put it in the footer to show it on every page.",
 "popup, offer, guest, newsletter, email, modal, commons", MPOPUP)

MFOOTER = grp(N([
    BODIES["commons-signup"],
    grp(N([cols([
        col(N([dyn("site-title", {"level": 0, "fontSize": "x-large", "fontFamily": SF}),
               p("The voice of Springfield business since 1930: 412 members helping each other grow and making the town a better place to work.", None, "main-accent"),
               mtel("xx-large"), social(["facebook", "instagram", "linkedin"])]), "34%"),
        col(flinks("Programs", [(n, f"/programs/{s}/") for n, s, *_ in PROGRAMS])),
        col(flinks("The chamber", [("About us", "/about/"), ("Events", "/events/"), ("Member directory", "/directory/"), ("Member stories", "/member-stories/"), ("Member deals", "/member-deals/"), ("Volunteer", "/volunteer/"), ("News", "/news/"), ("Questions", "/faq/")])),
        col(N([h("Visit or call", 3, "medium"), p(ADDRESS, None, "main-accent", bind="address"), p("Office: Mon to Fri, 9am to 5pm", None, "main-accent", bind="hours"),
               btns([("Join the chamber", None, JOIN)])]))], "large", "wide", "top"),
        sep(),
        row([p("© Springfield Chamber of Commerce. A nonprofit membership organization.", "small", "main-accent"),
             p('<a href="/privacy-policy/">' + T("Privacy") + '</a> · <a href="/contact/">' + T("Contact") + '</a>', "small", "main-accent", None, None, None, raw=True)], gap="small")]),
        "section-dark", ("x-large", "large", None, None), "large", {"type": "constrained", "contentSize": "80rem"}, align="full", name="Footer columns"),
    MPOPUP,
]), None, None, "0", {"type": "default"}, align="full", name="Footer")
write("commons-footer", "Commons footer: weekly email, links, address and the guest popup",
 "A site footer for a chamber, association or church: a band for the weekly email, then the phone number, programs, the group's pages, address and hours on dark, and the guest offer popup (needs the AnyPress Blocks plugin). Part of the Commons kit; choose it for the footer in the Site Editor.",
 "footer", "footer, links, newsletter, signup, phone, address, popup, chamber, commons", MFOOTER, "core/template-part/footer")

kit("commons-program-detail", K, "Commons program: what's included and how to take part",
 "The body of one program page: what it is in plain words, a list of what's included, a photo, and a box with the price or who it's for and buttons to sign up or call. Part of the Commons kit.",
 "program, details, included, price, sign up, commons",
 sec("Program details", cols([
   col(N([h("What happens", 2, "xx-large"),
          p("A hot breakfast, twenty minutes from a speaker who knows their subject, ten minutes of questions, and time to meet the other owners in the room. You're done by nine."),
          lst(["Breakfast and coffee from The Grand Hotel", "A local speaker on something that matters to small business", "Two-minute introductions, so you know who's there", "The slides and notes by email afterwards", "Guests welcome: the first one is free"], "medium"),
          zoom(mimg("Photo of the program: members at a breakfast table", "16/9"))]), "60%"),
   col(card(N([meye("Business breakfasts"), p("Free for members", "xx-large", None, None, SF, SERIF_T),
               p("Guests $25, first visit free. Second Thursday of every month, 7:30am to 9am."),
               btns([("Book a place", None, JOIN), ("Call " + MPHONE, "outline", MTEL, "phone")])]), "section-brand-soft", PAD_CARD))], "x-large", "wide", "top")))

kit("commons-members", K, "Commons members: businesses in one category",
 "Member businesses in one category of the directory as cards with the name, what they do, the street and a link, under a heading. Part of the Commons kit; for one directory category page.",
 "directory, members, businesses, listings, category, commons",
 sec("Members", N([mhead("Members in this category", "Eat and drink local"),
   grid([card(N([h(n, 3, "large"), p(d, None, "secondary"), p(a, "small"), link_p("Get in touch →", "/contact/", "small", {"fontWeight": "700"})]), "section-card", ("medium", "medium", "medium", "medium")) for n, d, a in [
     ("Asante Coffee", "Coffee roasters and a café with the best window seats in town.", "212 Main Street"),
     ("Riverside Brewery", "Small-batch beer, a big beer garden and a room for events.", "8 River Road"),
     ("The Grand Hotel", "Rooms, a ballroom and the breakfast you'll eat at our events.", "1 Capitol Square"),
     ("Okafor Bakeries", "Bread, cakes and catering from three shops around town.", "45 Elm Street"),
     ("Lucia's Kitchen", "Family Italian, open six nights, with a private room for twenty.", "310 Main Street"),
     ("Green Leaf Market", "A grocer full of food from farms within fifty miles.", "77 Market Street")]], 3, "16rem", "medium")]), "section-tint"))

kit("commons-deals", K, "Commons member deals: three offers",
 "Offers members give each other, as three cards with the saving in large type, who gives it and what it covers, then the small print. Part of the Commons kit; keep the offers current.",
 "member deals, discounts, offers, benefits, members, commons",
 sec("Member deals", N([grid([card(N([p(s, "xxx-large", None, None, SF, SERIF_T), h(t, 3, "large"), p(d), btns([("Become a member", None, JOIN)])]), st, PAD_CARD) for s, t, d, st in [
    ("15% off", "Printing at Main Street Print", "Business cards, flyers and signs, on every order. Show your member card.", "section-brand-soft"),
    ("Free", "A website check from Novak Digital", "A one-hour review of your website and Google listing, with a written list of fixes.", "section-tint"),
    ("$100 off", "Your first year with Ruiz Accounting", "Bookkeeping or year-end accounts for new clients who are members.", "section-brand-soft")]], 3, "16rem", "medium"),
    p("Member deals are offered by members to other members. Ask the business for the terms; the chamber isn't part of the deal.", "small", "secondary")])))

kit("commons-volunteer", K, "Commons volunteering: roles and how to apply",
 "Ways to volunteer: four reasons people do it, each open role with the time it takes, and the application. Part of the Commons kit; keep the roles current and put the site's application form in the named Form group.",
 "volunteer, get involved, roles, committees, mentoring, commons",
 sec("Volunteer", N([
   mhead("Why volunteer", "Give a few hours, meet the whole town"),
   grid([stackg([h(t, 3, "large"), p(d, None, "secondary")]) for t, d in [
     ("Meet people", "Volunteers get to know members faster than anyone."),
     ("Use your skills", "Mentor, run a workshop, or lend a hand with the books."),
     ("Make the town better", "From the street fair to the clean-up, you'll see the difference."),
     ("It fits around work", "Most roles take two or three hours a month.")]], 4, "13rem"),
   '<!-- wp:spacer {"height":"var:preset|spacing|large"} -->\n<div style="height:var(--wp--preset--spacing--large)" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->',
   h("Open roles", 2, "xx-large"),
   N([card(N([row([h(t, 3, "large"), p(when, None, None, None, None, {"fontWeight": "700"})], valign="center"), p(d, None, "secondary"), btns([("Volunteer for this", None, "#apply")])]), "section-tint") for t, when, d in [
     ("Event helper", "A few hours a month", "Welcome guests at the breakfasts and help run the summer street fair."),
     ("Business mentor", "One hour a month", "Meet a new business owner once a month for six months. Ten years in business or more."),
     ("Committee member", "Two hours a month", "Join the events, membership or downtown committee and help set the year's plans.")]]),
   grp(N([h("Sign up", 2, "xx-large"), p("Tell us who you are, the role you'd like and a few lines about you. Priya replies to everyone within a week."),
          form("apply", "Email the office", "mailto:jobs@example.com")]), "section-card", PAD_CARD, "small", {"type": "default"}, anchor="apply")])))

kit("commons-join-form", K, "Commons join: the application and what happens next",
 "The membership application: the form on one side, and on the other what happens after applying, the levels in short and the office number. Part of the Commons kit; put the site's application form in the named Form group.",
 "join, membership, application, form, sign up, commons",
 sec("Apply", cols([
   col(card(N([h("Apply to join", 2, "xx-large"), p("It takes five minutes. Pay online once we've welcomed you, or by check."),
               form("quote", "Call " + MPHONE, MTEL, "Prefer to talk? Call the office.")]), "section-card", PAD_CARD), "58%"),
   col(N([h("What happens next", 3, "x-large"),
          lst(["We reply within two working days.", "Joe calls to welcome you and answer questions.", "Your business goes in the directory the same week."], "medium"),
          card(N([meye("Not sure yet?"), h("Come to a breakfast first", 3, "large"), p("Your first one is free. Meet members and hear the speaker."), btns([("See upcoming events", "outline", "/events/")])]), "section-brand-soft")]))],
   "x-large", "wide", "top"), "section-tint"))

kit("commons-contact", K, "Commons contact: details, form and map",
 "A contact section for a chamber, association or church: phone, email, address and office hours beside the contact form, then a map with directions. Needs the AnyPress Blocks plugin for the map. Part of the Commons kit.",
 "contact, phone, email, address, hours, map, form, commons",
 sec("Contact", N([cols([
   col(N([h("Call, write or drop in", 2, "xx-large"), mtel("xxx-large"),
          p('<a href="mailto:hello@example.com">hello@example.com</a>', "medium", None, None, None, None, raw=True, bind="email_linked"),
          p(ADDRESS, "medium", bind="address"), p("Office: Mon to Fri, 9am to 5pm. Visitors welcome; the coffee is usually on.", None, "secondary")]), "42%"),
   col(card(N([h("Send a message", 3, "x-large"), form("contact", "Call " + MPHONE, MTEL, "We reply within one working day.")]), "section-tint", PAD_CARD))], "x-large", "wide", "top"),
   mapb(ADDRESS + ", Illinois", 39.8001, -89.6490, 15, "21/9")])))

kit("commons-events-list", K, "Commons events: the full calendar",
 "Every upcoming event as a row with a date block, title, time, place and a link to book, under a heading. Part of the Commons kit; for the Events page, kept to the next two or three months.",
 "events, calendar, schedule, upcoming, book, commons",
 sec("Calendar", N([mhead("Calendar", "The next three months"),
   stackg([event(*e).replace('href="/events/"', f'href="{JOIN}"').replace(">Details<", ">Book a place<") for e in EVENTS], "medium")]), content="64rem"))

# The home page, now with numbers, programs, stories and the directory.
kit_page("kit-community", "Home page: Commons kit, associations, chambers and churches",
 "A complete home page for a chamber of commerce, association, club, nonprofit or church in the Commons kit: a photo of members with how to join, numbers that count up, upcoming events, programs with photos, membership levels, member stories in a carousel, the directory with a map, the latest news, the people who run it, common questions and ways to get involved. Apply the Commons style for the look it was designed with.",
 "home, chamber of commerce, association, nonprofit, church, club, membership, events, kit, commons",
 ["commons-hero", "commons-numbers", "commons-events", "commons-programs", "commons-join", "commons-stories", "commons-directory-map", "commons-news", "commons-leaders", "commons-faq", "commons-involved"])

# ---------------------------------------------------------------- pages
def commons_page(slug, title, desc, kw, parts):
    write(slug, title, desc, "anypress/pages", kw, N(parts), "core/post-content", " * Post Types: page\n")

commons_page("commons-page-services", "Programs page: Commons kit",
 "A Programs page for a chamber or association: a heading, every program as a card linking to its own page, how to join, member stories and a closing band. Commons kit.",
 "programs, benefits, membership, services, commons",
 [mpage_hero("Programs", "Breakfasts, mentoring, workshops and a voice at city hall. Most are free for members.", "What members get", [("Join the chamber", None, JOIN)]),
  BODIES["commons-programs"], BODIES["commons-steps"], BODIES["commons-stories"], BODIES["commons-call"]])

commons_page("commons-page-service", "Program page: Commons kit (one program)",
 "A page for one program, such as the business breakfasts: a heading with a photo, what happens and what it costs, photos from past sessions, member stories, questions about this program and a closing band. Commons kit; make one per program under Programs.",
 "program page, breakfast, mentoring, workshop, single program, commons",
 [mpage_hero("Business breakfasts", "A speaker, a hot breakfast and forty other owners, on the second Thursday of every month.", "Programs / Business breakfasts", [("Book a place", None, JOIN), ("Call " + MPHONE, "outline", MTEL, "phone")], "This program: members talking over coffee at a business breakfast"),
  BODIES["commons-program-detail"], BODIES["commons-gallery"], BODIES["commons-stories"],
  sec("Questions", cols([col(h("About the breakfasts", 2, "xx-large"), "36%"), col(accordion([
    ("Do I need to book?", "Yes, so the hotel knows how many to cook for. Book by the Tuesday before."),
    ("Can I bring a guest?", "Yes. Their first breakfast is free; after that it's $25."),
    ("What if I can't come?", "Cancel by the Tuesday and there's no charge. The slides come by email either way."),
    ("Can I speak at one?", "We'd love to hear your idea. Tell Priya what you'd talk about and why it matters to small business.")]))], "x-large", "wide", "top")),
  BODIES["commons-call"]])

commons_page("commons-page-events", "Events page: Commons kit",
 "An Events page for a chamber, association or church: a heading, the full calendar with a link to book each event, photos from recent events, the weekly email and a closing band. Commons kit; keep the calendar current.",
 "events, calendar, schedule, upcoming, commons",
 [mpage_hero("Events", "Breakfasts, workshops, socials and the summer street fair. Most are free for members and open to guests.", "What's on", [("Join the chamber", None, JOIN)]),
  BODIES["commons-events-list"], BODIES["commons-gallery"], BODIES["commons-call"]])

commons_page("commons-page-about", "About page: Commons kit",
 "An About page for a chamber, association or church: a heading, the story with a photo, numbers that count up, the people who run it, ways to get involved and a closing band. Commons kit.",
 "about, about us, story, history, board, mission, commons",
 [mpage_hero("Speaking up for Springfield business since 1930", "Started by twelve shopkeepers on Main Street. Today we're 412 businesses of every size, from sole traders to the biggest employers in town.", "About us"),
  sec("Story", cols([
    col(N([h("Neighbors helping neighbors", 2, "xx-large"),
           p("The chamber started in 1930, when twelve Main Street shopkeepers met to help each other through hard times. Our job is still the same: help local businesses grow, and make Springfield a better place to work and live.", "large"),
           p("We're a nonprofit, run by a board of members elected each spring and a staff of three. Dues and sponsors pay for everything we do; the city gives us nothing, so we can speak freely."),
           p("We bring members together, we help new businesses get going, and we take members' views to the people who make decisions.")]), "50%", valign="center"),
    col(mimg("A crowd at a summer street fair on Main Street", "4/5", "placeholder-tall.svg"))], "x-large", "wide", "center")),
  BODIES["commons-numbers"], BODIES["commons-leaders"], BODIES["commons-involved"], BODIES["commons-call"]])

commons_page("commons-page-reviews", "Member stories page: Commons kit",
 "A Member stories page: a heading, members' quotes as cards with names and businesses, numbers that count up and a closing band. Commons kit; use real quotes, with permission.",
 "member stories, testimonials, quotes, members, commons",
 [mpage_hero("Member stories", "What members say about belonging. We asked; these are their words.", "Member stories", [("Join the chamber", None, JOIN)]),
  sec("All stories", grid([story_card(*s) for s in STORIES + [
    ("I joined for the directory. I stayed for the people.", "Tom Becker", "Becker Plumbing"),
    ("The workshops are short, practical and cheap. I've been to every one on hiring.", "Lena Ruiz", "Ruiz Accounting"),
    ("When the road works closed our street, the chamber made sure the city heard us.", "Sam Patel", "Riverside Brewery")]], 3, "18rem", "medium")),
  BODIES["commons-numbers"], BODIES["commons-call"]])

commons_page("commons-page-areas", "Member directory page: Commons kit",
 "A Member directory page: a heading, every category with a map, a card for each category linking to its own page, and a closing band. Commons kit.",
 "directory, members, businesses, categories, find, shop local, commons",
 [mpage_hero("Member directory", "Shop local: 412 member businesses, by category.", "Directory"),
  BODIES["commons-directory-map"],
  sec("Categories", grid([card(N([h(t, 3, "large"), p(f"Members in {t.lower()} across Springfield.", None, "secondary"), link_p(f"See {t.lower()}", f"/directory/{s}/", None, {"fontWeight": "700"})]), "section-card") for t, s, *_ in CATEGORIES], 4, "13rem", "medium"), "section-tint"),
  BODIES["commons-call"]])

commons_page("commons-page-area", "Directory category page: Commons kit (one category)",
 "A page for one category of the member directory, such as food and drink: a heading, a few lines with a map, the members in that category and a closing band. Commons kit; make one per category under the directory.",
 "directory category, members, businesses, listings, commons",
 [mpage_hero("Food and drink", "Cafés, bakeries, restaurants and a brewery, all members, all local.", "Directory / Food and drink", [("Join the chamber", None, JOIN)]),
  sec("Local", cols([
    col(N([h("Eat and drink local", 2, "xx-large"),
           p("Springfield's food and drink members range from a coffee roaster on Main Street to the hotel that feeds our breakfasts. Many offer member deals, and most cater for events."),
           lst(["Every listing is a paying member", "Many offer member deals", "Ask the office for catering for your event"], "medium")]), "50%"),
    col(mapb("Springfield, Illinois", 39.8017, -89.6436, 14, "4/3"))], "x-large", "wide", "top")),
  BODIES["commons-members"], BODIES["commons-call"]])

commons_page("commons-page-offers", "Member deals page: Commons kit",
 "A Member deals page: a heading, offers members give each other with the small print, the weekly email and a closing band. Commons kit; keep the offers current.",
 "member deals, discounts, offers, benefits, commons",
 [mpage_hero("Member deals", "Offers members give each other. Show your member card, or mention the chamber when you book.", "Member deals"),
  BODIES["commons-deals"], BODIES["commons-signup"], BODIES["commons-call"]])

commons_page("commons-page-join", "Join page: Commons kit",
 "A Join page: a heading, the membership levels, the application form with what happens next, how to join and common questions. Commons kit; put the site's application form in the named Form group.",
 "join, membership, apply, levels, dues, sign up, commons",
 [mpage_hero("Join the chamber", "Membership from $60 a year. Apply online in five minutes.", "Join"),
  BODIES["commons-join"], BODIES["commons-join-form"], BODIES["commons-steps"], BODIES["commons-faq"]])

commons_page("commons-page-faq", "Questions page: Commons kit",
 "A Questions page for a chamber or association: answers that open and close, grouped into membership, events, the directory and the chamber itself, and a closing band. Commons kit; answer with the group's real rules.",
 "faq, questions, answers, help, membership, commons",
 [mpage_hero("Questions and answers", "Straight answers about membership, events and what the chamber does.", "FAQ"),
  sec("Questions", N([N([h(group_t, 2, "xx-large"), accordion(qs)]) for group_t, qs in [
    ("Membership", [
      ("Who can join?", "Any business, nonprofit or person who works in or near Springfield. You don't need a shop front."),
      ("How much does it cost?", "From $60 a year for individuals, $240 for businesses with up to 25 staff and $900 for larger employers."),
      ("How do I pay?", "By card online once we've welcomed you, or by check. Dues are yearly, from the day you join."),
      ("Can I leave?", "Yes, any time. Membership doesn't renew without asking you.")]),
    ("Events", [
      ("Can guests come?", "Yes. A guest's first breakfast is free, and most workshops are open to everyone."),
      ("Do I need to book?", "For breakfasts and workshops, yes, so we know the numbers. Socials and the street fair, no."),
      ("Can my business sponsor an event?", "Yes. Sponsorship starts at $250. Ask the office for the packs.")]),
    ("The directory", [
      ("How do I get listed?", "Every member is listed. Send us your logo, a line about what you do and a photo."),
      ("Can I change my listing?", "Any time. Email the office and we'll update it the same week.")]),
    ("The chamber", [
      ("Is the chamber part of the city?", "No. We're an independent nonprofit, paid for by members' dues and sponsors."),
      ("Who decides what the chamber says?", "The board, elected by members each spring, after asking members what they think.")])]]),
    content="56rem"),
  BODIES["commons-call"]])

commons_page("commons-page-careers", "Volunteer page: Commons kit",
 "A Volunteer page for a chamber, association or church: a heading, why people volunteer, the open roles with the time each takes, the sign-up form and the people who run the group. Commons kit; keep the roles current and put the site's form in the named Form group.",
 "volunteer, get involved, roles, committees, mentoring, commons",
 [mpage_hero("Volunteer", "Mentor a new business, help at an event or join a committee. Most roles take a few hours a month.", "Get involved", [("See open roles", None, "#apply")]),
  BODIES["commons-volunteer"], BODIES["commons-leaders"]])

commons_page("commons-page-contact", "Contact page: Commons kit",
 "A Contact page for a chamber, association or church: a heading, the phone number, email, address and hours beside the contact form, a map, and a closing band. Commons kit; put the site's contact form in the named Form group.",
 "contact, contact us, phone, email, address, map, hours, commons",
 [mpage_hero("Contact us", "Questions about joining, events or the directory? Call, write or drop into the office.", "Contact"),
  BODIES["commons-contact"], BODIES["commons-call"]])

commons_page("commons-page-thanks", "Thank-you page: Commons kit",
 "The page visitors see after sending a form: thanks, what happens next and when, and links to keep reading. Commons kit; send every form here.",
 "thank you, thanks, confirmation, form sent, commons",
 [sec("Thanks", N([meye("Message sent", "main-accent"), h("Thank you. We'll be in touch soon.", 1, "xxx-large"),
    p("Joe or Priya will reply within two working days, Monday to Friday. Check your email for a copy of what you sent.", "large"),
    btns([("Back to the home page", None, "/"), ("See upcoming events", "outline", "/events/")])]), "section-brand", ("xxx-large", "xxx-large", None, None), "56rem"),
  BODIES["commons-stories"]])

print("commons ok")
