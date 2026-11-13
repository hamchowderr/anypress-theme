# Ledger (0.13.0): a whole website for an accountant, lawyer, consultant or agency, written for a small firm of
# accountants. Run by kits.py after kit_still.py, so every helper in kits.py, kits_more.py, kit_ridge.py and the kits
# before it is in scope.
#
# A report: a firm grotesk for headings, a serif for reading, teal on white and square buttons. Pages link to each
# other by slug: /services/ and one page per service under it, /book-a-call/, /team/, /industries/ and one page per
# industry under it, /about/, /clients/, /fees/, /careers/, /faq/, /insights/, /contact/, /thank-you/. Forms are named
# groups, as in Ridge: "Form: quote" books a free call, "Form: apply" is the job application.

LF2 = "libre-franklin"
LPH = "0113 555 0190"
LTL = "tel:01135550190"
LCALL = "/book-a-call/"
LADDR = "2 Park Square, Leeds LS1 2NE"
LLAT, LLON = 53.7993, -1.5545

def lsmall(text, color="primary"):
    return p(text, "small", color, None, LF2, {"fontWeight": "600", "letterSpacing": "0.04em", "textTransform": "uppercase"})

def ltel2(size="xx-large"):
    return p(f'<a href="{LTL}">' + T(LPH) + '</a>', size, None, None, LF2, {"fontWeight": "700", "lineHeight": "1.1"}, raw=True, bind="phone_linked")

def lhead2(eb, title, link=None, size="xx-large"):
    left = stackg([lsmall(eb), h(title, 2, size)])
    return row([left, btns([(link[0], "outline", link[1])])] if link else [left], valign="bottom")

def l2_buttons():
    """The header's buttons: the phone number and Book a free call on tablets and computers, just "Call" on phones."""
    book = f'<!-- wp:button {j({"metadata": {"blockVisibility": {"viewport": {"mobile": False}}}})} -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{LCALL}">{T("Book a free call")}</a></div>\n<!-- /wp:button -->'
    call = f'<!-- wp:button {j({"className": "is-style-outline", "metadata": {"blockVisibility": {"viewport": {"mobile": False}}, "bindings": button_bindings("phone")}})} -->\n<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="{LTL}">{T(LPH)}</a></div>\n<!-- /wp:button -->'
    short = f'<!-- wp:button {j({"metadata": {"blockVisibility": {"viewport": {"tablet": False, "desktop": False}}, "bindings": button_bindings("phone_link")}})} -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{LTL}">{T("Call")}</a></div>\n<!-- /wp:button -->'
    return '<!-- wp:buttons {"layout":{"type":"flex","flexWrap":"nowrap"}} -->\n<div class="wp-block-buttons">' + N([call, book, short]) + '</div>\n<!-- /wp:buttons -->'

def lpage_hero2(title, text, crumb=None, buttons=None, alt=None):
    words = N(([lsmall(crumb)] if crumb else []) + [h(title, 1, "xxx-large"), p(text, "large")] + ([btns(buttons)] if buttons else []))
    if not alt:
        return sec("Page hero", grp(words, gap="medium", layout={"type": "constrained", "contentSize": "48rem", "justifyContent": "left"}), "section-brand", ("xx-large", "xx-large", None, None), "72rem")
    return sec("Page hero", cols([col(words, "52%", valign="center"), col(img("placeholder-wide.svg", alt, "4/3"))], "xx-large", "wide", "center"), "section-brand", ("xx-large", "xx-large", None, None), "72rem")

# ---------------------------------------------------------------- content
LSERV = [
    ("Year-end accounts", "year-end-accounts", "Accounts and the company tax return, filed weeks before the deadline."),
    ("Bookkeeping and VAT", "bookkeeping-and-vat", "We keep the books in your software and file VAT every quarter."),
    ("Payroll", "payroll", "Payslips, pension and filings for teams of one to fifty."),
    ("Personal tax returns", "personal-tax", "Self-assessment for owners, landlords and anyone with untidy income."),
    ("Business advice", "business-advice", "Quarterly reviews, cash flow forecasts and a second opinion on big decisions."),
    ("Starting a business", "starting-a-business", "Sole trader or company, registered and set up properly from day one."),
]
LIND = [("Dentists", "dentists"), ("Builders and trades", "builders"), ("Restaurants and cafés", "restaurants"), ("Creative agencies", "creative-agencies")]
LSTORIES = [
    ("They found us eleven thousand pounds in the first year, and they explained how in plain English.", "Priya S.", "Owner, Northside Dental"),
    ("I used to dread January. Now my tax return is done by October and I know what I owe.", "Gary M.", "Electrician"),
    ("When we hired our tenth person, payroll just carried on. Nobody noticed, which is the point.", "Laura and Ben K.", "Two Pans Café"),
    ("Helen answers her own phone. After two firms where I never spoke to the same person twice, that's worth the fee alone.", "Sam T.", "Director, Tall Order Design"),
    ("They told us not to buy the van that year, and showed us why. They were right.", "Chris W.", "Wright Brothers Building"),
    ("Moving from our old accountant took one email from me. They did the rest.", "Aisha R.", "Physiotherapist"),
]

