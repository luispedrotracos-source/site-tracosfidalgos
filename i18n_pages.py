from pathlib import Path
import html, json
ROOT=Path(__file__).parent
WA='https://wa.me/351963194111?text=Hello%20Tra%C3%A7os%20Fidalgos%2C%20I%20would%20like%20to%20discuss%20a%20fashion%20production%20project.'
portfolio=json.loads((ROOT/'assets/portfolio/portfolio.json').read_text())
featured_ids={'tf-042','tf-043','tf-044','tf-045','tf-048','tf-049','tf-017','tf-053','tf-054'}
featured=[x for x in portfolio if x['id'] in featured_ids][:9]

DATA={
'en':{
 'base':'en','home':'/en/','atelier':'atelier','services':'services','process':'process','catalogues':'catalogues','paris':'paris','contact':'contact',
 'langlabel':'EN','title_home':'Traços Fidalgos — Portuguese Fashion Production Partner','desc_home':'Portuguese premium garment production partner for brands, designers, uniforms and textile projects in Europe.',
 'nav':{'atelier':'Atelier','services':'Services','portfolio':'Portfolio','process':'Process','paris':'Paris','contact':'Contact','quote':'Request quote'},
 'hero_eyebrow':'Made in Portugal · Since 2017','hero_h1':'Portuguese fashion production partner for brands, designers and demanding textile projects.','hero_lead':'We develop samples, prototypes, collections, uniforms and premium textile pieces in Portugal with technical rigour, close follow-up and consistent finishing.',
 'cta_quote':'Request quote','cta_portfolio':'View portfolio','stats':['2017','foundation','12','professionals','100k+','pieces'],
 'about_h':'Founded in Portugal, made for Europe.','about_p':'Traços Fidalgos is a Portuguese textile atelier founded in 2017 in Perafita, Matosinhos. We develop and manufacture garments and textile pieces with technical rigour, close follow-up and a premium sense of detail.',
 'value_h':'Precision, discretion and consistent finishing.','value_p':'We work as a production partner for fashion and textile projects that require adaptability, technical responsibility and careful presentation.',
 'services_h':'What we do','services_lead':'Garments, uniforms and premium textile products for brands and companies.','services_cards':[('Samples & prototypes','Technical interpretation, patterns, cutting, sewing, fitting and sample development.'),('Fashion collections','Capsule collections, dresses, blouses, tailoring, outerwear and detailed pieces.'),('Uniforms & textile projects','Premium uniforms, promotional textile pieces and customised textile products.'),('Production follow-up','Small and medium series with quality control and close communication.')],
 'process_h':'From concept to final piece.','process_lead':'A practical, precise and collaborative process from brief and sample to technical preparation, production and finishing.',
 'process_steps':[('Brief','References, drawings, technical files, quantities and deadline.'),('Technical review','Complexity, materials, finishes, patterns and feasibility.'),('Quote','Development and sample separated from production for transparency.'),('Sample','Pattern, cut, make, fitting and adjustment round.'),('Production','Small or medium series after sample approval.')],
 'portfolio_h':'Visual portfolio','portfolio_lead':'Detail, structure and material sensitivity — selected references showing proportion, fabric behaviour and finishing.',
 'paris_h':'Paris presentation','paris_lead':'Portuguese fashion production partner · presentation for European fashion and textile clients.','download':'Download full PDF book',
 'contact_h':'Let us review your project.','contact_lead':'Send references, drawings, technical files or a short description of the garment, collection or textile project you want to develop.',
 'email':'Email','whatsapp':'WhatsApp','brief':'For a quote','brief_p':'Send garment type, quantities, materials, sizes, reference images and desired deadline.'
},
'fr':{
 'base':'fr','home':'/fr/','atelier':'atelier','services':'services','process':'processus','catalogues':'catalogues','paris':'paris','contact':'contact',
 'langlabel':'FR','title_home':'Traços Fidalgos — Partenaire portugais de confection mode','desc_home':'Atelier portugais de confection haut de gamme pour marques, créateurs, uniformes et projets textiles en Europe.',
 'nav':{'atelier':'Atelier','services':'Services','portfolio':'Portfolio','process':'Processus','paris':'Paris','contact':'Contact','quote':'Demander un devis'},
 'hero_eyebrow':'Made in Portugal · Depuis 2017','hero_h1':'Partenaire portugais de confection mode pour marques, créateurs et projets textiles exigeants.','hero_lead':'Nous développons des prototypes, collections, uniformes et pièces textiles haut de gamme au Portugal avec rigueur technique, proximité et finitions régulières.',
 'cta_quote':'Demander un devis','cta_portfolio':'Voir le portfolio','stats':['2017','fondation','12','professionnels','100k+','pièces'],
 'about_h':'Fondé au Portugal, pensé pour l’Europe.','about_p':'Traços Fidalgos est un atelier textile portugais fondé en 2017 à Perafita, Matosinhos. Nous développons et confectionnons des vêtements et pièces textiles avec rigueur technique, proximité et souci du détail.',
 'value_h':'Précision, discrétion et finitions régulières.','value_p':'Nous travaillons comme partenaire de production pour des projets mode et textile nécessitant adaptabilité, responsabilité technique et présentation soignée.',
 'services_h':'Nos services','services_lead':'Vêtements, uniformes et pièces textiles haut de gamme pour marques et entreprises.','services_cards':[('Prototypes & échantillons','Interprétation technique, patronage, coupe, confection, essayage et développement de prototypes.'),('Collections mode','Collections capsules, robes, chemisiers, tailoring, outerwear et pièces détaillées.'),('Uniformes & projets textiles','Uniformes premium, articles promotionnels et pièces textiles personnalisées.'),('Suivi de production','Petites et moyennes séries avec contrôle qualité et communication proche.')],
 'process_h':'Du concept à la pièce finale.','process_lead':'Un processus pratique, précis et collaboratif, du brief et prototype à la préparation technique, production et finitions.',
 'process_steps':[('Brief','Références, dessins, dossiers techniques, quantités et délais.'),('Analyse technique','Complexité, matières, finitions, patronage et faisabilité.'),('Devis','Développement et prototype séparés de la production pour plus de transparence.'),('Prototype','Patronage, coupe, confection, essayage et ajustements.'),('Production','Petites ou moyennes séries après validation du prototype.')],
 'portfolio_h':'Portfolio visuel','portfolio_lead':'Détail, structure et sensibilité aux matières — références sélectionnées autour des proportions, matières et finitions.',
 'paris_h':'Présentation Paris','paris_lead':'Partenaire portugais de confection mode · présentation pour clients mode et textile en Europe.','download':'Télécharger le livre PDF complet',
 'contact_h':'Étudions votre projet.','contact_lead':'Envoyez références, dessins, dossiers techniques ou une courte description du vêtement, collection ou projet textile à développer.',
 'email':'Email','whatsapp':'WhatsApp','brief':'Pour un devis','brief_p':'Envoyez type de pièce, quantités, matières, tailles, images de référence et délai souhaité.'
}}

