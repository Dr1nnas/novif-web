# Generates demo sites. Run: python3 build.py
import html
RIB='<a class="novif-ribbon" href="../../">Demo site by <b>novif</b> — get a site like this →</a>'
RIBCSS='.novif-ribbon{position:fixed;right:14px;bottom:14px;z-index:99;background:#111;color:#fff;font:600 13px/1.2 system-ui,sans-serif;padding:10px 14px;border-radius:999px;text-decoration:none;box-shadow:0 6px 20px rgba(0,0,0,.25)}.novif-ribbon b{color:#7cf2c4}.novif-ribbon:hover{background:#000}'
BASE='''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:var(--body);color:var(--ink);background:var(--bg);line-height:1.6}img,svg{max-width:100%;display:block}a{color:inherit}
.wrap{max-width:1120px;margin:auto;padding:0 20px}header.nav{position:sticky;top:0;z-index:50;background:var(--navbg);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
header.nav .wrap{display:flex;align-items:center;justify-content:space-between;height:64px}.logo{font-family:var(--head);font-size:1.35rem;font-weight:700;text-decoration:none}
header nav a{margin-left:22px;text-decoration:none;font-size:.95rem;opacity:.85}header nav a:hover{opacity:1}
.btn{display:inline-block;background:var(--acc);color:var(--accink);padding:13px 24px;border-radius:var(--rad);text-decoration:none;font-weight:700;border:2px solid var(--acc)}.btn.ghost{background:transparent;color:inherit;border-color:currentColor}
section{padding:84px 0}h1,h2,h3{font-family:var(--head);line-height:1.15;margin:0 0 .5em}h2{font-size:clamp(1.8rem,4vw,2.6rem)}.eyebrow{text-transform:uppercase;letter-spacing:.16em;font-size:.78rem;color:var(--acc2);font-weight:700}
.hero{min-height:min(88vh,760px);display:flex;align-items:center;position:relative;overflow:hidden}.hero>.wrap{width:100%}.hero h1{font-size:clamp(2.4rem,7vw,4.8rem)}.hero p{font-size:1.15rem;max-width:540px}.cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}
.grid{display:grid;gap:22px}.g2{grid-template-columns:1fr 1fr}.g3{grid-template-columns:repeat(3,1fr)}
.price-list{list-style:none;padding:0;margin:0}.price-list li{display:flex;justify-content:space-between;gap:16px;padding:14px 0;border-bottom:1px dashed var(--line)}.price-list small{display:block;opacity:.7}.price-list .p{font-weight:700;white-space:nowrap}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--rad);padding:26px}
.gal{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.gal figure{margin:0;border-radius:var(--rad);overflow:hidden;aspect-ratio:1}.gal figure:nth-child(1){grid-column:span 2;grid-row:span 2}.gal svg{width:100%;height:100%}
.hours{list-style:none;padding:0}.hours li{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid var(--line)}
.map{width:100%;height:340px;border:0;border-radius:var(--rad)}.stars{color:var(--acc2);letter-spacing:2px}.sample{font-size:.75rem;background:var(--line);padding:2px 8px;border-radius:99px;vertical-align:middle}
footer{padding:40px 0 90px;font-size:.9rem;opacity:.8;border-top:1px solid var(--line)}
@media(max-width:820px){.g2,.g3{grid-template-columns:1fr}header nav a:not(.btn){display:none}.gal{grid-template-columns:1fr 1fr}section{padding:60px 0}.hero{min-height:auto;padding:70px 0}}
'''
def page(d):
    svc=''.join(f'<li><span>{n}<small>{s}</small></span><span class="p">{p}</span></li>' for n,s,p in d['items'])
    hours=''.join(f'<li><span>{a}</span><span>{b}</span></li>' for a,b in d['hours'])
    revs=''.join(f'<div class="card"><div class="stars">★★★★★</div><p>“{t}”</p><b>— {w}</b></div>' for t,w in d['reviews'])
    gal=''.join(f'<figure>{s}</figure>' for s in d['gallery'])
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>{d['name']} — demo website by novif</title><meta name="description" content="Fictional demo website for {d['name']}, made by novif.">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>{d['emoji']}</text></svg>">
{d.get('fonts','')}<style>:root{{{d['vars']}}}{BASE}{d['css']}{RIBCSS}</style></head><body>
<header class="nav"><div class="wrap"><a class="logo" href="#">{d['logo']}</a><nav><a href="#services">{d['svclabel']}</a><a href="#about">About</a><a href="#gallery">Gallery</a><a href="#visit">Visit</a><a class="btn" href="#book">{d['ctalabel']}</a></nav></div></header>
<section class="hero">{d['heroart']}<div class="wrap" style="position:relative"><div class="eyebrow">{d['tag']}</div><h1>{d['h1']}</h1><p>{d['lead']}</p><div class="cta"><a class="btn" href="#book">{d['ctalabel']}</a><a class="btn ghost" href="#services">{d['svclabel']}</a></div></div></section>
<section id="services"><div class="wrap grid g2"><div><div class="eyebrow">{d['svclabel']}</div><h2>{d['svch2']}</h2><p>{d['svcp']}</p></div><ul class="price-list">{svc}</ul></div></section>
<section id="about" class="alt"><div class="wrap grid g2" style="align-items:center"><div class="aboutart">{d['aboutart']}</div><div><div class="eyebrow">About</div><h2>{d['abouth']}</h2>{d['about']}</div></div></section>
<section id="gallery"><div class="wrap"><div class="eyebrow">Gallery</div><h2>{d['galh']}</h2><div class="gal">{gal}</div></div></section>
<section id="reviews" class="alt"><div class="wrap"><div class="eyebrow">Reviews <span class="sample">sample reviews</span></div><h2>What guests say</h2><div class="grid g3">{revs}</div><p style="font-size:.85rem;opacity:.7">Sample reviews for demonstration only.</p></div></section>
<section id="visit"><div class="wrap grid g2"><div><div class="eyebrow">Visit</div><h2>Opening hours</h2><ul class="hours">{hours}</ul><p>{d['addr']}</p></div><iframe class="map" loading="lazy" title="Map" src="https://www.openstreetmap.org/export/embed.html?bbox={d['bbox']}&amp;layer=mapnik"></iframe></div></section>
<section id="book" class="booking"><div class="wrap" style="text-align:center"><h2>{d['bookh']}</h2><p>{d['bookp']}</p><div class="cta" style="justify-content:center"><a class="btn" href="mailto:hello@example.com?subject={d['name']}%20booking">{d['ctalabel']}</a><a class="btn ghost" href="tel:+4700000000">Call +47 00 00 00 00</a></div><p style="font-size:.8rem;opacity:.7">Demo: booking button and phone number are placeholders.</p></div></section>
<footer><div class="wrap">© 2026 {d['name']} · <b>Fictional business</b> — this is a demo website made by <a href="../../">novif</a>. Address, phone and reviews are placeholders.</div></footer>
{RIB}</body></html>'''

def blob(c1,c2,shape):
    return f'<svg viewBox="0 0 200 200" preserveAspectRatio="xMidYMid slice"><defs><linearGradient id="g{c1[1:]}{c2[1:]}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs><rect width="200" height="200" fill="url(#g{c1[1:]}{c2[1:]})"/>{shape}</svg>'

# BARBER
pole='<g><rect x="88" y="30" width="24" height="140" rx="12" fill="#f4efe6"/><path d="M88 50l24-14v18l-24 14zM88 86l24-14v18l-24 14zM88 122l24-14v18l-24 14zM88 158l24-14v14l-24 10z" fill="#b8352b"/><rect x="82" y="24" width="36" height="12" rx="4" fill="#c9a45c"/><rect x="82" y="164" width="36" height="12" rx="4" fill="#c9a45c"/></g>'
scis='<g fill="none" stroke="#c9a45c" stroke-width="6"><circle cx="70" cy="140" r="18"/><circle cx="130" cy="140" r="18"/><path d="M82 126L140 40M118 126L60 40"/></g>'
razor='<g><rect x="40" y="90" width="120" height="22" rx="4" fill="#d9d4cb"/><rect x="40" y="112" width="70" height="14" rx="4" fill="#3a2d22"/><circle cx="150" cy="101" r="5" fill="#c9a45c"/></g>'
comb='<g fill="#c9a45c"><rect x="30" y="80" width="140" height="18" rx="4"/>'+''.join(f'<rect x="{34+i*9}" y="98" width="5" height="30"/>' for i in range(15))+'</g>'
chair='<g fill="#3a2d22"><rect x="60" y="70" width="80" height="60" rx="10" fill="#7a2d24"/><rect x="55" y="125" width="90" height="16" rx="6"/><rect x="95" y="141" width="10" height="30"/><rect x="70" y="168" width="60" height="8" rx="4"/></g>'
barber=dict(name='Nordkant Barbers',logo='NORDKANT<span style="color:var(--acc)">.</span>',emoji='💈',tag='Barbershop · Oslo (fictional)',
 h1='Sharp cuts.<br>Hot towels.<br>No rush.',lead='A classic gentlemen’s barbershop with modern technique. Walk in, sit down, leave looking like the best version of yourself.',
 svclabel='Prices',ctalabel='Book a chair',svch2='Cuts &amp; shaves',svcp='Every service includes a consultation, hot towel and styling. Prices in NOK.',
 items=[('Classic cut','Scissor or clipper, washed &amp; styled','450 kr'),('Skin fade','Precision fade, line-up included','520 kr'),('Beard trim &amp; shape','Hot towel, razor line','320 kr'),('Hot towel shave','Traditional straight razor','490 kr'),('Cut + beard','The full works','720 kr'),('Kids (under 12)','Patient barbers, promise','300 kr')],
 abouth='Old-school craft, new-school style',about='<p>Nordkant is a fictional barbershop built to show what a modern site for a small shop can look like. Picture three chairs, a record player in the corner, and barbers who actually listen.</p><p>Drop-ins welcome; bookings get priority.</p>',
 aboutart=f'<div style="border-radius:var(--rad);overflow:hidden;aspect-ratio:4/3">{blob("#2a211a","#120e0b",pole)}</div>',
 galh='Fresh from the chair',gallery=[blob('#2a211a','#120e0b',chair),blob('#3a2d22','#1b1511',scis),blob('#7a2d24','#3a1511',razor),blob('#1b1511','#3a2d22',comb),blob('#c9a45c','#7a5a28',scis.replace('#c9a45c','#1b1511'))],
 reviews=[('Best fade I’ve had in years. Booked my next one before I left.','Sample customer'),('Hot towel shave was pure luxury. Great music too.','Sample customer'),('Took my son for his first real haircut — they were brilliant.','Sample customer')],
 hours=[('Mon–Fri','10:00 – 19:00'),('Saturday','10:00 – 16:00'),('Sunday','Closed')],addr='Example street 12, 0150 Oslo (placeholder address)',bbox='10.735%2C59.908%2C10.760%2C59.918',
 bookh='Ready for a fresh cut?',bookp='Book online in under a minute, or just walk in.',
 fonts='',vars='--head:Georgia,"Times New Roman",serif;--body:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;--ink:#efe7da;--bg:#14100d;--card:#1d1713;--line:#3a2f26;--acc:#c9a45c;--accink:#14100d;--acc2:#d8b56c;--rad:4px;--navbg:rgba(20,16,13,.85)',
 css='.hero{background:radial-gradient(ellipse at 80% 30%,#3a2d22,#14100d 60%)}.hero h1{letter-spacing:-.01em}.heroart{position:absolute;right:6%;top:50%;transform:translateY(-50%);width:min(34vw,360px);opacity:.9}.alt{background:#1a1410}.booking{background:#c9a45c;color:#14100d}.booking .btn{background:#14100d;color:#efe7da;border-color:#14100d}@media(max-width:820px){.heroart{display:none}}',
 heroart=f'<svg class="heroart" viewBox="0 0 200 200">{pole}</svg>')

# COFFEE
cup='<g><ellipse cx="100" cy="150" rx="70" ry="14" fill="#e9dccb"/><path d="M50 80h100l-10 64a12 12 0 0 1-12 10H72a12 12 0 0 1-12-10z" fill="#fffaf2"/><path d="M150 92c22 0 22 34 0 34" fill="none" stroke="#fffaf2" stroke-width="9"/><ellipse cx="100" cy="82" rx="50" ry="10" fill="#6b4226"/><path d="M90 80c6-6 14-6 20 0" stroke="#e9cfae" stroke-width="4" fill="none"/><path d="M80 60c-8-12 8-16 0-30M100 56c-8-12 8-16 0-30M120 60c-8-12 8-16 0-30" stroke="#fff" stroke-opacity=".7" stroke-width="4" fill="none" stroke-linecap="round"/></g>'
bean='<g fill="#6b4226">'+''.join(f'<g transform="translate({x},{y}) rotate({r})"><ellipse rx="16" ry="11"/><path d="M-14 0c8-4 20 4 28 0" stroke="#3d2414" stroke-width="2.5" fill="none"/></g>' for x,y,r in [(60,60,20),(130,70,-30),(90,120,60),(150,140,10),(50,150,-40),(110,40,80)])+'</g>'
bun='<g><circle cx="100" cy="105" r="55" fill="#c88a4a"/><path d="M60 95c20-30 60-30 80 0M55 115c25-20 65-20 90 0" stroke="#8b5a2b" stroke-width="6" fill="none"/><circle cx="85" cy="90" r="3" fill="#fff"/><circle cx="110" cy="100" r="3" fill="#fff"/><circle cx="125" cy="88" r="3" fill="#fff"/></g>'
plant='<g><rect x="80" y="120" width="40" height="50" rx="6" fill="#d8754a"/><path d="M100 120C80 90 60 90 60 60c20 0 35 20 40 60zm0 0c20-30 40-40 40-75-20 5-35 30-40 75z" fill="#5f7d4e"/></g>'
coffee=dict(name='Morgenlys Kaffebar',logo='morgenlys',emoji='☕',tag='Specialty coffee · Bergen (fictional)',
 h1='Slow coffee for<br>fast mornings.',lead='Light-roasted single origins, fresh cardamom buns from our own oven, and big windows full of morning light.',
 svclabel='Menu',ctalabel='Order ahead',svch2='Today’s menu',svcp='Beans roasted weekly by local partners. Oat milk at no extra cost. Prices in NOK.',
 items=[('Espresso','Single origin, rotating','38 kr'),('Flat white','Double ristretto, silky milk','52 kr'),('Filter of the day','V60 or batch brew','45 kr'),('Iced oat latte','House vanilla optional','58 kr'),('Cardamom bun','Baked every morning','42 kr'),('Avocado sourdough','Chili, lemon, seeds','95 kr')],
 abouth='A neighbourhood living room',about='<p>Morgenlys (“morning light”) is a fictional café created as a demo. It imagines a small, bright space where regulars have a usual and laptops are welcome before noon.</p><p>Free Wi-Fi · Dog friendly · Plant-based options</p>',
 aboutart=f'<div style="border-radius:var(--rad);overflow:hidden;aspect-ratio:4/3">{blob("#f3e3cf","#e6c9a5",cup)}</div>',
 galh='Little moments',gallery=[blob('#f3e3cf','#e6c9a5',cup),blob('#efe1d0','#d9b892',bean),blob('#f7ead9','#ebcfae',bun),blob('#e3ecdc','#c9d9bd',plant),blob('#6b4226','#3d2414',cup.replace('#fffaf2','#e9cfae'))],
 reviews=[('The cardamom buns are dangerous. I come in every Saturday.','Sample guest'),('Perfect flat white and the staff remember my name.','Sample guest'),('Calm, bright, great for a morning of work.','Sample guest')],
 hours=[('Mon–Fri','07:00 – 17:00'),('Saturday','08:00 – 17:00'),('Sunday','09:00 – 16:00')],addr='Example square 3, 5003 Bergen (placeholder address)',bbox='5.318%2C60.390%2C5.335%2C60.398',
 bookh='Skip the queue',bookp='Order ahead and pick up at the counter — or book the corner table for your group.',
 fonts='',vars='--head:"Trebuchet MS","Avenir Next",system-ui,sans-serif;--body:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;--ink:#3d2414;--bg:#fbf6ef;--card:#fff;--line:#ecdcc8;--acc:#d8754a;--accink:#fff;--acc2:#b55a32;--rad:22px;--navbg:rgba(251,246,239,.85)',
 css='.hero{background:linear-gradient(120deg,#fbf6ef 40%,#f3e3cf)}.hero h1{font-weight:800;letter-spacing:-.02em}.heroart{position:absolute;right:5%;bottom:0;width:min(40vw,440px)}.alt{background:#f5ebdd}.logo{font-weight:800;letter-spacing:-.03em;color:var(--acc)}.booking{background:#3d2414;color:#fbf6ef}.card{box-shadow:0 8px 30px rgba(61,36,20,.07)}@media(max-width:820px){.heroart{position:relative;right:auto;margin:0 auto 20px;width:60%}.hero{flex-direction:column-reverse}}',
 heroart=f'<svg class="heroart" viewBox="0 0 200 200">{cup}</svg>')

# TRADES
house='<g><path d="M40 100L100 50l60 50v70H40z" fill="#fff"/><path d="M30 104L100 44l70 60" stroke="#ffb703" stroke-width="10" fill="none" stroke-linejoin="round"/><rect x="88" y="125" width="24" height="45" fill="#0b3954"/><rect x="55" y="110" width="22" height="22" fill="#9cc9e4"/><rect x="123" y="110" width="22" height="22" fill="#9cc9e4"/></g>'
wrench='<g transform="rotate(-40 100 100)"><rect x="92" y="60" width="16" height="110" rx="6" fill="#ffb703"/><path d="M75 40a28 28 0 1 0 50 0l-12 0v18h-26v-18z" fill="#ffb703"/></g>'
bolt='<path d="M110 20L50 115h45l-10 65 65-100h-48z" fill="#ffb703"/>'
pipe='<g fill="none" stroke="#9cc9e4" stroke-width="18" stroke-linecap="round"><path d="M30 60h80a30 30 0 0 1 30 30v80"/></g><circle cx="140" cy="172" r="8" fill="#9cc9e4"/>'
van='<g><rect x="25" y="85" width="110" height="60" rx="8" fill="#fff"/><path d="M135 100h25l15 22v23h-40z" fill="#fff"/><rect x="142" y="105" width="16" height="14" fill="#9cc9e4"/><rect x="25" y="112" width="110" height="10" fill="#ffb703"/><circle cx="60" cy="148" r="13" fill="#0b3954" stroke="#fff" stroke-width="4"/><circle cx="150" cy="148" r="13" fill="#0b3954" stroke="#fff" stroke-width="4"/></g>'
trades=dict(name='Fjordline Rør &amp; Elektro',logo='FJORDLINE <span style="font-weight:400">Rør &amp; Elektro</span>',emoji='🔧',tag='Plumbing &amp; electrical · Trondheim (fictional)',
 h1='Leaks fixed.<br>Lights on.<br>Same day.',lead='Certified plumbers and electricians for homes and small businesses. Upfront prices, tidy work, and a 2-year workmanship guarantee.',
 svclabel='Services',ctalabel='Get a free quote',svch2='Fair, upfront pricing',svcp='Fixed call-out fee, then clear prices before we start. All prices in NOK incl. VAT.',
 items=[('Call-out &amp; first hour','Within the city area','1 290 kr'),('Additional hour','Per technician','890 kr'),('Blocked drain','Most sinks, showers &amp; toilets','from 1 690 kr'),('New socket / switch','Incl. standard parts','from 1 450 kr'),('Water heater replacement','Supply &amp; fit, 200 L','from 14 900 kr'),('EV charger install','Incl. safety check','from 12 500 kr'),('Emergency (24/7)','Evenings &amp; weekends','+50%')],
 abouth='Local, licensed, on time',about='<p>Fjordline is a fictional trades company made for this demo. It shows how a plumber or electrician can win trust online: clear prices, real credentials, and a fast way to ask for a quote.</p><ul><li>Licensed &amp; insured (placeholder)</li><li>Clean-up included on every job</li><li>Fixed-price quotes for larger work</li></ul>',
 aboutart=f'<div style="border-radius:var(--rad);overflow:hidden;aspect-ratio:4/3">{blob("#0b3954","#08263a",van)}</div>',
 galh='Recent jobs (illustrations)',gallery=[blob('#0b3954','#08263a',house),blob('#123f5c','#0b2a40',wrench),blob('#0b3954','#071d2b',bolt),blob('#16506f','#0b3954',pipe),blob('#ffb703','#fb8500',van.replace('#ffb703','#0b3954'))],
 reviews=[('Came within two hours for a burst pipe. Calm, quick and tidy.','Sample customer'),('Clear quote for our EV charger and they stuck to it.','Sample customer'),('Finally an electrician who shows up when they say.','Sample customer')],
 hours=[('Mon–Fri','07:00 – 17:00'),('Saturday','By appointment'),('Emergencies','24/7')],addr='Service area: Trondheim &amp; surroundings (placeholder)',bbox='10.380%2C63.420%2C10.420%2C63.440',
 bookh='Describe the job, get a quote today',bookp='Send a few photos and a short description — we reply within business hours.',
 fonts='',vars='--head:"Arial Black","Helvetica Neue",Arial,sans-serif;--body:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;--ink:#0b2233;--bg:#ffffff;--card:#f4f8fb;--line:#dbe6ee;--acc:#ffb703;--accink:#0b2233;--acc2:#0b6e99;--rad:10px;--navbg:rgba(255,255,255,.9)',
 css='.hero{background:#0b3954;color:#fff}.hero .eyebrow{color:#ffb703}.heroart{position:absolute;right:4%;top:50%;transform:translateY(-50%);width:min(38vw,420px)}.alt{background:#f4f8fb}.booking{background:#ffb703}.booking .btn{background:#0b2233;color:#fff;border-color:#0b2233}.booking .btn.ghost{background:transparent;color:#0b2233}.price-list .p{color:#0b6e99}@media(max-width:820px){.heroart{display:none}}',
 heroart=f'<svg class="heroart" viewBox="0 0 200 200">{house}</svg>')

for slug,d in [('barbershop',barber),('coffee',coffee),('trades',trades)]:
    open(f'demos/{slug}/index.html','w').write(page(d))
