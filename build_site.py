from pathlib import Path
import json, html

ROOT = Path(__file__).parent
portfolio = json.loads((ROOT/'assets/portfolio/portfolio.json').read_text())

WA = 'https://wa.me/351963194111?text=Ol%C3%A1%20Tra%C3%A7os%20Fidalgos%2C%20gostaria%20de%20falar%20sobre%20um%20projeto%20de%20confe%C3%A7%C3%A3o.'

cats = [
 ('vestidos-silhuetas','Vestidos & silhuetas','Vestidos, silhuetas femininas e peças especiais com movimento, proporção e acabamento premium.'),
 ('blusas-camisas','Blusas & tops statement','Blusas, camisas e tops com volume, laços, textura e construção diferenciada.'),
 ('casacos-tailoring','Tailoring & outerwear','Casacos, peças estruturadas, outerwear e propostas com leitura técnica.'),
 ('rendas-transparencias','Rendas & transparências','Rendas, transparências e detalhes delicados que exigem precisão no corte e na confeção.'),
 ('saias-calcas','Saias, calças & coordenados','Bases comerciais e coordenados para cápsulas, boutiques e private label.'),
 ('atelier-processo','Atelier & processo','Bastidores, etiquetas, apresentação e detalhes de execução que reforçam o saber-fazer.'),
]
cat_titles = {c[0]: c[1] for c in cats}
cat_desc = {c[0]: c[2] for c in cats}

featured_ids = {'tf-042','tf-043','tf-044','tf-045','tf-048','tf-049','tf-017','tf-053','tf-054'}
featured = [x for x in portfolio if x['id'] in featured_ids][:9]

def rel(prefix=''):
    return prefix

def head(title, desc, prefix=''):
    return f'''<!doctype html><html lang="pt-PT"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="https://tracosfidalgos.pt/"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet"><link rel="stylesheet" href="{prefix}styles.css"></head><body id="top">'''

def header(prefix=''):
    return f'''<header class="site-header"><div class="shell nav-wrap"><a class="brand" href="{prefix}"><img src="{prefix}assets/logo-tf.svg" alt="Traços Fidalgos"><span>Traços Fidalgos</span></a><button class="nav-toggle" aria-label="Menu">☰</button><nav class="nav"><a href="{prefix}atelier/">Atelier</a><a href="{prefix}servicos/">Serviços</a><a href="{prefix}catalogos/">Portfólio</a><a href="{prefix}processo/">Processo</a><a href="{prefix}paris/">Paris</a><a href="{prefix}contacto/">Contacto</a><a class="pill" href="{WA}">WhatsApp</a><span class="lang"><a href="{prefix}">PT</a><a href="{prefix}en/">EN</a><a href="{prefix}fr/">FR</a></span></nav></div></header>'''

def footer(prefix=''):
    return f'''<a class="whatsapp-float" href="{WA}" target="_blank" rel="noopener" aria-label="Falar no WhatsApp"><span class="wa-icon">☎</span><span>WhatsApp</span></a><footer class="footer"><div class="shell"><span>© <span data-year></span> Traços Fidalgos</span><a href="#top">Top ↑</a></div></footer><script src="{prefix}script.js"></script></body></html>'''

def img_grid(items, prefix='', limit=None):
    if limit: items = items[:limit]
    out=['<div class="portfolio-grid">']
    for it in items:
        src = prefix + it['src']
        out.append(f'''<article class="portfolio-card reveal"><img src="{src}" alt="{html.escape(it['alt'])}" loading="lazy"><div class="portfolio-copy"><small>{html.escape(cat_titles.get(it['category'],'Portfólio'))}</small><h3>{html.escape(title_for(it))}</h3><p>{html.escape(short_desc(it))}</p></div></article>''')
    out.append('</div>')
    return ''.join(out)

def title_for(it):
    n=it['n']; cat=it['category']
    if cat=='vestidos-silhuetas': return 'Silhueta feminina premium'
    if cat=='blusas-camisas': return 'Blusa / top de coleção'
    if cat=='casacos-tailoring': return 'Peça estruturada'
    if cat=='rendas-transparencias': return 'Renda e detalhe delicado'
    if cat=='saias-calcas': return 'Coordenado comercial'
    if cat=='atelier-processo': return 'Detalhe de atelier'
    return f'Peça de portfólio {n:02d}'

def short_desc(it):
    return cat_desc.get(it['category'],'Referência visual de acabamento, material e construção para desenvolvimento de coleção.')

def page(path, title, desc, body, prefix=''):
    p=ROOT/path; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(head(title, desc, prefix)+header(prefix)+body+footer(prefix))