def links_for(lang, current):
    d=DATA[lang]
    # current key maps to path for each language
    maps={
     'home': {'pt':'/','en':'/en/','fr':'/fr/'},
     'atelier': {'pt':'/atelier/','en':'/en/atelier/','fr':'/fr/atelier/'},
     'services': {'pt':'/servicos/','en':'/en/services/','fr':'/fr/services/'},
     'process': {'pt':'/processo/','en':'/en/process/','fr':'/fr/processus/'},
     'catalogues': {'pt':'/catalogos/','en':'/en/catalogues/','fr':'/fr/catalogues/'},
     'paris': {'pt':'/paris/','en':'/en/paris/','fr':'/fr/paris/'},
     'contact': {'pt':'/contacto/','en':'/en/contact/','fr':'/fr/contact/'},
    }[current]
    return maps

def head(lang,current,title,desc,prefix='../'):
    maps=links_for(lang,current); canon='https://tracosfidalgos.pt'+maps[lang]
    alts=''.join([f'<link rel="alternate" hreflang="{code if code!="pt" else "pt-PT"}" href="https://tracosfidalgos.pt{url}">' for code,url in maps.items()])
    return f'<!doctype html><html lang="{ "en" if lang=="en" else "fr" }"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{canon}">{alts}<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet"><link rel="stylesheet" href="{prefix}styles.css"></head><body id="top">'

