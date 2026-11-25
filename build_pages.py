#!/usr/bin/env python3
"""La Cumis Cowffee — 2040 W 21st St. N, Wichita KS. Template-v2 multi-page build.
Every claim traced in evidence.json (press 11-13 + IG/hotplate 11-24). Unknowns
(phone was NOT in press but verified via IG; prices omitted) — never guessed.
Zero JS beyond the CSS checkbox drawer. Hand-rolled HTML/CSS. noindex demo host.
Design: "piloncillo & crema" — espresso ink, crema paper, mazapán gold, jarabel rojo,
cow-print spot bands. Shop identity only."""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(HERE, 'public')
os.makedirs(PUB, exist_ok=True)

ORIGIN = 'https://lacumis-cowffee-demo.up.railway.app'
BRAND = 'La Cumis Cowffee'
CITY = 'Wichita, KS'
STREET = '2040 W 21st St. N'
FULL_ADDR = '2040 W 21st St. N, Wichita, KS 67203'
ZIP = '67203'
PHONE_DISPLAY = '(316) 737-7120'
PHONE_TEL = '+13167377120'
EMAIL = 'haileyhernandez516@gmail.com'
IG = 'https://www.instagram.com/la_cumis/'
FB = 'https://www.facebook.com/tencia.hernandez.2025'
MAPQ = 'https://www.google.com/maps?q=' + '2040%20W%2021st%20St%20N%2C%20Wichita%2C%20KS%2067203'
LAT, LON = 37.7228478, -97.3639553  # OSM/Nominatim geocode of the press address — evidence.json notes
MAPSRC = 'https://www.google.com/maps?q=2040%20W%2021st%20St%20N%2C%20Wichita%2C%20KS%2067203&output=embed'

def head(title, desc, path):
    u = ORIGIN + path
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{u}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{u}">
<meta property="og:image" content="{ORIGIN}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{ORIGIN}/og.png">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="stylesheet" href="/style.css">
<link rel="preconnect" href="https://www.google.com"></head>
<body>'''

def nav():
    return '''<a class="skip" href="#main">Skip to content</a>
<header class="site">
  <a class="brand" href="/">La&nbsp;Cumis <span>Cowffee</span></a>
  <input type="checkbox" id="navtoggle" class="navtoggle" aria-label="Show navigation">
  <label for="navtoggle" class="navbtn" aria-hidden="true"><i></i></label>
  <nav aria-label="Main" class="links">
    <a href="/menu">Menu</a>
    <a href="/coffees">Coffees</a>
    <a href="/pan">Pan&nbsp;&amp;&nbsp;Pastries</a>
    <a href="/our-story">Our&nbsp;Story</a>
    <a href="/visit">Visit</a>
    <a class="btn btn-sm" href="/contact">Contact&nbsp;Us</a>
  </nav>
</header>'''

SPOTBAND = '<div class="spotband" aria-hidden="true"></div>'

def footer():
    return f'''<footer class="site">
  <div class="footgrid">
    <div class="footnap">
      <p class="fbrand">La Cumis Cowffee</p>
      <address>{STREET}<br>Wichita, KS {ZIP}</address>
      <p class="fline3"><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <div class="footcta">
      <p class="figold">Cow-print heart.<br>Mexican soul.</p>
      <p class="fsocial"><a href="{IG}" rel="noopener">Instagram</a> &nbsp;·&nbsp; <a href="{FB}" rel="noopener">Facebook</a></p>
      <p class="fline2">The cow-print trailer still runs Fri–Sun at 21st &amp; Fairview — pausing briefly while the storefront gets going.</p>
    </div>
  </div>
  <p class="footline">&copy; 2026 {BRAND} · Wichita, KS</p>
