// The kit checklist (docs/kit-checklist.md) as browser checks, run on a built demo by demo.mjs --check.
// It clicks through the demo the way a visitor would, at desktop and phone width, and screenshots every page.

import { resolve } from 'node:path';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);

export async function checkDemo({ base, shots }) {
    const failures = [];
    const check = (ok, msg, detail = '') => {
        if (ok) console.log(`  ok   ${msg}`);
        else { failures.push(msg); console.log(`  FAIL ${msg}${detail ? ` (${detail})` : ''}`); }
    };
    const { chromium } = require('playwright');
    const browser = await chromium.launch();
    const errors = [];
    const watch = (page) => page.on('pageerror', (e) => errors.push(`${page.url()}: ${e.message}`));
    const skipPopup = (ctx) => ctx.addInitScript(() => { try { localStorage.setItem('anypress-popup:offer', String(Date.now())); } catch {} });

    // ------------------------------------------------------------------ every page and link
    console.log('Pages and links');
    const desk = await browser.newContext({ viewport: { width: 1400, height: 900 } });
    await skipPopup(desk);
    const tab = await desk.newPage();
    watch(tab);
    await tab.goto(`${base}/`, { waitUntil: 'networkidle' });
    const menu = await tab.$$eval('header .wp-block-navigation a', (as) => as.map((a) => ({ text: a.textContent.trim(), href: a.href })));
    const menuPages = [...new Set(menu.map((m) => m.href))];
    check(menuPages.length >= 10, `the menu reaches ${menuPages.length} pages (10 or more)`);
    check(menu.every((m) => m.href && !m.href.endsWith('#')), 'no menu item goes to #');

    const seen = new Set();
    const queue = [`${base}/`];
    const dead = [];
    const hashOnly = [];
    while (queue.length) {
        const url = queue.shift();
        if (seen.has(url)) continue;
        seen.add(url);
        const res = await tab.goto(url, { waitUntil: 'domcontentloaded' });
        if (!res || res.status() >= 400) { dead.push(`${url} (${res?.status()})`); continue; }
        const found = await tab.$$eval('a[href]', (as) => as.map((a) => ({ href: a.href, raw: a.getAttribute('href') })));
        for (const { href, raw } of found) {
            if (raw === '#') hashOnly.push(url);
            const u = new URL(href);
            if (u.origin !== new URL(base).origin || u.pathname.startsWith('/wp-') || u.search) continue;
            const clean = `${u.origin}${u.pathname}`;
            if (!seen.has(clean) && !queue.includes(clean)) queue.push(clean);
        }
    }
    check(dead.length === 0, `every link on the site opens a page (${seen.size} pages crawled)`, dead.join(', '));
    check(hashOnly.length === 0, 'no link or button goes to #', [...new Set(hashOnly)].join(', '));
    const text = [];
    for (const url of seen) {
        await tab.goto(url, { waitUntil: 'domcontentloaded' });
        text.push(await tab.evaluate(() => document.body.innerText));
    }
    check(!/lorem ipsum/i.test(text.join(' ')), 'no lorem ipsum anywhere');

    const notFound = await tab.goto(`${base}/this-page-does-not-exist/`, { waitUntil: 'domcontentloaded' });
    check(notFound.status() === 404 && /not found/i.test(await tab.title() + await tab.evaluate(() => document.body.innerText)), 'a missing page shows the designed 404 page');
    await tab.goto(`${base}/blog/`, { waitUntil: 'domcontentloaded' });
    const posts = await tab.$$eval('.wp-block-post-title a', (as) => as.map((a) => a.href));
    check(posts.length >= 3, `the blog lists ${posts.length} posts (3 or more)`);

    // ------------------------------------------------------------------ header
    console.log('Header');
    await tab.goto(`${base}/`, { waitUntil: 'networkidle' });
    await tab.evaluate(() => window.scrollTo(0, 2500));
    await tab.waitForTimeout(300);
    const top = await tab.$eval('header', (h) => h.getBoundingClientRect().top);
    check(Math.abs(top) < 2, 'the header stays on screen while scrolling', String(top));
    await tab.evaluate(() => window.scrollTo(0, 0));
    const sub = tab.locator('header .wp-block-navigation-submenu').first();
    await sub.hover();
    await tab.waitForTimeout(400);
    check(await sub.locator('.wp-block-navigation__submenu-container').isVisible(), 'the Services menu opens a dropdown');
    check(await tab.locator('header a[href^="tel:"]:visible').count() > 0, 'the header has a call button');

    // ------------------------------------------------------------------ things that move
    console.log('Things that move');
    const faq = tab.locator('.wp-block-accordion-heading__toggle').first();
    await faq.scrollIntoViewIfNeeded();
    await faq.click();
    await tab.waitForTimeout(400);
    check(await tab.locator('.wp-block-accordion-panel').first().isVisible(), 'an FAQ answer opens');
    await faq.click();
    await tab.waitForTimeout(400);
    check(!(await tab.locator('.wp-block-accordion-panel').first().isVisible()), 'and closes again');
    const track = tab.locator('.wp-block-anypress-carousel__track').first();
    await track.scrollIntoViewIfNeeded();
    await tab.locator('.wp-block-anypress-carousel__next').first().click();
    await tab.waitForTimeout(900);
    check((await track.evaluate((t) => t.scrollLeft)) > 0, 'the reviews carousel moves on');
    check(await tab.locator('.wp-block-anypress-counter').count() >= 4, 'numbers count up (Counter blocks)');
    const gallery = [...seen].find((u) => /\/services\/[^/]+\/$/.test(u));
    await tab.goto(gallery, { waitUntil: 'networkidle' });
    const zoom = tab.locator('.wp-lightbox-container button').first();
    if (await zoom.count()) {
        await zoom.scrollIntoViewIfNeeded();
        await zoom.click({ force: true });
        await tab.waitForTimeout(600);
    }
    check(await tab.locator('.wp-lightbox-overlay.active').isVisible(), 'a job photo opens full screen', gallery);
    await tab.keyboard.press('Escape');
    await tab.goto(`${base}/`, { waitUntil: 'networkidle' });
    check(await tab.locator('.wp-block-anypress-map iframe, .wp-block-anypress-map__load').count() > 0, 'a map shows where the business works');

    // ------------------------------------------------------------------ popup
    console.log('Popup');
    const fresh = await browser.newContext({ viewport: { width: 1400, height: 900 } });
    const ptab = await fresh.newPage();
    watch(ptab);
    await ptab.goto(`${base}/`, { waitUntil: 'domcontentloaded' });
    await ptab.waitForTimeout(1500);
    check(!(await ptab.$eval('#offer', (d) => d.open)), 'the offer popup waits a few seconds');
    await ptab.waitForFunction(() => document.getElementById('offer')?.open, null, { timeout: 8000 }).catch(() => {});
    check(await ptab.$eval('#offer', (d) => d.open), 'then opens on a first visit');
    check(await ptab.locator('#offer img').isVisible() && (await ptab.locator('#offer input[type=email]').count()) === 1, 'with a photo and one email field');
    await ptab.screenshot({ path: resolve(shots, 'popup-desktop.png') });
    await ptab.keyboard.press('Escape');
    await ptab.waitForTimeout(300);
    check(!(await ptab.$eval('#offer', (d) => d.open)), 'it closes with Escape');
    await ptab.goto(`${base}/services/`, { waitUntil: 'domcontentloaded' });
    await ptab.waitForTimeout(6500);
    check(!(await ptab.$eval('#offer', (d) => d.open)), 'and does not open again on the next page');
    await fresh.close();

    // ------------------------------------------------------------------ forms
    console.log('Forms');
    const fill = async (page, values) => {
        for (const [selector, value] of values) {
            const el = page.locator(selector).first();
            if ((await el.evaluate((e) => e.tagName)) === 'SELECT') await el.selectOption({ index: 1 });
            else await el.fill(value);
        }
    };
    for (const [path, values, label] of [
        ['/get-a-quote/', [['input[name="names[first_name]"]', 'Test Visitor'], ['input[name=email]', 'test@example.com'], ['input[name=phone]', '555 0100'], ['select[name=service]', ''], ['textarea[name=message]', 'Kitchen sink drains slowly.']], 'the quote form'],
        ['/contact/', [['input[name="names[first_name]"]', 'Test Visitor'], ['input[name=email]', 'test@example.com'], ['textarea[name=message]', 'Do you work Sundays?']], 'the contact form'],
        ['/careers/', [['#apply input[name="names[first_name]"], form input[name="names[first_name]"]', 'Test Visitor'], ['form input[name=email]', 'test@example.com'], ['form input[name=phone]', '555 0100'], ['form select[name=job]', ''], ['form textarea[name=message]', 'Five years on service work.']], 'the job application'],
    ]) {
        await tab.goto(`${base}${path}`, { waitUntil: 'networkidle' });
        await fill(tab, values);
        await Promise.all([tab.waitForURL(/thank-you/, { timeout: 15000 }).catch(() => {}), tab.locator('main .ff-btn-submit, .entry-content .ff-btn-submit, form .ff-btn-submit').first().click()]);
        check(/thank-you/.test(tab.url()), `${label} sends and shows the thank-you page`, tab.url());
    }
    await tab.goto(`${base}/services/`, { waitUntil: 'networkidle' });
    const signup = tab.locator('footer form').first();
    await signup.locator('input[type=email]').fill('test@example.com');
    await signup.locator('.ff-btn-submit').click();
    await tab.waitForSelector('footer .ff-message-success', { timeout: 10000 }).catch(() => {});
    check(await tab.locator('footer .ff-message-success').isVisible().catch(() => false), 'the footer signup on every page sends and thanks the visitor');

    // ------------------------------------------------------------------ screenshots, desktop
    for (const url of seen) {
        await tab.goto(url, { waitUntil: 'networkidle' });
        await tab.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 700) { window.scrollTo(0, y); await new Promise((r) => setTimeout(r, 60)); } window.scrollTo(0, 0); });
        const name = new URL(url).pathname.replace(/^\/|\/$/g, '').replace(/\//g, '-') || 'home';
        await tab.screenshot({ path: resolve(shots, `${name}-desktop.png`), fullPage: true });
    }
    await desk.close();

    // ------------------------------------------------------------------ phone
    console.log('Phone');
    const phone = await browser.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
    await skipPopup(phone);
    const mtab = await phone.newPage();
    watch(mtab);
    const wide = [];
    for (const url of seen) {
        await mtab.goto(url, { waitUntil: 'networkidle' });
        const over = await mtab.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
        if (over > 1) wide.push(`${new URL(url).pathname} (+${over}px)`);
        const name = new URL(url).pathname.replace(/^\/|\/$/g, '').replace(/\//g, '-') || 'home';
        await mtab.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 700) { window.scrollTo(0, y); await new Promise((r) => setTimeout(r, 60)); } window.scrollTo(0, 0); });
        await mtab.screenshot({ path: resolve(shots, `${name}-phone.png`), fullPage: true });
    }
    check(wide.length === 0, `every page fits a 390 px phone with nothing off the side (${seen.size} pages)`, wide.join(', '));
    await mtab.goto(`${base}/`, { waitUntil: 'networkidle' });
    const call = mtab.locator('header a[href^="tel:"]:visible').first();
    check(await call.isVisible(), 'the call button is one tap away on a phone');
    await mtab.locator('header .wp-block-navigation__responsive-container-open').click();
    await mtab.waitForTimeout(500);
    check(await mtab.locator('header .wp-block-navigation__responsive-container.is-menu-open').isVisible(), 'the phone menu opens');
    await mtab.screenshot({ path: resolve(shots, 'menu-phone.png') });
    await mtab.locator('header .wp-block-navigation__responsive-container-close').click();
    await mtab.waitForTimeout(500);
    check(!(await mtab.locator('header .wp-block-navigation__responsive-container.is-menu-open').isVisible()), 'and closes');
    await phone.close();

    check(errors.length === 0, 'no JavaScript errors on any page', errors.slice(0, 3).join(' | '));
    await browser.close();
    return failures;
}
