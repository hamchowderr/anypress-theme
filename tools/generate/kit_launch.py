# Launch (0.10.0): a whole website for a software product, app or startup, written for an invoicing app for
# freelancers. Run by kits.py after kit_chapter.py, so every helper in kits.py, kits_more.py, kit_ridge.py,
# kit_commons.py and kit_chapter.py is in scope.
#
# A changelog: one grotesk at every size, green on paper, labels in mono. Pages link to each other by slug: /features/
# and one page per feature under it, /customers/, /for/ and one page per kind of customer under it, /pricing/,
# /integrations/, /changelog/, /about/, /demo/, /faq/, /careers/, /blog/, /contact/, /thank-you/. Forms are named
# groups, as in Ridge: "Form: quote" books a demo, "Form: apply" is the job application.

K = "anypress/kit-software"
LF = "schibsted-grotesk"
LPHONE = "555 0119"
LTEL = "tel:5550119"
LSTART = "/pricing/"
LDEMO = "/demo/"
LADDRESS = "Rua da Prata 80, Lisbon"
LBIG = {"lineHeight": "1", "fontWeight": "800", "letterSpacing": "-0.03em"}

def limg(alt, ratio="16/10", file="placeholder-wide.svg"):
    return img(file, alt, ratio)

def ltel(size="xx-large"):
    return p(f'<a href="{LTEL}">' + T(LPHONE) + '</a>', size, None, None, LF, LBIG, raw=True, bind="phone_linked")

def lhead(eb, title, link=None, size="xxx-large"):
    left = stackg([mono(eb, "primary"), h(title, 2, size)])
    return row([left, btns([(link[0], "outline", link[1])])] if link else [left], valign="bottom")

def l_buttons():
    """The header's buttons: talk to sales and Start free on tablets and computers, just "Call" on phones."""
    start = f'<!-- wp:button {j({"metadata": {"blockVisibility": {"viewport": {"mobile": False}}}})} -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{LSTART}">{T("Start free")}</a></div>\n<!-- /wp:button -->'
    call = f'<!-- wp:button {j({"className": "is-style-outline", "metadata": {"blockVisibility": {"viewport": {"mobile": False}}, "bindings": button_bindings("phone")}})} -->\n<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="{LTEL}">{T(LPHONE)}</a></div>\n<!-- /wp:button -->'
    short = f'<!-- wp:button {j({"metadata": {"blockVisibility": {"viewport": {"tablet": False, "desktop": False}}, "bindings": button_bindings("phone_link")}})} -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{LTEL}">{T("Call")}</a></div>\n<!-- /wp:button -->'
    return '<!-- wp:buttons {"layout":{"type":"flex","flexWrap":"nowrap"}} -->\n<div class="wp-block-buttons">' + N([call, start, short]) + '</div>\n<!-- /wp:buttons -->'

def lpage_hero(title, text, crumb=None, buttons=None, alt=None):
    words = N(([mono(crumb, "primary")] if crumb else []) + [h(title, 1, "xxx-large"), p(text, "large", "secondary")] + ([btns(buttons)] if buttons else []))
    if not alt:
        return sec("Page hero", grp(words, gap="medium", layout={"type": "constrained", "contentSize": "48rem", "justifyContent": "left"}), None, ("xx-large", "x-large", None, None), "72rem")
    return sec("Page hero", cols([col(words, "50%", valign="center"), col(limg(alt, "4/3"))], "x-large", "wide", "center"), None, ("xx-large", "x-large", None, None), "72rem")

# ---------------------------------------------------------------- content
FEATURES = [
    ("Invoices", "invoices", "Pick the client, add the hours, send. Your logo and payment details are already on it.", "A freelancer typing on a laptop at a wooden desk"),
    ("Reminders", "reminders", "Late payers get a friendly nudge at 3, 7 and 14 days, in your words.", "A phone on a desk showing a new message"),
    ("Payments", "payments", "Clients pay by card or bank from the invoice. Money lands in your account in two days.", "Someone paying with a card on a laptop"),
    ("Tax", "tax", "See what to save for tax from every payment, as you go, and never dread April again.", "A calculator, a notebook and receipts on a desk"),
    ("Bank matching", "bank-matching", "Payments match themselves to invoices. No spreadsheets, no guessing who paid.", "Two people looking at charts on a laptop screen"),
    ("For accountants", "accountants", "Give your accountant read-only access at year end, and skip the shoebox of receipts.", "An accountant working through papers with a pen"),
]
AUDIENCES = [("Designers", "designers"), ("Developers", "developers"), ("Photographers", "photographers"), ("Writers", "writers"), ("Consultants", "consultants"), ("Small studios", "studios")]
LSTORIES = [
    ("I used to spend every other Friday chasing invoices. Now the reminders do it and I just get paid.", "Ines Ferreira", "Brand designer"),
    ("Moving from spreadsheets took ten minutes. My accountant actually thanked me this year.", "Sam Okoye", "Freelance developer"),
    ("The tax figure on every payment changed how I sleep. I know exactly what's mine.", "Lucy Chen", "Photographer"),
    ("We're four people now and still on Tally. Shared clients and approvals keep it tidy.", "Marco Rossi", "Northwind Studio"),
    ("Clients pay faster when they can tap a card. Average time to paid went from 31 days to 9.", "Aisha Bello", "Copywriter"),
    ("Support answered in eleven minutes, on a Sunday. From a real person who knew invoicing.", "Tom Hale", "Consultant"),
]