</footer>'''

def breadcrumbs(name, path):
    items = [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': ORIGIN + '/'},
    ]
    if path != '/':
        items.append({'@type': 'ListItem', 'position': 2, 'name': name, 'item': ORIGIN + path})
    return json.dumps({'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': items}, ensure_ascii=False)

def ld_home():
    obj = {
        '@context': 'https://schema.org', '@type': 'CafeRestaurant',
        'name': BRAND,
        'image': ORIGIN + '/og.png',
        'url': ORIGIN + '/',
        'servesCuisine': ['Mexican-style coffee', 'Mexican pastries'],
        'email': EMAIL,
        'telephone': '+' + PHONE_TEL,
        'address': {'@type': 'PostalAddress', 'streetAddress': '2040 W 21st St. N', 'addressLocality': 'Wichita', 'addressRegion': 'KS', 'postalCode': ZIP, 'addressCountry': 'US'},
        'geo': {'@type': 'GeoCoordinates', 'latitude': LAT, 'longitude': LON},
        'hasMap': MAPQ,
        'sameAs': [IG, FB],
        'openingHoursSpecification': [
            {'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 'opens': '07:00', 'closes': '21:00'}
        ],
    }
    return json.dumps(obj, ensure_ascii=False)

def ld_faq():
    obj = {
        '@context': 'https://schema.org', '@type': 'FAQPage',
        'mainEntity': [
            {'@type': 'Question', 'name': 'Where is La Cumis Cowffee in Wichita?',
             'acceptedAnswer': {'@type': 'Answer', 'text': 'At 2040 W 21st St. N — the strip center near 21st and Amidon, in the old Blend Nutrition space.'}},
            {'@type': 'Question', 'name': 'What are the hours?',
             'acceptedAnswer': {'@type': 'Answer', 'text': '7 a.m. to 9 p.m. every day but Wednesday, as announced for the opening. Opening-week hours can shift — Instagram carries the latest.'}},
            {'@type': 'Question', 'name': 'Will the cow-print trailer still be around?',
             'acceptedAnswer': {'@type': 'Answer', 'text': 'Yes — the trailer runs Fridays through Sundays at 21st and Fairview. Owner Hailey Hernandez says it takes a short break while the storefront gets going, then comes back.'}},
            {'@type': 'Question', 'name': 'Is there seating?',
             'acceptedAnswer': {'@type': 'Answer', 'text': 'Yes — the storefront has dine-in seating, from morning coffee to an afternoon of pan con café.'}},
        ],
    }
    return json.dumps(obj, ensure_ascii=False)

def ld_menu():
    obj = {
        '@context': 'https://schema.org', '@type': 'Menu',
        'name': 'La Cumis Cowffee Menu',
        'inServingCurrency': 'USD',
        'hasMenuSection': [
            {'@type': 'MenuSection', 'name': 'Mexican-Style Coffees (hot & iced)',
             'hasMenuItem': [
                 {'@type': 'MenuItem', 'name': 'Mazapán Latte'},
                 {'@type': 'MenuItem', 'name': 'Banana Latte'},
                 {'@type': 'MenuItem', 'name': 'Mexican Mocha'},
                 {'@type': 'MenuItem', 'name': 'Coconut Matcha'},
                 {'@type': 'MenuItem', 'name': 'Cookie Butter Matcha'},
             ]},
            {'@type': 'MenuSection', 'name': 'Panadería — homemade Mexican bread & pastries',
             'hasMenuItem': [
                 {'@type': 'MenuItem', 'name': 'Conchas'},
                 {'@type': 'MenuItem', 'name': 'Gorditas'},
                 {'@type': 'MenuItem', 'name': 'Croissants'},
                 {'@type': 'MenuItem', 'name': 'Empanadas'},
             ]},
            {'@type': 'MenuSection', 'name': 'Coming soon — announced by the owner',
             'hasMenuItem': [
                 {'@type': 'MenuItem', 'name': 'Atole (warm Mexican corn-masa drink)'},
                 {'@type': 'MenuItem', 'name': 'Breakfast burritos'},
                 {'@type': 'MenuItem', 'name': 'Tamales'},
             ]},
        ],
    }
    return json.dumps(obj, ensure_ascii=False)

def ld_service(name, path, desc):
    obj = {
        '@context': 'https://schema.org', '@type': 'Service',
        'name': name,
        'description': desc,
        'areaServed': {'@type': 'City', 'name': 'Wichita', 'addressRegion': 'KS'},
        'provider': {'@type': 'CafeRestaurant', 'name': BRAND, 'address': {'@type': 'PostalAddress', 'streetAddress': '2040 W 21st St. N', 'addressLocality': 'Wichita', 'addressRegion': 'KS', 'postalCode': ZIP, 'addressCountry': 'US'}},
    }
    return json.dumps(obj, ensure_ascii=False)

PAGES = {}

# ---------- HOME ----------
PAGES['index.html'] = (head(f'{BRAND} — Mexican-Style Coffees &amp; Mexican Pan, {CITY}',
    'Mexican-inspired coffees — mazapan latte, Mexican mocha, banana latte, matcha — plus homemade Mexican breads and pastries, by owner Hailey Hernandez at 2040 W 21st St. N, Wichita, KS.',
    '/'), f'''{nav()}
