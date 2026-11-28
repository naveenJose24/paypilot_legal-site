"""Build PayPilot's money guides from tool/guides_*.py.

Writes blog/<slug>.html for each guide, refreshes the cards on blog/index.html,
removes merged guides, writes _redirects (301s from merged slugs) and updates sitemap.xml.
Then run: python3 tool/add_internal_links.py
"""
import json
import re
import sys
from html import escape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from guides_a import GUIDES_A  # noqa: E402
from guides_b import GUIDES_B  # noqa: E402
from guides_c import GUIDES_C, REDIRECTS  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
BLOG = ROOT / "blog"
BASE = "https://paypilot.appgenie.in"
PUBLISHED = "2026-10-01"
UPDATED = "2026-11-28"
UPDATED_TEXT = "Updated 28 November 2026"
GUIDES = GUIDES_A + GUIDES_B + GUIDES_C
BY_SLUG = {g["slug"]: g for g in GUIDES}

index_html = (BLOG / "index.html").read_text()
HEADER = index_html[index_html.find("<header"):index_html.find("</header>") + 9]
FOOTER = index_html[index_html.find("<footer"):index_html.find("</body>")]
HEAD_ASSETS = ('<link rel="icon" type="image/png" href="../paypilot_logo.png"><link rel="preconnect" href="https://fonts.googleapis.com">'
               '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800&display=swap" rel="stylesheet">')


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + "</script>"


def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


def image(slug):
    p = f"images/blog-generated/{slug}.webp"
    return p if (ROOT / p).exists() else "images/blog-generated/spending.webp"


def card(g):
    return (f'<a class="card card-link" href="{g["slug"]}"><span class="eyebrow">{escape(g["category"])}</span>'
            f'<h3>{escape(g["title"])}</h3><p>{escape(g["desc"])}</p></a>')


def article(g):
    slug, title, desc = g["slug"], g["title"], g["desc"]
    assert len(desc) <= 155, (slug, len(desc))
    url = f"{BASE}/blog/{slug}"
    img = image(slug)
    toc = "".join(f'<a href="#{sid}">{escape(h)}</a>' for sid, h, _ in g["sections"]) + '<a href="#faq">FAQ</a>'
    sections = "".join(f'<section id="{sid}"><h2>{escape(h)}</h2>{body.strip()}</section>' for sid, h, body in g["sections"])
    faq = "".join(f"<details><summary>{escape(q)}</summary><p>{a}</p></details>" for q, a in g["faq"])
    related = "".join(card(BY_SLUG[s]) for s in g["related"])
    schema = [
        {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc, "image": [f"{BASE}/{img}"],
         "datePublished": PUBLISHED, "dateModified": UPDATED, "author": {"@type": "Organization", "name": "PayPilot"},
         "publisher": {"@type": "Organization", "name": "AppGenie", "logo": {"@type": "ImageObject", "url": f"{BASE}/paypilot_logo.png"}},
         "articleSection": g["category"], "mainEntityOfPage": url},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "PayPilot", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": "Money guides", "item": f"{BASE}/blog/"},
            {"@type": "ListItem", "position": 3, "name": title, "item": url}]},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in g["faq"]]},
    ]
    t, d = escape(title), escape(desc)
    head = (f'<!doctype html>\n<html lang="en"><head>{HEAD_ASSETS}<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<meta name="description" content="{d}"><meta name="robots" content="index,follow"><link rel="canonical" href="{url}">'
            f'<meta property="og:type" content="article"><meta property="og:title" content="{t} — PayPilot"><meta property="og:description" content="{d}">'
            f'<meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}/{img}"><meta name="twitter:card" content="summary_large_image">'
            f'<meta name="twitter:title" content="{t} — PayPilot"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{BASE}/{img}">'
            f'<title>{t} — PayPilot</title><link rel="stylesheet" href="../styles.css">{"".join(ld(s) for s in schema)}<script async src="/clarity.js"></script></head>\n')
    main = (f'<main class="page-shell"><article class="blog-article"><div class="blog-hero"><div><span class="eyebrow">{escape(g["category"])} · PayPilot money guide</span>'
            f'<h1>{t}</h1><p class="lede">{escape(g["lede"])}</p><p class="meta">{UPDATED_TEXT} · By the PayPilot team</p></div>'
            f'<img class="blog-art" src="../{img}" alt="Illustration for {t}" width="800" height="1417"></div>'
            f'<div class="blog-layout"><aside class="toc" aria-label="On this page"><strong>On this page</strong>{toc}</aside>'
            f'<div class="legal-content">{sections}<section id="faq"><h2>Frequently asked questions</h2><div class="faq-list">{faq}</div></section>'
            '<section><div class="callout warning"><p><strong>Important:</strong> PayPilot is a tracking and organisation tool, not a bank, lender, tax adviser or investment adviser. '
            'Figures in this guide are examples. Check important details against official records and get professional advice for your own situation.</p></div></section>'
            '</div></div></article>'
            f'<section class="section"><div class="section-head"><span class="eyebrow">Keep reading</span><h2>Related money guides</h2></div><div class="grid">{related}</div></section></main>')
    return head + f"<body>{HEADER}{main}{FOOTER}</body></html>\n"


def tags(g):
    return g["tags"]


def main():
    for s in REDIRECTS.values():
        assert s in BY_SLUG, s
    for g in GUIDES:
        for r in g["related"]:
            assert r in BY_SLUG and r != g["slug"], (g["slug"], r)
        (BLOG / f"{g['slug']}.html").write_text(article(g), encoding="utf-8")

    removed = 0
    for old in REDIRECTS:
        f = BLOG / f"{old}.html"
        if f.exists():
            f.unlink(); removed += 1

    # blog index cards
    cards = "".join(
        f'<a class="card card-link blog-card" data-category="{tags(g)}" href="{g["slug"]}"><img src="../{image(g["slug"])}" alt="Illustration for {escape(g["title"])}" '
        f'width="800" height="1417" loading="lazy"><span class="eyebrow">{escape(g["category"])}</span><h2>{escape(g["title"])}</h2><p>{escape(g["desc"])}</p>'
        f'<span class="read-more">Read guide →</span></a>' for g in GUIDES)
    idx = (BLOG / "index.html").read_text()
    idx, n = re.subn(r'(<div class="blog-grid">).*?(</div></section>)', lambda m: m.group(1) + cards + m.group(2), idx, count=1, flags=re.S)
    assert n == 1
    (BLOG / "index.html").write_text(idx, encoding="utf-8")

    # redirects (Cloudflare _redirects)
    lines = ["# Guides merged on 2026-11-28"]
    for old, new in REDIRECTS.items():
        lines += [f"/blog/{old} /blog/{new} 301", f"/blog/{old}.html /blog/{new} 301"]
    (ROOT / "_redirects").write_text("\n".join(lines) + "\n")

    # sitemap
    sm = (ROOT / "sitemap.xml").read_text()
    for old in REDIRECTS:
        sm = re.sub(rf"<url><loc>{re.escape(BASE)}/blog/{old}</loc>.*?</url>", "", sm)
    for slug in list(BY_SLUG) + [""]:
        sm = re.sub(rf"(<url><loc>{re.escape(BASE)}/blog/{slug}</loc><lastmod>)[^<]*", rf"\g<1>{UPDATED}", sm)
    (ROOT / "sitemap.xml").write_text(sm)
    print(f"built {len(GUIDES)} guides, removed {removed}, {len(REDIRECTS)} redirects")


if __name__ == "__main__":
    main()
