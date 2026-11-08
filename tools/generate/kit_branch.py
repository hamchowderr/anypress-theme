# Branch (0.20.0): a whole website for a franchise or any business with several locations, written for a swim school
# with six pools that also sells franchises. Run by kits.py after kit_assay.py, so every helper in kits.py,
# kits_more.py, kit_ridge.py and the kits before it is in scope.
#
# A bright, friendly brand: a chunky grotesk for headings, a plain sans for reading, pool blue and sunny orange. Pages
# link to each other by slug: /programs/ and one page per programme under it, /locations/ and one page per location
# under it, /book-a-trial/, /offers/, /own-a-franchise/, /about/, /reviews/, /faq/, /careers/, /news/ (the blog),
# /contact/, /thank-you/. Forms are named groups, as in Ridge: "Form: quote" books a free trial lesson, "Form: apply"
# is the job and franchise application.

FK2 = "anypress/kit-franchise"
FHEAD = "bricolage-grotesque"
FPH = "(512) 555-0174"
FTL = "tel:5125550174"
FTRIAL = "/book-a-trial/"
FADDR = "3400 South Lamar Boulevard, Austin, TX 78704"
FLAT, FLON = 30.2493, -97.7810
FHOURS = "Lessons Monday to Friday 3pm to 8pm, Saturday and Sunday 8am to 2pm"

variation("kit-branch", "Branch (franchise and multi-location)", PALS["branch"], "figtree", FHEAD, "800", "-0.03em", "1",
    button("var:preset|border-radius|full", "figtree", "700"), blocks=site_title(FHEAD, "800", None, "-0.03em"))

def flabel(text, color="primary", size="small"):
    return p(text, size, color, None, None, {"fontWeight": "700", "letterSpacing": "0.04em", "textTransform": "uppercase"})

def fhead(label, title, link=None, size="xx-large"):
    left = stackg([flabel(label), h(title, 2, size)])
    return row([left, btns([(link[0], "outline", link[1])])] if link else [left], valign="bottom")

def f_buttons():
    """The header's button: Free trial, everywhere. Locations are in the menu."""
    go = f'<!-- wp:button -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{FTRIAL}">{T("Free trial")}</a></div>\n<!-- /wp:button -->'
    return '<!-- wp:buttons {"layout":{"type":"flex","flexWrap":"nowrap"}} -->\n<div class="wp-block-buttons">' + go + '</div>\n<!-- /wp:buttons -->'

def fpage_hero(title, text, crumb=None, buttons=None, alt=None):
    words = N(([flabel(crumb)] if crumb else []) + [h(title, 1, "xxx-large", None, None, {"lineHeight": "0.98"}), p(text, "large")] + ([btns(buttons)] if buttons else []))
    if not alt:
        return sec("Page hero", grp(words, gap="medium", layout={"type": "constrained", "contentSize": "50rem", "justifyContent": "left"}), "section-brand-soft", ("xx-large", "xx-large", None, None), "80rem")
    return sec("Page hero", cols([col(words, "52%", valign="center"), col(img("placeholder-wide.svg", alt, "4/3", "lg"))], "xx-large", "wide", "center"), "section-brand-soft", ("xx-large", "xx-large", None, None), "80rem")

def ffact(label, value):
    return grp(N([p(label, None, "secondary"), p(value, None, None, "right", None, {"fontWeight": "700"})]), layout={"type": "flex", "flexWrap": "nowrap", "justifyContent": "space-between", "verticalAlignment": "top"}, gap="small")

def fcard(inner, style="section-card", gap="small"):
    return grp(N(inner), style, PAD_CARD, gap, {"type": "default"})

def fspacer():
    return '<!-- wp:spacer {"height":"var:preset|spacing|large"} -->\n<div style="height:var(--wp--preset--spacing--large)" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->'

# ---------------------------------------------------------------- content
FPROG = [  # name, slug, ages, price, line
    ("Little splashers", "little-splashers", "6 months to 3 years", "$98 a month", "Parent and baby in the water together: songs, floating and getting happy with a splash."),
    ("Preschool", "preschool", "3 to 5 years", "$124 a month", "Four children, one instructor, and the first big steps: kicking, floating and blowing bubbles."),
    ("Learn to swim", "learn-to-swim", "5 to 12 years", "$124 a month", "From the first width to four strokes and safe treading water, at your child's own pace."),
    ("Swim team prep", "swim-team-prep", "7 to 14 years", "$148 a month", "Turns, starts and stamina for swimmers getting ready to join a team."),
]
FLOC = [  # name, slug, address, line
    ("Austin, South Lamar", "austin", "3400 South Lamar Boulevard", "Our first pool, and where every instructor trains."),
    ("Round Rock", "round-rock", "2701 Parker Drive", "Six lanes and a warm teaching pool by the Dell Diamond."),
    ("San Antonio, Stone Oak", "san-antonio", "20079 Stone Oak Parkway", "Our biggest pool, with Saturday family swims."),
    ("Houston, the Heights", "houston", "1201 Yale Street", "A glass-roofed pool, a short walk from Heights Boulevard."),
    ("Frisco", "frisco", "6800 Warren Parkway", "Our newest pool, opened this spring."),
    ("Fort Worth", "fort-worth", "2900 West 7th Street", "A family-owned franchise near the Cultural District."),
]
FREVIEWS = [
    ("Our son was scared of the bath. Twelve weeks later he jumped in to his instructor. I cried.", "Melissa R.", "Preschool, Round Rock"),
    ("The water is warm, the classes are tiny and the make-up lessons are easy to book. That's all we wanted.", "Andre and Kim", "Learn to swim, Austin"),
    ("We moved from Austin to Frisco and just carried on at the new pool. Same levels, same app, same everything.", "The Patel family", "Learn to swim, Frisco"),
    ("Coach Dani got my daughter ready for her first team tryout in one term.", "Grace O.", "Swim team prep, San Antonio"),
    ("Baby classes on Saturday mornings are the best hour of our week.", "Jordan T.", "Little splashers, Houston"),
    ("Every instructor knows my kids' names, and every pool feels the same. That's rare.", "Lisa M.", "Two children, Fort Worth"),
]
FTEAM = [("Rosa and Mark Delgado", "Founders", "Former college swimmers who opened the first Bluegill pool in Austin in 2012."),
         ("Dani Okafor", "Head of teaching", "Writes every lesson plan and trains every new instructor, at every pool."),
         ("Luis Herrera", "Franchise partner, Fort Worth", "Ran a pool for ten years before opening his own Bluegill in 2023.")]

