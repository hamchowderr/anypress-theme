# Rep (0.16.0): a whole website for a gym, boxing club, CrossFit box or fitness studio, written for a small coached gym.
# Run by kits.py after kit_gloss.py, so every helper in kits.py, kits_more.py, kit_ridge.py and the kits before it is
# in scope.
#
# A loud page: heavy condensed capitals, red and lime, bold colour tiles. Pages link to each other by slug: /classes/
# and one page per class under it, /timetable/, /memberships/, /trial/, /coaches/ and one page per coach under it,
# /about/, /reviews/, /careers/, /faq/, /blog/, /contact/, /thank-you/. Forms are named groups, as in Ridge: "Form: quote"
# claims the free trial week, "Form: apply" is the job application.

RK = "anypress/kit-fitness"
RHEAD_F = "archivo"
RPH = "(503) 555-0162"
RTL = "tel:5035550162"
RTRIAL = "/trial/"
RADDR = "740 SE Hawthorne Blvd, Portland, OR 97214"
RLAT, RLON = 45.5121, -122.6580
RHOURS = "Monday to Friday, 6am to 9pm. Saturday, 8am to 1pm."

def rsmall(text, color=None):
    return p(text, "small", color, None, RHEAD_F, {"fontWeight": "800", "letterSpacing": "0.1em", "textTransform": "uppercase"})

def rhead(eb, title, link=None, size="xxx-large"):
    left = stackg([rsmall(eb, "primary"), h(title, 2, size)])
    return row([left, btns([(link[0], "outline", link[1])])] if link else [left], valign="bottom")

def r_buttons():
    """The header's button: the free week, everywhere; short so the name fits beside it on a phone."""
    return '<!-- wp:buttons {"layout":{"type":"flex","flexWrap":"nowrap"}} -->\n<div class="wp-block-buttons"><!-- wp:button -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="' + RTRIAL + '">' + T("Free week") + '</a></div>\n<!-- /wp:button --></div>\n<!-- /wp:buttons -->'

def rpage_hero(title, text, crumb=None, buttons=None, alt=None):
    words = N(([rsmall(crumb)] if crumb else []) + [h(title, 1, "xxx-large", None, None, {"lineHeight": "0.95"}), p(text, "large")] + ([btns(buttons)] if buttons else []))
    if not alt:
        return sec("Page hero", grp(words, gap="medium", layout={"type": "constrained", "contentSize": "56rem", "justifyContent": "left"}), "section-dark", ("xx-large", "xx-large", None, None), "80rem")
    return sec("Page hero", cols([col(words, "55%", valign="center"), col(img("placeholder-wide.svg", alt, "4/3"))], "xx-large", "wide", "center"), "section-dark", ("xx-large", "xx-large", None, None), "80rem")

def rfact(label, value):
    """A label and its value on one line, with a thin rule under it; never wraps in a narrow card."""
    return grp(N([p(label, None, None, None, None, {"fontWeight": "700"}), p(value)]),
               layout={"type": "flex", "flexWrap": "nowrap", "justifyContent": "space-between", "verticalAlignment": "top"}, gap="small")

def rcard(inner, style="section-tint", gap="medium"):
    return grp(N(inner), style, PAD_CARD, gap, {"type": "default"})

# ---------------------------------------------------------------- content
RCLS = [
    ("Strength", "strength", "Squats, deadlifts and presses, coached in small groups so your form is right from the first lift."),
    ("Conditioning", "conditioning", "Short, hard circuits on bikes, rowers and kettlebells, scaled to where you are today."),
    ("Boxing", "boxing", "Pad work, bag rounds and footwork with Priya. No sparring unless you want it."),
    ("Mobility", "mobility", "Thirty easy minutes of stretching and joint work to help you move and recover better."),
    ("Personal training", "personal-training", "One to one with a coach, for a goal, an injury comeback or a first start."),
]
RTEAM = [("Marcus", "marcus", "Head coach", "Strength and beginners. Former rugby player."),
         ("Priya", "priya", "Boxing coach", "Boxing and conditioning. Twelve years in the ring."),
         ("Dee", "dee", "Strength coach", "Strength for women, and lifting through pregnancy."),
         ("Tom", "tom", "Conditioning coach", "Conditioning, gymnastics and pull-ups.")]
