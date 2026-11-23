#!/usr/bin/env python3
"""Builds the partner resource pages (/alloy/, /rise/).

To add a handout:
  1. Put the PDF in /resources/files/ (lowercase-with-dashes name, US Letter).
  2. Make a thumbnail of page 1:
       pdftoppm -f 1 -l 1 -r 80 -jpeg -singlefile resources/files/NAME.pdf resources/img/NAME
  3. Add an entry to RESOURCES below (newest first), then run: python3 _src/partner-resources/build.py
Every partner page gets every resource unless the entry lists "partners".

To add a partner: add an entry to PARTNERS and run the script. The page appears at /<slug>/.
"""
import html, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]

# Paste the JotForm link here once the "Request a resource" form exists.
REQUEST_FORM_URL = "https://form.jotform.com/SouthwestDietitianGroup/request-a-resource"
CONSULT_URL = "https://sdg.intakeq.com/booking?serviceId=68c0e8e5-5097-4298-bee4-f5482008c1e0"

RESOURCES = [
    {
        "slug": "protein-pairing-cheat-sheet",
        "title": "Protein Pairing Cheat Sheet",
        "tag": "Protein",
        "pages": 4,
        "blurb": "Pair two protein sources in one meal to get past 30 grams. Breakfast, lunch and dinner ideas with the grams listed for each item.",
    },
    {
        "slug": "pre-and-post-workout-carb-snacks",
        "title": "Pre and Post Workout Snacks",
        "tag": "Training fuel",
        "pages": 2,
        "blurb": "What to eat in the hour before a hard session and the hours after it. Whole food, packaged and drinkable options.",
    },
]

PARTNERS = {
    "alloy": {
        "name": "Alloy Personal Training",
        "short": "Alloy",
        "logo": "/resources/img/alloy-logo.png",
        "logo_w": 300,
        "locations": [
            ("South Tempe", "https://alloypersonaltraining.com/location/south-tempe-az/"),
            ("Ahwatukee Foothills", "https://alloypersonaltraining.com/location/ahwatukee-foothills-az/"),
        ],
        "back_title": "Train with Alloy",
        "back_text": "SDG patients receive two complimentary weeks of training at Alloy, six sessions in all. Choose your location to get started.",
    },
    "rise": {
        "name": "RISE Modern Wellness",
        "short": "RISE",
        "logo": "/resources/img/rise-logo.png",
        "logo_w": 204,
        "locations": [
            ("Chandler", "https://risemodernwellness.com/locations/chandler-arizona/"),
        ],
        "back_title": "Recover and recharge at RISE",
        "back_text": "SDG patients receive six complimentary wellness sessions over two weeks at RISE Modern Wellness in Chandler, to support recovery, reduce inflammation and improve energy.",
    },
}

e = html.escape


def card(r):
    pdf = f"/resources/files/{r['slug']}.pdf"
    pages = f"{r['pages']} page{'s' if r['pages'] != 1 else ''} · PDF"
    return f"""
        <article class="res">
          <a class="res-thumb" href="{pdf}" target="_blank" rel="noopener" aria-label="Open {e(r['title'])}">
            <img src="/resources/img/{r['slug']}.jpg" alt="" width="680" height="880" loading="lazy">
          </a>
          <div class="res-body">
            <p class="eyebrow">{e(r['tag'])}</p>
            <h3>{e(r['title'])}</h3>
            <p class="res-blurb">{e(r['blurb'])}</p>
            <p class="res-meta">{pages}</p>
            <div class="res-actions">
              <a class="btn btn-rust" href="{pdf}" download>Download</a>
              <a class="text-link" href="{pdf}" target="_blank" rel="noopener">Open in browser</a>
            </div>
          </div>
        </article>"""


def page(slug, p):
    res = [r for r in RESOURCES if slug in r.get("partners", PARTNERS)]
    cards = "".join(card(r) for r in res)
    locs = "".join(
        f'<a class="btn btn-peach" href="{u}" target="_blank" rel="noopener">{e(p["short"])} {e(n)}</a>'
        for n, u in p["locations"]
    )
    return TEMPLATE.format(
        name=e(p["name"]), short=e(p["short"]), logo=p["logo"], logo_w=p["logo_w"],
        cards=cards, locs=locs, back_title=e(p["back_title"]), back_text=e(p["back_text"]),
        request=REQUEST_FORM_URL, consult=CONSULT_URL, count=len(res),
    )


TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Nutrition resources for {name} members | Southwest Dietitian Group</title>
<meta name="robots" content="noindex">
<meta name="description" content="Complimentary nutrition handouts for {name} members from the registered dietitians at Southwest Dietitian Group.">
<meta property="og:title" content="Nutrition resources for {name} members">
<meta property="og:description" content="Complimentary handouts from the registered dietitians at Southwest Dietitian Group.">
<meta property="og:image" content="https://go.southwestdietitiangroup.com/assets/sdg-badge.png">
<link rel="icon" type="image/png" sizes="64x64" href="/assets/favicon-64.png?v=2">
<link rel="apple-touch-icon" href="/assets/favicon-180.png?v=2">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Josefin+Sans:wght@400;600&family=Mulish:wght@400;600;700&display=swap">
<link rel="stylesheet" href="/resources/partner.css">
</head>
<body>
<div class="sdg-lp">
  <header class="hero">
    <div class="wrap">
      <div class="cobrand">
        <img class="partner-logo" src="{logo}" alt="{name}" style="width:{logo_w}px">
        <span class="x" aria-hidden="true">+</span>
        <a class="logo-link" href="https://southwestdietitiangroup.com/" target="_blank" rel="noopener"><img class="sdg-logo" src="/assets/sdg-logo-white.png" alt="Southwest Dietitian Group"></a>
      </div>
      <p class="eyebrow">For {name} members</p>
      <h1>Nutrition resources from your dietitians</h1>
      <p class="lede">Complimentary handouts from the registered dietitians at Southwest Dietitian Group, made to support your training. Download them, print them or save them to your phone.</p>
      <div class="hero-actions">
        <a class="btn btn-peach" href="#resources">See the handouts</a>
        <a class="btn btn-ghost" href="{request}" target="_blank" rel="noopener">Request a topic</a>
      </div>
    </div>
  </header>

  <main>
    <section class="band" id="resources">
      <div class="wrap">
        <p class="eyebrow">The library</p>
        <h2>Handouts</h2>
        <div class="grid">{cards}
        </div>
      </div>
    </section>

    <section class="band band-white" id="request">
      <div class="wrap split">
        <div>
          <p class="eyebrow">Ask us</p>
          <h2>Want a handout on something else?</h2>
        </div>
        <div class="split-body">
          <p class="lede">Tell us the topic and our dietitians will create it. New handouts get added to this page for every {short} member.</p>
          <a class="btn btn-rust" href="{request}" target="_blank" rel="noopener">Request a resource</a>
        </div>
      </div>
    </section>

    <section class="band" id="consult">
      <div class="wrap split">
        <div>
          <p class="eyebrow">For {short} members</p>
          <h2>Your complimentary nutrition consult</h2>
        </div>
        <div class="split-body">
          <p class="lede">Book a 30-minute nutrition consult with Maya Nahra, RD, LD, owner of Southwest Dietitian Group and a registered dietitian for 18 years. It's on us.</p>
          <a class="btn btn-rust" href="{consult}" target="_blank" rel="noopener">Book my consult</a>
        </div>
      </div>
    </section>

    <section class="band band-plum" id="partner">
      <div class="wrap center">
        <img class="partner-logo" src="{logo}" alt="{name}" style="width:{logo_w}px">
        <h2>{back_title}</h2>
        <p class="lede">{back_text}</p>
        <div class="hero-actions">{locs}</div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="wrap">
      <a class="logo-link" href="https://southwestdietitiangroup.com/" target="_blank" rel="noopener"><img src="/assets/sdg-logo-white.png" alt="Southwest Dietitian Group home"></a>
      <div class="footer-text">
        <a class="site-link" href="https://southwestdietitiangroup.com/" target="_blank" rel="noopener">southwestdietitiangroup.com</a>
        <span>Educational handouts, not medical advice. Talk with your dietitian or doctor about your own needs.</span>
      </div>
    </div>
  </footer>
</div>
</body>
</html>
"""

if __name__ == "__main__":
    for slug, p in PARTNERS.items():
        out = ROOT / slug / "index.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(page(slug, p))
        print("wrote", out.relative_to(ROOT))