def lstory(text, name, role, size="medium"):
    return card(N([p("“" + text + "”", size, None, None, None, {"lineHeight": "1.4"}), p(f"{name}, {role}", "small", "secondary", None, None, {"fontWeight": "700"})]), "section-card")

# ---------------------------------------------------------------- sections
kit("launch-topbar", K, "Launch top bar: what's new and the sales number",
 "A thin dark bar above the header with the latest product news and a link to the changelog, and a number for sales. Part of the Launch kit; keep the news current.",
 "top bar, announcement, news, changelog, phone, header, launch",
 grp(row([p(T("New: bank matching now works with 2,400 banks") + ' · <a href="/changelog/">' + T("What's new") + '</a>', "small", None, None, None, None, raw=True),
          hide_on(p(T("Talk to sales") + f' <a href="{LTEL}">' + T(LPHONE) + '</a>', "small", None, None, None, None, raw=True), "mobile")], gap="small"),
     "section-dark", ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Top bar"))

LHEADER = grp(N([
    BODIES["launch-topbar"],
    grp(row([
        row([dyn("site-logo", {"width": 36, "shouldSyncIcon": True}), dyn("site-title", {"level": 0, "fontSize": "large", "fontFamily": LF, "style": {"typography": {"lineHeight": "1", "fontWeight": "800", "letterSpacing": "-0.03em"}}})], "left", "small", False, "center"),
        row([dyn("navigation", {"overlayMenu": "mobile", "layout": {"type": "flex", "justifyContent": "right"}, "style": {"typography": {"fontWeight": "600"}}}),
             l_buttons()], "right", "medium", False, "center")], "space-between", "medium", False, "center"),
        None, ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Main bar").replace(
        '<!-- wp:group {', '<!-- wp:group {"backgroundColor":"base",', 1).replace('class="wp-block-group alignfull', 'class="wp-block-group alignfull has-base-background-color has-background', 1),
]), "sticky", None, "0", {"type": "default"}, align="full", name="Header")
write("launch-header", "Launch header: news, menu and a Start free button",
 "A site header for a software product, app or startup that stays at the top while visitors scroll: a dark bar with the latest news and the sales number, then the logo, the menu (with dropdowns for features and who it's for), the phone number and a Start free button. Part of the Launch kit; choose it for the header in the Site Editor.",
 "header", "header, menu, navigation, sticky, sign up, phone, saas, launch", LHEADER, "core/template-part/header")

kit("launch-numbers", K, "Launch numbers: four figures that count up",
 "Four big numbers that count up as they scroll into view (customers, money handled, days faster, uptime), each with a short label. Needs the AnyPress Blocks plugin. Part of the Launch kit; use real figures only.",
 "numbers, statistics, counter, metrics, results, launch",
 sec("Numbers", grid([stackg([counter(n, suf, pre, "xx-large", LF, d), p(lbl, "medium", "secondary")]) for n, suf, pre, d, lbl in
     [(3000, "+", "", 0, "studios and freelancers"), (48, "M", "$", 0, "invoiced through Tally last year"), (22, " days", "", 0, "sooner paid, on average"), (99.98, "%", "", 2, "uptime over the last year")]], 4, "14rem", "x-large")))

kit("launch-stories", K, "Launch customer stories: a carousel of quotes",
 "Customers in their own words, in a carousel, three at a time on a computer and one on a phone, with each customer's name and work. Needs the AnyPress Blocks plugin. Part of the Launch kit; use real quotes, with permission.",
 "testimonials, customer stories, reviews, quotes, carousel, launch",
 sec("Customer stories", N([lhead("Customer stories", "Freelancers who stopped chasing", ("All stories", "/customers/")),
                            carousel([lstory(*s) for s in LSTORIES], 3, "Customer stories")]), "section-tint"))

kit("launch-screens", K, "Launch screens: the app in pictures",
 "Pictures of the product in a carousel, each opening full screen when clicked, with a caption saying what it shows. Needs the AnyPress Blocks plugin. Part of the Launch kit; use real screenshots.",
 "screenshots, gallery, product tour, carousel, lightbox, launch",
 sec("Screens", N([lhead("A closer look", "See it at work"), carousel([stackg([zoom(limg(alt, "16/10")), p(cap, None, "secondary")]) for alt, cap in [
    ("A freelancer typing on a laptop at a wooden desk", "Write an invoice from your last week's hours"),
    ("Someone paying with a card on a laptop", "Your client's payment page, with card and bank"),
    ("Two people looking at charts on a laptop screen", "Every payment matched to its invoice"),
    ("A calculator, a notebook and receipts on a desk", "What to set aside for tax, month by month"),
    ("A phone on a desk showing a new message", "A reminder, sent in your words")]], 2, "Pictures of the app", 6)])))

kit("launch-office", K, "Launch office: where the team is, with a map",
 "Where the company works, with a few lines about the team and its support hours beside a map. Needs the AnyPress Blocks plugin for the map. Part of the Launch kit.",
 "office, team, support, location, map, about, launch",
 sec("Office", cols([
   col(N([mono("Real people", "primary"), h("Made in Lisbon, used in 40 countries", 2, "xxx-large"),
          p("Fourteen of us in a small office by the river, plus support in three time zones. When you write, a person who knows invoicing writes back, usually within the hour.", "medium", "secondary"),
          lst(["Support every day, 7am to midnight UK time", "Sales calls on weekdays", "Visitors welcome; book first"]),
          btns([("Talk to us", "outline", "/contact/")])]), "40%"),
   col(mapb(LADDRESS + ", Portugal", 38.7092, -9.1366, 15, "4/3"))], "x-large", "wide", "center")))

kit("launch-faq-open", K, "Launch questions: answers that open and close",
 "The questions people ask before signing up, as answers that open and close, beside a heading and a link to all questions. Part of the Launch kit; answer the real questions from sales and support.",
 "faq, questions, answers, accordion, support, launch",
 sec("Questions", cols([
   col(N([mono("Questions", "primary"), h("Before you sign up", 2, "xxx-large"), p("Can't see yours? Ask in the chat or call sales. A person answers.", "medium", "secondary"), btns([("All questions", "outline", "/faq/")])]), "36%"),
   col(accordion([
     ("Is my data safe?", "Your data is encrypted, backed up every day and never sold. You can export or delete it at any time."),
     ("Can I import my old invoices?", "Yes. Upload a spreadsheet or connect your old tool and we bring everything across."),
     ("What happens when the trial ends?", "You choose a plan or stay on Free. Nothing is deleted."),
     ("Do you take a cut of payments?", "No. Card payments cost the processor's fee, and bank payments are free."),
     ("Can I cancel any time?", "Yes, in two clicks, and you keep your invoices to download.")]))], "x-large", "wide", "top")))

kit("launch-signup", K, "Launch signup: the monthly email",
 "A band asking visitors to join a monthly email with tips and product news, with the signup form beside it. Part of the Launch kit; sits above the footer on every page.",
 "newsletter, signup, email, tips, subscribe, launch",
 sec("Signup", cols([
   col(N([h("Money tips for freelancers, once a month", 2, "xx-large"), p("Pricing, late payers, tax and the odd new feature. 18,000 freelancers read it. Unsubscribe any time.", "medium", "secondary")]), "55%", valign="center"),
   col(form("newsletter", "Read past issues", "/blog/"), valign="center")], "large", "wide", "center"), "section-tint", ("x-large", "x-large", None, None)))

LPOPUP = popup("offer", N([
    img("placeholder-wide.svg", "A freelancer typing on a laptop at a wooden desk", "16/9"),
    grp(N([mono("Switching from another tool?", "primary"), h("Three months of Pro, free", 2, "xx-large"),
           p("Leave your email and we'll send a code for three months of Pro, plus a guide to moving your clients across in ten minutes."),
           form("offer", "See pricing", LSTART)]), None, (None, None, "large", "large"), "small", {"type": "default"})]),
    label="Three months of Pro free")
kit("launch-popup", K, "Launch popup: three months free for switchers",
 "A popup that opens five seconds into a first visit with a picture, an offer for people switching tools and one field for an email address; it closes with its button, Escape or a click outside and stays closed for two weeks. Needs the AnyPress Blocks plugin. Part of the Launch kit; put it in the footer to show it on every page.",
 "popup, offer, trial, discount, newsletter, email, modal, launch", LPOPUP)

LFOOTER = grp(N([
    BODIES["launch-signup"],
    grp(N([cols([
        col(N([dyn("site-title", {"level": 0, "fontSize": "x-large", "fontFamily": LF, "style": {"typography": {"fontWeight": "800", "letterSpacing": "-0.03em"}}}),
               p("Invoicing for freelancers and small studios. Send the invoice, get paid, get back to work.", None, "main-accent"),
               ltel("xx-large"), social(["x", "linkedin", "youtube"])]), "34%"),
        col(flinks("Product", [(n, f"/features/{s}/") for n, s, *_ in FEATURES] + [("Integrations", "/integrations/"), ("What's new", "/changelog/")])),
        col(flinks("Company", [("About", "/about/"), ("Customer stories", "/customers/"), ("Who it's for", "/for/"), ("Pricing", "/pricing/"), ("Careers", "/careers/"), ("Blog", "/blog/"), ("Questions", "/faq/"), ("Contact", "/contact/")])),
        col(N([h("Talk to us", 3, "medium"), p(LADDRESS, None, "main-accent", bind="address"), p("Support every day, 7am to midnight", None, "main-accent", bind="hours"),
               btns([("Book a demo", None, LDEMO)])]))], "large", "wide", "top"),
        sep(),
        row([p("© Tally. Card payments by our payment partner; we never see your card numbers.", "small", "main-accent"),
             p('<a href="/privacy-policy/">' + T("Privacy") + '</a> · <a href="/contact/">' + T("Contact") + '</a>', "small", "main-accent", None, None, None, raw=True)], gap="small")]),
        "section-dark", ("x-large", "large", None, None), "large", {"type": "constrained", "contentSize": "80rem"}, align="full", name="Footer columns"),
    LPOPUP,
]), None, None, "0", {"type": "default"}, align="full", name="Footer")
write("launch-footer", "Launch footer: monthly email, product links and the switcher offer",
 "A site footer for a software product, app or startup: a band for the monthly email, then the phone number, product and company links and the office on dark, and the switcher offer popup (needs the AnyPress Blocks plugin). Part of the Launch kit; choose it for the footer in the Site Editor.",
 "footer", "footer, links, newsletter, signup, phone, popup, saas, launch", LFOOTER, "core/template-part/footer")

kit("launch-feature-detail", K, "Launch feature: how one feature works",
 "The body of one feature page: what it does in plain words, a list of the details people ask about, a picture, and a box with the plan it comes on and buttons to start or book a demo. Part of the Launch kit.",
 "feature, details, how it works, product, plan, launch",
 sec("Feature details", cols([
   col(N([h("How it works", 2, "xx-large"),
          p("Open a client, add the hours or items, and press send. Tally fills in your details, numbers the invoice, adds the tax and gives your client a page where they can pay by card or bank."),
          lst(["Templates with your logo, colours and payment terms", "Hours from your timer or a spreadsheet", "Any currency, with the rate on the day", "Invoices numbered the way your accountant wants", "A copy as a PDF for your records"], "medium"),
          zoom(limg("This feature: an invoice being written in the app", "16/10"))]), "60%"),
   col(card(N([mono("Invoices", "primary"), p("On every plan", "xx-large", None, None, LF, LBIG),
               p("Free for your first ten clients. Pro from $12 a month for unlimited clients."),
               btns([("Start free", None, LSTART), ("Book a demo", "outline", LDEMO)])]), "section-brand-soft", PAD_CARD))], "x-large", "wide", "top")))

kit("launch-audience", K, "Launch audience: how one kind of customer uses it",
 "The body of a page for one kind of customer, such as designers: three things that matter to them, each with a heading and a line, and a quote from one of them. Part of the Launch kit; for pages under Who it's for.",
 "audience, use case, solutions, customers, industry, launch",
 sec("For you", N([cols([col(h("Built for how designers get paid", 2, "xxx-large"), "55%"), col(p("Deposits, stages and the endless last round of changes: Tally handles the money side of design work.", "large", "secondary"), None, None, None, "bottom")], "x-large", "wide", "bottom"),
   grid([feat("01", "Deposits and stages", "Invoice 50% up front and the rest on delivery, from one project."),
         feat("02", "Extra rounds, billed", "Add a line for the extra round of changes in a click, with your rate already on it."),
         feat("03", "Clients abroad", "Bill in their currency and get paid in yours, at a fair rate.")], 3, "16rem", "x-large"),
   lstory("I invoice a deposit before I open Figma now. It changed how clients treat my time.", "Ines Ferreira", "Brand designer", "large")])))

kit("launch-plans", K, "Launch plans: compare every plan",
 "Every plan compared feature by feature in a table, under the plan cards, with a note on trials and refunds. Part of the Launch kit; for the Pricing page, matched to the real plans.",
 "pricing, compare plans, table, features, saas, launch",
 sec("Compare", N([h("Compare the plans", 2, "xx-large"),
   '<!-- wp:table {"className":"is-style-stripes"} -->\n<figure class="wp-block-table is-style-stripes"><table class="has-fixed-layout"><thead><tr><th>' + T("Feature") + '</th><th>' + T("Free") + '</th><th>' + T("Pro") + '</th><th>' + T("Team") + '</th></tr></thead><tbody>'
   + "".join(f"<tr><td>{T(a)}</td><td>{T(b)}</td><td>{T(c)}</td><td>{T(d)}</td></tr>" for a, b, c, d in [
       ("Clients", "Up to 10", "Unlimited", "Unlimited"), ("Card and bank payments", "Yes", "Yes", "Yes"), ("Reminders", "Yes", "Yes", "Yes"),
       ("Tax set aside", "No", "Yes", "Yes"), ("Bank matching", "No", "Yes", "Yes"), ("Your own domain on invoices", "No", "Yes", "Yes"),
       ("People", "1", "1", "Up to 10"), ("Shared clients and approvals", "No", "No", "Yes"), ("Support", "Email", "Email and chat", "Email, chat and phone")])
   + '</tbody></table></figure>\n<!-- /wp:table -->',
   p("Every paid plan starts with a 30-day free trial, no card needed. Pay yearly and get two months free.", None, "secondary")]), content="64rem"))

kit("launch-deals", K, "Launch offers: ways to pay less",
 "Three offers as cards with the saving in large type, who it's for and a button: switching from another tool, paying yearly, and nonprofits or students. Part of the Launch kit; keep the offers current.",
 "offers, discounts, deals, yearly, switch, nonprofit, launch",
 sec("Offers", N([lhead("Ways to pay less", "Offers"), grid([card(N([p(s, "xx-large", None, None, LF, LBIG), h(t, 3, "large"), p(d), btns([(b, None, l)])]), st, PAD_CARD) for s, t, d, b, l, st in [
    ("3 months", "Free for switchers", "Moving from another invoicing tool? Get three months of Pro free, and we'll move your clients for you.", "Claim the offer", LDEMO, "section-brand-soft"),
    ("2 months", "Free when you pay yearly", "Pay for a year of Pro or Team and get two months free, with a refund on unused months if you leave.", "Start a free trial", LSTART, "section-card"),
    ("50% off", "Students and nonprofits", "Half price on Pro for as long as you're studying or running a registered nonprofit.", "Ask about it", "/contact/", "section-brand-soft")]], 3, "16rem", "medium")]), "section-tint"))

kit("launch-integrations", K, "Launch integrations: the tools it works with",
 "The tools the product connects to, as a grid of cards with the tool's name in large type and what it does with it. Part of the Launch kit; only list integrations that exist.",
 "integrations, apps, connect, tools, partners, launch",
 sec("Integrations", N([lhead("Works with", "The tools you already use"), grid([card(N([p(n, "x-large", None, None, LF, LBIG), p(d, None, "secondary")]), "section-card") for n, d in [
    ("Your bank", "Payments match themselves to invoices, with read-only access to 2,400 banks."),
    ("Calendar", "Turn the hours in your calendar into lines on an invoice."),
    ("Time trackers", "Bring hours in from the timer you already use."),
    ("Accounting software", "Send paid invoices and fees to your accountant's software every night."),
    ("Email", "Invoices and reminders go from your own address, not ours."),
    ("Zapier and Make", "Connect Tally to thousands of other apps without code.")]], 3, "16rem", "medium")])))

kit("launch-changelog", K, "Launch changelog: what's new, newest first",
 "Recent product updates as a list, newest first, each with a date label, a heading and a line on what changed. Part of the Launch kit; for the What's new page.",
 "changelog, updates, release notes, what's new, product, launch",
 sec("Changelog", N([stackg([cols([col(mono(d, "primary"), "10rem"), col(stackg([h(t, 3, "large"), p(x, None, "secondary")], "x-small"))], "large", None, "top", False) for d, t, x in [
    ("4 Nov", "Bank matching for 2,400 banks", "Banks in the UK, Ireland and Portugal join the US and Canada. Payments now match in under a minute."),
    ("21 Oct", "Deposits and stages", "Split one project into a deposit and stage payments, and invoice each when it's due."),
    ("2 Oct", "Reminders in your words", "Write your own reminder emails, or pick from three tones: gentle, firm and final."),
    ("15 Sep", "Faster payment pages", "Your clients' payment page now loads in half the time and remembers their card if they want."),
    ("28 Aug", "Tax for Portugal and Ireland", "The tax set-aside figure now knows the rules in two more countries.")]], "x-large")]), content="56rem"))

kit("launch-jobs", K, "Launch careers: why work here and the open roles",
 "Why people work at the company, each open role with where and how much, and the application. Part of the Launch kit; keep the roles current and put the site's application form in the named Form group.",
 "careers, jobs, hiring, roles, apply, team, launch",
 sec("Careers", N([
   lhead("Why work here", "Small team, real customers"),
   grid([stackg([h(t, 3, "large"), p(d, None, "secondary")]) for t, d in [
     ("Remote or Lisbon", "Work from home anywhere in Europe, or from the office by the river."),
     ("Four-day weeks in August", "Every Friday off in August, paid."),
     ("Salaries in the open", "Every salary band is on this page, and the same for everyone in a role."),
     ("A budget to learn", "$1,500 a year for books, courses and conferences.")]], 4, "13rem"),
   '<!-- wp:spacer {"height":"var:preset|spacing|large"} -->\n<div style="height:var(--wp--preset--spacing--large)" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->',
   h("Open roles", 2, "xx-large"),
   N([card(N([row([h(t, 3, "large"), p(when, None, None, None, None, {"fontWeight": "700"})], valign="center"), p(d, None, "secondary"), btns([("Apply for this", None, "#apply")])]), "section-tint") for t, when, d in [
     ("Senior product engineer", "Remote, €70k to €85k", "Build the features freelancers use every day, from payments to reminders, in TypeScript and Postgres."),
     ("Customer support lead", "Lisbon, €45k to €55k", "Lead a team of five and keep our replies under an hour, every day of the week."),
     ("Product designer", "Remote, €60k to €72k", "Design the app and the invoices our customers' clients see, with a lot of say in both.")]]),
   grp(N([h("Apply", 2, "xx-large"), p("Tell us who you are, the role you'd like and a link to your work or CV. We reply to everyone within a week."),
          form("apply", "Email the team", "mailto:jobs@example.com")]), "section-card", PAD_CARD, "small", {"type": "default"}, anchor="apply")])))

kit("launch-demo-form", K, "Launch demo: book a call",
 "A form to book a demo call, beside what happens on the call and a card offering the free plan instead. Part of the Launch kit; put the site's form in the named Form group.",
 "demo, book a call, sales, contact sales, form, launch",
 sec("Apply", cols([
   col(card(N([h("Book a 20-minute demo", 2, "xx-large"), p("Tell us a little about your work and pick a day. We'll send a calendar invite within one working day."),
               form("quote", "Call " + LPHONE, LTEL, "Prefer to talk now? Call sales.")]), "section-card", PAD_CARD), "58%"),
   col(N([h("On the call", 3, "x-large"),
          lst(["A tour of the parts that matter to you", "Your questions about moving from another tool", "An honest answer on which plan fits"], "medium"),
          card(N([mono("Rather just try it?", "primary"), h("Start on the free plan", 3, "large"), p("Free for your first ten clients, no card needed."), btns([("Start free", "outline", LSTART)])]), "section-brand-soft")]))],
   "x-large", "wide", "top"), "section-tint"))

kit("launch-contact", K, "Launch contact: support, sales and the office",
 "A contact section for a software company: the sales number, support email, office address and support hours beside the contact form, then a map. Needs the AnyPress Blocks plugin for the map. Part of the Launch kit.",
 "contact, support, sales, email, office, map, form, launch",
 sec("Contact", N([cols([
   col(N([h("Talk to a person", 2, "xx-large"), ltel("xxx-large"),
          p('<a href="mailto:hello@example.com">hello@example.com</a>', "medium", None, None, None, None, raw=True, bind="email_linked"),
          p(LADDRESS, "medium", bind="address"), p("Support every day, 7am to midnight UK time. Sales on weekdays.", None, "secondary")]), "42%"),
   col(card(N([h("Send a message", 3, "x-large"), form("contact", "Call " + LPHONE, LTEL, "We reply within the hour during support hours.")]), "section-tint", PAD_CARD))], "x-large", "wide", "top"),
   mapb(LADDRESS + ", Portugal", 38.7092, -9.1366, 15, "21/9")])))

# The home page: numbers, stories, screens, the office and open questions join the original sections.
kit_page("kit-software", "Home page: Launch kit, startup and software",
 "A complete home page for a software product, app or startup in the Launch kit: what the product does with a screenshot, customer names, numbers that count up, six features, three steps, customer stories in a carousel, pricing, the team with a map, questions and a sign-up close. Apply the Launch style for the look it was designed with.",
 "home, saas, software, app, startup, product, pricing, kit, launch",
 ["launch-hero", "launch-logos", "launch-numbers", "launch-features", "launch-steps", "launch-stories", "launch-pricing", "launch-office", "launch-faq-open", "launch-cta"])

# ---------------------------------------------------------------- pages
def launch_page(slug, title, desc, kw, parts):
    write(slug, title, desc, "anypress/pages", kw, N(parts), "core/post-content", " * Post Types: page\n")

launch_page("launch-page-services", "Features page: Launch kit",
 "A Features page for a software product: a heading, every feature with a link to its own page, the app in pictures, how to start, customer stories and a sign-up close. Launch kit.",
 "features, product, tour, what it does, launch",
 [lpage_hero("Everything after you finish the work", "Invoices, reminders, payments, tax and your bank, in one place. Here's what each part does.", "Features", [("Start free", None, LSTART), ("Book a demo", "outline", LDEMO)]),
  sec("All features", grid([stackg([sep(), mono(f"0{i + 1}", "primary"), h(n, 3, "large"), p(d, None, "secondary"), link_p(f"More about {n.lower()} →", f"/features/{s}/", None, {"fontWeight": "700"})], "small") for i, (n, s, d, _) in enumerate(FEATURES)], 3, "16rem", "x-large")),
  BODIES["launch-screens"], BODIES["launch-steps"], BODIES["launch-stories"], BODIES["launch-cta"]])

launch_page("launch-page-service", "Feature page: Launch kit (one feature)",
 "A page for one feature, such as invoices: a heading with a picture, how it works and which plans have it, the app in pictures, customer stories, questions about this feature and a sign-up close. Launch kit; make one per feature under Features.",
 "feature page, single feature, how it works, product, launch",
 [lpage_hero("Invoices", "Pick the client, add the hours, send. Your logo and payment details are already on it.", "Features / Invoices", [("Start free", None, LSTART), ("Book a demo", "outline", LDEMO)], "This feature: a freelancer typing on a laptop at a wooden desk"),
  BODIES["launch-feature-detail"], BODIES["launch-screens"], BODIES["launch-stories"],
  sec("Questions", cols([col(h("About this feature", 2, "xx-large"), "36%"), col(accordion([
    ("Can I use my own invoice numbers?", "Yes. Start from any number, add a prefix, or reset each year."),
    ("Can I invoice in another currency?", "Yes, in any of 40 currencies, with the exchange rate on the day you send."),
    ("Can I send invoices from my own email?", "Yes, on Pro and Team. Clients see your address, not ours."),
    ("What does my client see?", "A clean page with your logo, the invoice and buttons to pay by card or bank.")]))], "x-large", "wide", "top")),
  BODIES["launch-cta"]])

launch_page("launch-page-about", "About page: Launch kit",
 "An About page for a software company: a heading, the story with a picture, numbers that count up, the team with a map and a sign-up close. Launch kit.",
 "about, about us, story, team, company, launch",
 [lpage_hero("We built the invoicing tool we wanted", "Tally started as a spreadsheet for two freelancers who hated chasing money. Now 3,000 studios and freelancers use it.", "About"),
  sec("Story", cols([
    col(N([h("Fourteen people, one job", 2, "xxx-large"),
           p("Rita and Joel were a designer and a developer who spent more time chasing invoices than doing the work. In 2021 they turned their spreadsheet into an app for their friends, and their friends told their friends.", "large"),
           p("Today we're fourteen people in Lisbon and three other countries. We're paid for by our customers, not investors, so we build what freelancers ask for and nothing that gets in their way."),
           p("We read every message, and the roadmap is mostly what you've asked for.")]), "50%", valign="center"),
    col(limg("Two people looking at charts on a laptop screen", "4/5", "placeholder-tall.svg"))], "x-large", "wide", "center")),
  BODIES["launch-numbers"], BODIES["launch-office"], BODIES["launch-cta"]])

launch_page("launch-page-reviews", "Customer stories page: Launch kit",
 "A Customer stories page: a heading, customers' quotes as cards with names and work, customer names, numbers that count up and a sign-up close. Launch kit; use real quotes, with permission.",
 "customer stories, testimonials, case studies, reviews, launch",
 [lpage_hero("Customer stories", "Freelancers and studios on what changed when they stopped chasing invoices.", "Customers", [("Start free", None, LSTART)]),
  sec("All stories", grid([lstory(*s) for s in LSTORIES + [
    ("Three clients paid the same day I sent the invoice. That never happened before.", "Priya Nair", "Illustrator"),
    ("The accountant login alone saves me a weekend every April.", "Ben Carter", "Video editor"),
    ("Clear pricing, no cut of payments, and it just works. That's all I wanted.", "Elena Petrova", "UX researcher")]], 3, "18rem", "medium"), "section-tint"),
  BODIES["launch-logos"], BODIES["launch-numbers"], BODIES["launch-cta"]])

launch_page("launch-page-areas", "Who it's for page: Launch kit",
 "A Who it's for page for a software product: a heading, a card for each kind of customer linking to its own page, customer stories and a sign-up close. Launch kit.",
 "who it's for, solutions, use cases, audiences, customers, launch",
 [lpage_hero("Who it's for", "Anyone who sends invoices for their own work, from a first client to a studio of ten.", "Who it's for"),
  sec("Audiences", grid([card(N([h(t, 3, "large"), p(f"How {t.lower()} use Tally to get paid sooner.", None, "secondary"), link_p(f"Tally for {t.lower()} →", f"/for/{s}/", None, {"fontWeight": "700"})]), "section-card") for t, s in AUDIENCES], 3, "15rem", "medium"), "section-tint"),
  BODIES["launch-stories"], BODIES["launch-cta"]])

launch_page("launch-page-area", "Audience page: Launch kit (one kind of customer)",
 "A page for one kind of customer, such as designers: a heading, what matters to them and how the product helps, the features they use most, a story and a sign-up close. Launch kit; make one per audience under Who it's for.",
 "audience, use case, solutions, industry, launch",
 [lpage_hero("Tally for designers", "Deposits, stages and clients abroad, without the awkward money emails.", "Who it's for / Designers", [("Start free", None, LSTART), ("Book a demo", "outline", LDEMO)]),
  BODIES["launch-audience"], BODIES["launch-features"], BODIES["launch-cta"]])

launch_page("launch-page-offers", "Pricing page: Launch kit",
 "A Pricing page for a software product: plan cards, every plan compared in a table, ways to pay less, questions and a sign-up close. Launch kit; match it to the real plans.",
 "pricing, plans, compare, offers, discounts, launch",
 [lpage_hero("Pricing", "Free for your first ten clients. Pro and Team when you grow. No cut of your payments, ever.", "Pricing"),
  BODIES["launch-pricing"], BODIES["launch-plans"], BODIES["launch-deals"], BODIES["launch-faq-open"], BODIES["launch-cta"]])

launch_page("launch-page-join", "Book a demo page: Launch kit",
 "A Book a demo page: a heading, the demo form with what happens on the call, customer names and how to start. Launch kit; put the site's form in the named Form group.",
 "demo, book a demo, sales, contact sales, launch",
 [lpage_hero("Book a demo", "Twenty minutes with a person who knows invoicing, at a time that suits you.", "Demo"),
  BODIES["launch-demo-form"], BODIES["launch-logos"], BODIES["launch-steps"]])

launch_page("launch-page-integrations", "Integrations page: Launch kit",
 "An Integrations page: a heading, the tools the product works with, how to start and a sign-up close. Launch kit.",
 "integrations, apps, connect, tools, launch",
 [lpage_hero("Integrations", "Tally fits in with the bank, calendar and accounting tools you already use.", "Integrations"),
  BODIES["launch-integrations"], BODIES["launch-steps"], BODIES["launch-cta"]])

launch_page("launch-page-changelog", "What's new page: Launch kit",
 "A What's new page: a heading, recent updates newest first, the monthly email and a sign-up close. Launch kit; add an entry for every release.",
 "changelog, what's new, updates, release notes, launch",
 [lpage_hero("What's new", "Every update to Tally, newest first. Most of them came from customers' ideas.", "Changelog"),
  BODIES["launch-changelog"], BODIES["launch-cta"]])

launch_page("launch-page-faq", "Questions page: Launch kit",
 "A Questions page for a software product: answers that open and close, grouped into getting started, payments, plans and billing, and your data, and a sign-up close. Launch kit; answer the real questions from sales and support.",
 "faq, questions, answers, help, support, launch",
 [lpage_hero("Questions and answers", "Straight answers about getting started, payments, plans and your data.", "FAQ"),
  sec("Questions", N([N([h(group_t, 2, "xx-large"), accordion(qs)]) for group_t, qs in [
    ("Getting started", [
      ("How long does it take to set up?", "About ten minutes: add your details and logo, import your clients and send your first invoice."),
      ("Can I import my old invoices?", "Yes. Upload a spreadsheet or connect your old tool and we bring everything across."),
      ("Is there an app?", "Yes, for iPhone and Android, as well as the web app.")]),
    ("Payments", [
      ("Do you take a cut of payments?", "No. Card payments cost the processor's fee, and bank payments are free."),
      ("How fast does money arrive?", "Card payments land in two working days, bank payments the same or next day.")]),
    ("Plans and billing", [
      ("What happens when the trial ends?", "You choose a plan or stay on Free. Nothing is deleted."),
      ("Can I cancel any time?", "Yes, in two clicks. You keep your invoices to download.")]),
    ("Your data", [
      ("Is my data safe?", "Your data is encrypted, backed up every day and never sold. You can export or delete it at any time."),
      ("Where is it stored?", "In the European Union, with backups in a second EU country.")])]]),
    content="56rem"),
  BODIES["launch-cta"]])

launch_page("launch-page-careers", "Careers page: Launch kit",
 "A Careers page for a software company: a heading, why people work there, the open roles with pay, the application form and the team with a map. Launch kit; keep the roles current and put the site's form in the named Form group.",
 "careers, jobs, hiring, team, apply, launch",
 [lpage_hero("Careers", "We're fourteen people building the tool freelancers wish they'd always had. Salaries are on this page.", "Careers", [("See open roles", None, "#apply")]),
  BODIES["launch-jobs"], BODIES["launch-office"]])

launch_page("launch-page-contact", "Contact page: Launch kit",
 "A Contact page for a software company: a heading, the sales number, support email, office and hours beside the contact form, a map, and a sign-up close. Launch kit; put the site's contact form in the named Form group.",
 "contact, support, sales, help, office, launch",
 [lpage_hero("Contact us", "Questions about Tally, your account or a demo? A person answers, usually within the hour.", "Contact"),
  BODIES["launch-contact"], BODIES["launch-cta"]])

launch_page("launch-page-thanks", "Thank-you page: Launch kit",
 "The page visitors see after sending a form: thanks, what happens next and when, and links to keep reading. Launch kit; send every form here.",
 "thank you, thanks, confirmation, form sent, launch",
 [sec("Thanks", N([mono("Message sent", "primary"), h("Thanks. We'll be in touch soon.", 1, "xxx-large"),
    p("A person on our team will reply within one working day, usually much sooner. Check your email for a copy of what you sent.", "large", "secondary"),
    btns([("Back to the home page", None, "/"), ("See the features", "outline", "/features/")])]), None, ("xxx-large", "xxx-large", None, None), "56rem"),
  BODIES["launch-stories"]])

print("launch ok")