home_body = f'''<main><section class="hero"><div class="shell hero-grid"><div class="reveal"><p class="eyebrow">Made in Portugal · Since 2017</p><h1>Confeção premium portuguesa para marcas, designers e projetos exigentes.</h1><p class="lead">Desenvolvemos amostras, protótipos, coleções e produção especializada em Portugal, com rigor técnico, atenção ao detalhe e acabamento de alto nível.</p><div class="actions"><a class="btn primary" href="contacto/">Pedir orçamento</a><a class="btn ghost" href="catalogos/">Ver portfólio</a></div><div class="stats"><div><strong>2017</strong><span>fundação</span></div><div><strong>12</strong><span>profissionais</span></div><div><strong>100k+</strong><span>peças</span></div></div></div><div class="hero-media reveal"><div class="video-stack"><figure class="hero-video-card"><video src="assets/videos/atelier-video.mp4" autoplay muted loop playsinline controls preload="metadata" aria-label="Vídeo do atelier Traços Fidalgos"></video></figure><figure class="image-card two video-overlap"><img src="assets/portfolio/treated/tf-042.webp" alt="Portfólio Traços Fidalgos"></figure></div><div class="float-badge"><strong>Premium</strong><span>Atelier & production</span></div></div></div></section><div class="marquee"><span>Samples · Prototypes · Collections · Private Label · Made in Portugal · Premium Finishing · </span></div><section class="section"><div class="shell split"><div class="reveal"><p class="eyebrow">Atelier</p><h2>Experiência técnica com imagem premium.</h2><p class="lead">Um parceiro português para transformar ideias, fichas técnicas e referências em peças reais.</p><div class="actions"><a class="btn primary" href="atelier/">Conhecer atelier</a><a class="btn ghost" href="servicos/">Serviços</a></div></div><div class="panel reveal"><p>A Traços Fidalgos é uma empresa portuguesa de confeção premium e alta costura, fundada em 2017 e sediada em Perafita, Matosinhos.</p><p>Trabalhamos com marcas, designers, boutiques e projetos B2B que procuram desenvolvimento cuidado, flexibilidade e confiança na produção europeia.</p></div></div></section><section class="section dark"><div class="shell"><p class="eyebrow">Portfólio</p><h2>Peças e referências de coleção</h2><p class="lead">Imagens tratadas com correção de cor, enquadramento editorial e organização por categoria.</p>{img_grid(featured, limit=9)}<div class="actions"><a class="btn primary" href="catalogos/">Ver todas as imagens</a></div></div></section></main>'''
page(Path('index.html'),'Traços Fidalgos — Confeção Premium em Portugal','Confeção premium portuguesa para marcas, designers, coleções e private label.',home_body,'')

page(Path('atelier/index.html'),'Atelier — Traços Fidalgos','Atelier português de confeção premium em Perafita, Matosinhos.', '''<main><section class="page-hero"><div class="shell"><p class="eyebrow">Atelier</p><h1>Produção portuguesa com rigor técnico e sensibilidade estética.</h1><p class="lead">Desde 2017, a Traços Fidalgos trabalha com marcas e clientes que procuram confiança, detalhe e acabamento premium na produção europeia.</p></div></section><section class="section"><div class="shell split"><div><h2>Quem somos</h2></div><div class="panel"><p>Atelier em Perafita, Matosinhos, com equipa experiente, capacidade técnica e acompanhamento próximo desde o briefing até à peça final.</p><p><strong>Rua 9 de Julho 1277, 4455-508 Perafita · Matosinhos · Portugal</strong></p></div></div></section></main>''', '../')

page(Path('servicos/index.html'),'Serviços — Traços Fidalgos','Serviços de samples, protótipos, private label, produção e peças especiais.', '''<main><section class="page-hero"><div class="shell"><p class="eyebrow">Serviços</p><h1>Do protótipo à produção.</h1><p class="lead">Apoiamos marcas em samples, protótipos, cápsulas, private label e pequena/média produção.</p></div></section><section class="section dark"><div class="shell"><div class="services"><article class="service reveal"><span>01</span><h3>Samples</h3><p>Interpretação técnica, modelagem, corte, confeção e fitting.</p></article><article class="service reveal"><span>02</span><h3>Cápsulas</h3><p>Pequenas séries premium para boutiques, designers e marcas.</p></article><article class="service reveal"><span>03</span><h3>Produção</h3><p>Produção europeia com controlo de qualidade e comunicação próxima.</p></article><article class="service reveal"><span>04</span><h3>Projetos especiais</h3><p>Vestidos, blusas, tailoring, kimonos, lenços e peças detalhadas.</p></article></div></div></section></main>''', '../')

page(Path('processo/index.html'),'Processo — Traços Fidalgos','Processo de trabalho para desenvolvimento de peças e coleções.', '''<main><section class="page-hero"><div class="shell"><p class="eyebrow">Processo</p><h1>Um processo claro para projetos exigentes.</h1><p class="lead">Da primeira referência à produção final, cada etapa é analisada com transparência técnica.</p></div></section><section class="section"><div class="shell"><ol class="process reveal"><li><strong>Briefing</strong><span>Referências, desenhos, fichas técnicas, quantidades e prazos.</span></li><li><strong>Análise técnica</strong><span>Complexidade, materiais, acabamentos, modelagem e viabilidade.</span></li><li><strong>Orçamento</strong><span>Desenvolvimento/amostra separado da produção para maior clareza.</span></li><li><strong>Amostra</strong><span>Modelagem, corte, confeção, fitting e ajustes combinados.</span></li><li><strong>Produção</strong><span>Pequena/média série após aprovação da amostra.</span></li></ol></div></section></main>''', '../')

