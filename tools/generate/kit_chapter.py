# Chapter (0.9.0): a whole website for an online course, membership or coaching programme, written for a drawing
# teacher who sells online courses and runs weekend workshops in a few cities. Run by kits.py after kit_commons.py, so
# every helper in kits.py, kits_more.py, kit_ridge.py and kit_commons.py is in scope.
#
# A workbook: ink blue, school yellow, a friendly serif. Pages link to each other by slug: /courses/ and one page per
# course under it, /community/, /about/, /student-stories/, /workshops/ and one page per city under it, /offers/,
# /join/, /faq/, /teach/, /journal/, /contact/, /thank-you/. Forms are named groups, as in Ridge: "Form: quote" asks
# about a course, "Form: apply" is the teaching assistant application.

K = "anypress/kit-courses"
CF = "fraunces"
CPHONE = "555 0142"
CTEL = "tel:5550142"
CJOIN = "/join/"
CADDRESS = "214 SE Ash Street, Portland"
CSERIF = {"lineHeight": "1", "fontWeight": "600"}

def cimg(alt, ratio="3/2", file="placeholder-wide.svg"):
    return img(file, alt, ratio)

def ctel(size="xx-large"):
    return p(f'<a href="{CTEL}">' + T(CPHONE) + '</a>', size, None, None, CF, CSERIF, raw=True, bind="phone_linked")

def chead(eb, title, link=None, size="xx-large"):
    left = stackg([mono(eb, "primary"), h(title, 2, size)])
    return row([left, btns([(link[0], "outline", link[1])])] if link else [left], valign="bottom")

def c_buttons():
    """The header's buttons: the number and Join on tablets and computers, just "Call" on phones."""
    join = f'<!-- wp:button {j({"metadata": {"blockVisibility": {"viewport": {"mobile": False}}}})} -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{CJOIN}">{T("Join a course")}</a></div>\n<!-- /wp:button -->'
    call = f'<!-- wp:button {j({"className": "is-style-outline", "metadata": {"blockVisibility": {"viewport": {"mobile": False}}, "bindings": button_bindings("phone")}})} -->\n<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="{CTEL}">{T(CPHONE)}</a></div>\n<!-- /wp:button -->'
    short = f'<!-- wp:button {j({"metadata": {"blockVisibility": {"viewport": {"tablet": False, "desktop": False}}, "bindings": button_bindings("phone_link")}})} -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{CTEL}">{T("Call")}</a></div>\n<!-- /wp:button -->'
    return '<!-- wp:buttons {"layout":{"type":"flex","flexWrap":"nowrap"}} -->\n<div class="wp-block-buttons">' + N([call, join, short]) + '</div>\n<!-- /wp:buttons -->'

def cpage_hero(title, text, crumb=None, buttons=None, alt=None):
    words = N(([mono(crumb, "primary-alt-accent")] if crumb else []) + [h(title, 1, "xxx-large"), p(text, "medium")] + ([btns(buttons)] if buttons else []))
    if not alt:
        return sec("Page hero", words, "section-second-brand", ("xx-large", "x-large", None, None), "80rem")
    return sec("Page hero", cols([col(words, "58%", valign="center"), col(cimg(alt, "4/3"))], "x-large", "wide", "center"), "section-second-brand", ("xx-large", "x-large", None, None), "80rem")

# ---------------------------------------------------------------- content
COURSES = [
    ("Draw people in 30 days", "draw-people-in-30-days", "Fifteen minutes a day, one short lesson at a time, with feedback from a working illustrator.", "$149", "30 lessons", "A sketchbook open on a table with pencil drawings of people"),
    ("The sketchbook habit", "sketchbook-habit", "Fourteen days of tiny prompts that get you drawing every day, even when you're busy.", "$49", "14 lessons", "A hand drawing in a small sketchbook with a pen"),
    ("Faces and portraits", "faces-and-portraits", "Likeness, expression and light, from quick heads to a finished portrait you're proud of.", "$99", "20 lessons", "A pencil portrait of a woman's face on paper"),
    ("Urban sketching", "urban-sketching", "Draw streets, cafés and buildings on the spot, with simple perspective and quick colour.", "$99", "18 lessons", "Someone sketching a city street from a café table"),
    ("Watercolor for sketchers", "watercolor-for-sketchers", "Add loose, fresh colour to your line drawings with a small travel palette.", "$99", "16 lessons", "Watercolor paints and brushes beside a painted sketch"),
    ("Hands and feet", "hands-and-feet", "The two things everyone hides in their drawings, made simple in ten short lessons.", "$59", "10 lessons", "Pencil studies of hands on a sheet of paper"),
]
CITIES = [("Portland", "portland", 45.5231, -122.6765), ("Seattle", "seattle", 47.6062, -122.3321), ("San Francisco", "san-francisco", 37.7749, -122.4194),
          ("Denver", "denver", 39.7392, -104.9903), ("Chicago", "chicago", 41.8781, -87.6298), ("Brooklyn", "brooklyn", 40.6782, -73.9442)]
