# Assay (0.20.0): a whole website for a shop that sells regulated health products (peptides, supplements, CBD and
# other goods that need lab results, age checks and careful wording), written for a doctor-led peptide therapy shop.
# Run by kits.py after kit_byline.py, so every helper in kits.py, kits_more.py, kit_ridge.py and the kits before it
# is in scope.
#
# A lab report: a calm book serif for headings, a plain sans for reading, batch numbers and labels in mono, deep teal
# and amber-glass. Pages link to each other by slug: /treatments/ and one page per treatment under it, /lab-results/,
# /how-it-works/, /states/ and one page per state under it, /pricing/, /get-started/, /about/, /reviews/, /faq/,
# /careers/, /learn/ (the blog), /contact/, /thank-you/. Forms are named groups, as in Ridge: "Form: quote" asks for a
# consultation, "Form: apply" is the job application.

AK = "anypress/kit-regulated"
ASERIF = "newsreader"
APH = "(480) 555-0162"
ATL = "tel:4805550162"
ASTART = "/get-started/"
AADDR = "7150 East Camelback Road, Suite 300, Scottsdale, AZ 85251"
ALAT, ALON = 33.5025, -111.9269
AHOURS = "Care team: Monday to Friday, 7am to 6pm, and Saturday 8am to noon (Arizona time)"
ARULE = "Prescription only. Treatments are prescribed only when a licensed provider decides they suit you. Compounded medicines are not FDA approved. These statements have not been evaluated by the FDA."

variation("kit-assay", "Assay (regulated health products)", PALS["assay"], "figtree", ASERIF, "500", "-0.015em", "1.08",
    button("var:preset|border-radius|full", "figtree", "600"), blocks=site_title(ASERIF, "600", None, "-0.01em"))

def alabel(text, color="secondary", size="small"):
    """A small label in mono capitals, like a batch number on a lab report."""
    return p(text, size, color, None, "monospace", {"textTransform": "uppercase", "letterSpacing": "0.06em"})

def ahead(label, title, link=None, size="xx-large"):
    left = stackg([alabel(label, "primary"), h(title, 2, size)])
    return row([left, btns([(link[0], "outline", link[1])])] if link else [left], valign="bottom")

def a_buttons():
    """The header's buttons: Sign in on tablets and computers, and Get started everywhere."""
    sign = f'<!-- wp:button {j({"className": "is-style-outline", "metadata": {"blockVisibility": {"viewport": {"mobile": False}}}})} -->\n<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/contact/">{T("Talk to us")}</a></div>\n<!-- /wp:button -->'
    go = f'<!-- wp:button -->\n<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{ASTART}">{T("Get started")}</a></div>\n<!-- /wp:button -->'
    return '<!-- wp:buttons {"layout":{"type":"flex","flexWrap":"nowrap"}} -->\n<div class="wp-block-buttons">' + N([sign, go]) + '</div>\n<!-- /wp:buttons -->'

def apage_hero(title, text, crumb=None, buttons=None, alt=None):
    words = N(([alabel(crumb, "primary")] if crumb else []) + [h(title, 1, "xxx-large", None, None, {"lineHeight": "1.05"}), p(text, "large")] + ([btns(buttons)] if buttons else []))
    if not alt:
        return sec("Page hero", grp(words, gap="medium", layout={"type": "constrained", "contentSize": "50rem", "justifyContent": "left"}), "section-tint", ("xx-large", "xx-large", None, None), "80rem")
    return sec("Page hero", cols([col(words, "52%", valign="center"), col(img("placeholder-wide.svg", alt, "4/3", "md"))], "xx-large", "wide", "center"), "section-tint", ("xx-large", "xx-large", None, None), "80rem")

def afact(label, value):
    return grp(N([alabel(label), p(value)]), layout={"type": "flex", "flexWrap": "nowrap", "justifyContent": "space-between", "verticalAlignment": "top"}, gap="small")

def acard(inner, style="section-card", gap="small"):
    return grp(N(inner), style, PAD_CARD, gap, {"type": "default"})

def aspacer():
    return '<!-- wp:spacer {"height":"var:preset|spacing|large"} -->\n<div style="height:var(--wp--preset--spacing--large)" aria-hidden="true" class="wp-block-spacer"></div>\n<!-- /wp:spacer -->'

# ---------------------------------------------------------------- content
ATREAT = [  # name, slug, price, line
    ("NAD+", "nad-plus", "From $149 a month", "Small injections at home, a few times a week, for people who want to support energy and healthy ageing."),
    ("Sermorelin", "sermorelin", "From $199 a month", "A nightly injection that asks your own body to make more growth hormone, often chosen for sleep and recovery."),
    ("Glutathione", "glutathione", "From $119 a month", "A weekly injection of the body's own antioxidant, prescribed alongside a plan for everyday wellness."),
    ("Copper peptide serum", "copper-peptide-serum", "$89 a bottle", "GHK-Cu in a light serum for the face and neck. No prescription needed; tested like everything else."),
]
ASTATES = [("Arizona", "arizona"), ("Texas", "texas"), ("Florida", "florida"), ("Colorado", "colorado")]
ABATCH = [  # batch, product, purity, lab, date
    ("TL-2611-04", "NAD+ 500 mg", "99.4%", "Kestrel Analytical", "Nov 4"),
    ("TL-2610-29", "Sermorelin 9 mg", "99.1%", "Kestrel Analytical", "Oct 29"),
    ("TL-2610-21", "Glutathione 1,500 mg", "99.6%", "Saguaro Labs", "Oct 21"),
    ("TL-2610-14", "Copper peptide serum", "Passed", "Saguaro Labs", "Oct 14"),
    ("TL-2610-07", "NAD+ 500 mg", "99.2%", "Kestrel Analytical", "Oct 7"),
]
AREVIEWS = [
    ("The video visit took fifteen minutes and the doctor actually listened. My first box came two days later.", "Laura P.", "NAD+, Phoenix"),
    ("I checked the lab report for my batch before I opened it. That's why I stayed.", "Marcus D.", "Sermorelin, Austin"),
    ("Clear prices, no upsell, and a nurse who calls back the same day.", "Renee T.", "Glutathione, Tampa"),
    ("They told me one treatment wasn't right for me and didn't charge for the visit. Honest.", "James W.", "Consultation, Denver"),
    ("The serum is the only thing I've used that didn't irritate my skin.", "Ana G.", "Copper peptide serum, Scottsdale"),
    ("Every refill is on time, and the box is plain, which I appreciate.", "Chris M.", "NAD+, Dallas"),
]
ATEAM = [("Dr. Maya Okonkwo", "Medical director", "Board-certified in internal medicine. Reviews every new treatment we offer before it's added."),
         ("Daniel Reyes, PharmD", "Pharmacy lead", "Works with our partner pharmacy on every batch and reads every lab report first."),
         ("Sara Lindqvist, RN", "Care team lead", "Answers your questions, checks in after your first month and keeps refills on time.")]