# catalog index
cat_cards=''.join([f'''<a class="catalog-card reveal" href="#{slug}"><img src="../assets/portfolio/treated/{ {'vestidos-silhuetas':'tf-042','blusas-camisas':'tf-001','casacos-tailoring':'tf-017','rendas-transparencias':'tf-053','saias-calcas':'tf-052','atelier-processo':'tf-009'}[slug] }.webp" alt="{html.escape(title)}"><div class="copy"><small>Portfólio</small><h3>{html.escape(title)}</h3><p>{html.escape(desc)}</p></div></a>''' for slug,title,desc in cats])
sections=[]
for slug,title,desc in cats:
    items=[x for x in portfolio if x['category']==slug]
    sections.append(f'''<section class="section portfolio-section" id="{slug}"><div class="shell"><p class="eyebrow">{html.escape(title)}</p><h2>{html.escape(title)}</h2><p class="lead">{html.escape(desc)}</p>{img_grid(items, prefix='../')}</div></section>''')
page(Path('catalogos/index.html'),'Portfólio & Catálogos — Traços Fidalgos','Galeria organizada de peças, acabamentos e referências de moda produzidas pela Traços Fidalgos.', f'''<main><section class="page-hero"><div class="shell"><p class="eyebrow">Portfólio</p><h1>Catálogos visuais organizados por categoria.</h1><p class="lead">Fotografias tratadas para apresentação profissional, com correção de cor e enquadramento consistente.</p><div class="catalog-grid">{cat_cards}</div></div></section>{''.join(sections)}</main>''', '../')

# contact page
page(Path('contacto/index.html'),'Contacto — Traços Fidalgos','Contactos da Traços Fidalgos para pedidos de orçamento e projetos de confeção.', f'''<main><section class="page-hero"><div class="shell"><p class="eyebrow">Contacto</p><h1>Vamos analisar o seu projeto?</h1><p class="lead">Envie referências, desenhos, fichas técnicas ou uma descrição da peça/coleção que pretende desenvolver.</p><div class="actions"><a class="btn primary" href="mailto:geralt.fidalgos@gmail.com?subject=Pedido%20de%20or%C3%A7amento%20-%20Tra%C3%A7os%20Fidalgos">Email</a><a class="btn ghost" href="{WA}">WhatsApp</a></div></div></section><section class="section"><div class="shell contact-grid"><address class="panel reveal"><strong>Traços Fidalgos</strong><br>Rua 9 de Julho 1277<br>4455-508 Perafita<br>Matosinhos, Portugal<br><br><a href="mailto:geralt.fidalgos@gmail.com">geralt.fidalgos@gmail.com</a><br><a href="tel:+351963194111">+351 96 31 94 111</a></address><div class="panel reveal"><h3>Para pedir orçamento</h3><p>Envie tipo de peça, quantidades, materiais, tamanhos, imagens de referência e prazo desejado.</p></div></div></section></main>''', '../')

# Paris presentation page
paris_imgs=''.join([f'<article class="portfolio-card reveal wide"><img src="../assets/portfolio/paris/paris-{i:02d}.webp" alt="Traços Fidalgos Paris presentation {i:02d}" loading="lazy"><div class="portfolio-copy"><small>Paris presentation</small><h3>Imagem {i:02d}</h3><p>Material visual de apresentação B2B para feira/reunião em Paris.</p></div></article>' for i in range(1,12)])
page(Path('paris/index.html'),'Paris Presentation — Traços Fidalgos','Material de apresentação Traços Fidalgos Paris para clientes B2B.', f'''<main><section class="page-hero"><div class="shell"><p class="eyebrow">Paris</p><h1>Traços Fidalgos Paris presentation.</h1><p class="lead">Apresentação visual para parceiros de produção de moda portuguesa, com foco em detalhe, atelier e capacidade B2B.</p></div></section><section class="section"><div class="shell"><div class="portfolio-grid presentation-grid">{paris_imgs}</div></div></section></main>''', '../')

# keep old category pages redirect/mini pages to new sections
for old, anchor, title in [('catalogos/alta-costura.html','vestidos-silhuetas','Alta Costura'),('catalogos/lencos.html','atelier-processo','Lenços & Foulards'),('catalogos/tailoring.html','casacos-tailoring','Tailoring')]:
    page(Path(old), f'{title} — Traços Fidalgos', 'Catálogo Traços Fidalgos.', f'''<main><section class="page-hero"><div class="shell"><p class="eyebrow">Catálogo</p><h1>{title}</h1><p class="lead">Esta categoria está integrada no novo portfólio visual.</p><div class="actions"><a class="btn primary" href="../catalogos/#{anchor}">Ver categoria</a></div></div></section></main>''', '../')

print('site generated')