CSTORIES = [
    ("I had started and quit drawing three times. The group is why I finished this time.", "Tom B.", "Draw people in 30 days"),
    ("Fifteen minutes a day was the trick. I drew on the bus, at lunch, in waiting rooms. Now I can't stop.", "Priya S.", "The sketchbook habit"),
    ("Mara's notes on my drawings were kind and exact. I improved more in a month than in a year on my own.", "Daniel K.", "Draw people in 30 days"),
    ("I drew my grandmother from life for the first time. She asked for a copy for the fridge.", "Ana M.", "Faces and portraits"),
    ("I sketch every café I visit now. My travel journals are the best souvenirs I own.", "Leo R.", "Urban sketching"),
    ("The live sessions feel like a real class. I've made friends in four countries.", "Hannah W.", "Course and community"),
]

def course_card(name, slug, text, price, lessons, alt):
    return card(N([cimg(alt, "3/2"), mono(lessons, "primary"), h(name, 3, "large"), p(text, None, "secondary"),
                   row([p(price, "large", None, None, CF, CSERIF), link_p("See the course →", f"/courses/{slug}/", None, {"fontWeight": "700"})], valign="center")]),
                "section-card", ("medium", "medium", "medium", "medium"))

def cstory(text, name, course, size="medium"):
    return card(N([p("“" + text + "”", size, None, None, CF, {"lineHeight": "1.35"}), p(f"{name}, {course}", "small", "secondary", None, None, {"fontWeight": "700"})]), "section-tint")