<main id="main">
<section class="hero">
  <p class="kicker">Wichita · Northside — 2040 W 21st St. N</p>
  <h1>Mexican-style coffees.<br><em>From-scratch Mexican pan.</em></h1>
  <p class="lead">Mazapán lattes, Mexican mocha, banana lattes and matcha the La Cumis way — with conchas, gorditas and sweet bread baked fresh by Hailey Hernandez. From a cow-print coffee trailer to our own storefront on 21st Street.</p>
  <p class="cta">
    <a class="btn btn-big" href="/menu">See the Menu</a>
    <a class="btn btn-ghost btn-big" href="{MAPQ}" rel="noopener">Get Directions</a>
  </p>
  <p class="herophone">Prefer to talk to a human? <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
</section>
{SPOTBAND}
<section class="cards">
  <h2 class="sr-only">What we serve</h2>
  <a class="card" href="/coffees">
    <span class="dot" aria-hidden="true"></span>
    <h3>Mexican-Style Coffees</h3>
    <p>Mazapán latte, Mexican mocha, banana latte, coconut matcha, cookie butter matcha — hot or iced, all built by hand.</p>
    <span class="more">The coffees &rsaquo;</span>
  </a>
  <a class="card" href="/pan">
    <span class="dot" aria-hidden="true"></span>
    <h3>Pan &amp; Pastries</h3>
    <p>Conchas, gorditas, croissants, empanadas — the homemade Mexican breads that started this whole thing on Facebook.</p>
    <span class="more">The panadería &rsaquo;</span>
  </a>
  <a class="card" href="/visit">
    <span class="dot" aria-hidden="true"></span>
    <h3>Our New Spot</h3>
    <p>The old Blend Nutrition space in the strip near 21st &amp; Amidon, reborn as a coffee-and-pan living room. Dine-in seating.</p>
    <span class="more">Visit us &rsaquo;</span>
  </a>
</section>
<section class="strip">
  <div class="stripin">
    <p class="bigquote">&ldquo;We&rsquo;re going to take a break from it [the trailer] to get this going, and then we&rsquo;ll be back over there.&rdquo;</p>
    <p class="attrib">— Hailey Hernandez, owner, <em>Wichita Eagle</em></p>
  </div>
</section>
<section class="storyteaser">
  <div class="sttext">
    <p class="kicker">The story so far</p>
    <h2>From middle-schooler empanadas to a storefront</h2>
    <p>Hailey Hernandez started baking as a kid — sweet-potato empanadas with her mom, then a home bakery on Facebook, then a weekend route of gorditas, conchas and croissants. In 2024 the family bought a food trailer and painted it cow-print. Now, at 21, she&rsquo;s opening her first real café.</p>
    <p><a class="more" href="/our-story">Read the full story &rsaquo;</a></p>
  </div>
  <div class="stfig" aria-hidden="true">
    <p class="figrule"></p>
    <p class="figline">Four wheels<br><b>to four walls</b></p>
    <p class="figsub">2024: a cow-print trailer.<br>2026: a home on 21st Street.</p>
    <p class="figrule"></p>
  </div>
