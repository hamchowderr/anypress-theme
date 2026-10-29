# Kit checklist

A kit is done when its demo feels like a real business website, not a home page with placeholders. Someone who lands on the demo should be able to click every menu item, open every button, fill in every form and get a popup, on a phone as well as a computer. Check every item below on the running demo, by clicking through it, before a kit ships.

## A real website experience

- [ ] **Every menu item opens a finished page.** At least 10 pages, matched to the business. For a local trade: Home, Services (and one page per main service), About, Reviews, Service areas, Special offers, Book or Get a quote, FAQ, Careers, Blog, Contact. No menu item, button or link goes to `#` or to a page that does not exist.
- [ ] **A popup.** A newsletter or offer popup opens a few seconds after the first visit, with a photo, one field and a clear close button. It closes with the close button, the Escape key and a click outside, and it does not open again on every page.
- [ ] **Working forms.** A booking or quote form with real fields (name, email, phone, service, date, message), a contact form, and a newsletter signup in the footer of every page. Each one submits and shows a thank-you message.
- [ ] **Header.** The header stays on screen while scrolling, has a main button (Book, Get a quote, Call), and opens dropdown menus where a section has several pages.
- [ ] **Phone.** The phone menu opens and closes, every page reads at 390 px wide with nothing running off the side, and the main action (Call, Book) is one tap away.
- [ ] **Things that move when touched.** FAQ answers open and close; reviews or projects scroll in a carousel; numbers count up; a hero video or gallery opens full screen; a map shows on the Service areas or Contact page.
- [ ] **Real content, not filler.** Business name, services, prices, team with photos, reviews with names, 3 or more blog posts that open, and no lorem ipsum anywhere.
- [ ] **The odd pages.** A designed 404 page and a thank-you page after each form.

## Design

- [ ] Compared side by side with the reference kits (Darrel Wilson's for the same trade) and holds up on first look.
- [ ] Photos lead most sections; every photo fits the business.
- [ ] Only theme tokens: colours, fonts, sizes and spacing from `theme.json`, so the Site Editor and the site tools can restyle it.
- [ ] Every colour pair passes WCAG AA (`npm run contrast`).

## Checks that run by themselves

`cd tests && npm run theme` must pass: valid blocks, tokens only, descriptions and keywords, in-page links that reach their sections, no PHP errors, no sideways scroll on a phone.

## How to check a kit by hand

Open the demo in a browser at desktop width and at 390 px. Wait for the popup, close it, then click every menu item, every button and every link, fill in and send every form, open every FAQ answer, gallery and video, and scroll each page to the bottom. Note anything that goes nowhere or looks unfinished, fix it, and check again.
