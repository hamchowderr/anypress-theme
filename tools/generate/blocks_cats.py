# AnyPress Blocks: every shared (non-kit) section goes in one of these groups. Core categories stay alongside
# (footer patterns need "footer" to be offered for the footer template part).
import os, re, sys
GROUPS = {
 "heroes": ["hero-cover", "hero-split", "hero-statement"],
 "about": ["about-story", "team", "text-statement", "gallery-grid"],
 "services": ["services-list", "menu", "features-text", "steps", "pricing-plans", "product-box"],
 "proof": ["credentials", "reviews-three", "testimonial-single", "logo-row", "numbers-band"],
 "calls-to-action": ["call-to-action-dark", "call-to-action-split", "newsletter-signup", "social-follow", "notice"],
 "contact": ["contact-details", "contact-form-section", "faq"],
 "blog": ["latest-posts", "author-box", "pros-cons", "table-of-contents"],
 "footers": ["footer-columns", "footer-small"],
}
OLD = {"anypress-heroes", "anypress-proof", "anypress-details"}
def apply(folder):
    for group, slugs in GROUPS.items():
        for slug in slugs:
            f = os.path.join(folder, slug + ".php"); s = open(f).read()
            m = re.search(r"^ \* Categories: (.*)$", s, re.M)
            cats = [c.strip() for c in m.group(1).split(",") if c.strip() not in OLD and not c.strip().startswith("anypress/blocks-")]
            cats = [f"anypress/blocks-{group}"] + cats
            s = s[:m.start(1)] + ", ".join(cats) + s[m.end(1):]
            open(f, "w").write(s)
if __name__ == "__main__":
    apply(sys.argv[1])