</section>
</main>
{footer()}
<script type="application/ld+json">{ld_home()}</script>
<script type="application/ld+json">{breadcrumbs('Home', '/')}</script>
</body>
</html>''')

# ---------- MENU ----------
PAGES['menu.html'] = (head(f'Menu — {BRAND}, {CITY}',
    'The La Cumis Cowffee menu: mazapán latte, banana latte, Mexican mocha, coconut and cookie-butter matcha, homemade conchas, gorditas, croissants and empanadas. Wichita, KS.',
    '/menu'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">The Menu</p>
  <h1>Cowffee, conchas<br>and warm things coming</h1>
  <p class="lead">The same drinks and breads that made the trailer a Northside favorite — now served indoors. Everything below is what the café serves or has announced.</p>
  <p class="cta"><a class="btn" href="/visit">Plan your visit</a> <a class="btn btn-ghost" href="{MAPQ}" rel="noopener">Get Directions</a></p>
</section>
{SPOTBAND}
<div class="menuwrap">
  <section class="menu-sec">
    <h2>Mexican-Style Coffees <span>— hot &amp; iced</span></h2>
    <dl class="items">
      <div><dt><a href="/coffees">Mazapán Latte</a></dt><dd>Espresso and milk with the taste of mazapán — the classic Mexican peanut-caramel candy.</dd></div>
      <div><dt><a href="/coffees">Banana Latte</a></dt><dd>Espresso and milk with banana — sweet, smooth, and dangerously easy to order.</dd></div>
      <div><dt><a href="/coffees">Mexican Mocha</a></dt><dd>Mexican coffee and chocolate, the way abuelas made it, upgraded with espresso.</dd></div>
      <div><dt><a href="/coffees">Coconut Matcha</a></dt><dd>Matcha with coconut — creamy without being heavy.</dd></div>
      <div><dt><a href="/coffees">Cookie Butter Matcha</a></dt><dd>Matcha swirled with cookie butter. Dessert in a cup, no judgment.</dd></div>
    </dl>
  </section>
  <section class="menu-sec">
    <h2>Panadería <span>— baked by Hailey</span></h2>
    <dl class="items">
      <div><dt><a href="/pan">Conchas</a></dt><dd>Soft sweet bread with the sugar shell on top — the panadería signature.</dd></div>
      <div><dt><a href="/pan">Gorditas</a></dt><dd>Fresh masa cakes, split and stuffed.</dd></div>
      <div><dt><a href="/pan">Croissants</a></dt><dd>On the weekend repertoire since the Facebook-bakery days.</dd></div>
      <div><dt><a href="/pan">Empanadas</a></dt><dd>Where the whole story started — sweet-potato empanadas with her mom.</dd></div>
    </dl>
  </section>
  <section class="menu-note">
    <p class="figrule" aria-hidden="true"></p>
    <h2>Coming soon <span>— announced by the owner</span></h2>
    <p class="newitems">Atole · Breakfast burritos · Tamales</p>
    <p class="fineprint">Atole — the warm Mexican corn-masa drink — arrives with the cold weather. Burritos and tamales are on the way too.</p>
  </section>
  <p class="fineprint center">The menu rotates with the season. Today&rsquo;s lineup and specials go up on <a href="{IG}" rel="noopener">Instagram</a> — the counter is the place of record. Baked goods sell out.</p>
</div>
</main>
{footer()}
<script type="application/ld+json">{ld_menu()}</script>
<script type="application/ld+json">{breadcrumbs('Menu', '/menu')}</script>
</body>
</html>''')