def header(lang,current,prefix='../'):
    d=DATA[lang]; maps=links_for(lang,current); nav=d['nav']
    return f'<header class="site-header"><div class="shell nav-wrap"><a class="brand" href="/{d["base"]}/"><img src="{prefix}assets/logo-tf.svg" alt="Traços Fidalgos"><span>Traços Fidalgos</span></a><button class="nav-toggle" aria-label="Menu">☰</button><nav class="nav"><a href="/{d["base"]}/{d["atelier"]}/">{nav["atelier"]}</a><a href="/{d["base"]}/{d["services"]}/">{nav["services"]}</a><a href="/{d["base"]}/{d["catalogues"]}/">{nav["portfolio"]}</a><a href="/{d["base"]}/{d["process"]}/">{nav["process"]}</a><a href="/{d["base"]}/paris/">{nav["paris"]}</a><a href="/{d["base"]}/{d["contact"]}/">{nav["contact"]}</a><a class="pill" href="/{d["base"]}/{d["contact"]}/">{nav["quote"]}</a><span class="lang"><a href="{maps["pt"]}">PT</a><a href="{maps["en"]}">EN</a><a href="{maps["fr"]}">FR</a></span></nav></div></header>'

def footer(prefix='../'):
    return f'<a class="whatsapp-float" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp"><span class="wa-icon">☎</span><span>WhatsApp</span></a><footer class="footer"><div class="shell"><span>© <span data-year></span> Traços Fidalgos</span><a href="#top">Top ↑</a></div></footer><script src="{prefix}script.js"></script></body></html>'

def portfolio_grid(prefix='../', items=featured):
    out=['<div class="portfolio-grid">']
    for it in items:
        out.append(f'<article class="portfolio-card reveal"><img src="{prefix}{it["src"]}" alt="{html.escape(it["alt"])}" loading="lazy"><div class="portfolio-copy"><small>Portfolio</small><h3>Premium textile piece</h3><p>Construction, finishing and material sensitivity for European fashion projects.</p></div></article>')
    return ''.join(out)+'</div>'

def page(lang,current,path,title,desc,body,prefix='../'):
    p=ROOT/path; p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(head(lang,current,title,desc,prefix)+header(lang,current,prefix)+body+footer(prefix))