def freview(text, name, what, size="medium"):
    return grp(N([p("★★★★★", None, "primary"), p("“" + text + "”", size, None, None, None, {"lineHeight": "1.45"}), p(f"{name} · {what}", "small", "secondary", None, None, {"fontWeight": "700"})]),
               "section-card", PAD_CARD, "small", {"type": "default"})

def fprog_card(name, slug, ages, price, line):
    return grp(N([zoom(img("placeholder-wide.svg", f"Programme: {name}", "4/3", "lg")), flabel(ages), hlink(name, f"/programs/{slug}/", 3, "x-large"), p(line, None, "secondary"),
                  p(price, None, None, None, None, {"fontWeight": "700"})]), gap="small", layout={"type": "default"})

def floc_card(name, slug, addr, line):
    return fcard([h(name, 3, "large"), p(addr, None, "secondary"), p(line, "small", "secondary"), link_p("See this pool →", f"/locations/{slug}/", None, {"fontWeight": "700"})])

# ---------------------------------------------------------------- sections
kit("branch-topbar", FK2, "Branch top bar: the newest location and the franchise link",
 "A thin bar above the header announcing the newest location and linking to the franchise page, with the main phone number. Part of the Branch kit (franchise and multi-location); keep it current.",
 "top bar, announcement, new location, franchise, phone, header, branch",
 grp(row([p(T("Now open in Frisco") + ' · <a href="/own-a-franchise/">' + T("Own a Bluegill franchise") + '</a>', "small", None, None, None, None, raw=True),
          p(T("Call any pool") + f' <a href="{FTL}">' + T(FPH) + '</a>', "small", None, None, None, None, raw=True)], gap="small"),
     "section-dark", ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Top bar"))

FHEADER = grp(N([
    BODIES["branch-topbar"],
    grp(row([
        row([dyn("site-logo", {"width": 36, "shouldSyncIcon": True}), dyn("site-title", {"level": 0, "fontSize": "x-large", "fontFamily": FHEAD, "style": {"typography": {"lineHeight": "1"}}})], "left", "small", False, "center"),
        row([dyn("navigation", {"overlayMenu": "mobile", "layout": {"type": "flex", "justifyContent": "right"}}), f_buttons()], "right", "medium", False, "center")], "space-between", "medium", False, "center"),
        None, ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Main bar").replace(
        '<!-- wp:group {', '<!-- wp:group {"backgroundColor":"base",', 1).replace('class="wp-block-group alignfull', 'class="wp-block-group alignfull has-base-background-color has-background', 1),
]), "sticky", None, "0", {"type": "default"}, align="full", name="Header")
write("branch-header", "Branch header: newest location, menu and a Free trial button",
 "A site header for a franchise or a business with several locations that stays at the top while visitors scroll: a bar with the newest location and the franchise link, then the logo, the menu (with dropdowns for programmes and locations), and a Free trial button. Part of the Branch kit; choose it for the header in the Site Editor.",
 "header", "header, menu, navigation, sticky, locations, franchise, booking, branch", FHEADER, "core/template-part/header")

kit("branch-hero", FK2, "Branch hero: one promise, six locations",
 "Opening section for a franchise: a big friendly headline, one sentence, a trial button and a find-a-location button, the number of locations, and a large photo. Part of the Branch kit; use the owner's own photo.",
 "hero, franchise, locations, swim school, kids, booking, branch",
 sec("Hero", cols([
   col(N([flabel("Swim lessons for every age"), h("Happy, safe swimmers at six warm pools across Texas", 1, "xxx-large", None, None, {"lineHeight": "0.98"}),
          p("Small classes of four, water at 90°F and instructors trained the same way at every pool. Your first lesson is free.", "large"),
          btns([("Book a free trial", None, FTRIAL), ("Find a pool near you", "outline", "/locations/")]),
          row([p(t, "small", None, None, None, {"fontWeight": "700"}) for t in ["★ 4.9 from 2,300 families", "6 pools", "Since 2012"]], "left", "medium")]), "50%", valign="center"),
   col(img("placeholder-tall.svg", "Two girls in goggles smiling at the side of the pool", "4/5", "lg"))], "xx-large", "wide", "center"),
   "section-brand-soft", ("x-large", "xx-large", None, None)))

kit("branch-promise", FK2, "Branch promises: what's the same at every location",
 "Four promises that hold at every location, each with a big number or word and a line: class size, water temperature, trained staff and make-up lessons. Part of the Branch kit; only promise what every location does.",
 "promises, standards, every location, quality, franchise, branch",
 sec("Promises", N([fhead("At every pool", "The same lessons, wherever you go"), grid([fcard([p(big, "xx-large", "primary", None, FHEAD, {"lineHeight": "1", "fontWeight": "800"}), h(t, 3, "large"), p(d, None, "secondary")], "section-card") for big, t, d in [
    ("4", "Children per class", "Never more than four, so every child gets time with the instructor."),
    ("90°F", "Warm water", "Our teaching pools are kept at 90°F, so little ones stay happy."),
    ("40 hrs", "Instructor training", "Every instructor trains for forty hours in Austin before they teach."),
    ("Free", "Make-up lessons", "Missed one? Book a make-up at any of our pools, in the app.")]], 4, "13rem", "medium")]), "section-tint"))

kit("branch-programs", FK2, "Branch programmes: every class with ages and price",
 "Every programme as a card with a photo that opens full screen, the ages, its name (linking to its own page), a line about it and the monthly price. Part of the Branch kit; keep prices the same as at the locations.",
 "programmes, classes, services, ages, prices, lessons, branch",
 sec("Programmes", N([fhead("Programmes", "A class for every age", ("All programmes", "/programs/")), grid([fprog_card(*x) for x in FPROG], 4, "14rem", "large")])))

kit("branch-locations", FK2, "Branch locations: every location as a card",
 "Every location as a card with its name, address, a line about it and a link to its page. Part of the Branch kit; add a card for each new location.",
 "locations, find a location, branches, stores, addresses, franchise, branch",
 sec("Locations", N([fhead("Find a pool", "Six pools across Texas", ("All locations", "/locations/")), grid([floc_card(*x) for x in FLOC], 3, "16rem", "medium")]), "section-tint"))

kit("branch-map", FK2, "Branch map: where the locations are",
 "The locations as a list of links beside a map of the area they cover, with a line on what's the same at every one. Needs the AnyPress Blocks plugin for the map. Part of the Branch kit.",
 "locations, map, find a location, branches, franchise, branch",
 sec("Map", cols([
   col(N([flabel("Locations"), h("A pool near you", 2, "xx-large"), p("Book at any pool and swim at all of them: your level, your lessons and your make-ups go with you.", "medium"),
          stackg([link_p(f"{n} →", f"/locations/{s}/", "large", {"fontWeight": "700"}) for n, s, _, _ in FLOC], "x-small")]), "40%"),
   col(mapb("Austin, TX", 30.9, -97.3, 6, "4/3"))], "xx-large", "wide", "center")))

kit("branch-first-lesson", FK2, "Branch first lesson: four steps to the water",
 "How the first visit works, in four numbered steps from booking a free trial to the first term. Part of the Branch kit; one sentence each.",
 "how it works, first lesson, trial, steps, booking, branch",
 sec("First lesson", N([fhead("Your first lesson", "Four steps to the water"), grid([stackg([p(n, "xxx-large", "primary", None, FHEAD, {"lineHeight": "1", "fontWeight": "800"}), h(t, 3, "large"), p(d, None, "secondary")]) for n, t, d in [
    ("1", "Book a free trial", "Choose a pool and a time online. It takes two minutes."),
    ("2", "Meet your instructor", "Arrive ten minutes early. We'll show you the changing rooms and the pool."),
    ("3", "Find the right level", "The instructor watches, plays and suggests the right class."),
    ("4", "Start your term", "Join a weekly class at the same time, with the same instructor.")]], 4, "12rem", "x-large")])))

kit("branch-numbers", FK2, "Branch numbers: four figures that count up",
 "Four numbers that count up as they scroll into view (swimmers, locations, instructors, years), on the brand colour. Needs the AnyPress Blocks plugin. Part of the Branch kit; use real figures only.",
 "numbers, statistics, counter, proof, franchise, branch",
 sec("Numbers", grid([stackg([counter(n, sfx, "", "xxx-large", FHEAD, 0).replace('"fontWeight":"900"', '"fontWeight":"800"'), p(lbl, None, None, None, None, {"fontWeight": "700"})]) for n, sfx, lbl in
     [(5200, "", "swimmers every week"), (6, "", "pools across Texas"), (140, "", "trained instructors"), (14, "", "years of lessons")]], 4, "12rem", "x-large"),
   "section-brand", ("x-large", "x-large", None, None)))

kit("branch-reviews", FK2, "Branch reviews: families from every location",
 "Reviews in a carousel, three at a time on a computer and one on a phone, each with stars, the family's name, the class and the location. Needs the AnyPress Blocks plugin. Part of the Branch kit; use real reviews from several locations.",
 "reviews, testimonials, families, stars, carousel, locations, branch",
 sec("Reviews", N([fhead("Reviews", "Loved by families at every pool", ("All reviews", "/reviews/")),
                   carousel([freview(*r) for r in FREVIEWS], 3, "Family reviews")]), "section-tint"))

kit("branch-faq-open", FK2, "Branch questions: lessons, locations and money",
 "The questions families ask first, about classes, switching locations, missed lessons and fees, as answers that open and close beside a heading and a link to all questions. Part of the Branch kit; answer the real questions.",
 "faq, questions, lessons, locations, fees, accordion, branch",
 sec("Questions", cols([
   col(N([flabel("Good to know"), h("Questions families ask", 2, "xx-large"), p("Something else? Call any pool, or send us a message.", None, "secondary"), btns([("All questions", "outline", "/faq/")])]), "36%"),
   col(accordion([
     ("Can we switch pools?", "Yes. Your level and lessons go with you, so you can move pools or book a make-up anywhere."),
     ("What if we miss a lesson?", "Book a free make-up at any pool in the app, up to 60 days later."),
     ("Is there a joining fee?", "A $35 joining fee covers your swimmer's cap and level card. It's free this month."),
     ("Do parents get in the water?", "Only in Little splashers. Everyone else watches from the viewing area."),
     ("How do I cancel?", "Give 30 days' notice in the app or at the front desk. No questions asked.")]))], "xx-large", "wide", "top")))

kit("branch-franchise-teaser", FK2, "Branch own a franchise: the opportunity in short",
 "A dark band inviting people to open their own location: a headline, a sentence on the support, three key figures and a button to the franchise page. Part of the Branch kit; state real figures from the franchise disclosure document.",
 "franchise, opportunity, own a location, investment, business, branch",
 sec("Franchise", cols([
   col(img("placeholder-wide.svg", "Franchise: a new pool, ready for opening day", "4/3", "lg"), "45%"),
   col(N([flabel("Own a franchise", "primary-alt"), h("Bring Bluegill to your town", 2, "xx-large"),
          p("We help you find the site, build the pool, hire and train your team and fill your classes. You run a business families love.", "medium"),
          grid([stackg([p(big, "x-large", None, None, FHEAD, {"fontWeight": "800", "lineHeight": "1"}), p(small, "small", "main-accent")]) for big, small in [("$780k", "typical total investment"), ("1 year", "from signing to opening"), ("6%", "royalty on sales")]], 3, "8rem", "medium"),
          btns([("Learn about franchising", None, "/own-a-franchise/")])]), valign="center")], "xx-large", "wide", "center"), "section-dark"))

kit("branch-program", FK2, "Branch programme: what happens in class and the price",
 "The body of a page for one programme: what happens in a class, what swimmers learn, a card with ages, class size, length and the monthly price, and four photos that open full screen. Part of the Branch kit; make one per programme.",
 "programme, class, details, price, lessons, branch",
 sec("Programme", N([cols([
   col(N([h("What happens in class", 2, "xx-large"),
          p("Each thirty-minute class is a parent and baby in the water with one instructor and up to five other families. We sing, float, splash and practise safe entries, and babies learn to love the water before they learn to swim.", "medium"),
          h("What they'll learn", 3, "large"),
          lst(["Happy in the water, face wet and all", "Floating on their back with help", "Kicking and reaching for a toy", "Holding on to the wall on their own", "Safe ways to get in and out"])]), "58%"),
   col(fcard([flabel("At a glance"), p("$98 a month", "xx-large", None, None, FHEAD, {"lineHeight": "1", "fontWeight": "800"}), ffact("Ages", "6 months to 3 years"), ffact("Class size", "Up to 6 families"), ffact("Lesson", "30 minutes, weekly"), ffact("Where", "All six pools"),
              btns([("Book a free trial", None, FTRIAL), ("Find a pool", "outline", "/locations/")])], "section-tint"))], "xx-large", "wide", "top"),
   grid([zoom(img("placeholder-wide.svg", a, "4/3", "lg")) for a in ["This class: in the water together", "This class: first splashes", "This class: floating and kicking", "This class: big smiles after"]], 2, "18rem", "medium")]), content="80rem"))

kit("branch-location", FK2, "Branch location: address, hours, the team and a map",
 "The body of a page for one location: what's special about it, its address, opening hours, pool details and manager, a booking button and a map. Needs the AnyPress Blocks plugin for the map. Part of the Branch kit; make one per location.",
 "location, branch, store, address, hours, map, manager, branch",
 sec("Location", cols([
   col(N([flabel("Austin, South Lamar"), h("Our first pool", 2, "xx-large"),
          p("Where Bluegill started in 2012, and where every instructor still trains. A warm teaching pool, a six-lane pool for older swimmers and a big viewing area with free coffee.", "medium"),
          ffact("Address", "3400 South Lamar Boulevard"), ffact("Lessons", "Weekdays 3 to 8pm, weekends 8am to 2pm"), ffact("Pools", "Teaching pool and 6 lanes"), ffact("Manager", "Priya Shah"),
          btns([("Book a free trial here", None, FTRIAL), ("Call this pool", "outline", FTL)])]), "42%"),
   col(mapb(FADDR, FLAT, FLON, 14, "4/3"))], "xx-large", "wide", "top")))

kit("branch-offers", FK2, "Branch offers: ways to start and save",
 "Three offers as cards with the saving in large type, who it's for and a button: a free trial, a sibling discount and no joining fee. Part of the Branch kit; keep the offers current and the same at every location.",
 "offers, discount, free trial, siblings, deals, branch",
 sec("Offers", N([fhead("Offers", "Ways to start and save"), grid([fcard([p(s, "xxx-large", "primary", None, FHEAD, {"lineHeight": "1", "fontWeight": "800"}), h(t, 3, "large"), p(d, None, "secondary"), btns([(b, "outline", l)])], st) for s, t, d, b, l, st in [
    ("Free", "Your first lesson", "Try a class at any pool before you sign up. No card needed.", "Book a free trial", FTRIAL, "section-card"),
    ("10% off", "For brothers and sisters", "Every extra child in the family gets 10% off, for as long as they swim.", "See programmes", "/programs/", "section-brand-soft"),
    ("$0", "Joining fee this month", "Sign up before the end of the month and we'll skip the $35 joining fee.", "Find a pool", "/locations/", "section-card")]], 3, "16rem", "medium")])))

kit("branch-team", FK2, "Branch team: the founders and the people behind every location",
 "The founders, the head of teaching and a franchise partner, each with a photo, their role and a line about them. Part of the Branch kit; use real people with permission.",
 "team, founders, franchise partners, people, about, branch",
 sec("Team", N([fhead("The people", "Founders, teachers and partners"), grid([stackg([img("placeholder-tall.svg", f"Team: {n}", "4/5", "lg"), h(n, 3, "x-large"), flabel(r), p(d, None, "secondary")]) for n, r, d in FTEAM], 3, "14rem", "x-large")])))

kit("branch-jobs", FK2, "Branch careers: why work here and the open roles",
 "Why people work at the business, each open role with its location, hours and pay, and the application. Part of the Branch kit; keep the roles current and put the site's application form in the named Form group.",
 "careers, jobs, hiring, instructor, apply, locations, branch",
 sec("Careers", N([
   fhead("Why work here", "Teach kids to swim, and get paid to train"),
   grid([stackg([h(t, 3, "large"), p(d, None, "secondary")]) for t, d in [
     ("Paid training", "Forty hours in Austin, paid, before your first class."),
     ("Steady shifts", "Afternoons and weekends, the same every week, at the pool you choose."),
     ("Grow with us", "Instructors become lead teachers, managers and, some day, franchise owners."),
     ("Free lessons", "Your own children swim with us for free.")]], 4, "13rem"),
   fspacer(),
   h("Open roles", 2, "xx-large"),
   N([grp(N([row([h(t, 3, "large"), flabel(when)], valign="center"), p(d, None, "secondary"), btns([("Apply for this", None, "#apply")])]), "section-tint", PAD_CARD, "small", {"type": "default"}) for t, when, d in [
     ("Swim instructor", "All pools, $18 to $22 an hour", "Teach small classes in the water. We train you; you need to be a strong swimmer and love kids."),
     ("Front desk", "All pools, $16 an hour", "Welcome families, book trials and keep the viewing area running."),
     ("Pool manager", "Frisco, $58,000 a year", "Run our newest pool: the team, the schedule and the families.")]]),
   grp(N([h("Apply", 2, "xx-large"), p("Tell us a little about you, the role and the pool you'd like. We reply to everyone within a week."),
          form("apply", "Email the team", "mailto:jobs@example.com")]), "section-card", PAD_CARD, "small", {"type": "default"}, anchor="apply")])))

kit("branch-trial-form", FK2, "Branch free trial: the form and what to bring",
 "A form to book a free trial lesson at any location, beside what happens next and what to bring. Part of the Branch kit; put the site's form in the named Form group.",
 "free trial, booking, book, class, form, locations, branch",
 sec("Trial", cols([
   col(fcard([h("Book a free trial", 2, "xx-large"), p("Choose a class and a pool. We'll call or text within a day with a time that suits you."),
              form("quote", "Call " + FPH, FTL, "Rather talk to someone? Call any pool.")], "section-card", "medium"), "58%"),
   col(N([h("What happens next", 3, "large"),
          lst(["We confirm a time within a day", "You meet the instructor at the pool", "They suggest the right class and level"]),
          h("What to bring", 3, "large"), lst(["A swimsuit (swim diapers for little ones)", "A towel and goggles if they have them", "Ten minutes to settle in before the lesson"])]))],
   "xx-large", "wide", "top"), "section-tint"))

kit("branch-contact-full", FK2, "Branch contact: head office, phone and form",
 "A contact section for a business with several locations: the main phone number, email, head office address and hours beside the contact form, then a map. Needs the AnyPress Blocks plugin for the map. Part of the Branch kit.",
 "contact, phone, email, head office, map, form, branch",
 sec("Contact us", N([cols([
   col(N([h("Talk to us", 2, "xx-large"), p(f'<a href="{FTL}">' + T(FPH) + '</a>', "xx-large", None, None, FHEAD, {"fontWeight": "800"}, raw=True, bind="phone_linked"),
          p('<a href="mailto:hello@example.com">hello@example.com</a>', None, None, None, None, None, raw=True, bind="email_linked"),
          p(FADDR, None, bind="address"), p(FHOURS, None, "secondary", bind="hours"),
          p("Each pool has its own number on its page. This one reaches whichever pool is nearest.", "small", "secondary")]), "40%"),
   col(fcard([h("Send a message", 3, "large"), form("contact", "Call " + FPH, FTL, "We reply the same day, seven days a week.")], "section-tint", "medium"))], "xx-large", "wide", "top"),
   mapb(FADDR, FLAT, FLON, 13, "21/9")])))

kit("branch-franchise-full", FK2, "Branch franchise: investment, support, steps and enquiry",
 "The body of a franchise page: what the investment is, what support comes with it, the steps from first call to opening, open territories and the enquiry form. Part of the Branch kit; take every figure from the franchise disclosure document and put the site's form in the named Form group.",
 "franchise, opportunity, investment, support, territories, enquiry, branch",
 sec("Franchise", N([
   cols([col(N([h("The investment", 2, "xx-large"), p("Figures from our latest franchise disclosure document. Ask us for the full document before you decide.", None, "secondary"),
                table(["", "Typical range"], [("Franchise fee", "$55,000"), ("Building and pool", "$520,000 to $760,000"), ("Equipment and fit-out", "$90,000 to $140,000"), ("Opening costs and cash", "$60,000 to $90,000"), ("Royalty", "6% of sales"), ("Marketing fund", "2% of sales")], "stripes")]), "50%"),
         col(N([h("What you get", 2, "xx-large"), lst(["Help finding and fitting out the site", "Our pool design and supplier prices", "Instructor training in Austin", "The booking app, website and phone line", "Marketing before you open, and after", "A partner coach who visits every month"])]))], "xx-large", "wide", "top"),
   fspacer(),
   fhead("From first call to opening day", "Five steps, about twelve months"),
   grid([stackg([p(n, "xx-large", "primary", None, FHEAD, {"fontWeight": "800", "lineHeight": "1"}), h(t, 3, "large"), p(d, None, "secondary")]) for n, t, d in [
     ("1", "A first call", "Tell us about you and your town."), ("2", "Discovery day", "Spend a day at our Austin pool and meet the team."),
     ("3", "Sign and find a site", "We help you choose and lease the right building."), ("4", "Build and hire", "Six to nine months to build the pool and train your team."),
     ("5", "Open the doors", "We're there on opening week, and every month after.")]], 5, "10rem", "large"),
   fspacer(),
   grp(N([h("Open territories", 2, "xx-large"), p("Dallas, Plano, Katy, The Woodlands, New Braunfels, Waco, and towns in Oklahoma and Louisiana. Ask about yours.", "medium")]), "section-tint", PAD_CARD, "small", {"type": "default"}),
   grp(N([h("Ask about a franchise", 2, "xx-large"), p("Choose \"Owning a franchise\" and tell us your town. A member of our franchise team calls within two working days."),
          form("apply", "Email the franchise team", "mailto:jobs@example.com")]), "section-card", PAD_CARD, "small", {"type": "default"}, anchor="apply")]), content="80rem"))

kit("branch-signup", FK2, "Branch signup: news and offers by email",
 "A band asking visitors to join the email list for new locations, holiday camps and offers, with the signup form beside it. Part of the Branch kit; sits above the footer on every page.",
 "newsletter, signup, email, offers, branch",
 sec("Signup", cols([
   col(N([h("Splash news, once a month", 2, "xx-large"), p("New pools, holiday swim camps and offers, in one short email a month.", None, "secondary")]), "55%", valign="center"),
   col(form("newsletter", "See offers", "/offers/"), valign="center")], "x-large", "wide", "center"), "section-brand-soft", ("x-large", "x-large", None, None)))

FPOP = popup("offer", N([
    img("placeholder-wide.svg", "A child floating on a ring in a blue pool", "16/9"),
    grp(N([flabel("New families"), h("Your first lesson is free", 2, "xx-large"),
           p("Leave your email and we'll send a free trial code for any of our six pools, plus a guide to choosing the right class."),
           form("offer", "See offers", "/offers/")]), None, (None, None, "large", "large"), "small", {"type": "default"})]),
    label="Your first lesson is free")
kit("branch-popup", FK2, "Branch popup: a free first lesson",
 "A popup that opens five seconds into a first visit with a photo, a free trial offer and one field for an email address; it closes with its button, Escape or a click outside and stays closed for two weeks. Needs the AnyPress Blocks plugin. Part of the Branch kit; put it in the footer to show it on every page.",
 "popup, offer, free trial, newsletter, email, modal, branch", FPOP)

FFOOT = grp(N([
    BODIES["branch-signup"],
    grp(N([cols([
        col(N([dyn("site-title", {"level": 0, "fontSize": "x-large", "fontFamily": FHEAD, "style": {"typography": {"lineHeight": "1"}}}),
               p("Swim lessons for every age at six warm pools across Texas. Your first lesson is free.", None, "main-accent"),
               p(f'<a href="{FTL}">' + T(FPH) + '</a>', "x-large", None, None, FHEAD, {"fontWeight": "800"}, raw=True, bind="phone_linked"),
               social(["instagram", "facebook", "youtube"])]), "30%"),
        col(flinks("Locations", [(n, f"/locations/{s}/") for n, s, _, _ in FLOC])),
        col(flinks("Programmes", [(n, f"/programs/{s}/") for n, s, _, _, _ in FPROG] + [("Offers", "/offers/"), ("Book a free trial", FTRIAL)])),
        col(flinks("Bluegill", [("About us", "/about/"), ("Reviews", "/reviews/"), ("Own a franchise", "/own-a-franchise/"), ("Careers", "/careers/"), ("Questions", "/faq/"), ("News", "/news/"), ("Contact", "/contact/")]))], "large", "wide", "top"),
        sep(),
        row([p("© Bluegill Swim School. Each location is independently owned and operated under licence.", "small", "main-accent"),
             p('<a href="/privacy-policy/">' + T("Privacy") + '</a> · <a href="/own-a-franchise/">' + T("Franchising") + '</a>', "small", "main-accent", None, None, None, raw=True)], gap="small")]),
        "section-dark", ("x-large", "large", None, None), "large", {"type": "constrained", "contentSize": "80rem"}, align="full", name="Footer columns"),
    FPOP,
]), None, None, "0", {"type": "default"}, align="full", name="Footer")
write("branch-footer", "Branch footer: news by email, every location and the free-trial popup",
 "A site footer for a franchise or a business with several locations: a band for the email list, then the main phone number, every location, the programmes and company links on dark, the franchise notice and the free-trial popup (needs the AnyPress Blocks plugin). Part of the Branch kit; choose it for the footer in the Site Editor.",
 "footer", "footer, links, locations, franchise, newsletter, popup, branch", FFOOT, "core/template-part/footer")

# The home page.
kit_page("kit-franchise", "Home page: Branch kit, franchise and multi-location",
 "A complete home page for a franchise or a business with several locations in the Branch kit: a hero with a free trial, what's the same at every location, programmes with prices, every location and a map, the first visit in four steps, numbers that count up, reviews from every location, questions and an invitation to own a franchise. Apply the Branch style for the look it was designed with.",
 "home, franchise, multi-location, locations, branches, swim school, kids, classes, kit, branch",
 ["branch-hero", "branch-promise", "branch-programs", "branch-map", "branch-first-lesson", "branch-numbers", "branch-reviews", "branch-faq-open", "branch-franchise-teaser"])

# ---------------------------------------------------------------- pages
def branch_page(slug, title, desc, kw, parts):
    write(slug, title, desc, "anypress/pages", kw, N(parts), "core/post-content", " * Post Types: page\n")

branch_page("branch-page-services", "Programmes page: Branch kit",
 "A Programmes page for a franchise: a heading, every programme with ages, price and a link to its own page, the promises every location keeps, offers and reviews. Branch kit.",
 "programmes, classes, services, prices, branch",
 [fpage_hero("Programmes", "From babies to swim team, every class is four children or fewer, in warm water, at all six pools.", "Programmes", [("Book a free trial", None, FTRIAL)]),
  BODIES["branch-programs"], BODIES["branch-promise"], BODIES["branch-offers"], BODIES["branch-reviews"]])

branch_page("branch-page-service", "Programme page: Branch kit (one programme)",
 "A page for one programme, such as the baby class: a heading with a photo, what happens in class and the price, the first lesson, reviews and questions. Branch kit; make one per programme.",
 "programme, class, details, price, branch",
 [fpage_hero("Little splashers", "Parent and baby in the water together: songs, floating and getting happy with a splash.", "Programmes / Little splashers", [("Book a free trial", None, FTRIAL)], "Programme page: Little splashers"),
  BODIES["branch-program"], BODIES["branch-first-lesson"], BODIES["branch-reviews"], BODIES["branch-faq-open"]])

branch_page("branch-page-about", "About page: Branch kit",
 "An About page for a franchise: a heading, the founders' story beside a photo, numbers that count up, the team, the promises every location keeps and an invitation to own a franchise. Branch kit.",
 "about, our story, founders, team, franchise, branch",
 [fpage_hero("About Bluegill", "Two college swimmers, one rented pool in Austin, and fourteen years later six pools and 5,200 swimmers a week.", "About"),
  sec("Story", cols([
    col(N([h("It started with one pool and twelve kids", 2, "xx-large"),
           p("Rosa and Mark Delgado swam in college and coached on weekends. In 2012 they rented a small pool on South Lamar and taught twelve children on the first Saturday.", "large"),
           p("Families kept coming, so they wrote down exactly how they teach and trained others to do it the same way. That's what every Bluegill pool still does, whether we own it or a franchise partner does.")]), "50%", valign="center"),
    col(img("placeholder-tall.svg", "Our story: children learning in the teaching pool", "4/5", "lg"))], "xx-large", "wide", "center")),
  BODIES["branch-numbers"], BODIES["branch-team"], BODIES["branch-promise"], BODIES["branch-franchise-teaser"]])

branch_page("branch-page-reviews", "Reviews page: Branch kit",
 "A Reviews page for a franchise: a heading, reviews from every location as cards, numbers that count up and the locations. Branch kit; use real reviews with permission.",
 "reviews, testimonials, families, stars, locations, branch",
 [fpage_hero("Reviews", "Rated 4.9 out of 5 by more than 2,300 families, at every one of our pools.", "Reviews", [("Book a free trial", None, FTRIAL)]),
  sec("All reviews", grid([freview(*r) for r in FREVIEWS + [
    ("The viewing area has coffee and Wi-Fi, and I can see every minute of the lesson.", "Hannah W.", "Preschool, Austin"),
    ("We booked a make-up at the Houston pool while visiting grandma. Same lesson plan, same warmth.", "The Ortiz family", "Learn to swim, Round Rock"),
    ("My twins are in different levels but the same time slot. Whoever does the schedule is a genius.", "Sam P.", "Two children, San Antonio")]], 3, "18rem", "medium"), "section-tint"),
  BODIES["branch-numbers"], BODIES["branch-locations"]])

branch_page("branch-page-areas", "Locations page: Branch kit",
 "A Locations page for a franchise or business with several locations: a heading, a map with every location, a card for each linking to its own page, and the promises every location keeps. Branch kit.",
 "locations, find a location, branches, stores, map, branch",
 [fpage_hero("Find a pool", "Six warm pools across Texas. Book at one and swim at all of them.", "Locations", [("Book a free trial", None, FTRIAL)]),
  BODIES["branch-map"], BODIES["branch-locations"], BODIES["branch-promise"]])

branch_page("branch-page-area", "Location page: Branch kit (one location)",
 "A page for one location: a heading with a photo, its address, hours, pools and manager with a map, the programmes it runs and reviews. Branch kit; make one per location.",
 "location, branch, store, address, hours, map, branch",
 [fpage_hero("Bluegill Austin, South Lamar", "Our first pool, open since 2012. Lessons every weekday afternoon and weekend morning.", "Locations / Austin", [("Book a free trial here", None, FTRIAL)], "Location page: Austin"),
  BODIES["branch-location"], BODIES["branch-programs"], BODIES["branch-reviews"]])

branch_page("branch-page-offers", "Offers page: Branch kit",
 "An Offers page for a franchise: a heading, ways to start and save, the programmes and questions. Branch kit; keep the offers current and the same at every location.",
 "offers, deals, discounts, free trial, branch",
 [fpage_hero("Offers", "A free first lesson, 10% off for brothers and sisters, and no joining fee this month. At every pool.", "Offers"),
  BODIES["branch-offers"], BODIES["branch-programs"], BODIES["branch-faq-open"]])

branch_page("branch-page-join", "Free trial page: Branch kit",
 "A Book a free trial page for a franchise: a heading, the booking form beside what happens next, the first lesson in four steps and reviews. Branch kit; put the site's form in the named Form group.",
 "free trial, booking, book, class, branch",
 [fpage_hero("Book a free trial", "Choose a class and a pool, and we'll find a time that suits you. No card needed.", "Free trial"),
  BODIES["branch-trial-form"], BODIES["branch-first-lesson"], BODIES["branch-reviews"]])

branch_page("branch-page-faq", "Questions page: Branch kit",
 "A Questions page for a franchise: answers that open and close, grouped into lessons, locations and money, and the contact details. Branch kit; answer the real questions.",
 "faq, questions, lessons, locations, fees, branch",
 [fpage_hero("Questions", "About classes, switching pools, missed lessons and money.", "Questions"),
  sec("Questions", N([N([h(group_t, 2, "xx-large"), accordion(qs)]) for group_t, qs in [
    ("Lessons", [
      ("How long is a lesson?", "Thirty minutes for Little splashers and Preschool, forty-five for Learn to swim and Swim team prep."),
      ("Do parents get in the water?", "Only in Little splashers. Everyone else watches from the viewing area."),
      ("How do you choose the level?", "The instructor watches the free trial and suggests a level. Swimmers move up when they're ready, not on a schedule.")]),
    ("Locations", [
      ("Can we switch pools?", "Yes. Your level and lessons go with you, so you can move pools or book a make-up anywhere."),
      ("Are franchise pools different?", "No. Every pool uses the same lesson plans, training, prices and app, whoever owns it.")]),
    ("Money", [
      ("Is there a joining fee?", "A $35 joining fee covers your swimmer's cap and level card. It's free this month."),
      ("What if we miss a lesson?", "Book a free make-up at any pool in the app, up to 60 days later."),
      ("How do I cancel?", "Give 30 days' notice in the app or at the front desk. No questions asked.")])]]),
    content="56rem"),
  BODIES["branch-contact-full"]])

branch_page("branch-page-careers", "Careers page: Branch kit",
 "A Careers page for a franchise: a heading, why people work there, the open roles at every location with pay, the application form and an invitation to own a franchise. Branch kit; keep the roles current and put the site's form in the named Form group.",
 "careers, jobs, hiring, instructor, branch",
 [fpage_hero("Careers", "Teach children to swim at any of our six pools. We pay for your training.", "Careers", [("See open roles", None, "#apply")]),
  BODIES["branch-jobs"], BODIES["branch-franchise-teaser"]])

branch_page("branch-page-contact", "Contact page: Branch kit",
 "A Contact page for a franchise: a heading, the main phone number, email and head office beside the contact form, a map, every location and questions. Branch kit; put the site's contact form in the named Form group.",
 "contact, phone, email, locations, branch",
 [fpage_hero("Contact", "Call any pool, send a message or visit the front desk. We reply the same day.", "Contact"),
  BODIES["branch-contact-full"], BODIES["branch-locations"], BODIES["branch-faq-open"]])

branch_page("branch-page-franchise", "Own a franchise page: Branch kit",
 "An Own a franchise page: a heading with a photo, the investment and support, the steps to opening, open territories and the enquiry form, then a franchise partner's story and the numbers. Branch kit; take figures from the franchise disclosure document.",
 "franchise, opportunity, investment, own a location, branch",
 [fpage_hero("Own a Bluegill franchise", "Bring warm water, small classes and happy swimmers to your town, with a team that's done it six times.", "Own a franchise", [("Ask about a franchise", None, "#apply")], "Own a franchise: a finished teaching pool"),
  BODIES["branch-franchise-full"],
  sec("Partner story", cols([col(img("placeholder-tall.svg", "Franchise partner: Luis Herrera", "4/5", "lg"), "36%"),
    col(N([quote("I ran a pool for ten years. With Bluegill I finally run my own, and I've never been short of families or support.", "Luis Herrera, Bluegill Fort Worth", "x-large", FHEAD)]), valign="center")], "xx-large", "wide", "center"), "section-tint"),
  BODIES["branch-numbers"]])

branch_page("branch-page-thanks", "Thank-you page: Branch kit",
 "The page visitors see after sending a form: thanks, what happens next and when, and links to keep exploring. Branch kit; send every form here.",
 "thank you, thanks, confirmation, form sent, branch",
 [sec("Thanks", N([flabel("Message sent"), h("Thank you! We'll be in touch soon.", 1, "xxx-large"),
    p("We'll call or text within a day, seven days a week. Check your email for a copy of what you sent.", "large", "secondary"),
    btns([("Back to the home page", None, "/"), ("Find a pool", "outline", "/locations/")])]), None, ("xxx-large", "xxx-large", None, None), "56rem"),
  BODIES["branch-programs"]])

print("branch ok")
