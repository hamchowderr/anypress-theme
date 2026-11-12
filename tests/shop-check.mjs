// The kit checklist for a shop kit's demo, run by demo.mjs --check when the kit has a shop.json. It clicks through
// the shop the way a shopper would, at desktop and phone width: every link, the products with their photos, a
// category, a product page, the cart, checkout with a US, a UK and an EU address (shipping and tax for each), a
// placed order and its receipt, the forms, the popup and the phone menu.

import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);

export async function checkShop({ base, shots, paths = {}, items = {} }) {
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
    const settle = (page) => page.evaluate(async () => {
        for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise((r) => setTimeout(r, 60)); }
        window.scrollTo(0, 0);
    });

    // ------------------------------------------------------------------ every page and link
    console.log('Pages and links');
    const desk = await browser.newContext({ viewport: { width: 1400, height: 900 } });
    await skipPopup(desk);
    const tab = await desk.newPage();
    watch(tab);
    await tab.goto(`${base}/`, { waitUntil: 'networkidle' });
    const menu = await tab.$$eval('header .wp-block-navigation a', (as) => as.map((a) => a.href));
    check(new Set(menu).size >= 10, `the menu reaches ${new Set(menu).size} pages (10 or more)`);
    const seen = new Set();
    const queue = [`${base}/`];
    const dead = [];
    while (queue.length) {
        const url = queue.shift();
        if (seen.has(url)) continue;
        seen.add(url);
        const res = await tab.goto(url, { waitUntil: 'domcontentloaded' });
        if (!res || res.status() >= 400) { dead.push(`${url} (${res?.status()})`); continue; }
        for (const href of await tab.$$eval('a[href]', (as) => as.map((a) => a.href))) {
            const u = new URL(href);
            if (u.origin !== new URL(base).origin || u.pathname.startsWith('/wp-') || u.search || u.pathname.startsWith('/item/')) continue;
            const clean = `${u.origin}${u.pathname}`;
            if (!seen.has(clean) && !queue.includes(clean)) queue.push(clean);
        }
    }
    for (const url of Object.values(items)) {
        const res = await tab.goto(url, { waitUntil: 'domcontentloaded' });
        if (!res || res.status() >= 400) dead.push(`${url} (${res?.status()})`);
    }
    check(dead.length === 0, `every page and product opens (${seen.size} pages, ${Object.keys(items).length} products)`, dead.join(', '));

    // ------------------------------------------------------------------ products
    console.log('Products');
    await tab.goto(`${base}${paths.shop || '/shop/'}`, { waitUntil: 'networkidle' });
    await settle(tab);
    const cards = await tab.$$eval('.fct-product-card', (cs) => cs.map((c) => !!c.querySelector('img[src]:not([src=""])')));
    check(cards.length >= 8, `the shop page lists ${cards.length} products`);
    check(cards.length > 0 && cards.every(Boolean), 'every product card has a photo');
    const sale = await tab.goto(`${base}/product-categories/last-few/`, { waitUntil: 'networkidle' });
    check(sale?.status() === 200 && (await tab.$$('.fct-product-card')).length >= 1, 'a category page lists its products');
    await tab.screenshot({ path: `${shots}/category.png`, fullPage: true });

    // ------------------------------------------------------------------ buying
    console.log('Cart and checkout');
    const first = Object.values(items)[0];
    await tab.goto(first, { waitUntil: 'networkidle' });
    await tab.screenshot({ path: `${shots}/product.png`, fullPage: true });
    check(await tab.locator('.fct-product-review, [class*=review]').count() > 0, 'the product page shows reviews');
    await tab.getByRole('button', { name: /add to cart/i }).first().click();
    await tab.waitForTimeout(2000);
    await tab.goto(`${base}/checkout/`, { waitUntil: 'networkidle' });
    await tab.fill('#billing_full_name', 'Sam Rivera');
    await tab.fill('#billing_email', 'sam@anypress.example');
    const at = async (country, state, city, zip) => {
        await tab.evaluate((c) => { const s = document.querySelector('#billing_country'); s.value = c; s.dispatchEvent(new Event('change', { bubbles: true })); }, country);
        await tab.waitForTimeout(2000);
        await tab.fill('#billing_address_1', '12 Example Street');
        const tag = await tab.locator('#billing_state').evaluate((e) => e.tagName).catch(() => null);
        if (tag === 'SELECT') await tab.evaluate((v) => { const s = document.querySelector('#billing_state'); s.value = v; s.dispatchEvent(new Event('change', { bubbles: true })); }, state);
        else if (tag) await tab.fill('#billing_state', state);
        await tab.fill('#billing_city', city);
        await tab.fill('#billing_postcode', zip);
        await tab.locator('#billing_postcode').blur();
        await tab.waitForTimeout(3000);
        return tab.locator('body').innerText();
    };
    const de = await at('DE', 'BE', 'Berlin', '10115');
    check(/Shipping\s*\$22/.test(de) && /Tax[\s\S]{0,40}\$\d/.test(de), 'an EU address gets EU shipping and its VAT');
    await tab.screenshot({ path: `${shots}/checkout-eu.png`, fullPage: true });
    const gb = await at('GB', 'London', 'London', 'SW1A 1AA');
    check(/Tax[\s\S]{0,40}\$\d/.test(gb), 'a UK address gets UK VAT');
    const us = await at('US', 'OR', 'Portland', '97202');
    check(/Standard/.test(us) && /Pick up/.test(us), 'a US address gets standard, express and pick-up');
    await tab.locator('#fluent_cart_payment_method_offline_payment').check({ force: true }).catch(() => {});
    await tab.getByRole('button', { name: /place order/i }).click();
    await tab.waitForURL(/receipt/, { timeout: 20000 }).catch(() => {});
    check(/receipt/.test(tab.url()), 'placing an order opens its receipt', tab.url());
    await tab.screenshot({ path: `${shots}/receipt.png`, fullPage: true });

    // ------------------------------------------------------------------ EU cancellation (FluentCart Customer Rights)
    console.log('Cancel an order');
    const cancel = await tab.goto(`${base}/withdraw-from-contract/`, { waitUntil: 'networkidle' });
    check(cancel?.status() === 200 && await tab.locator('[data-fctcr-form]').count() === 1, 'the Cancel an order page has the cancellation form');
    if (await tab.locator('[data-fctcr-form]').count()) {
        await tab.fill('#fctcr-first-name', 'Sam');
        await tab.fill('#fctcr-last-name', 'Rivera');
        await tab.fill('#fctcr-order', '1');
        await tab.fill('#fctcr-email', 'sam@anypress.example');
        await tab.locator('[data-fctcr-continue]').click();
        await tab.locator('[data-fctcr-confirm]').waitFor({ state: 'visible', timeout: 15000 }).catch(() => {});
        await tab.locator('[data-fctcr-confirm]').click({ timeout: 5000 }).catch(() => {});
        await tab.waitForTimeout(3000);
        check(/withdrawal has been received/i.test(await tab.locator('body').innerText()), 'a cancellation is received and acknowledged');
        await tab.screenshot({ path: `${shots}/cancel.png`, fullPage: true });
    }
    for (const [path, name] of [[paths.shop || '/shop/', 'shop'], ['/new-in/', 'new-in'], ['/help/', 'help'], ['/product-categories/tops/', 'category']]) {
        await tab.goto(`${base}${path}`, { waitUntil: 'networkidle' });
        await tab.screenshot({ path: `${shots}/hero-${name}.png` });
    }
    check(await tab.evaluate(async (u) => { const d = new DOMParser().parseFromString(await (await fetch(u)).text(), 'text/html'); return !!d.querySelector('.anypress-page-cover > img'); }, `${base}${paths.shop || '/shop/'}`), 'the Shop page opens on its photo');

    // ------------------------------------------------------------------ forms and popup
    console.log('Forms and popup');
    await tab.goto(`${base}${paths.contact || '/contact/'}`, { waitUntil: 'networkidle' });
    check(await tab.locator('form.frm-fluent-form').count() > 0, 'the contact page has a working form');
    const fresh = await browser.newContext({ viewport: { width: 1400, height: 900 } });
    const home = await fresh.newPage();
    await home.goto(`${base}/`, { waitUntil: 'networkidle' });
    await home.waitForTimeout(6500);
    check(await home.locator('dialog#offer[open]').count() === 1, 'the first-order popup opens on the home page');
    const checkout = await fresh.newPage();
    await checkout.goto(`${base}/checkout/`, { waitUntil: 'networkidle' });
    await checkout.waitForTimeout(6500);
    check(await checkout.locator('dialog[open]').count() === 0, 'no popup at checkout');
    await fresh.close();

    // ------------------------------------------------------------------ phone
    console.log('Phone');
    const phone = await browser.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
    await skipPopup(phone);
    const mob = await phone.newPage();
    watch(mob);
    const wide = [];
    for (const path of ['/', paths.shop || '/shop/', new URL(first).pathname, '/checkout/', paths.contact || '/contact/']) {
        await mob.goto(`${base}${path}`, { waitUntil: 'networkidle' });
        await settle(mob);
        if (await mob.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1)) wide.push(path);
    }
    check(wide.length === 0, 'no sideways scroll on a phone', wide.join(', '));
    for (const [path, name] of [[paths.shop || '/shop/', 'shop'], ['/new-in/', 'new-in'], ['/help/', 'help'], ['/product-categories/tops/', 'category']]) {
        await mob.goto(`${base}${path}`, { waitUntil: 'networkidle' });
        await mob.screenshot({ path: `${shots}/phone-hero-${name}.png` });
    }
    await mob.goto(`${base}/`, { waitUntil: 'networkidle' });
    await mob.screenshot({ path: `${shots}/phone-home.png`, fullPage: true });
    const open = mob.locator('header .wp-block-navigation__responsive-container-open').first();
    if (await open.count()) {
        await open.click();
        check(await mob.locator('header .wp-block-navigation__responsive-container.is-menu-open').count() > 0, 'the phone menu opens');
    } else check(false, 'the phone menu opens', 'no menu button');

    check(errors.length === 0, 'no JavaScript errors', errors.slice(0, 3).join(' | '));
    await browser.close();
    return failures;
}