# ---------------------------------------------------------------- sections
kit("chapter-topbar", K, "Chapter top bar: the next start date and a phone number",
 "A thin dark bar above the header with the next start date and a link to join, and a number to call with questions. Part of the Chapter kit; keep the date current.",
 "top bar, announcement, start date, cohort, phone, header, chapter",
 grp(row([p(T("Next cohort starts 3 March") + ' · <a href="/join/">' + T("Save your place") + '</a>', "small", None, None, None, None, raw=True),
          hide_on(p(T("Questions? Call or text") + f' <a href="{CTEL}">' + T(CPHONE) + '</a>', "small", None, None, None, None, raw=True), "mobile")], gap="small"),
     "section-dark", ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Top bar"))

CHEADER = grp(N([
    BODIES["chapter-topbar"],
    grp(row([
        row([dyn("site-logo", {"width": 44, "shouldSyncIcon": True}), dyn("site-title", {"level": 0, "fontSize": "large", "fontFamily": CF, "style": {"typography": {"lineHeight": "1", "fontWeight": "700"}}})], "left", "small", False, "center"),
        row([dyn("navigation", {"overlayMenu": "mobile", "layout": {"type": "flex", "justifyContent": "right"}, "style": {"typography": {"fontWeight": "600"}}}),
             c_buttons()], "right", "medium", False, "center")], "space-between", "medium", False, "center"),
        None, ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Main bar").replace(
        '<!-- wp:group {', '<!-- wp:group {"backgroundColor":"base",', 1).replace('class="wp-block-group alignfull', 'class="wp-block-group alignfull has-base-background-color has-background', 1),
]), "sticky", None, "0", {"type": "default"}, align="full", name="Header")
write("chapter-header", "Chapter header: start date, menu and a Join button",
 "A site header for an online course, membership or coaching programme that stays at the top while visitors scroll: a dark bar with the next start date and a number for questions, then the logo, the menu (with dropdowns for courses and workshops), the phone number and a Join button. Part of the Chapter kit; choose it for the header in the Site Editor.",
 "header", "header, menu, navigation, sticky, join, phone, course, chapter", CHEADER, "core/template-part/header")

kit("chapter-numbers", K, "Chapter numbers: four figures that count up",
 "Four big numbers that count up as they scroll into view (students, lessons, average review, countries), each with a short label, on the brand colour. Needs the AnyPress Blocks plugin. Part of the Chapter kit; use real figures only.",
 "numbers, statistics, counter, students, reviews, results, chapter",
 sec("Numbers", grid([stackg([counter(n, suf, pre, "xxx-large", CF, d), p(lbl, "medium", "main-accent")]) for n, suf, pre, d, lbl in
     [(4800, "", "", 0, "students since 2021"), (137, "", "", 0, "video lessons across six courses"), (4.9, " / 5", "", 1, "average review"), (38, "", "", 0, "countries in the community")]], 4, "12rem"),
     "section-brand", ("x-large", "x-large", None, None)))

kit("chapter-courses", K, "Chapter courses: cards with photos and prices",
 "Every course as a card with a photo, the number of lessons, one line about it, the price and a link to its own page, three across. Part of the Chapter kit; each link goes to /courses/<course>/.",
 "courses, catalogue, products, cards, prices, lessons, chapter",
 sec("Courses", N([chead("Six courses", "Start where you are", ("All courses", "/courses/")),
                   grid([course_card(*x) for x in COURSES], 3, "18rem", "medium")]), "section-tint"))

kit("chapter-steps", K, "Chapter steps: how the courses work",
 "Three numbered steps from buying a course to finishing it, in big serif numerals, so people know what taking part involves. Part of the Chapter kit.",
 "how it works, steps, process, lessons, feedback, chapter",
 sec("How it works", N([chead("How it works", "Fifteen minutes a day"), grid([stackg([p(n, "xxx-large", "primary", None, CF, {"lineHeight": "1", "fontWeight": "300"}), h(t, 3, "large"), p(d, None, "secondary")]) for n, t, d in [
    ("01", "Watch a short lesson", "Every lesson is a 10 to 15 minute video you can watch on any device, whenever suits you."),
    ("02", "Do one exercise", "Each lesson ends with one drawing to do. Paper and a pencil are all you need to start."),
    ("03", "Get feedback", "Post your drawing in the group and get notes from Mara or a teaching assistant within two days.")]], 3, "16rem", "x-large")])))

kit("chapter-stories", K, "Chapter student stories: a carousel of quotes",
 "Students in their own words, in a carousel, three at a time on a computer and one on a phone, with each student's name and course. Needs the AnyPress Blocks plugin. Part of the Chapter kit; use real quotes, with permission.",
 "testimonials, reviews, student stories, quotes, carousel, slider, chapter",
 sec("Student stories", N([chead("Student stories", "4,800 students and counting", ("All stories", "/student-stories/")),
                           carousel([cstory(*s) for s in CSTORIES], 3, "Student stories")])))

kit("chapter-gallery", K, "Chapter gallery: drawings by students",
 "Students' work in a carousel, each drawing opening full screen when clicked, with who drew it and in which course. Needs the AnyPress Blocks plugin. Part of the Chapter kit; use students' own work, with permission.",
 "gallery, student work, portfolio, photos, carousel, lightbox, chapter",
 sec("Gallery", N([chead("Student work", "Drawn in the first month"), carousel([stackg([zoom(img("placeholder-tall.svg", alt, "4/5")), p(cap, None, "secondary")]) for alt, cap in [
    ("A sketchbook open on a table with pencil drawings of people", "Tom B., day 30 of Draw people in 30 days"),
    ("A pencil portrait of a woman's face on paper", "Ana M., Faces and portraits"),
    ("Someone sketching a city street from a café table", "Leo R., Urban sketching in Lisbon"),
    ("Pencil studies of hands on a sheet of paper", "Daniel K., Hands and feet"),
    ("Watercolor paints and brushes beside a painted sketch", "Hannah W., Watercolor for sketchers")]], 3, "Drawings by students", 6)]), "section-tint"))

kit("chapter-workshops-map", K, "Chapter workshops: in-person weekends and a map",
 "Where the teacher runs in-person workshops: every city as a link to its own page, beside a map of the home studio. Needs the AnyPress Blocks plugin for the map. Part of the Chapter kit.",
 "workshops, in person, cities, locations, map, studio, chapter",
 sec("Workshops", cols([
   col(N([mono("In person", "primary"), h("Draw with us for a weekend", 2, "xx-large"), p("Twice a year Mara takes the course on the road: two days of drawing from life with twelve people, in a studio near you.", "medium", "secondary"),
          '<!-- wp:list {"className":"is-style-no-bullets","fontSize":"large","style":{"typography":{"lineHeight":"1.6","fontWeight":"600"}}} -->\n'
          '<ul class="wp-block-list is-style-no-bullets has-large-font-size" style="line-height:1.6;font-weight:600">'
          + "\n\n".join(f'<!-- wp:list-item -->\n<li><a href="/workshops/{s}/">{T(t)}</a></li>\n<!-- /wp:list-item -->' for t, s, *_ in CITIES) + '</ul>\n<!-- /wp:list -->']), "38%"),
   col(N([mapb(CADDRESS + ", Oregon", 45.5221, -122.6610, 14, "4/3"), p("The home studio, " + CADDRESS + ". Open for drop-in drawing on Thursday evenings.", "small", "secondary")]))], "x-large", "wide", "top")))

kit("chapter-faq", K, "Chapter questions: answers that open and close",
 "The questions people ask before buying a course, as answers that open and close, beside a heading and a link to all questions. Part of the Chapter kit; answer with the course's real rules.",
 "faq, questions, answers, accordion, refund, course, chapter",
 sec("Questions", cols([
   col(N([mono("Questions", "primary"), h("Before you start", 2, "xx-large"), p("Can't see yours? Call or text: you'll reach Mara or Sam, not a robot.", "medium", "secondary"), btns([("All questions", "outline", "/faq/")])]), "36%"),
   col(accordion([
     ("I can't draw at all. Is it for me?", "Yes. Most students start from stick figures. The first week is about looking, not talent."),
     ("How long do I have the lessons?", "For life. Watch them as often as you like, and get every update free."),
     ("What do I need?", "A pencil, an eraser and some cheap paper. We send a list of nicer things if you want them later."),
     ("What if it's not for me?", "Ask within thirty days and you get every cent back, no questions asked."),
     ("Can I buy a course as a gift?", "Yes. Gift cards are on the Offers page and arrive by email on the day you choose.")]))], "x-large", "wide", "top")))

kit("chapter-call", K, "Chapter closing band: join or ask",
 "A closing band on the second brand colour asking visitors to start, with the Join button and a number to call or text. Part of the Chapter kit; ends most pages.",
 "call to action, join, enrol, phone, closing, chapter",
 sec("Join us", cols([
   col(N([h("Start drawing this week", 2, "xxx-large"), p("Courses from $49. Thirty days to change your mind.", "large")]), "60%", valign="center"),
   col(N([btns([("Join a course", None, CJOIN)]), p("Questions? Call or text"), ctel("xx-large")]), valign="center")], "x-large", "wide", "center"), "section-second-brand", ("x-large", "x-large", None, None)))

kit("chapter-signup", K, "Chapter signup: a weekly drawing prompt",
 "A band asking visitors to join a weekly email with a drawing prompt, with the signup form beside it. Part of the Chapter kit; sits above the footer on every page.",
 "newsletter, signup, email, prompt, subscribe, chapter",
 sec("Signup", cols([
   col(N([h("A drawing prompt every Monday", 2, "xx-large"), p("One small thing to draw this week, with a tip from Mara. Free, and 22,000 people already get it.", "medium", "secondary")]), "55%", valign="center"),
   col(form("newsletter", "Get the Monday prompt", "/courses/"), valign="center")], "large", "wide", "center"), "section-tint", ("x-large", "x-large", None, None)))

CPOPUP = popup("offer", N([
    img("placeholder-wide.svg", "A hand drawing in a small sketchbook with a pen", "16/9"),
    grp(N([mono("Try before you buy", "primary"), h("Get the first lesson free", 2, "xx-large"),
           p("Leave your email and we'll send lesson one of Draw people in 30 days, plus 15% off if you join this week."),
           form("offer", "See the courses", "/courses/")]), None, (None, None, "large", "large"), "small", {"type": "default"})]),
    label="The first lesson free")
kit("chapter-popup", K, "Chapter popup: the first lesson free",
 "A popup that opens five seconds into a first visit with a photo, a free first lesson and one field for an email address; it closes with its button, Escape or a click outside and stays closed for two weeks. Needs the AnyPress Blocks plugin. Part of the Chapter kit; put it in the footer to show it on every page.",
 "popup, offer, free lesson, lead magnet, newsletter, email, modal, chapter", CPOPUP)

CFOOTER = grp(N([
    BODIES["chapter-signup"],
    grp(N([cols([
        col(N([dyn("site-title", {"level": 0, "fontSize": "x-large", "fontFamily": CF}),
               p("Online drawing courses and weekend workshops with illustrator Mara Lind. Fifteen minutes a day, with a group that keeps you going.", None, "main-accent"),
               ctel("xx-large"), social(["instagram", "youtube", "facebook"])]), "34%"),
        col(flinks("Courses", [(n, f"/courses/{s}/") for n, s, *_ in COURSES])),
        col(flinks("The school", [("About Mara", "/about/"), ("The community", "/community/"), ("Workshops", "/workshops/"), ("Student stories", "/student-stories/"), ("Offers and gifts", "/offers/"), ("Teach with us", "/teach/"), ("Journal", "/journal/"), ("Questions", "/faq/")])),
        col(N([h("The studio", 3, "medium"), p(CADDRESS, None, "main-accent", bind="address"), p("Drop-in drawing on Thursdays, 6pm to 9pm", None, "main-accent", bind="hours"),
               btns([("Join a course", None, CJOIN)])]))], "large", "wide", "top"),
        sep(),
        row([p("© Draw with Mara. Thirty-day money-back promise on every course.", "small", "main-accent"),
             p('<a href="/privacy-policy/">' + T("Privacy") + '</a> · <a href="/contact/">' + T("Contact") + '</a>', "small", "main-accent", None, None, None, raw=True)], gap="small")]),
        "section-dark", ("x-large", "large", None, None), "large", {"type": "constrained", "contentSize": "80rem"}, align="full", name="Footer columns"),
    CPOPUP,
]), None, None, "0", {"type": "default"}, align="full", name="Footer")
write("chapter-footer", "Chapter footer: weekly prompt, links, studio and the free lesson popup",
 "A site footer for an online course, membership or coaching programme: a band for the weekly email, then the phone number, the courses, the school's pages and the studio on dark, and the free lesson popup (needs the AnyPress Blocks plugin). Part of the Chapter kit; choose it for the footer in the Site Editor.",
 "footer", "footer, links, newsletter, signup, phone, address, popup, course, chapter", CFOOTER, "core/template-part/footer")

kit("chapter-course-detail", K, "Chapter course: what's inside and the price",
 "The body of one course page: what students make in plain words, a list of what's included, a photo, and a box with the price and buttons to join or ask. Part of the Chapter kit.",
 "course, details, included, price, buy, enrol, chapter",
 sec("Course details", cols([
   col(N([h("What you'll make", 2, "xx-large"),
          p("A sketchbook full of people: quick gestures from the first day, then proportions, faces and hands, and by week four, drawings from life in cafés, parks and trains."),
          lst(["30 video lessons, 10 to 15 minutes each", "One drawing exercise per lesson, with an example", "Four live draw-along sessions with a model", "Feedback on your drawings in the private group", "Keep everything for life, with every update"], "medium"),
          zoom(cimg("This course: a page of quick figure drawings in pencil", "16/9"))]), "60%"),
   col(card(N([mono("Draw people in 30 days", "primary"), p("$149", "xxx-large", None, None, CF, CSERIF),
               p("Once, for life. Or $29 a month with the community. Next cohort starts 3 March."),
               btns([("Join the course", None, CJOIN), ("Call " + CPHONE, "outline", CTEL, "phone")])]), "section-brand-soft", PAD_CARD))], "x-large", "wide", "top")))

kit("chapter-offers", K, "Chapter offers: three ways to save",
 "Three offers as cards with the saving in large type, what it is and a button, then the small print. Part of the Chapter kit; keep the offers current.",
 "offers, discounts, gift cards, free lesson, bundle, chapter",
 sec("Offers", N([grid([card(N([p(s, "xxx-large", None, None, CF, CSERIF), h(t, 3, "large"), p(d), btns([(b, None, l)])]), st, PAD_CARD) for s, t, d, b, l, st in [
    ("Free", "The first lesson of every course", "Watch lesson one of any course before you buy, and get 15% off if you join within a week.", "See the courses", "/courses/", "section-brand-soft"),
    ("Gift", "A course for someone who keeps saying they can't draw", "Choose a course and a date, and we email a gift card with a note from you.", "Ask about a gift", CJOIN, "section-tint"),
    ("25% off", "Three courses together", "Draw people in 30 days, Faces and portraits and Hands and feet, for $230 instead of $307.", "Join the bundle", CJOIN, "section-brand-soft")]], 3, "16rem", "medium"),
    p("Offers can't be combined. Every course comes with the thirty-day money-back promise.", "small", "secondary")])))

kit("chapter-teach", K, "Chapter teaching assistants: roles and how to apply",
 "Ways to teach with the school: why people do it, each open role with the hours it takes, and the application. Part of the Chapter kit; keep the roles current and put the site's application form in the named Form group.",
 "careers, jobs, teach, teaching assistant, apply, chapter",
 sec("Teach", N([
   chead("Why teach with us", "Help people draw, from anywhere"),
   grid([stackg([h(t, 3, "large"), p(d, None, "secondary")]) for t, d in [
     ("Work from home", "Every role is online, apart from the weekend workshops."),
     ("Choose your hours", "Most assistants give feedback for five to ten hours a week."),
     ("Paid fairly", "$32 an hour, paid monthly, plus every course free."),
     ("Keep learning", "A monthly session with Mara on teaching and your own work.")]], 4, "13rem"),
   '<!-- wp:spacer {"height":"var:preset|spacing|large"} -->\n<div style="height:var(--wp--preset--spacing--large)" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->',
   h("Open roles", 2, "xx-large"),
   N([card(N([row([h(t, 3, "large"), p(when, None, None, None, None, {"fontWeight": "700"})], valign="center"), p(d, None, "secondary"), btns([("Apply for this", None, "#apply")])]), "section-tint") for t, when, d in [
     ("Feedback assistant", "5 to 10 hours a week", "Give kind, exact notes on students' drawings in the group. You'll need a portfolio of figure drawing."),
     ("Live session host", "2 evenings a month", "Run the live draw-along sessions with a model, and keep the chat friendly."),
     ("Workshop assistant", "4 weekends a year", "Help Mara run the in-person weekends: set up, model bookings and one-to-one help.")]]),
   grp(N([h("Apply", 2, "xx-large"), p("Tell us about yourself, the role you'd like and where we can see your drawings. Sam replies to everyone within a week."),
          form("apply", "Email the studio", "mailto:jobs@example.com")]), "section-card", PAD_CARD, "small", {"type": "default"}, anchor="apply")])))

kit("chapter-join-form", K, "Chapter join: ask about a course",
 "A form for questions before joining or to save a place in the next cohort, beside what happens next and a card offering the free first lesson. Part of the Chapter kit; put the site's form in the named Form group.",
 "join, enrol, sign up, questions, form, cohort, chapter",
 sec("Apply", cols([
   col(card(N([h("Save your place or ask a question", 2, "xx-large"), p("Tell us which course and what you'd like to get better at. We'll send the link to join, or answer your question first."),
               form("quote", "Call " + CPHONE, CTEL, "Prefer to talk? Call or text.")]), "section-card", PAD_CARD), "58%"),
   col(N([h("What happens next", 3, "x-large"),
          lst(["We reply within one working day.", "You get a link to pay, and your lessons open straight away.", "You're added to the group before the next cohort starts."], "medium"),
          card(N([mono("Not sure yet?", "primary"), h("Watch the first lesson free", 3, "large"), p("Every course's first lesson is free to watch."), btns([("See the courses", "outline", "/courses/")])]), "section-brand-soft")]))],
   "x-large", "wide", "top"), "section-tint"))

kit("chapter-contact", K, "Chapter contact: details, form and the studio map",
 "A contact section for an online course or school: phone, email, the studio's address and hours beside the contact form, then a map. Needs the AnyPress Blocks plugin for the map. Part of the Chapter kit.",
 "contact, phone, email, address, studio, map, form, chapter",
 sec("Contact", N([cols([
   col(N([h("Call, write or come and draw", 2, "xx-large"), ctel("xxx-large"),
          p('<a href="mailto:hello@example.com">hello@example.com</a>', "medium", None, None, None, None, raw=True, bind="email_linked"),
          p(CADDRESS, "medium", bind="address"), p("Drop-in drawing on Thursdays, 6pm to 9pm. Bring paper; the tea is free.", None, "secondary")]), "42%"),
   col(card(N([h("Send a message", 3, "x-large"), form("contact", "Call " + CPHONE, CTEL, "We reply within one working day.")]), "section-tint", PAD_CARD))], "x-large", "wide", "top"),
   mapb(CADDRESS + ", Oregon", 45.5221, -122.6610, 15, "21/9")])))

def cevent(day, month, title, when, where):
    date = grp(N([p(day, "x-large", None, "center", CF, {"lineHeight": "1", "fontWeight": "700"}), p(month, "small", None, "center", None, {"textTransform": "uppercase", "letterSpacing": "0.08em"})]),
               "section-brand", ("small", "small", "small", "small"), "x-small")
    return cols([col(date, "5.5rem"), col(stackg([h(title, 3, "large"), p(f"{when} · {where}", None, "secondary"), p(f'<a href="{CJOIN}">' + T("Save a place") + "</a>", None, None, None, None, None, True)], "x-small"), None, None, None, "center")],
                "large", None, "center", False)

kit("chapter-workshop-dates", K, "Chapter workshop dates: the next weekends",
 "The next in-person weekends as rows with a date block, the city, the place and a link to save a place, under a heading. Part of the Chapter kit; for the Workshops page.",
 "workshops, dates, events, calendar, in person, chapter",
 sec("Dates", N([chead("Dates", "The next weekends"),
   stackg([cevent(d, m, t, w, wh) for d, m, t, w, wh in [
       ("14", "Mar", "Portland: drawing people from life", "Sat and Sun, 10am to 4pm", "The home studio"),
       ("11", "Apr", "Seattle: faces and portraits", "Sat and Sun, 10am to 4pm", "Pike Street Studios"),
       ("09", "May", "San Francisco: urban sketching", "Sat and Sun, 9am to 3pm", "Meet at the Ferry Building"),
       ("13", "Jun", "Denver: drawing people from life", "Sat and Sun, 10am to 4pm", "RiNo Art Hall"),
       ("12", "Sep", "Chicago: urban sketching", "Sat and Sun, 9am to 3pm", "Meet at the Cultural Center"),
       ("10", "Oct", "Brooklyn: faces and portraits", "Sat and Sun, 10am to 4pm", "Dumbo Drawing Room")]], "medium")]), content="64rem"))

kit("chapter-community-detail", K, "Chapter community: what members get each week",
 "What the community gives members, week by week: feedback, live sessions, monthly challenges and the members' library, each with a heading and a line, and a photo. Part of the Chapter kit; for the Community page.",
 "community, membership, live sessions, feedback, challenges, chapter",
 sec("Each week", cols([
   col(N([h("What members get", 2, "xx-large"), stackg([stackg([h(a, 3, "medium"), p(b, None, "secondary")], "x-small") for a, b in [
     ("Feedback on your drawings", "Post a drawing any day and get notes from Mara or an assistant within two days."),
     ("Two live sessions a week", "Draw along with a model on Tuesday evening and Saturday morning, with recordings for every time zone."),
     ("A challenge every month", "One theme, one month, and a gallery of everyone's drawings at the end."),
     ("Every course included", "All six courses, and every new one, for as long as you're a member.")]], "large")]), "50%"),
   col(cimg("Students drawing at easels in a bright studio", "4/5", "placeholder-tall.svg"), valign="center")], "xx-large", "wide", "center")))

# The home page: numbers, courses, stories, workshops with a map and questions join the original sections.
kit_page("kit-courses", "Home page: Chapter kit, courses and community",
 "A complete home page for an online course, coaching programme or membership in the Chapter kit: the course and what's inside, numbers that count up, outcomes, every course with photos, the weeks of the curriculum, the teacher, student stories in a carousel, the community, in-person workshops with a map, two ways to join and common questions. Apply the Chapter style for the look it was designed with.",
 "home, course, online course, coaching, membership, community, teacher, kit, chapter",
 ["chapter-hero", "chapter-numbers", "chapter-outcomes", "chapter-courses", "chapter-curriculum", "chapter-teacher", "chapter-stories", "chapter-community", "chapter-workshops-map", "chapter-pricing", "chapter-faq"])

# ---------------------------------------------------------------- pages
def chapter_page(slug, title, desc, kw, parts):
    write(slug, title, desc, "anypress/pages", kw, N(parts), "core/post-content", " * Post Types: page\n")

chapter_page("chapter-page-services", "Courses page: Chapter kit",
 "A Courses page for an online school: a heading, every course as a card linking to its own page, how it works, student stories and a closing band. Chapter kit.",
 "courses, catalogue, all courses, products, chapter",
 [cpage_hero("Courses", "Six courses, from your first sketchbook to finished portraits. Every first lesson is free.", "All courses", [("Join a course", None, CJOIN)]),
  BODIES["chapter-courses"], BODIES["chapter-steps"], BODIES["chapter-stories"], BODIES["chapter-call"]])

chapter_page("chapter-page-service", "Course page: Chapter kit (one course)",
 "A page for one course: a heading with a photo, what students make and the price, the weeks of the curriculum, students' drawings, stories, questions about this course and a closing band. Chapter kit; make one per course under Courses.",
 "course page, single course, curriculum, price, enrol, chapter",
 [cpage_hero("Draw people in 30 days", "Fifteen minutes a day, one short lesson at a time, with feedback from a working illustrator.", "Courses / Draw people in 30 days", [("Join the course", None, CJOIN), ("Call " + CPHONE, "outline", CTEL, "phone")], "This course: a sketchbook open on a table with pencil drawings of people"),
  BODIES["chapter-course-detail"], BODIES["chapter-curriculum"], BODIES["chapter-gallery"], BODIES["chapter-stories"],
  sec("Questions", cols([col(h("About this course", 2, "xx-large"), "36%"), col(accordion([
    ("How long does it take?", "Thirty days at fifteen minutes a day. Go slower if you like; the lessons don't expire."),
    ("When can I start?", "Today. The lessons open as soon as you join; the next group cohort starts 3 March."),
    ("Do I need to come to the live sessions?", "No. Every session is recorded, and most students watch the recordings."),
    ("What if I fall behind?", "Everyone does. Pick up where you left off; the group is there whenever you post.")]))], "x-large", "wide", "top")),
  BODIES["chapter-call"]])

chapter_page("chapter-page-community", "Community page: Chapter kit",
 "A Community page for a course or membership: a heading, what members get each week, the community in short, two ways to join, student stories and a closing band. Chapter kit.",
 "community, membership, group, live sessions, subscription, chapter",
 [cpage_hero("The community", "Feedback on your drawings, live sessions every week and every course included, for $29 a month.", "Community", [("Join with the community", None, CJOIN)], "Students drawing at easels in a bright studio"),
  BODIES["chapter-community-detail"], BODIES["chapter-community"], BODIES["chapter-pricing"], BODIES["chapter-stories"], BODIES["chapter-call"]])

chapter_page("chapter-page-about", "About page: Chapter kit",
 "An About page for a teacher or online school: a heading, the teacher's story with a photo, numbers that count up, the teacher in short, how the courses work and a closing band. Chapter kit.",
 "about, about me, teacher, story, bio, chapter",
 [cpage_hero("Hi, I'm Mara. I teach people who think they can't draw.", "Illustrator for twenty years, teacher for ten, and still drawing on the bus every morning.", "About"),
  sec("Story", cols([
    col(N([h("From the college to your kitchen table", 2, "xx-large"),
           p("I started teaching life drawing at the city college in 2015. Every term, the people who said they couldn't draw made the most progress, because nobody had ever shown them how to look.", "large"),
           p("In 2021 I recorded the class properly, cut out the boring bits and put it online. Today 4,800 people in 38 countries have taken it, and a small team of illustrators helps me give feedback."),
           p("I still draw every day, illustrate books and magazines, and run a few weekends a year in person, because nothing beats a room full of people drawing.")]), "50%", valign="center"),
    col(cimg("The teacher at a desk with a sketchbook", "4/5", "placeholder-tall.svg"))], "x-large", "wide", "center")),
  BODIES["chapter-numbers"], BODIES["chapter-steps"], BODIES["chapter-workshops-map"], BODIES["chapter-call"]])

chapter_page("chapter-page-reviews", "Student stories page: Chapter kit",
 "A Student stories page: a heading, students' quotes as cards with names and courses, their drawings, numbers that count up and a closing band. Chapter kit; use real quotes, with permission.",
 "student stories, reviews, testimonials, results, chapter",
 [cpage_hero("Student stories", "What students say after the course. We asked; these are their words.", "Student stories", [("Join a course", None, CJOIN)]),
  sec("All stories", grid([cstory(*s) for s in CSTORIES + [
    ("I'm 71 and I'd never drawn. My grandchildren now ask me to draw them every visit.", "Margaret F.", "Draw people in 30 days"),
    ("The hands course is ten lessons and it fixed the thing I'd been hiding for years.", "Sofia L.", "Hands and feet"),
    ("I bought it as a gift for my husband and ended up doing it with him.", "Grace O.", "The sketchbook habit")]], 3, "18rem", "medium")),
  BODIES["chapter-gallery"], BODIES["chapter-numbers"], BODIES["chapter-call"]])

chapter_page("chapter-page-areas", "Workshops page: Chapter kit",
 "A Workshops page for a teacher who also teaches in person: a heading, the cities with a map, the next dates, a card for each city linking to its own page, and a closing band. Chapter kit.",
 "workshops, in person, cities, dates, locations, chapter",
 [cpage_hero("In-person workshops", "Two days of drawing from life with twelve people and Mara, in six cities a year.", "Workshops", [("Save a place", None, CJOIN)]),
  BODIES["chapter-workshops-map"], BODIES["chapter-workshop-dates"],
  sec("Cities", grid([card(N([h(t, 3, "large"), p(f"Weekend workshops in {t}, once or twice a year.", None, "secondary"), link_p(f"Workshops in {t}", f"/workshops/{s}/", None, {"fontWeight": "700"})]), "section-card") for t, s, *_ in CITIES], 3, "15rem", "medium"), "section-tint"),
  BODIES["chapter-call"]])

chapter_page("chapter-page-area", "Workshop city page: Chapter kit (one city)",
 "A page for the workshops in one city, such as Portland: a heading, the weekend in a few lines with a map, the next dates, students' drawings and a closing band. Chapter kit; make one per city under Workshops.",
 "workshop, city, in person, location, dates, chapter",
 [cpage_hero("Portland", "Drawing weekends at the home studio, with a model, good coffee and twelve people at most.", "Workshops / Portland", [("Save a place", None, CJOIN)]),
  sec("Weekend", cols([
    col(N([h("A weekend at the studio", 2, "xx-large"),
           p("Two days, ten till four, in the studio where the courses are filmed. Saturday is gesture and proportion with a model; Sunday we draw faces in the morning and go out to sketch the neighbourhood after lunch."),
           lst(["Twelve places, so everyone gets time with Mara", "Paper, boards and lunch included", "$290 for the weekend, $240 for members"], "medium")]), "50%"),
    col(mapb("Portland, Oregon", 45.5221, -122.6610, 14, "4/3"))], "x-large", "wide", "top")),
  BODIES["chapter-workshop-dates"], BODIES["chapter-gallery"], BODIES["chapter-call"]])

chapter_page("chapter-page-offers", "Offers page: Chapter kit",
 "An Offers page for an online school: a heading, offers with the small print, the weekly prompt email and a closing band. Chapter kit; keep the offers current.",
 "offers, discounts, gift cards, bundle, free lesson, chapter",
 [cpage_hero("Offers and gifts", "A free first lesson, gift cards and a bundle of three courses.", "Offers"),
  BODIES["chapter-offers"], BODIES["chapter-signup"], BODIES["chapter-call"]])

chapter_page("chapter-page-join", "Join page: Chapter kit",
 "A Join page: a heading, the two ways to join, a form to save a place or ask a question, how it works and common questions. Chapter kit; put the site's form in the named Form group.",
 "join, enrol, sign up, pricing, buy, chapter",
 [cpage_hero("Join a course", "Pay once for a course, or join the community for every course and weekly feedback.", "Join"),
  BODIES["chapter-pricing"], BODIES["chapter-join-form"], BODIES["chapter-steps"], BODIES["chapter-faq"]])

chapter_page("chapter-page-faq", "Questions page: Chapter kit",
 "A Questions page for an online school: answers that open and close, grouped into the courses, the community, workshops and payment, and a closing band. Chapter kit; answer with the school's real rules.",
 "faq, questions, answers, help, refund, chapter",
 [cpage_hero("Questions and answers", "Straight answers about the courses, the community and the workshops.", "FAQ"),
  sec("Questions", N([N([h(group_t, 2, "xx-large"), accordion(qs)]) for group_t, qs in [
    ("The courses", [
      ("I can't draw at all. Is it for me?", "Yes. Most students start from stick figures. The first week is about looking, not talent."),
      ("How long do I have the lessons?", "For life. Watch them as often as you like, and get every update free."),
      ("What do I need?", "A pencil, an eraser and cheap paper. Each course lists anything extra, such as a small watercolour set."),
      ("Can I watch on my phone?", "Yes, on any phone, tablet or computer, and you can download lessons to watch offline.")]),
    ("The community", [
      ("What's the difference from buying a course?", "The community adds feedback on your drawings, two live sessions a week, monthly challenges and every course."),
      ("Can I cancel?", "Any time, in two clicks. You keep any course you bought separately.")]),
    ("Workshops", [
      ("Do I need to have done a course?", "No. Everyone's welcome, and we pair up beginners with more experienced students."),
      ("What if I can't come?", "Cancel up to two weeks before for a full refund, or move to another weekend any time.")]),
    ("Payment", [
      ("What's your refund policy?", "Thirty days, every cent, no questions asked."),
      ("Can I pay in instalments?", "Yes, for Draw people in 30 days: three payments of $50.")])]]),
    content="56rem"),
  BODIES["chapter-call"]])

chapter_page("chapter-page-careers", "Teach with us page: Chapter kit",
 "A Teach with us page for an online school: a heading, why people teach there, the open roles with the hours each takes, the application form and how the courses work. Chapter kit; keep the roles current and put the site's form in the named Form group.",
 "careers, jobs, teach, teaching assistant, apply, chapter",
 [cpage_hero("Teach with us", "We're looking for illustrators who love helping beginners. Online, part-time, paid fairly.", "Teach with us", [("See open roles", None, "#apply")]),
  BODIES["chapter-teach"], BODIES["chapter-teacher"]])

chapter_page("chapter-page-contact", "Contact page: Chapter kit",
 "A Contact page for an online school: a heading, the phone number, email, studio address and hours beside the contact form, a map, and a closing band. Chapter kit; put the site's contact form in the named Form group.",
 "contact, contact us, phone, email, studio, map, chapter",
 [cpage_hero("Contact us", "Questions about a course, the community or a workshop? Call, text or write.", "Contact"),
  BODIES["chapter-contact"], BODIES["chapter-call"]])

chapter_page("chapter-page-thanks", "Thank-you page: Chapter kit",
 "The page visitors see after sending a form: thanks, what happens next and when, and links to keep reading. Chapter kit; send every form here.",
 "thank you, thanks, confirmation, form sent, chapter",
 [sec("Thanks", N([mono("Message sent", "primary-alt-accent"), h("Thank you. We'll be in touch soon.", 1, "xxx-large"),
    p("Mara or Sam will reply within one working day. Check your email for a copy of what you sent.", "large"),
    btns([("Back to the home page", None, "/"), ("See the courses", "outline", "/courses/")])]), "section-second-brand", ("xxx-large", "xxx-large", None, None), "56rem"),
  BODIES["chapter-stories"]])

print("chapter ok")