for lang,d in DATA.items():
    base=d['base']
    home=f'<main><section class="hero"><div class="shell hero-grid"><div class="reveal"><p class="eyebrow">{d["hero_eyebrow"]}</p><h1>{d["hero_h1"]}</h1><p class="lead">{d["hero_lead"]}</p><div class="actions"><a class="btn primary" href="/{base}/{d["contact"]}/">{d["cta_quote"]}</a><a class="btn ghost" href="/{base}/{d["catalogues"]}/">{d["cta_portfolio"]}</a></div><div class="stats"><div><strong>{d["stats"][0]}</strong><span>{d["stats"][1]}</span></div><div><strong>{d["stats"][2]}</strong><span>{d["stats"][3]}</span></div><div><strong>{d["stats"][4]}</strong><span>{d["stats"][5]}</span></div></div></div><div class="hero-media reveal"><div class="video-stack"><figure class="hero-video-card"><video src="../assets/videos/atelier-video.mp4" autoplay muted loop playsinline controls preload="metadata"></video></figure><figure class="image-card two video-overlap"><img src="../assets/portfolio/treated/tf-042.webp" alt="Traços Fidalgos portfolio"></figure></div><div class="float-badge"><strong>Premium</strong><span>Atelier & production</span></div></div></div></section><section class="section"><div class="shell split"><div><p class="eyebrow">About</p><h2>{d["about_h"]}</h2><p class="lead">{d["about_p"]}</p></div><div class="panel"><h3>{d["value_h"]}</h3><p>{d["value_p"]}</p><div class="actions"><a class="btn primary" href="/{base}/paris/">{d["download"]}</a></div></div></div></section><section class="section dark"><div class="shell"><p class="eyebrow">Portfolio</p><h2>{d["portfolio_h"]}</h2><p class="lead">{d["portfolio_lead"]}</p>{portfolio_grid()}</div></section></main>'
    page(lang,'home',Path(base)/'index.html',d['title_home'],d['desc_home'],home)
    atelier=f'<main><section class="page-hero"><div class="shell"><p class="eyebrow">Atelier</p><h1>{d["about_h"]}</h1><p class="lead">{d["about_p"]}</p></div></section><section class="section dark"><div class="shell split"><div><p class="eyebrow">Our value</p><h2>{d["value_h"]}</h2></div><div class="panel"><p>{d["value_p"]}</p></div></div></section></main>'
    page(lang,'atelier',Path(base)/d['atelier']/'index.html',f'Atelier — Traços Fidalgos',d['about_p'],atelier)
    cards=''.join([f'<article class="service reveal"><span>{i:02d}</span><h3>{html.escape(t)}</h3><p>{html.escape(p)}</p></article>' for i,(t,p) in enumerate(d['services_cards'],1)])
    services=f'<main><section class="page-hero"><div class="shell"><p class="eyebrow">Services</p><h1>{d["services_h"]}</h1><p class="lead">{d["services_lead"]}</p></div></section><section class="section dark"><div class="shell"><div class="services">{cards}</div></div></section></main>'
    page(lang,'services',Path(base)/d['services']/'index.html',f'{d["services_h"]} — Traços Fidalgos',d['services_lead'],services)
    steps=''.join([f'<li><strong>{html.escape(t)}</strong><span>{html.escape(p)}</span></li>' for t,p in d['process_steps']])
    process=f'<main><section class="page-hero"><div class="shell"><p class="eyebrow">Process</p><h1>{d["process_h"]}</h1><p class="lead">{d["process_lead"]}</p></div></section><section class="section"><div class="shell"><ol class="process reveal">{steps}</ol></div></section></main>'
    page(lang,'process',Path(base)/d['process']/'index.html',f'{d["process_h"]} — Traços Fidalgos',d['process_lead'],process)
    cat=f'<main><section class="page-hero"><div class="shell"><p class="eyebrow">Portfolio</p><h1>{d["portfolio_h"]}</h1><p class="lead">{d["portfolio_lead"]}</p></div></section><section class="section"><div class="shell">{portfolio_grid(items=portfolio)}</div></section></main>'
    page(lang,'catalogues',Path(base)/d['catalogues']/'index.html',f'{d["portfolio_h"]} — Traços Fidalgos',d['portfolio_lead'],cat)
    book_imgs=''.join([f'<article class="portfolio-card reveal wide"><img src="../assets/book/paris/book-page-{i:02d}.webp" alt="Traços Fidalgos Paris presentation page {i:02d}" loading="lazy"><div class="portfolio-copy"><small>Paris book</small><h3>Page {i:02d}</h3><p>{html.escape(d["paris_lead"])}</p></div></article>' for i in range(1,7)])
    paris=f'<main><section class="page-hero"><div class="shell"><p class="eyebrow">Paris</p><h1>{d["paris_h"]}</h1><p class="lead">{d["paris_lead"]}</p><div class="actions"><a class="btn primary" href="../assets/downloads/tracos-fidalgos-paris-presentation.pdf" download>{d["download"]}</a><a class="btn ghost" href="/{base}/{d["contact"]}/">{d["cta_quote"]}</a></div></div></section><section class="section"><div class="shell"><div class="portfolio-grid presentation-grid">{book_imgs}</div></div></section></main>'
    page(lang,'paris',Path(base)/'paris'/'index.html',f'{d["paris_h"]} — Traços Fidalgos',d['paris_lead'],paris)
    contact=f'<main><section class="page-hero"><div class="shell"><p class="eyebrow">Contact</p><h1>{d["contact_h"]}</h1><p class="lead">{d["contact_lead"]}</p><div class="actions"><a class="btn primary" href="mailto:geralt.fidalgos@gmail.com?subject=Tra%C3%A7os%20Fidalgos%20project%20request">{d["email"]}</a><a class="btn ghost" href="{WA}">{d["whatsapp"]}</a></div></div></section><section class="section"><div class="shell contact-grid"><address class="panel reveal"><strong>Traços Fidalgos</strong><br>Rua 9 de Julho 1277<br>4455-508 Perafita<br>Matosinhos, Portugal<br><br><a href="mailto:geralt.fidalgos@gmail.com">geralt.fidalgos@gmail.com</a><br><a href="tel:+351963194111">+351 96 31 94 111</a></address><div class="panel reveal"><h3>{d["brief"]}</h3><p>{d["brief_p"]}</p></div></div></section></main>'
    page(lang,'contact',Path(base)/d['contact']/'index.html',f'{d["contact_h"]} — Traços Fidalgos',d['contact_lead'],contact)

# sitemap
urls=['/','/atelier/','/servicos/','/processo/','/catalogos/','/paris/','/contacto/',
      '/en/','/en/atelier/','/en/services/','/en/process/','/en/catalogues/','/en/paris/','/en/contact/',
      '/fr/','/fr/atelier/','/fr/services/','/fr/processus/','/fr/catalogues/','/fr/paris/','/fr/contact/']
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join([f'  <url><loc>https://tracosfidalgos.pt{u}</loc></url>\n' for u in urls]) + '</urlset>\n'
(ROOT/'sitemap.xml').write_text(sm)
print('generated i18n pages', len(urls))