def areview(text, name, what, size="medium"):
    return grp(N([p("★★★★★", None, "primary"), p("“" + text + "”", size, None, None, None, {"lineHeight": "1.45"}), alabel(f"{name} · {what}")]),
               "section-card", PAD_CARD, "small", {"type": "default"})

def atreat_card(name, slug, price, line):
    return grp(N([zoom(img("placeholder-wide.svg", f"Treatment: {name}", "4/3", "md")), alabel(price, "primary"),
                  hlink(name, f"/treatments/{slug}/", 3, "x-large"), p(line, None, "secondary"), link_p("Read more →", f"/treatments/{slug}/", None, {"fontWeight": "600"})]),
               gap="small", layout={"type": "default"})

def batch_table(rows):
    """Batch, product and result: three columns, so the table still reads on a phone."""
    return table(["Batch", "Product", "Result"], [(b, f"{prod}, {d}", pur) for b, prod, pur, lab, d in rows], "stripes")

# ---------------------------------------------------------------- sections
kit("assay-topbar", AK, "Assay top bar: prescription only, and the care team's number",
 "A thin bar above the header saying treatments are prescribed by licensed providers and every batch is tested, with the care team's phone number. Part of the Assay kit (regulated health products); keep the wording your lawyer approves.",
 "top bar, announcement, prescription, lab tested, phone, header, compliance, assay",
 grp(row([p(T("Prescribed by licensed US providers. Every batch tested by an independent lab.") + ' <a href="/lab-results/">' + T("See the results") + '</a>', "small", None, None, None, None, raw=True),
          p(T("Care team") + f' <a href="{ATL}">' + T(APH) + '</a>', "small", None, None, None, None, raw=True)], gap="small"),
     "section-dark", ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Top bar"))

AHEADER = grp(N([
    BODIES["assay-topbar"],
    grp(row([
        row([dyn("site-logo", {"width": 36, "shouldSyncIcon": True}), dyn("site-title", {"level": 0, "fontSize": "x-large", "fontFamily": ASERIF, "style": {"typography": {"lineHeight": "1"}}})], "left", "small", False, "center"),
        row([dyn("navigation", {"overlayMenu": "mobile", "layout": {"type": "flex", "justifyContent": "right"}}), a_buttons()], "right", "medium", False, "center")], "space-between", "medium", False, "center"),
        None, ("small", "small", None, None), None, {"type": "constrained", "contentSize": "80rem"}, align="full", name="Main bar").replace(
        '<!-- wp:group {', '<!-- wp:group {"backgroundColor":"base",', 1).replace('class="wp-block-group alignfull', 'class="wp-block-group alignfull has-base-background-color has-background', 1),
]), "sticky", None, "0", {"type": "default"}, align="full", name="Header")
write("assay-header", "Assay header: prescription notice, menu and a Get started button",
 "A site header for a shop that sells regulated health products, which stays at the top while visitors scroll: a bar saying treatments are prescribed and lab tested, then the logo, the menu (with dropdowns for treatments and the company) and a Get started button. Part of the Assay kit; choose it for the header in the Site Editor.",
 "header", "header, menu, navigation, sticky, prescription, lab tested, health, assay", AHEADER, "core/template-part/header")

kit("assay-hero", AK, "Assay hero: prescribed by a doctor, tested by a lab",
 "Opening section for a regulated health shop: a headline, one sentence on how it works, two buttons and three short promises, beside a photo of the lab. Part of the Assay kit; keep claims to what the business can show.",
 "hero, peptides, health, wellness, prescription, lab tested, telehealth, assay",
 sec("Hero", cols([
   col(N([alabel("Doctor-led peptide therapy", "primary"),
          h("Peptides prescribed by a doctor, with the lab report to prove it", 1, "xxx-large", None, None, {"lineHeight": "1.04"}),
          p("A short video visit with a licensed provider, medicine made by a US pharmacy, and an independent lab test for every batch, published before it ships.", "large"),
          btns([("Start your consultation", None, ASTART), ("See treatments", "outline", "/treatments/")]),
          row([alabel(t) for t in ["✓ Licensed in 4 states", "✓ Batch-tested", "✓ Ships in 2 days"]], "left", "medium")]), "52%", valign="center"),
   col(img("placeholder-tall.svg", "A scientist checking samples in the lab", "4/5", "md"))], "xx-large", "wide", "center"),
   None, ("x-large", "xx-large", None, None)))

kit("assay-promise", AK, "Assay promises: four things every order gets",
 "Four promises in a row on the tint colour: a licensed provider, a US pharmacy, an independent lab test and discreet shipping. Part of the Assay kit; only promise what the business does every time.",
 "promises, trust, pharmacy, lab tested, shipping, compliance, assay",
 sec("Promises", grid([stackg([alabel(n, "primary"), h(t, 3, "large"), p(d, None, "secondary")]) for n, t, d in [
    ("01", "A licensed provider", "Every prescription comes from a doctor or nurse practitioner licensed in your state."),
    ("02", "A US pharmacy", "Made to order by a state-licensed compounding pharmacy, never imported."),
    ("03", "Tested, then shipped", "An independent lab tests every batch for purity and strength. You can read the report."),
    ("04", "Plain, quick shipping", "Cold-packed in a plain box, at your door two days after it's made.")]], 4, "13rem", "x-large"), "section-tint", ("x-large", "x-large", None, None)))

kit("assay-treatments", AK, "Assay treatments: every product with its price",
 "Every treatment or product as a card with a photo that opens full screen, its starting price, its name (linking to its own page) and a line about it. Part of the Assay kit; describe what it is, not what it cures.",
 "treatments, products, catalogue, prices, peptides, shop, assay",
 sec("Treatments", N([ahead("Treatments", "What we prescribe", ("All treatments", "/treatments/")),
   grid([atreat_card(*t) for t in ATREAT], 4, "14rem", "large")])))

kit("assay-steps", AK, "Assay how it works: four steps from questions to your door",
 "How buying works, in four numbered steps: a short health form, a video visit, the pharmacy and lab, and check-ins. Part of the Assay kit; match the steps to the real process.",
 "how it works, process, steps, telehealth, consultation, assay",
 sec("How it works", N([ahead("How it works", "From first question to your door in about a week", ("The whole process", "/how-it-works/")),
   grid([stackg([p(n, "xx-large", "primary", None, ASERIF, {"lineHeight": "1"}), sep(), h(t, 3, "large"), p(d, None, "secondary")]) for n, t, d in [
     ("1", "Answer a few questions", "Ten minutes online about your health and what you hope for. It's free."),
     ("2", "Meet your provider", "A video visit with a licensed provider, usually within two days. If it isn't right for you, you pay nothing."),
     ("3", "Made, tested, shipped", "The pharmacy makes your medicine, the lab tests the batch, and it ships cold in a plain box."),
     ("4", "Check in, every month", "A nurse checks in after your first month, and your provider reviews your plan every three.")]], 4, "13rem", "x-large")])))

kit("assay-lab", AK, "Assay lab results: the latest batches in a table",
 "The latest batches in a table (batch number, product, purity, which lab tested it and when) beside a short note on how testing works and a link to every report. Part of the Assay kit; publish real reports only.",
 "lab results, certificate of analysis, COA, testing, purity, batches, compliance, assay",
 sec("Lab results", cols([
   col(N([alabel("Lab results", "primary"), h("Read the report before you open the box", 2, "xx-large"),
          p("An independent lab tests every batch for identity, purity, strength and sterility. Your batch number is on the label; its report is here.", "medium"),
          btns([("All lab results", None, "/lab-results/")])]), "38%"),
   col(N([batch_table(ABATCH[:4]), p("Tested by Kestrel Analytical and Saguaro Labs. Purity measured by HPLC; sterility and endotoxin tests passed on every injectable batch.", "small", "secondary")]))], "xx-large", "wide", "top"),
   "section-tint"))

kit("assay-numbers", AK, "Assay numbers: four figures that count up",
 "Four numbers that count up as they scroll into view (patients, batches tested, average purity, states), each with a short line. Needs the AnyPress Blocks plugin. Part of the Assay kit; use real figures only.",
 "numbers, statistics, counter, proof, patients, assay",
 sec("Numbers", grid([stackg([counter(n, sfx, "", "xxx-large", ASERIF, d).replace('"fontWeight":"900"', '"fontWeight":"500"'), alabel(lbl)]) for n, sfx, d, lbl in
     [(6400, "", 0, "patients treated"), (310, "", 0, "batches tested and published"), (99.3, "%", 1, "average purity"), (4, "", 0, "states we're licensed in")]], 4, "12rem", "x-large"),
   pad=("x-large", "x-large", None, None)))

kit("assay-reviews", AK, "Assay reviews: what patients say, in a carousel",
 "Patients in their own words, in a carousel, three at a time on a computer and one on a phone, with stars, a first name and what they used. Needs the AnyPress Blocks plugin. Part of the Assay kit; use real reviews with permission, and never results or health claims.",
 "reviews, testimonials, patients, stars, carousel, assay",
 sec("Reviews", N([ahead("Reviews", "Rated 4.8 out of 5 by patients", ("All reviews", "/reviews/")),
                   carousel([areview(*r) for r in AREVIEWS], 3, "Patient reviews")]), "section-tint"))

kit("assay-faq-open", AK, "Assay questions: prescriptions, safety and shipping",
 "The questions people ask before they buy, about prescriptions, safety, testing and shipping, as answers that open and close beside a heading and a link to all questions. Part of the Assay kit; have a provider check the answers.",
 "faq, questions, prescription, safety, shipping, accordion, assay",
 sec("Questions", cols([
   col(N([alabel("Before you start", "primary"), h("Good to know", 2, "xx-large"), p("Something else? The care team answers the phone and replies to every message the same day.", None, "secondary"), btns([("All questions", "outline", "/faq/")])]), "36%"),
   col(accordion([
     ("Do I need a prescription?", "Yes, for every injectable treatment. A licensed provider decides at your video visit whether it suits you. The copper peptide serum needs no prescription."),
     ("Are compounded medicines FDA approved?", "No. Compounded medicines are made by a licensed pharmacy for one patient at a time and are not FDA approved. That's why we test every batch and publish the results."),
     ("What if the provider says no?", "Then you pay nothing, and they'll tell you why and what else might help."),
     ("How is it shipped?", "Cold-packed in a plain box with no product names outside. Most orders arrive two days after they're made."),
     ("Can I cancel?", "Any time before your next refill, from your account or by calling the care team.")]))], "xx-large", "wide", "top")))

kit("assay-states", AK, "Assay states: where providers are licensed",
 "The states where the business can prescribe and ship, as cards with a line about each and a link to its page. Part of the Assay kit; keep the list to the states where providers are licensed.",
 "states, locations, where we treat, licensed, shipping, assay",
 sec("States", N([ahead("Where we treat", "Licensed in four states, with more to come"), grid([acard([h(n, 3, "x-large"), p(d, None, "secondary"), link_p(f"Peptide therapy in {n} →", f"/states/{s}/", None, {"fontWeight": "600"})]) for (n, s), d in zip(ASTATES, [
    "Our home state. Same-week visits, and next-day delivery to Phoenix and Tucson.",
    "Providers licensed across Texas, with two-day delivery to every major city.",
    "Licensed statewide, with cold-packed delivery in two days from Miami to Pensacola.",
    "Providers licensed in Colorado, with two-day delivery including the mountain towns."])], 4, "13rem", "medium")]), "section-tint"))

kit("assay-state", AK, "Assay state: one state, with a map",
 "The body of a page for one state: who the providers are, how fast delivery is, what's available there and a map. Needs the AnyPress Blocks plugin for the map. Part of the Assay kit; make one per state.",
 "state, location, licensed, delivery, map, assay",
 sec("State", cols([
   col(N([alabel("Arizona", "primary"), h("Peptide therapy in Arizona", 2, "xx-large"),
          p("Our home state, and where our medical team works. Visits are usually the same week, and the pharmacy is in Tempe, so most orders reach Phoenix and Tucson the next day.", "medium"),
          afact("Providers", "6 licensed in Arizona"), afact("First visit", "Usually within 2 days"), afact("Delivery", "Next day to Phoenix and Tucson"), afact("Available", "Every treatment"),
          btns([("Start your consultation", None, ASTART)])]), "42%"),
   col(mapb("Phoenix, AZ", 33.4484, -112.0740, 6, "4/3"))], "xx-large", "wide", "top")))

kit("assay-treatment", AK, "Assay treatment: what it is, who it's for and the price",
 "The body of a page for one treatment: what it is, who it may suit and who it doesn't, what's included, a card with the price and how it's taken, safety notes and four photos that open full screen. Part of the Assay kit; make one per treatment and have a provider check every word.",
 "treatment, product, peptide, details, price, safety, assay",
 sec("Treatment", N([cols([
   col(N([h("What NAD+ is", 2, "xx-large"),
          p("NAD+ is a molecule every cell in your body uses to turn food into energy, and levels fall as we age. Our NAD+ is made by a US pharmacy for you alone and taken as a small injection under the skin, a few times a week.", "medium"),
          h("Who it may suit", 3, "large"),
          p("Adults who want to support energy and healthy ageing, alongside sleep, food and exercise. It isn't for people who are pregnant or breastfeeding, or anyone being treated for cancer. Your provider will go through the rest."),
          h("What's included", 3, "large"),
          lst(["A video visit with a licensed provider", "Your medicine, made to order and lab tested", "Syringes, swabs and a sharps box", "A nurse check-in after the first month", "Free cold-packed shipping"])]), "58%"),
   col(acard([alabel("At a glance", "primary"), p("From $149 a month", "x-large", None, None, ASERIF, {"lineHeight": "1.05"}), afact("Taken", "Injection, 3 times a week"), afact("Supply", "30 days"), afact("Prescription", "Required"), afact("Tested", "Every batch"),
              btns([("Start your consultation", None, ASTART), ("Ask a question", "outline", "/contact/")])]))], "xx-large", "wide", "top"),
   grp(N([h("Safety", 3, "large"), p("The most common side effects are redness where you inject and, for some people, mild flushing or nausea. Stop and call us if anything worries you; a nurse answers the same day.", None, "secondary")]), "section-tint", PAD_CARD, "small", {"type": "default"}),
   grid([zoom(img("placeholder-wide.svg", a, "4/3", "md")) for a in ["This treatment: made by the pharmacy", "This treatment: tested by the lab", "This treatment: in your kit", "This treatment: part of your week"]], 2, "18rem", "medium")]), content="80rem"))

kit("assay-plans", AK, "Assay pricing: monthly, three months and membership",
 "Three ways to pay, as cards: month to month, three months at a time with a saving, and a membership with visits included, each with its price, what's included and a button. Part of the Assay kit; state the real prices.",
 "pricing, plans, subscription, membership, prices, offers, assay",
 sec("Pricing", N([ahead("Pricing", "One price, with the visit and shipping in it"),
   grid([acard([alabel(lab, "primary"), h(name, 3, "x-large"), p(price, "xx-large", None, None, ASERIF, {"lineHeight": "1"}), lst(items), btns([(btn, style, ASTART)])], cs) for lab, name, price, items, btn, style, cs in [
     ("Flexible", "Month to month", "From $119", ["Pay as you go, cancel any time", "Visit and shipping included", "Nurse check-in after month one"], "Start monthly", "outline", "section-tint"),
     ("Most chosen", "Three months", "Save 10%", ["Three months shipped together", "Your provider reviews your plan", "Free lab report for your batch"], "Start with three months", None, "section-card"),
     ("Membership", "The whole year", "$49 a month + medicine", ["Unlimited provider messages", "A visit every quarter", "15% off every treatment"], "Become a member", "outline", "section-tint")]], 3, "16rem", "large"),
   p("First visit free if your provider decides a treatment isn't right for you. $50 off your first month with the code from our email list.", "small", "secondary")])))

kit("assay-team", AK, "Assay team: the medical team",
 "The medical and care team with a photo, their name and credentials, their role and a line about them. Part of the Assay kit; use real people and real credentials.",
 "team, doctors, pharmacist, nurse, medical team, about, assay",
 sec("Team", N([ahead("The team", "The people who look after you"), grid([stackg([img("placeholder-tall.svg", f"Team: {n}", "4/5", "md"), h(n, 3, "x-large"), alabel(r, "primary"), p(d, None, "secondary")]) for n, r, d in ATEAM], 3, "14rem", "x-large")])))

kit("assay-standards", AK, "Assay standards: how products are made, tested and sold",
 "How the business keeps a regulated product safe and legal, as six short points: licensed providers, licensed pharmacies, independent labs, honest words, privacy and age checks. Part of the Assay kit; describe what the business really does.",
 "standards, compliance, quality, safety, testing, privacy, assay",
 sec("Standards", N([ahead("Our standards", "Careful about every step"), grid([acard([h(t, 3, "large"), p(d, None, "secondary")], "section-card") for t, d in [
    ("Licensed providers", "Every provider is licensed in the state you live in, and checked again every year."),
    ("Licensed pharmacies", "Medicine is made by state-licensed 503A compounding pharmacies, inspected by their state board."),
    ("Independent labs", "Every batch is tested by a lab we don't own, and every report is published here."),
    ("Honest words", "We say what a treatment is and how it's taken. We never promise results."),
    ("Private by default", "Health records are kept to HIPAA standards and never sold or used for advertising."),
    ("Adults only", "You must be 18 or older, and we check ID before the first prescription.")]], 3, "16rem", "medium")]), "section-tint"))

kit("assay-signup", AK, "Assay signup: $50 off the first month, by email",
 "A band asking visitors to join the email list for $50 off their first month and new lab results, with the signup form beside it. Part of the Assay kit; sits above the footer on every page.",
 "newsletter, signup, email, discount, assay",
 sec("Signup", cols([
   col(N([h("$50 off your first month", 2, "xx-large"), p("Join the list for the code, new lab results and one short email a month. No health details needed.", None, "secondary")]), "55%", valign="center"),
   col(form("newsletter", "See pricing", "/pricing/"), valign="center")], "x-large", "wide", "center"), "section-brand-soft", ("x-large", "x-large", None, None)))

APOP = popup("offer", N([
    img("placeholder-wide.svg", "Gloved hands holding a small glass vial", "16/9"),
    grp(N([alabel("New patients", "primary"), h("$50 off your first month", 2, "xx-large"),
           p("Leave your email and we'll send the code, plus a short guide to how peptide therapy works."),
           form("offer", "See pricing", "/pricing/")]), None, (None, None, "large", "large"), "small", {"type": "default"})]),
    label="$50 off your first month")
kit("assay-popup", AK, "Assay popup: $50 off the first month",
 "A popup that opens five seconds into a first visit with a photo, a first-month discount and one field for an email address; it closes with its button, Escape or a click outside and stays closed for two weeks. Needs the AnyPress Blocks plugin. Part of the Assay kit; put it in the footer to show it on every page.",
 "popup, offer, discount, first order, newsletter, email, modal, assay", APOP)

AFOOT = grp(N([
    BODIES["assay-signup"],
    grp(N([cols([
        col(N([dyn("site-title", {"level": 0, "fontSize": "xx-large", "fontFamily": ASERIF}),
               p("Doctor-led peptide therapy, made by US pharmacies and tested by independent labs.", None, "main-accent"),
               p(f'<a href="{ATL}">' + T(APH) + '</a>', "x-large", None, None, ASERIF, None, raw=True, bind="phone_linked"),
               social(["instagram", "youtube", "facebook"])]), "34%"),
        col(flinks("Treatments", [(n, f"/treatments/{s}/") for n, s, _, _ in ATREAT] + [("Pricing", "/pricing/"), ("Lab results", "/lab-results/")])),
        col(flinks("Company", [("How it works", "/how-it-works/"), ("About us", "/about/"), ("Reviews", "/reviews/"), ("Where we treat", "/states/"), ("Careers", "/careers/"), ("Questions", "/faq/"), ("Learn", "/learn/"), ("Contact", "/contact/")])),
        col(N([h("Care team", 3, "medium"), p(AADDR, None, "main-accent", bind="address"), p(AHOURS, None, "main-accent", bind="hours"),
               btns([("Start your consultation", None, ASTART)])]))], "large", "wide", "top"),
        sep(),
        p(ARULE, "small", "main-accent"),
        row([p("© Tessel Health. Scottsdale, Arizona.", "small", "main-accent"),
             p('<a href="/privacy-policy/">' + T("Privacy") + '</a> · <a href="/lab-results/">' + T("Lab results") + '</a> · <a href="/faq/">' + T("Questions") + '</a>', "small", "main-accent", None, None, None, raw=True)], gap="small")]),
        "section-dark", ("x-large", "large", None, None), "large", {"type": "constrained", "contentSize": "80rem"}, align="full", name="Footer columns"),
    APOP,
]), None, None, "0", {"type": "default"}, align="full", name="Footer")
write("assay-footer", "Assay footer: $50 off by email, links, the compliance notice and the popup",
 "A site footer for a shop that sells regulated health products: a band for the email list, then the care team's number, treatment and company links, the address and hours, the compliance notice on dark, and the first-month popup (needs the AnyPress Blocks plugin). Part of the Assay kit; choose it for the footer in the Site Editor, and add the AnyPress Blocks Age Check block to it if your products are age-restricted.",
 "footer", "footer, links, compliance, disclaimer, newsletter, popup, health, assay", AFOOT, "core/template-part/footer")

kit("assay-jobs", AK, "Assay careers: why work here and the open roles",
 "Why people work at the business, each open role with its hours and pay, and the application. Part of the Assay kit; keep the roles current and put the site's application form in the named Form group.",
 "careers, jobs, hiring, nurse, pharmacist, apply, assay",
 sec("Careers", N([
   ahead("Why work here", "Small team, careful work"),
   grid([stackg([h(t, 3, "large"), p(d, None, "secondary")]) for t, d in [
     ("Work from home", "Providers and the care team work remotely across our four states."),
     ("Time with patients", "Visits are booked for twenty minutes, not five."),
     ("Benefits from day one", "Health, dental and vision, and a 401(k) with a match."),
     ("Pay on the page", "Every role shows its pay, and it's reviewed every year.")]], 4, "13rem"),
   aspacer(),
   h("Open roles", 2, "xx-large"),
   N([grp(N([row([h(t, 3, "large"), alabel(when, "primary")], valign="center"), p(d, None, "secondary"), btns([("Apply for this", None, "#apply")])]), "section-tint", PAD_CARD, "small", {"type": "default"}) for t, when, d in [
     ("Nurse practitioner", "Remote, $62 an hour", "Video visits and plan reviews. Licensed in Arizona, Texas, Florida or Colorado."),
     ("Registered nurse, care team", "Remote, $41 an hour", "Patient check-ins, questions and refills, by phone and message."),
     ("Patient support", "Scottsdale, $22 an hour", "Answer the phone and messages, and help people through their first order.")]]),
   grp(N([h("Apply", 2, "xx-large"), p("Tell us a little about you and which role you'd like. We reply to everyone within a week."),
          form("apply", "Email the team", "mailto:jobs@example.com")]), "section-card", PAD_CARD, "small", {"type": "default"}, anchor="apply")])))

kit("assay-start-form", AK, "Assay start: the consultation form and what happens next",
 "A form to ask for a consultation, beside what happens next and what the first visit costs. Part of the Assay kit; put the site's form in the named Form group and keep health details out of it.",
 "consultation, start, intake, telehealth, form, assay",
 sec("Start", cols([
   col(acard([h("Start your consultation", 2, "xx-large"), p("Tell us which treatment you're curious about and when suits you. A care team member will send your health form and book your video visit."),
              form("quote", "Call " + APH, ATL, "Rather talk first? Call the care team.")], "section-card", "medium"), "58%"),
   col(N([h("What happens next", 3, "large"),
          lst(["We email your health form within the hour", "You meet a licensed provider by video", "If it suits you, the pharmacy starts your order"]),
          h("What it costs", 3, "large"), lst(["The first visit is included in your first month", "Nothing at all if your provider says no", "No membership needed"])]))],
   "xx-large", "wide", "top"), "section-tint"))

kit("assay-contact-full", AK, "Assay contact: phone, email, office and form",
 "A contact section for a regulated health shop: the care team's number, email, office address and hours beside the contact form, then a map. Needs the AnyPress Blocks plugin for the map. Part of the Assay kit.",
 "contact, phone, email, care team, map, form, assay",
 sec("Contact us", N([cols([
   col(N([h("Talk to the care team", 2, "xx-large"), p(f'<a href="{ATL}">' + T(APH) + '</a>', "xx-large", None, None, ASERIF, None, raw=True, bind="phone_linked"),
          p('<a href="mailto:hello@example.com">hello@example.com</a>', None, None, None, None, None, raw=True, bind="email_linked"),
          p(AADDR, None, bind="address"), p(AHOURS, None, "secondary", bind="hours"),
          p("For a medical emergency, call 911. Please don't send health details by email; we'll call you.", "small", "secondary")]), "40%"),
   col(acard([h("Send a message", 3, "large"), form("contact", "Call " + APH, ATL, "We reply the same working day.")], "section-tint", "medium"))], "xx-large", "wide", "top"),
   mapb(AADDR, ALAT, ALON, 14, "21/9")])))

kit("assay-results-full", AK, "Assay lab results: every batch, and how testing works",
 "Every batch's results in a table, then how a batch is tested, step by step, and how to find your batch number. Part of the Assay kit; publish real reports and link each batch to its PDF.",
 "lab results, certificate of analysis, COA, testing, purity, batches, compliance, assay",
 sec("All results", N([
   batch_table(ABATCH + [("TL-2609-30", "Sermorelin 9 mg", "98.9%", "Kestrel Analytical", "Sep 30"), ("TL-2609-22", "Glutathione 1,500 mg", "99.5%", "Saguaro Labs", "Sep 22")]),
   p("Purity by HPLC. Every injectable batch also passed sterility (USP 71) and endotoxin (USP 85) tests. Ask the care team for any report as a PDF.", "small", "secondary"),
   aspacer(),
   cols([col(N([h("How a batch is tested", 2, "xx-large"), lst([
     "The pharmacy makes a batch and holds it",
     "A sample goes to an independent lab we don't own",
     "The lab checks identity, purity, strength, sterility and endotoxins",
     "Only a batch that passes is labelled and shipped",
     "The report is published here the same day"])]), "55%"),
     col(acard([alabel("Your batch", "primary"), h("Find your batch number", 3, "large"), p("It's printed on the side of every vial and box, starting TL-. Match it to the table above."), btns([("Ask for a PDF", "outline", "/contact/")])], "section-tint"))], "xx-large", "wide", "top")]), content="80rem"))

kit("assay-where", AK, "Assay where we treat: the states, with a map",
 "Where the business can prescribe and ship: the states as a list of links beside a map, with a line on delivery times. Needs the AnyPress Blocks plugin for the map. Part of the Assay kit; list only states where providers are licensed.",
 "states, where we treat, locations, licensed, map, assay",
 sec("Where we treat", cols([
   col(N([alabel("Where we treat", "primary"), h("Four states, two-day delivery", 2, "xx-large"),
          p("Our providers are licensed in these states, and the pharmacy ships cold-packed to every one of them in about two days.", "medium"),
          stackg([link_p(f"{n} →", f"/states/{s}/", "large", {"fontWeight": "500"}) for n, s in ASTATES], "x-small"),
          btns([("Where we treat", "outline", "/states/")])]), "40%"),
   col(mapb("Phoenix, AZ", 33.4484, -112.0740, 4, "4/3"))], "xx-large", "wide", "center")))

# The home page.
kit_page("kit-regulated", "Home page: Assay kit, regulated health products",
 "A complete home page for a shop that sells regulated health products (peptides, supplements, CBD) in the Assay kit: a hero with a prescription promise, four promises, treatments with prices, how it works, the latest lab results, numbers that count up, the states it treats in with a map, reviews in a carousel and questions. Apply the Assay style for the look it was designed with.",
 "home, peptides, supplements, cbd, health, wellness, telehealth, regulated, high risk, kit, assay",
 ["assay-hero", "assay-promise", "assay-treatments", "assay-steps", "assay-lab", "assay-numbers", "assay-where", "assay-reviews", "assay-faq-open"])

# ---------------------------------------------------------------- pages
def assay_page(slug, title, desc, kw, parts):
    write(slug, title, desc, "anypress/pages", kw, N(parts), "core/post-content", " * Post Types: page\n")

assay_page("assay-page-services", "Treatments page: Assay kit",
 "A Treatments page for a regulated health shop: a heading, every treatment with its price and a link to its own page, how it works, pricing and reviews. Assay kit.",
 "treatments, products, catalogue, prices, assay",
 [apage_hero("Treatments", "Every treatment is prescribed by a licensed provider, made by a US pharmacy and tested before it ships.", "Treatments", [("Start your consultation", None, ASTART)]),
  BODIES["assay-treatments"], BODIES["assay-steps"], BODIES["assay-plans"], BODIES["assay-reviews"]])

assay_page("assay-page-service", "Treatment page: Assay kit (one treatment)",
 "A page for one treatment, such as NAD+: a heading with a photo, what it is and who it may suit, the price, safety notes, the latest lab results, reviews and questions. Assay kit; make one per treatment.",
 "treatment, product, peptide, details, assay",
 [apage_hero("NAD+", "Small injections at home, a few times a week, for people who want to support energy and healthy ageing.", "Treatments / NAD+", [("Start your consultation", None, ASTART)], "Treatment page: NAD+"),
  BODIES["assay-treatment"], BODIES["assay-lab"], BODIES["assay-reviews"], BODIES["assay-faq-open"]])

assay_page("assay-page-about", "About page: Assay kit",
 "An About page for a regulated health shop: a heading, the story beside a photo, numbers that count up, the medical team, the business's standards and where it treats. Assay kit.",
 "about, our story, team, standards, assay",
 [apage_hero("About Tessel Health", "A doctor, a pharmacist and a nurse who wanted peptide therapy to be as careful as any other medicine.", "About"),
  sec("Story", cols([
    col(N([h("We started with the lab report", 2, "xx-large"),
           p("In 2021 Dr. Maya Okonkwo kept meeting patients who had bought peptides online with no idea what was in the vial. She asked a pharmacist friend, Daniel Reyes, to test a few. Most weren't what the label said.", "large"),
           p("So they built the opposite: a licensed provider for every prescription, a licensed US pharmacy for every batch, and an independent lab report for every vial, published before it ships.")]), "50%", valign="center"),
    col(img("placeholder-tall.svg", "About us: a doctor talking with a patient", "4/5", "md"))], "xx-large", "wide", "center")),
  BODIES["assay-numbers"], BODIES["assay-team"], BODIES["assay-standards"], BODIES["assay-states"]])

assay_page("assay-page-reviews", "Reviews page: Assay kit",
 "A Reviews page for a regulated health shop: a heading, reviews as cards with stars, first names and what each person used, numbers that count up and treatments. Assay kit; use real reviews with permission.",
 "reviews, testimonials, patients, stars, assay",
 [apage_hero("Reviews", "Rated 4.8 out of 5 by more than 1,200 patients. Here's what some of them say, in their own words.", "Reviews", [("Start your consultation", None, ASTART)]),
  sec("All reviews", grid([areview(*r) for r in AREVIEWS + [
    ("I liked that the price on the website was the price I paid. Nothing extra at checkout.", "Priya S.", "NAD+, Houston"),
    ("The nurse check-in after a month was a real conversation, not a survey.", "Tom B.", "Sermorelin, Boulder"),
    ("Being able to look up my batch number online made me trust them straight away.", "Elena R.", "Glutathione, Orlando")]], 3, "18rem", "medium"), "section-tint"),
  sec("Note", p("Reviews describe people's own experience. Results differ from person to person, and your provider will tell you what to expect.", "small", "secondary"), pad=("medium", "medium", None, None)),
  BODIES["assay-numbers"], BODIES["assay-treatments"]])

assay_page("assay-page-areas", "Where we treat page: Assay kit",
 "A Where we treat page for a regulated health shop: a heading, a card for each state where providers are licensed, linking to its own page, standards and questions. Assay kit.",
 "states, locations, where we treat, licensed, assay",
 [apage_hero("Where we treat", "We can only prescribe where our providers are licensed: Arizona, Texas, Florida and Colorado, for now.", "Where we treat"),
  BODIES["assay-states"], BODIES["assay-steps"], BODIES["assay-faq-open"]])

assay_page("assay-page-area", "State page: Assay kit (one state)",
 "A page for one state: a heading with a photo, who the providers are, delivery times and a map, the treatments and reviews. Assay kit; make one per state.",
 "state, location, licensed, delivery, assay",
 [apage_hero("Peptide therapy in Arizona", "Licensed providers, same-week visits and next-day delivery to Phoenix and Tucson.", "Where we treat / Arizona", [("Start your consultation", None, ASTART)], "State page: Arizona"),
  BODIES["assay-state"], BODIES["assay-treatments"], BODIES["assay-reviews"]])

assay_page("assay-page-offers", "Pricing page: Assay kit",
 "A Pricing page for a regulated health shop: a heading, three ways to pay, every treatment with its price, and questions. Assay kit; keep the prices current.",
 "pricing, plans, prices, offers, subscription, assay",
 [apage_hero("Pricing", "One monthly price with the provider, the medicine, the lab test and shipping in it. No surprises at checkout.", "Pricing"),
  BODIES["assay-plans"], BODIES["assay-treatments"], BODIES["assay-faq-open"]])

assay_page("assay-page-join", "Start page: Assay kit",
 "A Get started page for a regulated health shop: a heading, the consultation form beside what happens next, how it works and reviews. Assay kit; put the site's form in the named Form group.",
 "consultation, start, get started, telehealth, assay",
 [apage_hero("Start your consultation", "Free to ask. You only pay if a licensed provider decides a treatment suits you.", "Get started"),
  BODIES["assay-start-form"], BODIES["assay-steps"], BODIES["assay-reviews"]])

assay_page("assay-page-faq", "Questions page: Assay kit",
 "A Questions page for a regulated health shop: answers that open and close, grouped into prescriptions, safety and testing, and orders, and the care team's details. Assay kit; have a provider check the answers.",
 "faq, questions, prescription, safety, shipping, assay",
 [apage_hero("Questions", "About prescriptions, safety, lab testing, shipping and money.", "Questions"),
  sec("Questions", N([N([h(group_t, 2, "xx-large"), accordion(qs)]) for group_t, qs in [
    ("Prescriptions", [
      ("Do I need a prescription?", "Yes, for every injectable treatment. A licensed provider decides at your video visit whether it suits you."),
      ("Who are the providers?", "Doctors and nurse practitioners licensed in the state where you live. Their names are on your visit summary."),
      ("What if the provider says no?", "Then you pay nothing, and they'll tell you why and what else might help.")]),
    ("Safety and testing", [
      ("Are compounded medicines FDA approved?", "No. Compounded medicines are made by a licensed pharmacy for one patient at a time and are not FDA approved. That's why we test every batch and publish the results."),
      ("What does the lab test for?", "Identity, purity, strength, sterility and endotoxins. A batch that fails is destroyed."),
      ("What are the side effects?", "Each treatment page lists the common ones. Your provider goes through them with you, and a nurse answers the phone the same day.")]),
    ("Orders", [
      ("How is it shipped?", "Cold-packed in a plain box with no product names outside. Most orders arrive two days after they're made."),
      ("Can I cancel?", "Any time before your next refill, from your account or by calling the care team."),
      ("Do you take insurance?", "No, but you can pay with an HSA or FSA card, and we'll send a receipt you can claim with.")])]]),
    content="56rem"),
  BODIES["assay-contact-full"]])

assay_page("assay-page-careers", "Careers page: Assay kit",
 "A Careers page for a regulated health shop: a heading, why people work there, the open roles with pay, the application form and the standards. Assay kit; keep the roles current and put the site's form in the named Form group.",
 "careers, jobs, hiring, nurse, assay",
 [apage_hero("Careers", "Remote roles for providers and nurses, and a small team in Scottsdale. Pay is on this page.", "Careers", [("See open roles", None, "#apply")]),
  BODIES["assay-jobs"], BODIES["assay-standards"]])

assay_page("assay-page-contact", "Contact page: Assay kit",
 "A Contact page for a regulated health shop: a heading, the care team's number, email, address and hours beside the contact form, a map and questions. Assay kit; put the site's contact form in the named Form group.",
 "contact, phone, email, care team, assay",
 [apage_hero("Contact", "Call, message or write. A real person on the care team replies the same working day.", "Contact"),
  BODIES["assay-contact-full"], BODIES["assay-faq-open"]])

assay_page("assay-page-results", "Lab results page: Assay kit",
 "A Lab results page for a regulated health shop: a heading, every batch's results in a table, how testing works, the standards and questions. Assay kit; publish real reports.",
 "lab results, certificate of analysis, COA, testing, assay",
 [apage_hero("Lab results", "Every batch, tested by an independent lab and published before it ships. Find yours by the number on the label.", "Lab results", None, "Lab results: a scientist with a tray of samples"),
  BODIES["assay-results-full"], BODIES["assay-standards"], BODIES["assay-faq-open"]])

assay_page("assay-page-how", "How it works page: Assay kit",
 "A How it works page for a regulated health shop: a heading, the steps from first question to delivery, what the first visit is like, pricing and questions. Assay kit.",
 "how it works, process, steps, telehealth, assay",
 [apage_hero("How it works", "From a ten-minute form to a tested medicine at your door, usually in about a week.", "How it works", [("Start your consultation", None, ASTART)], "How it works: a video visit on a laptop"),
  BODIES["assay-steps"],
  sec("First visit", cols([
    col(img("placeholder-wide.svg", "Your first visit: a provider with a patient", "4/3", "md"), "48%"),
    col(N([h("Your first visit", 2, "xx-large"), p("A twenty-minute video call with a licensed provider. They'll ask about your health, your goals and any medicines you take, and tell you honestly whether a treatment suits you.", "medium"),
           lst(["Have a photo ID ready", "Recent blood test results help, but aren't needed", "Ask anything; there's no rush"])]), valign="center")], "xx-large", "wide", "center"), "section-tint"),
  BODIES["assay-lab"], BODIES["assay-plans"], BODIES["assay-faq-open"]])

assay_page("assay-page-thanks", "Thank-you page: Assay kit",
 "The page visitors see after sending a form: thanks, what happens next and when, and links to keep reading. Assay kit; send every form here.",
 "thank you, thanks, confirmation, form sent, assay",
 [sec("Thanks", N([alabel("Message sent", "primary"), h("Thank you. We'll be in touch soon.", 1, "xxx-large"),
    p("A care team member will reply within the hour, Monday to Saturday. Check your email for a copy of what you sent.", "large", "secondary"),
    btns([("Back to the home page", None, "/"), ("See the lab results", "outline", "/lab-results/")])]), None, ("xxx-large", "xxx-large", None, None), "56rem"),
  BODIES["assay-treatments"]])

print("assay ok")