# ---------- COFFEES ----------
PAGES['coffees.html'] = (head(f'Mexican-Style Coffee — {BRAND}, {CITY}',
    'Mazapán latte, banana latte, Mexican mocha, coconut matcha and cookie-butter matcha, hot or iced — the La Cumis Cowffee coffee menu in Wichita, KS.',
    '/coffees'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">The Coffees</p>
  <h1>Cowffee — Mexican-style,<br>hot or iced</h1>
  <p class="lead">Hailey taught herself the long list of Mexican-inspired drinks drink by drink. These are the ones the trailer became known for — every one made to order, hot or iced.</p>
  <p class="cta"><a class="btn" href="/menu">Full Menu</a> <a class="btn btn-ghost" href="{MAPQ}" rel="noopener">Get Directions</a></p>
</section>
{SPOTBAND}
<div class="detailwrap">
  <section class="drink">
    <h2><span class="num" aria-hidden="true">1</span>Mazapán Latte</h2>
    <p>Named for mazapán — the classic Mexican peanut-and-sugar candy that melts into espresso and steamed milk. Caramel, peanut, a little crunch of memory. The cup people drive to the trailer for.</p>
  </section>
  <section class="drink">
    <h2><span class="num" aria-hidden="true">2</span>Banana Latte</h2>
    <p>Espresso and milk with banana — naturally sweet, smooth, and the one first-timers order when they don&rsquo;t want to gamble. Order it iced in August, hot in January.</p>
  </section>
  <section class="drink">
    <h2><span class="num" aria-hidden="true">3</span>Mexican Mocha</h2>
    <p>Mexican coffee and chocolate — the table at abuela&rsquo;s house, with espresso behind it. Not a syrup punch: coffee-forward, chocolate-deep.</p>
  </section>
  <section class="drink">
    <h2><span class="num" aria-hidden="true">4</span>Coconut Matcha &amp; Cookie Butter Matcha</h2>
    <p>Two matchas for two moods: one whipped with coconut, light and tropical; the other swirled with cookie butter, dessert-in-a-cup territory. Both hot or iced.</p>
  </section>
  <aside class="panel">
    <h2>For the cold days ahead</h2>
    <p><strong>Atole is on the way.</strong> The warm Mexican corn-masa drink is announced for cold weather — the trailer&rsquo;s regulars are already asking.</p>
    <p class="nodcaf">And per the shop&rsquo;s own house rule, posted on Instagram: <em>&ldquo;No decaf around here!!!&rdquo;</em></p>
    <p class="cta"><a class="btn" href="/visit">Come get one</a></p>
  </aside>
</div>
</main>
{footer()}
<script type="application/ld+json">{ld_service('Mexican-Style Coffees', '/coffees', 'Mazapan latte, banana latte, Mexican mocha, coconut matcha and cookie-butter matcha, hot or iced, at La Cumis Cowffee in Wichita, KS.')}</script>
<script type="application/ld+json">{breadcrumbs('Coffees', '/coffees')}</script>
</body>
</html>''')

# ---------- PAN ----------
PAGES['pan.html'] = (head(f'Mexican Bread &amp; Pastries — {BRAND}, {CITY}',
    'Conchas, gorditas, croissants and empanadas — homemade Mexican pan and pastries by owner Hailey Hernandez at La Cumis Cowffee, Wichita, KS.',
    '/pan'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">The Panadería</p>
  <h1>Pan made the slow way:<br>by hand, in small batches</h1>
  <p class="lead">The breads came before the coffee. What started as empanadas sold from the family kitchen is now the counter the café opens with — conchas, gorditas, croissants and whatever else the season asks for.</p>
  <p class="cta"><a class="btn" href="/menu">Full Menu</a> <a class="btn btn-ghost" href="{MAPQ}" rel="noopener">Get Directions</a></p>
</section>
{SPOTBAND}
<div class="detailwrap">
  <section class="drink">
    <h2>Conchas</h2>
    <p>Soft, slightly sweet yeast bread under a crackled sugar shell — the panadería signature, the one kids point at through the case.</p>
  </section>
  <section class="drink">
    <h2>Gorditas</h2>
    <p>Fresh masa cakes, split and stuffed — the weekend-baking staple that built the Facebook following.</p>
  </section>
  <section class="drink">
    <h2>Croissants &amp; empanadas</h2>
    <p>Empanadas are the origin story — sweet-potato empanadas with her mom, sold from home because people kept asking for more. Croissants joined the weekend repertoire as demand grew, and both stay on the counter.</p>
  </section>
  <aside class="panel">
    <h2>Seasonal bakes</h2>
    <p>Follow along on <a href="{IG}" rel="noopener">Instagram</a> — pan de muerto arrives around Día de Muertos, pumpkin conchas run in the fall, and drops sell out.</p>
    <p class="cta"><a class="btn" href="/visit">Plan your visit</a></p>
  </aside>
</div>
</main>
{footer()}
<script type="application/ld+json">{ld_service('Homemade Mexican Bread & Pastries', '/pan', 'Conchas, gorditas, croissants and empanadas baked by owner Hailey Hernandez at La Cumis Cowffee in Wichita, KS.')}</script>
<script type="application/ld+json">{breadcrumbs('Pan & Pastries', '/pan')}</script>
</body>
</html>''')

# ---------- OUR STORY ----------
PAGES['our-story.html'] = (head(f'Our Story — {BRAND}, {CITY}',
    'Hailey Hernandez went from sweet-potato empanadas sold on Facebook to a cow-print coffee trailer to a first storefront at 2040 W 21st St. N, Wichita, KS.',
    '/our-story'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">Our Story</p>
  <h1>&ldquo;La Cumis&rdquo; is what you<br>call a good girlfriend</h1>
  <p class="lead">So this café is named after the whole community that showed up — one sweet-potato empanada at a time. The cow in &ldquo;cowffee&rdquo;? That&rsquo;s a nod to a cow-print coffee trailer out in California that Hailey followed online before she ran her own.</p>
  <p class="cta"><a class="btn" href="/visit">See where we are now</a> <a class="btn btn-ghost" href="/menu">Try the menu</a></p>
</section>
{SPOTBAND}
<div class="story">
  <section class="tl">
    <div class="trow"><p class="tyr">Middle school</p><div class="tbody"><h2>Sweet potatoes into empanadas</h2><p>Hailey liked to bake. One day her dad came home with a pile of sweet potatoes, and she and her mom — Hortencia, who chefed at Green Acres in Bradley Fair for 13 years — turned them into empanadas.</p>
    <p>&ldquo;And shockingly, there was a lot of people wanting to buy it,&rdquo; Hailey told the Wichita Eagle. &ldquo;They were like, &lsquo;When are you going to make more? Do you make other breads?&rsquo;&rdquo;</p></div></div>
    <div class="trow"><p class="tyr">The home bakery</p><div class="tbody"><h2>Sold from the kitchen, on Facebook</h2><p>The family couldn&rsquo;t eat all the empanadas, so they sold them from home. The demand kept growing — weekend bakes added gorditas, conchas and croissants, and a following grew with them.</p></div></div>
    <div class="trow"><p class="tyr">2024</p><div class="tbody"><h2>The cow-print trailer</h2><p>The family bought a food trailer, painted it black-and-white cow-print, and parked it on the Northside on weekends — 21st &amp; Fairview. Hailey, a coffee-shop fan, taught herself one Mexican-inspired drink after another until the trailer&rsquo;s menu was its own thing.</p></div></div>
    <div class="trow"><p class="tyr">2026</p><div class="tbody"><h2>Home: 2040 W 21st St. N</h2><p>At 21, Hailey is opening her first brick-and-mortar — the old Blend Nutrition space near 21st &amp; Amidon, with dine-in seating. The trailer keeps its weekend post at 21st &amp; Fairview: it takes a short break while the storefront gets going, then heads back out.</p></div></div>
  </section>
  <aside class="panel wide">
    <h2>Who&rsquo;s behind the counter</h2>
    <p class="bigquote">&ldquo;And shockingly, there was a lot of people wanting to buy it.&rdquo;</p>
    <p class="attrib">— Hailey Hernandez, <em>Wichita Eagle</em>, November 2026</p>
    <p>Hailey Hernandez grew up in a food family — her mom ran the kitchen at Green Acres for over a decade — and stayed in it. La Cumis Cowffee is her first restaurant.</p>
    <p class="cta"><a class="btn" href="/visit">Visit the first one</a></p>
  </aside>
</div>
</main>
{footer()}
<script type="application/ld+json">{breadcrumbs('Our Story', '/our-story')}</script>
</body>
</html>''')

# ---------- VISIT ----------
PAGES['visit.html'] = (head(f'Visit — {BRAND}, {CITY}',
    'La Cumis Cowffee at 2040 W 21st St. N, Wichita, KS 67203 — near 21st and Amidon. Hours 7 a.m. to 9 p.m. every day but Wednesday. Phone (316) 737-7120.',
    '/visit'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">Now Opening</p>
  <h1>Find us on<br>21st Street</h1>
  <p class="lead">The storefront at 2040 W 21st St. N — the strip center near 21st &amp; Amidon where Blend Nutrition used to be — is opening with dine-in seating, Mexican-style coffees and pan fresh from the oven.</p>
  <p class="cta"><a class="btn btn-big" href="{MAPQ}" rel="noopener">Get Directions</a> <a class="btn btn-ghost btn-big" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a></p>
</section>
{SPOTBAND}
<div class="visitgrid">
  <section class="visitinfo">
    <h2>Where</h2>
    <address class="bigaddr">{STREET}<br>Wichita, KS {ZIP}</address>
    <p>The strip center near 21st &amp; Amidon, on the Northside.</p>
    <h2>When</h2>
    <p class="hours"><b>7 a.m. to 9 p.m. — every day but Wednesday</b>, as announced for the opening. Opening-week hours can shift; the latest word is always on <a href="{IG}" rel="noopener">Instagram</a>.</p>
    <h2>The trailer too</h2>
    <p>The cow-print trailer keeps its post at 21st &amp; Fairview, Fridays through Sundays — it takes a short break while the storefront gets going, then comes back.</p>
    <h2>Good to know</h2>
    <p>There is seating. Baked goods sell out, and the early crowd is real — the trailer era taught us to come early for the good conchas.</p>
    <p class="cta"><a class="btn btn-ghost" href="/menu">What we serve</a></p>
  </section>
  <section class="visitmap">
    <div class="mapbox">
      <iframe title="Map to La Cumis Cowffee, 2040 W 21st St. N, Wichita, KS" src="{MAPSRC}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
    <p class="fineprint">Map not loading? <a href="{MAPQ}" rel="noopener">Open it in Google Maps</a> or call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
  </section>
</div>
</main>
{footer()}
<script type="application/ld+json">{ld_service('Visit La Cumis Cowffee', '/visit', 'Mexican-style coffees and homemade Mexican pan at 2040 W 21st St. N, Wichita, KS 67203 — dine-in seating, 7 a.m. to 9 p.m. every day but Wednesday.')}</script>
<script type="application/ld+json">{ld_faq()}</script>
<script type="application/ld+json">{breadcrumbs('Visit', '/visit')}</script>
</body>
</html>''')

# ---------- CONTACT ----------
PAGES['contact.html'] = (head(f'Contact — {BRAND}, {CITY}',
    'Contact La Cumis Cowffee in Wichita, KS: phone (316) 737-7120, email, and a contact form for questions about the café or the trailer.',
    '/contact'), f'''{nav()}
<main id="main">
<section class="pagehead">
  <p class="kicker">Talk to Us</p>
  <h1>Contact La Cumis</h1>
  <p class="lead">Questions about hours, the menu, ordering ahead, or the trailer for your event? Call, email, or use the form — it goes straight to the café.</p>
</section>
<div class="contactgrid">
  <form class="cform" method="post" action="/contact">
    <h2>Send a message</h2>
    <p><label for="f-name">Your name</label><input id="f-name" name="name" type="text" required maxlength="120" autocomplete="name"></p>
    <p><label for="f-email">Email</label><input id="f-email" name="email" type="email" required maxlength="160" autocomplete="email"></p>
    <p><label for="f-msg">Message</label><textarea id="f-msg" name="message" rows="5" required maxlength="4000"></textarea></p>
    <p><button class="btn btn-big" type="submit">Send Message</button></p>
    <p class="fineprint">This form sends your note to the café. We never share your address.</p>
  </form>
  <section class="cinfo">
    <h2>Direct lines</h2>
    <p class="clabel">Call</p>
    <p class="cbig"><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
    <p class="clabel">Email</p>
    <p class="cbig"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <p class="clabel">Walk in</p>
    <address class="bigaddr">{STREET}<br>Wichita, KS {ZIP}</address>
    <p class="clabel">Social — hours &amp; specials</p>
    <p class="cbig"><a href="{IG}" rel="noopener">Instagram</a> · <a href="{FB}" rel="noopener">Facebook</a></p>
  </section>
</div>
</main>
{footer()}
<script type="application/ld+json">{breadcrumbs('Contact', '/contact')}</script>
</body>
</html>''')

# ---------- PRIVACY ----------
PAGES['privacy.html'] = (head(f'Privacy Policy — {BRAND}, {CITY}',
    'Privacy policy for La Cumis Cowffee: how the contact form handles your name, email and message. No trackers, no cookies.',
    '/privacy'), f'''{nav()}
<main id="main">
<section class="pagehead narrow">
  <p class="kicker">Privacy</p>
  <h1>Privacy Policy</h1>
</section>
<div class="prose">
  <p>This site belongs to {BRAND} ({FULL_ADDR}).</p>
  <h2>What we collect</h2>
  <p>The contact form on this site collects only the information you type into it — your name, your email address and your message — and sends it to the café&rsquo;s own email address so the owners can answer you. That is the entire purpose of the data. It is not sold, shared or used for advertising.</p>
  <h2>Cookies and tracking</h2>
  <p>This site sets no cookies and uses no advertising trackers or analytics pixels of its own. The embedded Google map may set its own cookies once you interact with it, governed by Google&rsquo;s privacy policy.</p>
  <h2>Your choices</h2>
  <p>Want your message deleted from the café&rsquo;s mailbox records? Email <a href="mailto:{EMAIL}">{EMAIL}</a> or call {PHONE_DISPLAY} and ask. Questions about this policy go to the same place.</p>
  <p class="fineprint">This policy covers this website only.</p>
</div>
</main>
{footer()}
<script type="application/ld+json">{breadcrumbs('Privacy', '/privacy')}</script>
</body>
</html>''')

# ---------- 404 ----------
PAGES['404.html'] = (head(f'Page not found — {BRAND}',
    'Page not found at the La Cumis Cowffee site. Back to the menu, or straight to the coffee page.',
    '/404'), f'''{nav()}
<main id="main">
<section class="pagehead center">
  <p class="kicker">404</p>
  <h1>This page wandered off<br>the pasture.</h1>
  <p class="lead">It doesn&rsquo;t exist — but the mazapán latte does, and it&rsquo;s one tap away.</p>
  <p class="cta"><a class="btn btn-big" href="/">Back to Home</a> <a class="btn btn-ghost btn-big" href="/menu">See the Menu</a></p>
</section>
</main>
{footer()}
</body>
</html>''')

# ---------- THANKS ----------
PAGES['thanks.html'] = (head(f'Message sent — {BRAND}',
    'Thanks for reaching out to La Cumis Cowffee in Wichita — Hailey will get back to you.',
    '/thanks'), f'''{nav()}
<main id="main">
<section class="pagehead center">
  <p class="kicker">Received</p>
  <h1>Your message is on its<br>way to Hailey.</h1>
  <p class="lead">Thank you — she answers personally. Meanwhile, the menu and the map are one click away.</p>
  <p class="cta"><a class="btn btn-big" href="/menu">See the Menu</a> <a class="btn btn-ghost btn-big" href="/visit">Plan your visit</a></p>
</section>
</main>
{footer()}
</body>
</html>''')

for fname, (h, body) in PAGES.items():
    with open(os.path.join(PUB, fname), 'w', encoding='utf-8') as f:
        f.write(h + '\n' + body)
    print('wrote', fname, len(h + body), 'bytes')

# ---------- sitemap / robots / favicon ----------
pages_order = ['/', '/menu', '/coffees', '/pan', '/our-story', '/visit', '/contact', '/privacy']
today = '2026-11-24'
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
    f'<url><loc>{ORIGIN}{p}</loc><lastmod>{today}</lastmod></url>\n' for p in pages_order) + '</urlset>\n'
open(os.path.join(PUB, 'sitemap.xml'), 'w').write(sitemap)
open(os.path.join(PUB, 'robots.txt'), 'w').write(f'''User-agent: *
Allow: /

Sitemap: {ORIGIN}/sitemap.xml
''')
# cow-print favicon: espresso ink tile, crema spots, mazapan gold cup-dot
favicon = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#231611"/><ellipse cx="16" cy="15" rx="9" ry="7" fill="#f7efe2"/><ellipse cx="46" cy="22" rx="11" ry="8" fill="#f7efe2"/><ellipse cx="24" cy="47" rx="8" ry="6" fill="#f7efe2"/><circle cx="48" cy="48" r="8" fill="#c98f3c"/><circle cx="48" cy="48" r="3.4" fill="#231611"/></svg>
'''
open(os.path.join(PUB, 'favicon.svg'), 'w').write(favicon)
print('wrote sitemap.xml robots.txt favicon.svg')
print('PAGES:', len([f for f in PAGES if f.endswith('.html')]))