RREVIEWS = [
    ("I'd never lifted a barbell. Six months later I deadlifted my body weight, and Marcus was more excited than me.", "Hannah K.", "Strength, since March"),
    ("Priya's boxing class is the best hour of my week. Hard, funny and nobody takes themselves too seriously.", "Leo M.", "Boxing, twice a week"),
    ("Small classes mean the coach actually watches you. My back has never felt better.", "Grace T.", "Strength and mobility"),
    ("I came back after a knee operation and Tom built every session around it. No pain, real progress.", "Sam R.", "Personal training"),
    ("Everyone knows your name by the second week. It's the first gym I haven't quit.", "Ade O.", "Unlimited member"),
    ("Dee coached me through lifting all the way through my pregnancy. I felt strong the whole time.", "Mia L.", "Strength with Dee"),
]

def rreview(text, name, what, size="medium"):
    return grp(N([p("★★★★★", None, "primary"), p("“" + text + "”", size, None, None, None, {"lineHeight": "1.45"}),
                  rsmall(f"{name} · {what}", "secondary")]), "section-card", PAD_CARD, "small", {"type": "default"})

# ---------------------------------------------------------------- sections
kit("rep-topbar", RK, "Rep top bar: the free week and the phone number",
 "A thin bar above the header with the free trial week and a link to it, and the gym's phone number. Part of the Rep kit; keep the offer current.",
 "top bar, announcement, offer, trial, phone, header, rep",
 grp(row([p(T("New here? Your first week is free") + f' · <a href="{RTRIAL}">' + T("Claim it") + '</a>', "small", None, None, None, None, raw=True),
          p(T("Call the front desk") + f' <a href="{RTL}">' + T(RPH) + '</a>', "small", None, None, None, None, raw=True)], gap="small"),
     "section-second-brand", ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Top bar"))

RHEADER = grp(N([
    BODIES["rep-topbar"],
    grp(row([
        row([dyn("site-logo", {"width": 36, "shouldSyncIcon": True}), dyn("site-title", {"level": 0, "fontSize": "medium", "fontFamily": RHEAD_F, "style": {"typography": {"lineHeight": "1", "fontWeight": "900", "textTransform": "uppercase"}}})], "left", "small", False, "center"),
        row([dyn("navigation", {"overlayMenu": "mobile", "layout": {"type": "flex", "justifyContent": "right"}}), r_buttons()], "right", "medium", False, "center")], "space-between", "medium", False, "center"),
        None, ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Main bar").replace(
        '<!-- wp:group {', '<!-- wp:group {"backgroundColor":"base",', 1).replace('class="wp-block-group alignfull', 'class="wp-block-group alignfull has-base-background-color has-background', 1),
]), "sticky", None, "0", {"type": "default"}, align="full", name="Header")
write("rep-header", "Rep header: free week, menu and a Free week button",
 "A site header for a gym, boxing club or fitness studio that stays at the top while visitors scroll: a bar with the free trial week and the phone number, then the logo, the menu (with dropdowns for classes and coaches) and a Free week button. Part of the Rep kit; choose it for the header in the Site Editor.",
 "header", "header, menu, navigation, sticky, trial, phone, gym, rep", RHEADER, "core/template-part/header")

kit("rep-numbers", RK, "Rep numbers: four figures that count up",
 "Four numbers that count up as they scroll into view (years open, members, star rating, classes a week), each with a short line. Needs the AnyPress Blocks plugin. Part of the Rep kit; use real figures only.",
 "numbers, statistics, counter, members, gym, rep",
 sec("Numbers", grid([stackg([counter(n, sfx, "", "xxx-large", RHEAD_F, d), p(lbl, "medium")]) for n, sfx, d, lbl in
     [(9, "", 0, "years on Hawthorne"), (420, "", 0, "members, every one coached"), (4.9, "", 1, "stars from 310 reviews"), (38, "", 0, "classes every week")]], 4, "13rem", "x-large"), "section-dark"))

kit("rep-gallery", RK, "Rep gallery: inside the gym, four photos that open full screen",
 "Four photos of the gym and its classes in a row, each opening full screen when clicked. Part of the Rep kit; use real photos of the members and the space.",
 "gallery, photos, gym, classes, lightbox, rep",
 sec("Gallery", N([rhead("Inside the gym", "Come and see it", ("Book a free week", RTRIAL)),
   grid([zoom(img("placeholder-wide.svg", a, "1")) for a in [
     "Inside the gym: barbells and plates on the floor", "Inside the gym: a kettlebell class", "Inside the gym: boxing on the heavy bag", "Inside the gym: stretching on mats by the window"]], 4, "13rem", "small")])))

kit("rep-reviews", RK, "Rep reviews: a carousel of what members say",
 "Members in their own words, in a carousel, three at a time on a computer and one on a phone, with five stars, each member's name and what they train. Needs the AnyPress Blocks plugin. Part of the Rep kit; use real reviews, with permission.",
 "reviews, testimonials, members, stars, carousel, rep",
 sec("Reviews", N([rhead("Reviews", "4.9 stars from 310 members", ("All reviews", "/reviews/")),
                   carousel([rreview(*r) for r in RREVIEWS], 3, "Member reviews")]), "section-tint"))

kit("rep-faq-open", RK, "Rep questions: answers that open and close",
 "The questions people ask before joining a gym, as answers that open and close, beside a heading and a link to all questions. Part of the Rep kit; answer the real questions.",
 "faq, questions, joining, beginners, trial, accordion, rep",
 sec("Questions", cols([
   col(N([rsmall("Before you start", "primary"), h("Good to know", 2, "xxx-large"), p("Something else? Call the front desk and ask for Marcus."), btns([("All questions", "outline", "/faq/")])]), "36%"),
   col(accordion([
     ("I've never been to a gym. Is this for me?", "Yes. Most of our members started as beginners. Every class is coached and every exercise has an easier version."),
     ("How does the free week work?", "Come to as many classes as you like for seven days. No card needed, and no pressure at the end."),
     ("How big are the classes?", "Twelve people at most, with one coach. Strength classes are eight."),
     ("Can I freeze my membership?", "Yes, for up to two months a year, for travel, injury or anything else."),
     ("What should I bring?", "Trainers, water and something comfortable. We have towels, chalk and lockers.")]))], "xx-large", "wide", "top")))

kit("rep-visit", RK, "Rep visit: the gym's address and hours, with a map",
 "Where the gym is, with the address, opening hours and parking beside a map. Needs the AnyPress Blocks plugin for the map. Part of the Rep kit.",
 "visit, location, address, hours, map, gym, rep",
 sec("Visit", cols([
   col(N([rsmall("Find us", "primary"), h("Next to the bridge", 2, "xx-large"), p(RADDR, "large", bind="address"),
          lst(["Monday to Friday, 6am to 9pm", "Saturday, 8am to 1pm", "Bike racks out front, street parking", "Showers and lockers inside"])]), "45%"),
   col(mapb(RADDR, RLAT, RLON, 16, "4/3"))], "xx-large", "wide", "center")))

kit("rep-signup", RK, "Rep signup: new classes and events by email",
 "A band asking visitors to join the email list for new classes, events and the odd challenge, with the signup form beside it. Part of the Rep kit; sits above the footer on every page.",
 "newsletter, signup, email, classes, events, rep",
 sec("Signup", cols([
   col(N([h("New classes, first", 2, "xx-large"), p("New classes, open days and the monthly challenge, once a month. Unsubscribe any time.")]), "55%", valign="center"),
   col(form("newsletter", "See the timetable", "/timetable/"), valign="center")], "x-large", "wide", "center"), "section-tint", ("x-large", "x-large", None, None)))

RPOP = popup("offer", N([
    img("placeholder-wide.svg", "Kettlebells lined up on a gym floor", "16/9"),
    grp(N([rsmall("New to the gym?", "primary"), h("Your first week is free", 2, "xx-large"),
           p("Leave your email and we'll send a pass for seven days of classes, plus the timetable."),
           form("offer", "Claim your free week", RTRIAL)]), None, (None, None, "large", "large"), "small", {"type": "default"})]),
    label="Your first week is free")
kit("rep-popup", RK, "Rep popup: a free first week",
 "A popup that opens five seconds into a first visit with a photo, the free trial week and one field for an email address; it closes with its button, Escape or a click outside and stays closed for two weeks. Needs the AnyPress Blocks plugin. Part of the Rep kit; put it in the footer to show it on every page.",
 "popup, offer, trial, free week, newsletter, email, modal, rep", RPOP)

RFOOT = grp(N([
    BODIES["rep-signup"],
    grp(N([cols([
        col(N([dyn("site-title", {"level": 0, "fontSize": "x-large", "fontFamily": RHEAD_F, "style": {"typography": {"lineHeight": "1", "fontWeight": "900", "textTransform": "uppercase"}}}),
               p("Coached strength, conditioning and boxing in Southeast Portland.", None, "main-accent"),
               p(f'<a href="{RTL}">' + T(RPH) + '</a>', "x-large", None, None, RHEAD_F, {"fontWeight": "900"}, raw=True, bind="phone_linked"),
               social(["instagram", "facebook", "youtube"])]), "34%"),
        col(flinks("Classes", [(n, f"/classes/{s}/") for n, s, _ in RCLS] + [("Timetable", "/timetable/")])),
        col(flinks("The gym", [("About us", "/about/"), ("Coaches", "/coaches/"), ("Memberships", "/memberships/"), ("Reviews", "/reviews/"), ("Careers", "/careers/"), ("Questions", "/faq/"), ("Blog", "/blog/"), ("Contact", "/contact/")])),
        col(N([h("Visit", 3, "medium"), p(RADDR, None, "main-accent", bind="address"), p(RHOURS, None, "main-accent", bind="hours"),
               btns([("Try a week free", None, RTRIAL)])]))], "large", "wide", "top"),
        sep(),
        row([p("© Ironside Gym. Coached training in Portland.", "small", "main-accent"),
             p('<a href="/privacy-policy/">' + T("Privacy") + '</a> · <a href="/faq/">' + T("Membership terms") + '</a>', "small", "main-accent", None, None, None, raw=True)], gap="small")]),
        "section-dark", ("x-large", "large", None, None), "large", {"type": "constrained", "contentSize": "80rem"}, align="full", name="Footer columns"),
    RPOP,
]), None, None, "0", {"type": "default"}, align="full", name="Footer")
write("rep-footer", "Rep footer: news by email, classes and the free-week popup",
 "A site footer for a gym, boxing club or fitness studio: a band for the email list, then the phone number, class and gym links and the address and hours on dark, and the free-week popup (needs the AnyPress Blocks plugin). Part of the Rep kit; choose it for the footer in the Site Editor.",
 "footer", "footer, links, hours, newsletter, phone, popup, gym, rep", RFOOT, "core/template-part/footer")

kit("rep-class-detail", RK, "Rep class: what happens, who it's for and when",
 "The body of a page for one class: what happens in a session, who it suits, a photo that opens full screen, and a card with the length, level, times and a free-trial button. Part of the Rep kit.",
 "class, details, workout, times, trial, rep",
 sec("Class details", cols([
   col(N([h("What happens", 2, "xxx-large"),
          p("Every session starts with a ten-minute warm-up, then the coach teaches one main lift and you build up in sets of five. We finish with a short, hard finisher and a stretch. The coach writes down what you lifted, so next week you know what to aim for."),
          h("Who it's for", 3, "x-large"),
          lst(["Complete beginners, coached from the empty bar", "Anyone who wants to get stronger", "People coming back after a break", "Runners and players who want fewer injuries"]),
          zoom(img("placeholder-wide.svg", "This class: hands gripping a barbell before a lift", "16/10"))]), "54%"),
   col(rcard([rsmall("At a glance", "primary"), rfact("Length", "60 minutes"), rfact("Level", "All levels"), rfact("Group size", "Eight at most"), rfact("Times", "Mon, Wed, Fri 6:30am"),
              p("Included in every membership.", "small"),
              btns([("Try it free", None, RTRIAL), ("Timetable", "outline", "/timetable/")])]))], "xx-large", "wide", "top"), content="80rem"))

kit("rep-coach-list", RK, "Rep coaches: every coach, with a link to their page",
 "Every coach with a photo, name, role and what they are known for, each linking to their own page. Part of the Rep kit; use the real coaches.",
 "coaches, trainers, team, staff, people, rep",
 sec("Coaches", N([rhead("Coaches", "The people who'll coach you"), grid([stackg([img("placeholder-tall.svg", f"Coach: {n}", "3/4"), hlink(n, f"/coaches/{s}/", 3, "x-large"), rsmall(r, "primary"), p(d)]) for n, s, r, d in RTEAM], 4, "13rem", "large")])))

kit("rep-coach", RK, "Rep coach: what one coach is known for",
 "The body of a page for one coach: their story, what to train with them for, the classes they coach and their personal training price, and a quote from one of their members. Part of the Rep kit; make one per coach.",
 "coach, trainer, profile, personal training, rep",
 sec("Coach", N([cols([
   col(N([rsmall("Head coach", "primary"), h("Marcus has been teaching beginners to lift since the day we opened", 2, "xx-large"),
          p("Marcus played rugby for ten years before a shoulder injury taught him how much good coaching matters. He opened Ironside in 2017 to coach people who had never touched a barbell, and still takes most of the beginner classes himself.", "medium"),
          h("Train with Marcus for", 3, "x-large"), lst(["Your first barbell lifts", "Getting strong after an injury", "Deadlift and squat technique", "A plan you can stick to"])]), "55%"),
   col(rcard([rsmall("Marcus coaches", "primary"), rfact("Strength", "Mon, Wed, Fri 6:30am"), rfact("Team workout", "Saturday 9am"), rfact("Personal training", "$70 an hour"),
              btns([("Train with Marcus", None, RTRIAL)])]))], "xx-large", "wide", "top"),
   rreview("I'd never lifted a barbell. Six months later I deadlifted my body weight, and Marcus was more excited than me.", "Hannah K.", "Strength, since March", "large")]), content="80rem"))

kit("rep-offers", RK, "Rep offers: ways to start and save",
 "Three offers as cards with the saving in large type, who it's for and a button: the free week, bringing a friend and a discount for students and key workers. Part of the Rep kit; keep the offers current.",
 "offers, discounts, trial, refer a friend, students, rep",
 sec("Offers", N([rhead("Ways to start", "Offers"), grid([grp(N([p(s, "xxx-large", None, None, RHEAD_F, {"lineHeight": "1", "fontWeight": "900"}), h(t, 3, "x-large"), p(d), btns([(b, "outline", l)])]), st, PAD_CARD, "small", {"type": "default"}) for s, t, d, b, l, st in [
    ("Free", "Your first week", "Seven days of classes, as many as you like. No card needed.", "Claim your week", RTRIAL, "section-second-brand"),
    ("$30", "Off for you and a friend", "Bring a friend who joins and you both get $30 off your next month.", "Bring a friend", RTRIAL, "section-card"),
    ("15% off", "Students and key workers", "Students, teachers, nurses and firefighters save 15% on any membership.", "Ask at the desk", "/contact/", "section-card")]], 3, "16rem", "medium")])))

kit("rep-jobs", RK, "Rep careers: why coach here and the open roles",
 "Why coaches work at the gym, each open role with its pay, and the application. Part of the Rep kit; keep the roles current and put the site's application form in the named Form group.",
 "careers, jobs, hiring, coach, trainer, apply, rep",
 sec("Careers", N([
   rhead("Why coach here", "A gym that pays its coaches properly"),
   grid([stackg([h(t, 3, "large"), p(d)]) for t, d in [
     ("Paid by the hour", "Every class is paid, including the 6:30am ones, at a fair rate."),
     ("Courses paid for", "Two coaching courses a year, paid for, in lifting, boxing or rehab."),
     ("Small classes", "Twelve people at most, so you can actually coach."),
     ("Free membership", "Train for free, and bring your partner at half price.")]], 4, "13rem"),
   '<!-- wp:spacer {"height":"var:preset|spacing|large"} -->\n<div style="height:var(--wp--preset--spacing--large)" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->',
   h("Open roles", 2, "xxx-large"),
   N([grp(N([row([h(t, 3, "x-large"), p(when, None, None, None, None, {"fontWeight": "700"})], valign="center"), p(d), btns([("Apply for this", None, "#apply")])]), "section-tint", PAD_CARD, "small", {"type": "default"}) for t, when, d in [
     ("Strength coach", "Part time, $32 an hour", "A coaching qualification and a year or more coaching groups. Patience with beginners matters most."),
     ("Kids' coach", "Saturday mornings, $28 an hour", "Run our games-based class for eight to twelve year olds. A background check is needed."),
     ("Front desk", "Part time, $19 an hour", "Welcome members, run the booking system and keep the gym tidy.")]]),
   grp(N([h("Apply", 2, "xxx-large"), p("Tell us a little about you and how you coach. We reply to everyone within a week."),
          form("apply", "Email the gym", "mailto:jobs@example.com")]), "section-card", PAD_CARD, "small", {"type": "default"}, anchor="apply")])))

kit("rep-trial-form", RK, "Rep free week: the form and what happens next",
 "A form to claim the free trial week, beside what happens on the first visit and what to bring. Part of the Rep kit; put the site's form in the named Form group.",
 "trial, free week, join, sign up, form, gym, rep",
 sec("Trial", cols([
   col(rcard([h("Claim your free week", 2, "xxx-large"), p("Tell us a little about you and which classes you'd like to try. We'll reply the same day with a time for your first visit."),
              form("quote", "Call " + RPH, RTL, "Rather talk now? Call the front desk.")], "section-card"), "58%"),
   col(N([h("Your first visit", 3, "x-large"),
          lst(["A coach meets you at the door", "Fifteen minutes on how you move", "Then straight into a class, scaled for you"]),
          h("Bring", 3, "x-large"), lst(["Trainers and something comfortable", "A bottle of water", "Any injuries we should know about"])]))],
   "xx-large", "wide", "top"), "section-tint"))

kit("rep-contact-full", RK, "Rep contact: phone, email, hours and form",
 "A contact section for a gym: the phone number, email, address and hours beside the contact form, then a map. Needs the AnyPress Blocks plugin for the map. Part of the Rep kit.",
 "contact, phone, email, hours, map, form, rep",
 sec("Contact us", N([cols([
   col(N([h("Call, write or drop in", 2, "xxx-large"), p(f'<a href="{RTL}">' + T(RPH) + '</a>', "xx-large", None, None, RHEAD_F, {"fontWeight": "900"}, raw=True, bind="phone_linked"),
          p('<a href="mailto:hello@example.com">hello@example.com</a>', None, None, None, None, None, raw=True, bind="email_linked"),
          p(RADDR, None, bind="address"), p(RHOURS, None, None, bind="hours")]), "40%"),
   col(rcard([h("Send a message", 3, "x-large"), form("contact", "Call " + RPH, RTL, "We reply the same day, Monday to Saturday.")]))], "xx-large", "wide", "top"),
   mapb(RADDR, RLAT, RLON, 16, "21/9")])))

# The home page: numbers, the gallery, reviews, questions and the map join the original sections.
kit_page("kit-fitness", "Home page: Rep kit, gym and classes",
 "A complete home page for a gym, boxing club, CrossFit box or fitness studio in the Rep kit: a training photo with a loud headline, classes on bold tiles, numbers that count up, the weekly timetable, memberships, coaches, a gallery that opens full screen, reviews in a carousel, questions, the gym with a map and a free-trial close. Apply the Rep style for the look it was designed with.",
 "home, gym, fitness, crossfit, boxing, studio, personal trainer, classes, kit, rep",
 ["rep-hero", "rep-classes", "rep-numbers", "rep-timetable", "rep-prices", "rep-coaches", "rep-gallery", "rep-reviews", "rep-faq-open", "rep-visit", "rep-trial"])

# ---------------------------------------------------------------- pages
def rep_page(slug, title, desc, kw, parts):
    write(slug, title, desc, "anypress/pages", kw, N(parts), "core/post-content", " * Post Types: page\n")

rep_page("rep-page-services", "Classes page: Rep kit",
 "A Classes page for a gym or studio: a heading, every class with a photo and a link to its own page, the timetable and reviews. Rep kit.",
 "classes, programs, workouts, gym, rep",
 [rpage_hero("Classes", "Strength, conditioning, boxing and mobility, all coached, all scaled to you.", "Classes", [("Try a week free", None, RTRIAL), ("Timetable", "outline", "/timetable/")]),
  sec("All classes", grid([stackg([img("placeholder-wide.svg", f"Class: {n.lower()}", "4/3"), hlink(n, f"/classes/{s}/", 3, "xx-large"), p(d)], "small") for n, s, d in RCLS], 3, "16rem", "x-large")),
  BODIES["rep-timetable"], BODIES["rep-reviews"], BODIES["rep-trial"]])

rep_page("rep-page-service", "Class page: Rep kit (one class)",
 "A page for one class, such as strength: a heading with a photo, what happens and who it's for, the times, reviews, questions about it and the free trial. Rep kit; make one per class.",
 "class page, single class, workout, gym, rep",
 [rpage_hero("Strength", "Squats, deadlifts and presses, coached in small groups so your form is right from the first lift.", "Classes / Strength", [("Try it free", None, RTRIAL)], "Classes: a lifter with a loaded barbell"),
  BODIES["rep-class-detail"], BODIES["rep-reviews"],
  sec("Questions", cols([col(N([rsmall("About this class", "primary"), h("Good to know", 2, "xxx-large")]), "36%"), col(accordion([
    ("I've never lifted. Can I come?", "Yes. You start with an empty bar and the coach builds you up week by week."),
    ("Will I get bulky?", "Not by accident. You'll get stronger and fitter; size takes years of eating for it."),
    ("How often should I come?", "Two or three times a week, with a rest day between."),
    ("What if I have a bad back?", "Tell the coach. Lifting well often helps backs, and every lift has an easier version.")]))], "xx-large", "wide", "top")),
  BODIES["rep-trial"]])

rep_page("rep-page-about", "About page: Rep kit",
 "An About page for a gym: a heading, the gym's story beside a photo, numbers that count up, the coaches, a gallery and the gym with a map. Rep kit.",
 "about, about us, gym, story, coaches, rep",
 [rpage_hero("About the gym", "Four coaches, one big room and a promise that someone will always watch your form.", "About"),
  sec("Story", cols([
    col(N([h("A gym for people who don't like gyms", 2, "xxx-large"),
           p("Marcus opened Ironside in 2017 in an old tyre shop on Hawthorne. He wanted a gym where beginners were coached properly and nobody felt watched for the wrong reasons.", "large"),
           p("Nine years on there are four coaches, 420 members and a waiting list for the 6pm strength class. Most new members come because a friend dragged them along.")]), "50%", valign="center"),
    col(img("placeholder-wide.svg", "Inside the gym: a coach and members in a kettlebell class", "4/3"))], "xx-large", "wide", "center")),
  BODIES["rep-numbers"], BODIES["rep-coach-list"], BODIES["rep-gallery"], BODIES["rep-visit"]])

rep_page("rep-page-reviews", "Reviews page: Rep kit",
 "A Reviews page for a gym: a heading, reviews as cards with stars, names and what each member trains, numbers that count up and the free trial. Rep kit; use real reviews, with permission.",
 "reviews, testimonials, members, stars, rep",
 [rpage_hero("Reviews", "4.9 stars from 310 members. Here's what some of them say.", "Reviews", [("Try a week free", None, RTRIAL)]),
  sec("All reviews", grid([rreview(*r) for r in RREVIEWS + [
    ("Tom got me my first pull-up at 52. I may have cried a little.", "Rob D.", "Conditioning with Tom"),
    ("The 6:30am crew are the reason I get out of bed.", "Nina W.", "Strength, mornings"),
    ("They never once tried to sell me supplements.", "Jay P.", "Unlimited member")]], 3, "18rem", "medium"), "section-tint"),
  BODIES["rep-numbers"], BODIES["rep-trial"]])

rep_page("rep-page-areas", "Coaches page: Rep kit",
 "A Coaches page for a gym: a heading, every coach with a link to their own page, a gallery and reviews. Rep kit.",
 "coaches, trainers, team, staff, rep",
 [rpage_hero("Coaches", "Every class is coached by one of us. Here's who you'll meet.", "Coaches"),
  BODIES["rep-coach-list"], BODIES["rep-gallery"], BODIES["rep-reviews"]])

rep_page("rep-page-area", "Coach page: Rep kit (one coach)",
 "A page for one coach: a heading with their photo, their story, the classes they coach and their personal training price, a member's quote, a gallery and the free trial. Rep kit; make one per coach.",
 "coach, trainer, profile, personal training, rep",
 [rpage_hero("Marcus", "Head coach. Strength and beginners. Former rugby player.", "Coaches / Marcus", [("Train with Marcus", None, RTRIAL)], "Coach: Marcus at the gym"),
  BODIES["rep-coach"], BODIES["rep-gallery"], BODIES["rep-trial"]])

rep_page("rep-page-offers", "Memberships page: Rep kit",
 "A Memberships page for a gym: a heading, the memberships with their prices, ways to start and save, questions and the free trial. Rep kit; match the prices to the gym's real memberships.",
 "memberships, prices, offers, trial, rep",
 [rpage_hero("Join the gym", "No joining fee, no contracts and your first week free.", "Memberships", [("Try a week free", None, RTRIAL)]),
  BODIES["rep-prices"], BODIES["rep-offers"], BODIES["rep-faq-open"]])

rep_page("rep-page-join", "Free week page: Rep kit",
 "A Free week page for a gym: a heading, the form to claim the trial beside what happens on the first visit, the coaches and reviews. Rep kit; put the site's form in the named Form group.",
 "trial, free week, join, sign up, rep",
 [rpage_hero("Try a week free", "Seven days of classes, as many as you like. No card needed, and no pressure at the end.", "Free week"),
  BODIES["rep-trial-form"], BODIES["rep-coach-list"], BODIES["rep-reviews"]])

rep_page("rep-page-timetable", "Timetable page: Rep kit",
 "A Timetable page for a gym: a heading, the weekly timetable, every class with a link to its page and the free trial. Rep kit; keep it current.",
 "timetable, schedule, class times, rep",
 [rpage_hero("Timetable", "Thirty-eight classes a week, from 6:30am to 6pm, plus Saturday's team workout.", "Timetable", [("Book a free week", None, RTRIAL)]),
  BODIES["rep-timetable"], BODIES["rep-classes"], BODIES["rep-trial"]])

rep_page("rep-page-faq", "Questions page: Rep kit",
 "A Questions page for a gym: answers that open and close, grouped into starting, classes and memberships, and the free trial. Rep kit; answer the real questions.",
 "faq, questions, answers, membership, beginners, rep",
 [rpage_hero("Ask us anything", "Starting, classes and memberships, answered plainly.", "Questions"),
  sec("Questions", N([N([h(group_t, 2, "xx-large"), accordion(qs)]) for group_t, qs in [
    ("Starting", [
      ("I've never been to a gym. Is this for me?", "Yes. Most of our members started as beginners. Every class is coached and every exercise has an easier version."),
      ("How does the free week work?", "Come to as many classes as you like for seven days. No card needed, and no pressure at the end.")]),
    ("Classes", [
      ("Do I need to book?", "Yes, in the app, so we know how many are coming. You can book up to a week ahead."),
      ("What if I'm late?", "Up to ten minutes is fine; do the warm-up on your own and join in.")]),
    ("Memberships", [
      ("Can I freeze my membership?", "Yes, for up to two months a year, for travel, injury or anything else."),
      ("How do I cancel?", "Tell the front desk or email us. Thirty days' notice, no fee.")])]]),
    content="56rem"),
  BODIES["rep-trial"]])

rep_page("rep-page-careers", "Careers page: Rep kit",
 "A Careers page for a gym: a heading, why coaches work there, the open roles with pay, the application form and the gym with a map. Rep kit; keep the roles current and put the site's form in the named Form group.",
 "careers, jobs, hiring, coach, trainer, rep",
 [rpage_hero("Careers", "A small gym that pays every class, pays for your courses and keeps classes small.", "Careers", [("See open roles", None, "#apply")]),
  BODIES["rep-jobs"], BODIES["rep-visit"]])

rep_page("rep-page-contact", "Contact page: Rep kit",
 "A Contact page for a gym: a heading, the phone number, email, address and hours beside the contact form, a map and questions. Rep kit; put the site's contact form in the named Form group.",
 "contact, phone, email, hours, rep",
 [rpage_hero("Contact", "Call the front desk, send a message or drop in on Hawthorne.", "Contact"),
  BODIES["rep-contact-full"], BODIES["rep-faq-open"]])

rep_page("rep-page-thanks", "Thank-you page: Rep kit",
 "The page visitors see after sending a form: thanks, what happens next and when, and links to keep browsing. Rep kit; send every form here.",
 "thank you, thanks, confirmation, form sent, rep",
 [sec("Thanks", N([rsmall("Message sent", "primary"), h("Thanks. See you soon.", 1, "poster", None, None, {"lineHeight": "0.9"}),
    p("We'll reply the same day, Monday to Saturday. Check your email for a copy of what you sent.", "large"),
    btns([("Back to the home page", None, "/"), ("See the timetable", "outline", "/timetable/")])]), "section-dark", ("xxx-large", "xxx-large", None, None), "56rem"),
  BODIES["rep-reviews"]])

print("rep ok")