def lstory2(text, name, role, size="medium"):
    return grp(N([p("“" + text + "”", size, None, None, None, {"lineHeight": "1.4"}), p(f"{name}, {role}", "small", "secondary", None, LF2, {"fontWeight": "600"})]), "section-card", PAD_CARD, "medium", {"type": "default"})

# ---------------------------------------------------------------- sections
kit("ledger-topbar", L, "Ledger top bar: the next deadline and the phone number",
 "A thin bar above the header with the next tax deadline and a link to book a call, and the phone number. Part of the Ledger kit; keep the deadline current.",
 "top bar, announcement, deadline, phone, header, ledger",
 grp(row([p(T("Next deadline: tax returns due 31 January") + ' · <a href="/book-a-call/">' + T("Get it done early") + '</a>', "small", None, None, None, None, raw=True),
          hide_on(p(T("Call the office") + f' <a href="{LTL}">' + T(LPH) + '</a>', "small", None, None, None, None, raw=True), "mobile")], gap="small"),
     "section-dark", ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Top bar"))

LHEAD2 = grp(N([
    BODIES["ledger-topbar"],
    grp(row([
        row([dyn("site-logo", {"width": 36, "shouldSyncIcon": True}), dyn("site-title", {"level": 0, "fontSize": "large", "fontFamily": LF2, "style": {"typography": {"lineHeight": "1", "fontWeight": "700"}}})], "left", "small", False, "center"),
        row([dyn("navigation", {"overlayMenu": "mobile", "layout": {"type": "flex", "justifyContent": "right"}, "style": {"typography": {"fontWeight": "600"}}}),
             l2_buttons()], "right", "medium", False, "center")], "space-between", "medium", False, "center"),
        None, ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Main bar").replace(
        '<!-- wp:group {', '<!-- wp:group {"backgroundColor":"base",', 1).replace('class="wp-block-group alignfull', 'class="wp-block-group alignfull has-base-background-color has-background', 1),
]), "sticky", None, "0", {"type": "default"}, align="full", name="Header")
write("ledger-header", "Ledger header: next deadline, menu and a Book a call button",
 "A site header for an accountant, lawyer, consultant or agency that stays at the top while visitors scroll: a dark bar with the next deadline and the phone number, then the logo, the menu (with dropdowns for services and the firm), the phone number and a Book a free call button. Part of the Ledger kit; choose it for the header in the Site Editor.",
 "header", "header, menu, navigation, sticky, book a call, phone, accountant, ledger", LHEAD2, "core/template-part/header")

kit("ledger-numbers", L, "Ledger numbers: four figures that count up",
 "Four big numbers that count up as they scroll into view (clients, years, returns filed late, average saving), each with a short line. Needs the AnyPress Blocks plugin. Part of the Ledger kit; use real figures only.",
 "numbers, statistics, counter, results, firm, ledger",
 sec("Numbers", grid([stackg([counter(n, suf, pre, "xx-large", LF2, 0).replace('"fontWeight":"900"', '"fontWeight":"700"'), p(lbl, None, "secondary")]) for n, suf, pre, lbl in
     [(340, "", "", "small businesses on our books"), (18, "", "", "years at Park Square"), (0, "", "", "returns filed late, ever"), (4200, "", "$", "saved in tax per client, on average")]], 4, "13rem", "x-large"), "section-tint"))

kit("ledger-process", L, "Ledger how we work: four steps",
 "How the firm works with a new client in four numbered steps, from the first call to the yearly review. Part of the Ledger kit; one sentence each.",
 "process, how it works, steps, onboarding, ledger",
 sec("How we work", N([lhead2("How we work", "From the first call to the first year-end"), grid([stackg([p(n, "xx-large", "primary", None, LF2, {"fontWeight": "700", "lineHeight": "1"}), sep(), h(t, 3, "large"), p(d, None, "secondary")]) for n, t, d in [
    ("01", "A free call", "Thirty minutes about your business and what you need. No obligation."),
    ("02", "A fixed fee", "A written quote for the year, so you know the cost before we start."),
    ("03", "We take it over", "We write to your old accountant and the tax office. You sign one form."),
    ("04", "Every quarter", "A short review of the numbers, and a call whenever you need one.")]], 4, "13rem", "x-large")])))

kit("ledger-stories", L, "Ledger client stories: a carousel of quotes",
 "Clients in their own words, in a carousel, three at a time on a computer and one on a phone, with each client's name and business. Needs the AnyPress Blocks plugin. Part of the Ledger kit; use real quotes, with permission.",
 "testimonials, client stories, reviews, quotes, carousel, ledger",
 sec("Client stories", N([lhead2("Client stories", "What clients say", ("All client stories", "/clients/")),
                          carousel([lstory2(*s) for s in LSTORIES], 3, "Client stories")]), "section-tint"))

kit("ledger-office", L, "Ledger office: where the firm is, with a map",
 "Where the firm works, with the address, opening hours and parking beside a map. Needs the AnyPress Blocks plugin for the map. Part of the Ledger kit.",
 "office, location, address, map, visit, ledger",
 sec("Office", cols([
   col(N([lsmall("Our office"), h("On Park Square, by the town hall", 2, "xx-large"), p(LADDR, "large", bind="address"),
          lst(["Monday to Friday, 8:30am to 5:30pm", "Five minutes' walk from Leeds station", "Meeting room on the ground floor, step-free"])]), "40%"),
   col(mapb(LADDR + ", UK", LLAT, LLON, 16, "4/3"))], "xx-large", "wide", "center")))

kit("ledger-faq-open", L, "Ledger questions: answers that open and close",
 "The questions people ask before they switch accountants, as answers that open and close, beside a heading and a link to all questions. Part of the Ledger kit; answer the real questions.",
 "faq, questions, answers, accordion, switching, ledger",
 sec("Questions", cols([
   col(N([lsmall("Questions"), h("Before you switch", 2, "xx-large"), p("Can't see yours? Call the office and ask for Helen.", None, "secondary"), btns([("All questions", "outline", "/faq/")])]), "36%"),
   col(accordion([
     ("Is it hard to change accountants?", "No. Sign one form and we write to your old accountant for your records. Most switches take two weeks."),
     ("Do you charge for phone calls?", "Never. Calls and emails are part of the fixed monthly fee."),
     ("Which software do you use?", "Xero, QuickBooks or FreeAgent, whichever you prefer. We'll set it up if you have none."),
     ("Can you help if I'm behind on my returns?", "Yes. We'll catch up the late ones first and talk to the tax office for you."),
     ("Do I have to come to the office?", "No. Most clients never do. We meet by video, phone or at your place.")]))], "xx-large", "wide", "top")))

kit("ledger-signup", L, "Ledger signup: deadlines and tax news by email",
 "A band asking visitors to join a monthly email with deadlines and tax changes, with the signup form beside it. Part of the Ledger kit; sits above the footer on every page.",
 "newsletter, signup, email, deadlines, tax news, ledger",
 sec("Signup", cols([
   col(N([h("Deadlines and tax changes, once a month", 2, "xx-large"), p("A short email with the dates coming up and what's changed, in plain English. Unsubscribe in one click.", None, "secondary")]), "55%", valign="center"),
   col(form("newsletter", "Read our insights", "/insights/"), valign="center")], "x-large", "wide", "center"), "section-brand-soft", ("x-large", "x-large", None, None)))

LPOP2 = popup("offer", N([
    img("placeholder-wide.svg", "Two people going through papers at a desk", "16/9"),
    grp(N([lsmall("Switching accountants?"), h("Your first month free", 2, "xx-large"),
           p("Leave your email and we'll send our switching checklist and a code for your first month's fee free."),
           form("offer", "See our fees", "/fees/")]), None, (None, None, "large", "large"), "small", {"type": "default"})]),
    label="First month free")
kit("ledger-popup", L, "Ledger popup: first month free for switchers",
 "A popup that opens five seconds into a first visit with a photo, an offer for people switching firms and one field for an email address; it closes with its button, Escape or a click outside and stays closed for two weeks. Needs the AnyPress Blocks plugin. Part of the Ledger kit; put it in the footer to show it on every page.",
 "popup, offer, switch, discount, newsletter, email, modal, ledger", LPOP2)

LFOOT2 = grp(N([
    BODIES["ledger-signup"],
    grp(N([cols([
        col(N([dyn("site-title", {"level": 0, "fontSize": "x-large", "fontFamily": LF2, "style": {"typography": {"fontWeight": "700"}}}),
               p("Accounts, tax and payroll for small firms in Leeds, on fixed monthly fees.", None, "main-accent"),
               ltel2("xx-large"), social(["linkedin", "facebook", "google"])]), "34%"),
        col(flinks("Services", [(n, f"/services/{s}/") for n, s, _ in LSERV] + [("Fees", "/fees/")])),
        col(flinks("The firm", [("About us", "/about/"), ("Our team", "/team/"), ("Who we help", "/industries/"), ("Client stories", "/clients/"), ("Careers", "/careers/"), ("Insights", "/insights/"), ("Questions", "/faq/"), ("Contact", "/contact/")])),
        col(N([h("Office", 3, "medium"), p(LADDR, None, "main-accent", bind="address"), p("Monday to Friday, 8:30am to 5:30pm", None, "main-accent", bind="hours"),
               btns([("Book a free call", None, LCALL)])]))], "large", "wide", "top"),
        sep(),
        row([p("© Hartley Shaw Accountants. Chartered accountants, regulated for audit and accounts work.", "small", "main-accent"),
             p('<a href="/privacy-policy/">' + T("Privacy") + '</a> · <a href="/contact/">' + T("Contact") + '</a>', "small", "main-accent", None, None, None, raw=True)], gap="small")]),
        "section-dark", ("x-large", "large", None, None), "large", {"type": "constrained", "contentSize": "80rem"}, align="full", name="Footer columns"),
    LPOP2,
]), None, None, "0", {"type": "default"}, align="full", name="Footer")
write("ledger-footer", "Ledger footer: monthly deadlines email, services and the switcher offer",
 "A site footer for an accountant, lawyer, consultant or agency: a band for the monthly email, then the phone number, service and firm links and the office on dark, and the switcher offer popup (needs the AnyPress Blocks plugin). Part of the Ledger kit; choose it for the footer in the Site Editor.",
 "footer", "footer, links, office, newsletter, phone, popup, accountant, ledger", LFOOT2, "core/template-part/footer")

def lfee(name, detail, price):
    return grp(N([h(name, 3, "medium"), p(price, "x-large", "primary", None, LF2, {"fontWeight": "700", "lineHeight": "1.1"}),
                  p(detail, "small", "secondary")]), gap="x-small", layout={"type": "default"})
kit("ledger-service-detail", L, "Ledger service: what's included and the fee",
 "The body of a page for one service: what it covers in plain words, what's included as a list, a photo that opens full screen, and a card with the fee and a button to book a call. Part of the Ledger kit.",
 "service, details, included, fee, accountant, ledger",
 sec("Service details", cols([
   col(N([h("What we do", 2, "xx-large"),
          p("We prepare your company's accounts and corporation tax return from your books, go through them with you in a short meeting, and file both weeks before the deadline. You see the tax bill early enough to plan for it."),
          h("What's included", 3, "large"),
          lst(["Statutory accounts for Companies House", "The corporation tax return", "A meeting to go through the numbers", "Tax planning before the year ends", "Dividend and salary advice for directors"]),
          zoom(img("placeholder-wide.svg", "This service: an accountant going through a set of accounts", "16/10"))]), "54%"),
   col(grp(N([lsmall("The fee"), lfee("Sole trader", "Accounts and your tax return", "$95 / month"), lfee("Limited company", "Accounts and company tax", "$180 / month"),
              p("Fixed, agreed in writing before we start. Calls and emails included.", "small", "secondary"),
              btns([("Book a free call", None, LCALL), ("Call " + LPH, "outline", LTL)])]), "section-brand-soft", PAD_CARD, "medium", {"type": "default"}))], "xx-large", "wide", "top"), content="72rem"))

kit("ledger-industries", L, "Ledger who we help: the industries the firm knows",
 "The kinds of business the firm knows best, as cards with what it does for each and a link to each one's page. Part of the Ledger kit.",
 "industries, sectors, who we help, clients, specialisms, ledger",
 sec("Industries", N([lhead2("Who we help", "Firms we know inside out"), grid([grp(N([h(n, 3, "large"), p(d, None, "secondary"), link_p(f"Accountants for {n.lower()} →", f"/industries/{s}/", None, {"fontWeight": "600"})]), "section-card", PAD_CARD, "small", {"type": "default"}) for (n, s), d in zip(LIND, [
    "Practice accounts, associate pay and NHS income, for 40 practices across Yorkshire.",
    "CIS returns, van and tool costs and cash flow between stage payments.",
    "Tips, staff rotas and VAT on food, for cafés, bars and restaurants.",
    "Project costs, contractors and research tax credits for design and digital studios."])], 4, "13rem", "medium")]), "section-tint"))

kit("ledger-industry", L, "Ledger industry: what the firm does for one kind of business",
 "The body of a page for one industry: three things that matter to that kind of business, each with a heading and a line, and a quote from a client in it. Part of the Ledger kit; make one per industry.",
 "industry, sector, specialism, clients, ledger",
 sec("For you", N([cols([col(h("Accounts that understand a dental practice", 2, "xx-large"), "55%"), col(p("Associates, NHS contracts, private fees and a practice that might one day be sold: we know how the money works.", "large", "secondary"), None, None, None, "bottom")], "x-large", "wide", "bottom"),
   grid([stackg([p(n, "xx-large", "primary", None, LF2, {"fontWeight": "700", "lineHeight": "1"}), h(t, 3, "large"), p(d, None, "secondary")]) for n, t, d in [
     ("01", "Associate pay", "Associate fees and lab bills worked out right, every month."),
     ("02", "NHS and private income", "Both kinds of income tracked apart, so you can see what pays."),
     ("03", "Ready to sell", "Clean accounts that hold up when a buyer looks at them.")]], 3, "16rem", "x-large"),
   lstory2("They found us eleven thousand pounds in the first year, and they explained how in plain English.", "Priya S.", "Owner, Northside Dental", "large")])))

kit("ledger-offers", L, "Ledger offers: ways to pay less",
 "Three offers as cards with the saving in large type, who it's for and a button: switching firms, new businesses and paying yearly. Part of the Ledger kit; keep the offers current.",
 "offers, discounts, switch, new business, yearly, ledger",
 sec("Offers", N([lhead2("Ways to pay less", "Offers"), grid([grp(N([p(s, "xx-large", None, None, LF2, {"fontWeight": "700", "lineHeight": "1"}), h(t, 3, "large"), p(d, None, "secondary"), btns([(b, "outline", l)])]), st, PAD_CARD, "small", {"type": "default"}) for s, t, d, b, l, st in [
    ("1 month free", "Switching firms", "Move to us from another accountant and your first month's fee is on us.", "Book a free call", LCALL, "section-brand-soft"),
    ("6 months half price", "New businesses", "In your first year of trading? Half the monthly fee for six months.", "Start properly", "/services/starting-a-business/", "section-card"),
    ("2 months free", "Pay yearly", "Pay for the year up front and get two months free.", "Ask about it", "/contact/", "section-brand-soft")]], 3, "16rem", "medium")])))

kit("ledger-team", L, "Ledger team: the people clients speak to",
 "The people at the firm, each with a photo, their name, role and what they look after. Part of the Ledger kit; use real photos, with permission.",
 "team, staff, partners, people, about, ledger",
 sec("Team", N([lhead2("Our team", "The people you'll speak to"), grid([stackg([img("placeholder-tall.svg", alt, "4/5"), h(n, 3, "large"), p(r, None, "primary", None, LF2, {"fontWeight": "600"}), p(d, None, "secondary")]) for n, r, d, alt in [
    ("Helen Hartley", "Partner", "Dentists and creative agencies. Founded the firm in 2008.", "Our team: Helen Hartley"),
    ("David Shaw", "Partner", "Builders, trades and anyone with a tricky tax question.", "Our team: David Shaw"),
    ("Mei Lin", "Senior accountant", "Restaurants and cafés, and every payroll we run.", "Our team: Mei Lin"),
    ("Kwame Asante", "Accountant", "Sole traders, landlords and personal tax returns.", "Our team: Kwame Asante")]], 4, "13rem", "large")])))

kit("ledger-jobs", L, "Ledger careers: why work here and the open roles",
 "Why people work at the firm, each open role with its pay, and the application. Part of the Ledger kit; keep the roles current and put the site's application form in the named Form group.",
 "careers, jobs, hiring, accountant, trainee, apply, ledger",
 sec("Careers", N([
   lhead2("Why work here", "A small firm that trains its people"),
   grid([stackg([h(t, 3, "large"), p(d, None, "secondary")]) for t, d in [
     ("Exams paid for", "We pay for your exams and give you study days before each one."),
     ("Home by six", "No late nights in January. We plan the work so nobody needs them."),
     ("Your own clients", "Every accountant looks after their own clients from the first year."),
     ("Hybrid", "Two days in the office on Park Square, the rest wherever you like.")]], 4, "13rem"),
   '<!-- wp:spacer {"height":"var:preset|spacing|large"} -->\n<div style="height:var(--wp--preset--spacing--large)" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->',
   h("Open roles", 2, "xx-large"),
   N([grp(N([row([h(t, 3, "large"), p(when, None, None, None, LF2, {"fontWeight": "600"})], valign="center"), p(d, None, "secondary"), btns([("Apply for this", None, "#apply")])]), "section-tint", PAD_CARD, "small", {"type": "default"}) for t, when, d in [
     ("Trainee accountant", "Leeds, $32,000 plus exams", "Start with bookkeeping and payroll and work towards your own clients, with your exams paid."),
     ("Payroll administrator", "Leeds, $34,000", "Run payroll for around sixty small businesses with Mei, monthly and weekly."),
     ("Senior accountant", "Leeds or hybrid, $58,000", "Look after forty clients of your own, from their books to their year-end meeting.")]]),
   grp(N([h("Apply", 2, "xx-large"), p("Tell us about you, the role and your qualifications so far. We reply to everyone within a week."),
          form("apply", "Email the partners", "mailto:jobs@example.com")]), "section-card", PAD_CARD, "small", {"type": "default"}, anchor="apply")])))

kit("ledger-call-form", L, "Ledger book a call: the form and what happens next",
 "A form to book a free call, beside what happens on the call and what to have ready. Part of the Ledger kit; put the site's form in the named Form group.",
 "book a call, consultation, appointment, contact, form, ledger",
 sec("Contact", cols([
   col(grp(N([h("Book a free 30-minute call", 2, "xx-large"), p("Tell us a little about your business and pick a day. We'll call at a time that suits you, usually within two working days."),
              form("quote", "Call " + LPH, LTL, "Rather talk now? Call the office.")]), "section-card", PAD_CARD, "medium", {"type": "default"}), "58%"),
   col(N([h("On the call", 3, "large"),
          lst(["What your business does and how it's set up", "What you'd like us to take on", "A fixed fee, in writing, the same week"]),
          h("Good to have ready", 3, "large"), lst(["Your last set of accounts", "Which software you use, if any", "Any letters from the tax office"])]))],
   "xx-large", "wide", "top"), "section-tint"))

kit("ledger-contact-full", L, "Ledger contact: phone, email, office and form",
 "A contact section for a professional firm: the phone number, email, office address and hours beside the contact form, then a map. Needs the AnyPress Blocks plugin for the map. Part of the Ledger kit.",
 "contact, phone, email, office, hours, map, form, ledger",
 sec("Contact us", N([cols([
   col(N([h("Speak to an accountant", 2, "xx-large"), ltel2("xx-large"),
          p('<a href="mailto:hello@example.com">hello@example.com</a>', None, None, None, None, None, raw=True, bind="email_linked"),
          p(LADDR, None, bind="address"), p("Monday to Friday, 8:30am to 5:30pm", None, "secondary", bind="hours")]), "40%"),
   col(grp(N([h("Send a message", 3, "large"), form("contact", "Call " + LPH, LTL, "We reply the same working day.")]), "section-tint", PAD_CARD, "medium", {"type": "default"}))], "xx-large", "wide", "top"),
   mapb(LADDR + ", UK", LLAT, LLON, 16, "21/9")])))

# The home page: numbers, how we work, client stories, questions and the office join the original sections.
kit_page("kit-professional", "Home page: Ledger kit, professional services",
 "A complete home page for an accountant, lawyer, consultant or agency in the Ledger kit: a title panel beside a photo, services set like a report, numbers that count up, how the firm works, a client quotation, client stories in a carousel, a fees table, questions, the office with a map and contact. Apply the Ledger style for the look it was designed with.",
 "home, accountant, lawyer, consultant, agency, professional, firm, kit, ledger",
 ["ledger-masthead", "ledger-services", "ledger-numbers", "ledger-process", "ledger-quote", "ledger-stories", "ledger-fees", "ledger-faq-open", "ledger-office", "ledger-contact"])

# ---------------------------------------------------------------- pages
def ledger_page(slug, title, desc, kw, parts):
    write(slug, title, desc, "anypress/pages", kw, N(parts), "core/post-content", " * Post Types: page\n")

ledger_page("ledger-page-services", "Services page: Ledger kit",
 "A Services page for an accountant or professional firm: a heading, every service with a link to its own page, how the firm works, client stories and a call to book. Ledger kit.",
 "services, what we do, practice areas, ledger",
 [lpage_hero2("Services", "Everything a small business needs from an accountant, on one fixed monthly fee.", "Services", [("Book a free call", None, LCALL)]),
  sec("All services", grid([stackg([sep(), h(n, 3, "large"), p(d, None, "secondary"), link_p("More about this →", f"/services/{s}/", None, {"fontWeight": "600"})], "small") for n, s, d in LSERV], 3, "16rem", "x-large")),
  BODIES["ledger-process"], BODIES["ledger-stories"], BODIES["ledger-contact"]])

ledger_page("ledger-page-service", "Service page: Ledger kit (one service)",
 "A page for one service, such as year-end accounts: a heading with a photo, what's included and the fee, client stories, questions about it and a call to book. Ledger kit; make one per service.",
 "service page, single service, accountant, fee, ledger",
 [lpage_hero2("Year-end accounts", "Accounts and the company tax return, filed weeks before the deadline.", "Services / Year-end accounts", [("Book a free call", None, LCALL)], "Inside the firm: an accountant at a desk with a calculator and papers"),
  BODIES["ledger-service-detail"], BODIES["ledger-stories"],
  sec("Questions", cols([col(N([lsmall("About this service"), h("Good to know", 2, "xx-large")]), "36%"), col(accordion([
    ("When will my accounts be ready?", "Within six weeks of your year-end, as long as your books are up to date."),
    ("What do you need from me?", "Access to your bookkeeping software and bank statements. We'll ask for anything else."),
    ("Can you file late accounts?", "Yes. We'll catch up and talk to Companies House about any penalties."),
    ("Is the fee really fixed?", "Yes. It only changes if your business changes a lot, and we'd agree it with you first.")]))], "xx-large", "wide", "top")),
  BODIES["ledger-contact"]])

ledger_page("ledger-page-about", "About page: Ledger kit",
 "An About page for an accountant or professional firm: a heading, the firm's story beside a photo, numbers that count up, the team and the office with a map. Ledger kit.",
 "about, about us, firm, history, team, ledger",
 [lpage_hero2("About the firm", "Two partners, eight accountants and 340 small businesses who can always get one of us on the phone.", "About"),
  sec("Story", cols([
    col(N([h("Started by two accountants who were tired of big firms", 2, "xx-large"),
           p("Helen Hartley and David Shaw met at a big city firm, where small clients got a different junior every year. In 2008 they set up on Park Square to do it the other way: one accountant for each client, fixed fees and phones that get answered.", "large"),
           p("Eighteen years on, most of our clients came from another client's recommendation. We'd like to keep it that way.")]), "50%", valign="center"),
    col(img("placeholder-tall.svg", "Inside the firm: a meeting around a table with laptops", "4/5"))], "xx-large", "wide", "center")),
  BODIES["ledger-numbers"], BODIES["ledger-team"], BODIES["ledger-office"]])

ledger_page("ledger-page-team", "Team page: Ledger kit",
 "A Team page for a professional firm: a heading, the people with photos and what each looks after, how the firm works and a call to book. Ledger kit.",
 "team, people, staff, partners, ledger",
 [lpage_hero2("Our team", "Every client has one accountant who knows their business. These are the people you'll speak to.", "Team"),
  BODIES["ledger-team"], BODIES["ledger-process"], BODIES["ledger-contact"]])

ledger_page("ledger-page-reviews", "Client stories page: Ledger kit",
 "A Client stories page: a heading, client quotes as cards with names and businesses, numbers that count up and a call to book. Ledger kit; use real quotes, with permission.",
 "client stories, testimonials, reviews, case studies, ledger",
 [lpage_hero2("Client stories", "Owners, directors and sole traders on what changed when they switched to us.", "Clients", [("Book a free call", None, LCALL)]),
  sec("All stories", grid([lstory2(*s) for s in LSTORIES + [
    ("Our year-end meeting is the one meeting I actually look forward to.", "Fiona D.", "Director, Ashby Architects"),
    ("They caught a VAT mistake our old firm made three years running.", "Raj P.", "Owner, Spice Route"),
    ("Clear fees, clear advice, and nobody makes me feel stupid for asking.", "Hannah L.", "Photographer")]], 3, "18rem", "medium"), "section-tint"),
  BODIES["ledger-quote"], BODIES["ledger-numbers"], BODIES["ledger-contact"]])

ledger_page("ledger-page-areas", "Who we help page: Ledger kit",
 "A Who we help page for a professional firm: a heading, a card for each industry linking to its own page, client stories and a call to book. Ledger kit.",
 "industries, sectors, who we help, specialisms, ledger",
 [lpage_hero2("Who we help", "We work for all kinds of small business, and know four kinds especially well.", "Who we help"),
  BODIES["ledger-industries"], BODIES["ledger-stories"], BODIES["ledger-contact"]])

ledger_page("ledger-page-area", "Industry page: Ledger kit (one industry)",
 "A page for one industry, such as dentists: a heading, what matters to that business and how the firm helps, the services they use most and a call to book. Ledger kit; make one per industry.",
 "industry, sector, specialism, ledger",
 [lpage_hero2("Accountants for dentists", "Associates, NHS contracts and private fees, handled by people who do it for 40 practices.", "Who we help / Dentists", [("Book a free call", None, LCALL)]),
  BODIES["ledger-industry"], BODIES["ledger-services"], BODIES["ledger-contact"]])

ledger_page("ledger-page-offers", "Fees page: Ledger kit",
 "A Fees page for an accountant or professional firm: a heading, the fees table, ways to pay less, questions and a call to book. Ledger kit; match it to the real fees.",
 "fees, prices, pricing, offers, ledger",
 [lpage_hero2("Fees", "Fixed monthly fees, agreed in writing before we start. Calls and emails are always included.", "Fees"),
  BODIES["ledger-fees"], BODIES["ledger-offers"], BODIES["ledger-faq-open"], BODIES["ledger-contact"]])

ledger_page("ledger-page-join", "Book a call page: Ledger kit",
 "A Book a call page: a heading, the booking form beside what happens on the call, how the firm works and client stories. Ledger kit; put the site's form in the named Form group.",
 "book a call, consultation, appointment, ledger",
 [lpage_hero2("Book a free call", "Thirty minutes with an accountant, about your business and what you need. No obligation.", "Book a call"),
  BODIES["ledger-call-form"], BODIES["ledger-process"], BODIES["ledger-stories"]])

ledger_page("ledger-page-faq", "Questions page: Ledger kit",
 "A Questions page for an accountant or professional firm: answers that open and close, grouped into switching, fees and working together, and a call to book. Ledger kit; answer the real questions.",
 "faq, questions, answers, ledger",
 [lpage_hero2("Questions", "Switching, fees and how we work, answered plainly.", "FAQ"),
  sec("Questions", N([N([h(group_t, 2, "xx-large"), accordion(qs)]) for group_t, qs in [
    ("Switching to us", [
      ("Is it hard to change accountants?", "No. Sign one form and we write to your old accountant for your records. Most switches take two weeks."),
      ("Can you help if I'm behind on my returns?", "Yes. We'll catch up the late ones first and talk to the tax office for you.")]),
    ("Fees", [
      ("Do you charge for phone calls?", "Never. Calls and emails are part of the fixed monthly fee."),
      ("What if my business grows?", "We'll look at the fee once a year with you, and never change it without agreeing first.")]),
    ("Working together", [
      ("Which software do you use?", "Xero, QuickBooks or FreeAgent, whichever you prefer."),
      ("Do I have to come to the office?", "No. Most clients never do. We meet by video, phone or at your place.")])]]),
    content="56rem"),
  BODIES["ledger-contact"]])

ledger_page("ledger-page-careers", "Careers page: Ledger kit",
 "A Careers page for a professional firm: a heading, why people work there, the open roles with pay, the application form and the office with a map. Ledger kit; keep the roles current and put the site's form in the named Form group.",
 "careers, jobs, hiring, accountant, ledger",
 [lpage_hero2("Careers", "A small firm that pays for your exams and gives you your own clients. Salaries are on this page.", "Careers", [("See open roles", None, "#apply")]),
  BODIES["ledger-jobs"], BODIES["ledger-office"]])

ledger_page("ledger-page-contact", "Contact page: Ledger kit",
 "A Contact page for a professional firm: a heading, the phone number, email, office and hours beside the contact form, a map and questions. Ledger kit; put the site's contact form in the named Form group.",
 "contact, phone, email, office, ledger",
 [lpage_hero2("Contact", "Call the office, send a message or come and see us on Park Square.", "Contact"),
  BODIES["ledger-contact-full"], BODIES["ledger-faq-open"]])

ledger_page("ledger-page-thanks", "Thank-you page: Ledger kit",
 "The page visitors see after sending a form: thanks, what happens next and when, and links to keep reading. Ledger kit; send every form here.",
 "thank you, thanks, confirmation, form sent, ledger",
 [sec("Thanks", N([lsmall("Message sent"), h("Thank you. We'll be in touch soon.", 1, "xxx-large"),
    p("One of our accountants will reply within one working day. Check your email for a copy of what you sent.", "large", "secondary"),
    btns([("Back to the home page", None, "/"), ("See our services", "outline", "/services/")])]), None, ("xxx-large", "xxx-large", None, None), "56rem"),
  BODIES["ledger-stories"]])

print("ledger ok")
