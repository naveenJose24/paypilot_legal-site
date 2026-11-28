"""Add contextual internal links between PayPilot's tools, guides and homepage.

Idempotent: each block is wrapped in <!-- il:NAME --> ... <!-- /il:NAME --> and replaced on re-run.
Run after tool/build_guides.py:  python3 tool/add_internal_links.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TOOLS = {
    "emi-calculator": ("Loan tool", "EMI calculator", "Monthly EMI, total interest and total cost for personal, car and home loans in AED or INR."),
    "uae-gratuity-calculator": ("UAE tool", "UAE gratuity calculator", "Estimate end-of-service gratuity in Dubai, Abu Dhabi and Sharjah, including DIFC rules."),
    "budget-calculator": ("Budget tool", "Salary budget & safe-to-spend calculator", "Split your salary into bills, savings and what is safe to spend each day."),
    "sms-expense-tracker-iphone": ("iPhone guide", "Track bank SMS expenses on iPhone", "Log bank SMS and Apple Pay payments automatically with a one-time Shortcuts setup."),
}

# guide slug -> (eyebrow, title)
GUIDES = {}
for f in sorted((ROOT / "blog").glob("*.html")):
    if f.name == "index.html":
        continue
    html = f.read_text()
    t = re.search(r"<h1>(.*?)</h1>", html)
    e = re.search(r'<span class="eyebrow">([^<·]+)', html)
    GUIDES[f.stem] = ((e.group(1).strip() if e else "Guide"), (t.group(1) if t else f.stem))

RULES = [  # keyword in guide slug -> tools to recommend
    (("loan", "emi", "repayment", "credit-card"), ["emi-calculator", "budget-calculator"]),
    (("uae", "aed", "dubai", "expat", "nri", "rent"), ["uae-gratuity-calculator", "budget-calculator"]),
    (("sms", "bank", "automatic", "money-manager"), ["sms-expense-tracker-iphone", "budget-calculator"]),
    (("budget", "cash-flow", "income", "freelancer", "spend", "subscription"), ["budget-calculator", "emi-calculator"]),
]

TOOL_GUIDES = {  # guides to show on each tool page
    "emi-calculator": ["loan-tracker-money-lent", "credit-card-spending-tracker", "dubai-salary-budget"],
    "uae-gratuity-calculator": ["nri-expense-tracker-uae-india", "dubai-salary-budget", "best-expense-tracker-app-uae"],
    "budget-calculator": ["dubai-salary-budget", "safe-to-spend-calculator", "freelancer-variable-income-tracker"],
    "sms-expense-tracker-iphone": ["automatic-expense-tracker-bank-sms", "is-sms-expense-tracker-safe", "best-expense-tracker-app-india"],
}


def card(href, eyebrow, title, desc=""):
    p = f"<p>{desc}</p>" if desc else ""
    return f'<a class="card card-link" href="{href}"><span class="eyebrow">{eyebrow}</span><h3>{title}</h3>{p}</a>'


def block(name, eyebrow, heading, cards, extra=""):
    return (f'<!-- il:{name} --><section class="section{extra}"><div class="section-head"><span class="eyebrow">{eyebrow}</span>'
            f'<h2>{heading}</h2></div><div class="grid">{"".join(cards)}</div></section><!-- /il:{name} -->')


def put(html, name, new, before):
    html = re.sub(rf"<!-- il:{name} -->.*?<!-- /il:{name} -->", "", html, flags=re.S)
    i = html.find(before)
    if i < 0:
        raise SystemExit(f"anchor not found for {name}: {before[:40]}")
    return html[:i] + new + html[i:]


def tools_for(slug):
    for keys, tools in RULES:
        if any(k in slug for k in keys):
            return tools
    return ["budget-calculator", "sms-expense-tracker-iphone"]


changed = 0
# 1. Homepage: free tools + popular guides
idx = ROOT / "index.html"
html = idx.read_text()
cards = [card(s, *TOOLS[s]) for s in TOOLS]
html = put(html, "tools", block("tools", "Free tools", "Free money calculators and guides", cards, " page-shell"), '<section class="landing-guides')
popular = ["best-expense-tracker-app-uae", "best-expense-tracker-app-india", "automatic-expense-tracker-bank-sms",
           "subscription-tracker-monthly-bills", "loan-tracker-money-lent", "is-sms-expense-tracker-safe"]
pcards = [card(f"blog/{s}", *GUIDES[s]) for s in popular if s in GUIDES]
html = put(html, "popular", block("popular", "Popular guides", "Start with these money guides", pcards, " page-shell"), '</main>')
idx.write_text(html); changed += 1

# 2. Tool pages: other tools + related guides
for slug in TOOLS:
    f = ROOT / f"{slug}.html"
    html = f.read_text()
    cards = [card(s, *TOOLS[s]) for s in TOOLS if s != slug]
    cards += [card(f"blog/{g}", *GUIDES[g]) for g in TOOL_GUIDES[slug] if g in GUIDES]
    html = put(html, "more", block("more", "Keep going", "More free tools and guides", cards), "</main>")
    f.write_text(html); changed += 1

# 3. Guides: two relevant tools before "Keep reading"
for slug in GUIDES:
    f = ROOT / "blog" / f"{slug}.html"
    html = f.read_text()
    cards = [card(f"../{t}", *TOOLS[t]) for t in tools_for(slug)]
    html = put(html, "tools", block("tools", "Free tools", "Try the free calculator", cards),
               '<section class="section"><div class="section-head"><span class="eyebrow">Keep reading')
    f.write_text(html); changed += 1

print("updated", changed, "pages")
