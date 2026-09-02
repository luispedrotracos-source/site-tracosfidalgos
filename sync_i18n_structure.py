from pathlib import Path
import re

ROOT = Path(__file__).parent

PAGES = {
    'atelier': ('atelier/index.html', 'en/atelier/index.html', 'fr/atelier/index.html'),
    'servicos': ('servicos/index.html', 'en/services/index.html', 'fr/services/index.html'),
    'processo': ('processo/index.html', 'en/process/index.html', 'fr/processus/index.html'),
    'catalogos': ('catalogos/index.html', 'en/catalogues/index.html', 'fr/catalogues/index.html'),
    'paris': ('paris/index.html', 'en/paris/index.html', 'fr/paris/index.html'),
    'contacto': ('contacto/index.html', 'en/contact/index.html', 'fr/contact/index.html'),
}

DETAIL_PAGES = {
    'alta-costura': ('catalogos/alta-costura.html', 'en/catalogues/haute-couture.html', 'fr/catalogues/haute-couture.html'),
    'lencos': ('catalogos/lencos.html', 'en/catalogues/scarves.html', 'fr/catalogues/foulards.html'),
    'tailoring': ('catalogos/tailoring.html', 'en/catalogues/tailoring.html', 'fr/catalogues/tailoring.html'),
}

ROUTES = {
    'en': [
        ('../contacto/', '/en/contact/'), ('../catalogos/', '/en/catalogues/'), ('../processo/', '/en/process/'),
        ('../servicos/', '/en/services/'), ('../atelier/', '/en/atelier/'), ('../paris/', '/en/paris/'),
        ('contacto/', '/en/contact/'), ('catalogos/', '/en/catalogues/'), ('processo/', '/en/process/'),
        ('servicos/', '/en/services/'), ('atelier/', '/en/atelier/'), ('paris/', '/en/paris/'),
    ],
    'fr': [
        ('../contacto/', '/fr/contact/'), ('../catalogos/', '/fr/catalogues/'), ('../processo/', '/fr/processus/'),
        ('../servicos/', '/fr/services/'), ('../atelier/', '/fr/atelier/'), ('../paris/', '/fr/paris/'),
        ('contacto/', '/fr/contact/'), ('catalogos/', '/fr/catalogues/'), ('processo/', '/fr/processus/'),
        ('servicos/', '/fr/services/'), ('atelier/', '/fr/atelier/'), ('paris/', '/fr/paris/'),
    ],
}

COMMON_EN = {
    'Atelier': 'Atelier', 'Serviços': 'Services', 'Portfólio': 'Portfolio', 'Processo': 'Process', 'Paris': 'Paris',
    'Catálogo': 'Catalogue', 'Ver categoria': 'View category',
    'Alta Costura': 'Haute Couture', 'Lenços & Foulards': 'Scarves & Foulards',
    'Esta categoria está integrada no novo portfólio visual.': 'This category is now integrated into the new visual portfolio.',
    'Contacto': 'Contact', 'Pedir orçamento': 'Request quote', 'Falar connosco': 'Talk to us',
    'Falar sobre um projeto': 'Discuss a project', 'Ver portfólio': 'View portfolio', 'Email': 'Email',
    'WhatsApp': 'WhatsApp', 'Traços Fidalgos': 'Traços Fidalgos', 'Top ↑': 'Top ↑',
    'Rua 9 de Julho 1277, 4455-508 Perafita · Matosinhos · Portugal': 'Rua 9 de Julho 1277, 4455-508 Perafita · Matosinhos · Portugal',
    'Rua 9 de Julho 1277, 4455-508 Perafita, Portugal': 'Rua 9 de Julho 1277, 4455-508 Perafita, Portugal',
}
COMMON_FR = {
    'Atelier': 'Atelier', 'Serviços': 'Services', 'Portfólio': 'Portfolio', 'Processo': 'Processus', 'Paris': 'Paris',
    'Catálogo': 'Catalogue', 'Ver categoria': 'Voir la catégorie',
    'Alta Costura': 'Haute Couture', 'Lenços & Foulards': 'Carrés & Foulards',
    'Esta categoria está integrada no novo portfólio visual.': 'Cette catégorie est désormais intégrée au nouveau portfolio visuel.',
    'Contacto': 'Contact', 'Pedir orçamento': 'Demander un devis', 'Falar connosco': 'Nous contacter',
    'Falar sobre um projeto': 'Parler d’un projet', 'Ver portfólio': 'Voir le portfolio', 'Email': 'Email',
    'WhatsApp': 'WhatsApp', 'Traços Fidalgos': 'Traços Fidalgos', 'Top ↑': 'Haut ↑',
    'Rua 9 de Julho 1277, 4455-508 Perafita · Matosinhos · Portugal': 'Rua 9 de Julho 1277, 4455-508 Perafita · Matosinhos · Portugal',
    'Rua 9 de Julho 1277, 4455-508 Perafita, Portugal': 'Rua 9 de Julho 1277, 4455-508 Perafita, Portugal',
}

TRANSLATIONS = {
'en': {
    **COMMON_EN,
    # atelier
    'Produção portuguesa com rigor técnico e sensibilidade estética.': 'Portuguese production with technical rigour and aesthetic sensitivity.',
    'Desde 2017, a Traços Fidalgos trabalha com marcas e clientes que procuram confiança, detalhe e acabamento premium na produção europeia.': 'Since 2017, Traços Fidalgos has worked with brands and clients looking for reliability, detail and premium finishing in European production.',
    'Quem somos': 'Who we are',
    'Atelier em Perafita, Matosinhos, com equipa experiente, capacidade técnica e acompanhamento próximo desde o briefing até à peça final.': 'An atelier in Perafita, Matosinhos, with an experienced team, technical capability and close follow-up from the brief to the final piece.',
    'Sobre nós': 'About us',
    'Fundada em Portugal, preparada para a Europa.': 'Founded in Portugal, ready for Europe.',
    'A Traços Fidalgos, Unipessoal LDA é um atelier têxtil português fundado em 2017 em Perafita, Matosinhos. Desenvolvemos e confecionamos peças de vestuário e projetos têxteis com rigor técnico, acompanhamento próximo e sentido premium do detalhe.': 'Traços Fidalgos, Unipessoal LDA is a Portuguese textile atelier founded in 2017 in Perafita, Matosinhos. We develop and manufacture garments and textile projects with technical rigour, close follow-up and a premium sense of detail.',
    'Construção, preparação técnica e acabamento consistentes.': 'Consistent construction, technical preparation and finishing.',
    'Acompanhamento próximo': 'Close follow-up',
    'Acompanhamento próximo desde o briefing até à peça final.': 'Close follow-up from the brief to the final piece.',
    'Parceiro europeu': 'European partner',
    'Produção portuguesa para marcas, empresas e projetos têxteis premium.': 'Portuguese production for brands, companies and premium textile projects.',
    'Por que trabalhar connosco?': 'Why work with us?',
    'Parceiro fiável para projetos exigentes.': 'A reliable partner for demanding projects.',
    'O livreto destaca produção portuguesa, comunicação direta, atenção a materiais, personalização para marcas e acompanhamento do conceito à peça final — uma proposta pensada para clientes europeus que procuram flexibilidade, discrição e acabamento consistente.': 'The booklet highlights Portuguese production, direct communication, attention to materials, brand customisation and follow-up from concept to final piece — a proposal designed for European clients seeking flexibility, discretion and consistent finishing.',
    'O atelier como prova de confiança': 'The atelier as proof of trust',
    'As imagens de trabalho real mostram método, equipa e controlo: cada peça passa por mãos experientes antes de chegar ao cliente.': 'Real work images show method, team and control: each piece passes through experienced hands before reaching the client.',
    'Conhecer o processo': 'Discover the process',
    # services
    'Do protótipo à produção.': 'From prototype to production.',
    'Apoiamos marcas em amostras, protótipos, cápsulas, marca própria e pequena/média produção.': 'We support brands with samples, prototypes, capsules, private label and small/medium production.',
    'Amostras': 'Samples',
    'Interpretação técnica, modelagem, corte, confeção e fitting.': 'Technical interpretation, pattern making, cutting, sewing and fitting.',
    'Cápsulas': 'Capsules',
    'Pequenas séries premium para boutiques, designers e marcas.': 'Premium small series for boutiques, designers and brands.',
    'Produção': 'Production',
    'Produção europeia com controlo de qualidade e comunicação próxima.': 'European production with quality control and close communication.',
    'Projetos especiais': 'Special projects',
    'Vestidos, blusas, tailoring, kimonos, lenços e peças detalhadas.': 'Dresses, blouses, tailoring, kimonos, scarves and detailed pieces.',
    'Our value': 'Our value',
    'Precision, discretion and consistent finishing.': 'Precision, discretion and consistent finishing.',
    'We work as a production partner for fashion and textile projects that require adaptability, technical responsibility and careful presentation.': 'We work as a production partner for fashion and textile projects that require adaptability, technical responsibility and careful presentation.',
    'We support brands and companies in the development and production of garments, uniforms, promotional articles and personalised textile pieces.': 'We support brands and companies in the development and production of garments, uniforms, promotional articles and personalised textile pieces.',
    'Serviços destacados no livreto': 'Services highlighted in the booklet',
    'Mais do que confeção: desenvolvimento têxtil completo.': 'More than sewing: complete textile development.',
    'Materiais delicados': 'Delicate materials',
    'Rendas, tecidos fluidos e matérias que exigem corte preciso, costura limpa e manuseamento técnico.': 'Lace, fluid fabrics and materials that require precise cutting, clean stitching and technical handling.',
    'Peças com identidade': 'Pieces with identity',
    'Peças personalizadas para marcas, boutiques, eventos e projetos profissionais.': 'Custom pieces for brands, boutiques, events and professional projects.',
    'Lenços personalizados': 'Custom scarves',
    'Desenvolvimento de foulards e acessórios têxteis com design, produção e acabamento coordenados.': 'Development of scarves and textile accessories with coordinated design, production and finishing.',
    'Polar diagonal 320 g/m²': 'Diagonal fleece 320 g/m²',
    'Propostas de vestuário em molleton/polar diagonal para peças confortáveis, estruturadas e comerciais.': 'Garment proposals in diagonal molleton/fleece for comfortable, structured and commercial pieces.',
    'Serviços com imagem, método e acabamento': 'Services with image, method and finishing',
    'Do protótipo à pequena produção, a apresentação também conta: etiquetas, packaging, fichas e acabamentos reforçam o valor de cada peça.': 'From prototype to small production, presentation also matters: labels, packaging, technical sheets and finishing reinforce the value of each piece.',
    # process
    'Do briefing à peça final, com método e detalhe.': 'From brief to final piece, with method and detail.',
    'Um processo visual e claro para marcas, empresas e projetos têxteis que precisam de acompanhamento técnico, protótipos bem resolvidos e produção cuidada em Portugal.': 'A clear visual process for brands, companies and textile projects that need technical follow-up, well-resolved prototypes and careful production in Portugal.',
    'Cada etapa tem uma função concreta.': 'Each stage has a concrete purpose.',
    'Não trabalhamos apenas por inspiração. Organizamos referências, materiais, medidas, acabamentos e prazos para que o cliente saiba em que fase está o projeto e o que precisa ser decidido antes da produção.': 'We do not work by inspiration alone. We organise references, materials, measurements, finishes and deadlines so the client knows the project stage and what must be decided before production.',
    'Briefing e referências': 'Briefing and references',
    'Recebemos imagens, desenhos, peças exemplo, fichas técnicas ou uma descrição simples do que precisa ser desenvolvido. Nesta fase definimos objetivo, uso, quantidades, materiais e nível de acabamento.': 'We receive images, drawings, sample garments, technical sheets or a simple description of what needs to be developed. At this stage we define purpose, use, quantities, materials and finishing level.',
    'Análise técnica': 'Technical analysis',
    'Avaliamos construção, proporções, tecido, detalhes, dificuldades de confeção e melhor caminho produtivo. Quando necessário, sugerimos ajustes para melhorar resultado, custo e viabilidade.': 'We assess construction, proportions, fabric, details, sewing complexity and the best production path. When necessary, we suggest adjustments to improve result, cost and feasibility.',
    'Protótipo ou amostra': 'Prototype or sample',
    'Desenvolvemos a primeira peça para testar caimento, estrutura, medidas, acabamentos e leitura visual. É a fase ideal para corrigir antes da produção.': 'We develop the first piece to test fit, structure, measurements, finishes and visual reading. This is the ideal stage to correct before production.',
    'Preparação da produção': 'Production preparation',
    'Com a peça aprovada, organizamos materiais, sequência de confeção, instruções, controlo de qualidade e detalhes finais para manter consistência.': 'Once the piece is approved, we organise materials, sewing sequence, instructions, quality control and final details to maintain consistency.',
    'Confeção e controlo': 'Sewing and control',
    'A produção é acompanhada com atenção aos acabamentos, proporções, etiquetas, passadoria e apresentação final.': 'Production is followed with attention to finishing, proportions, labels, pressing and final presentation.',
    'Entrega e continuidade': 'Delivery and continuity',
    'Entregamos o projeto pronto e deixamos uma base clara para futuras reposições, novas cápsulas, ajustes ou desenvolvimento de outras peças.': 'We deliver the finished project and leave a clear basis for future replenishments, new capsules, adjustments or development of other pieces.',
    'Resultado': 'Outcome',
    'O que o cliente recebe': 'What the client receives',
    'clareza sobre etapas e decisões': 'clarity on stages and decisions',
    'acompanhamento próximo': 'close follow-up',
    'atenção aos materiais e acabamentos': 'attention to materials and finishes',
    'produção em Portugal com responsabilidade técnica': 'production in Portugal with technical responsibility',
    'resultado adequado para marca, empresa ou projeto especial': 'a result suited to the brand, company or special project',
    'Tem uma coleção, uniforme ou peça personalizada para desenvolver?': 'Do you have a collection, uniform or custom piece to develop?',
    'Envie-nos referências, quantidades aproximadas, materiais pretendidos e prazo. Respondemos com o melhor caminho para transformar a ideia numa peça real.': 'Send us references, approximate quantities, desired materials and deadline. We reply with the best path to turn the idea into a real piece.',
    # contact
    'Vamos analisar o seu projeto?': 'Shall we review your project?',
    'Envie referências, desenhos, fichas técnicas ou uma descrição da peça/coleção que pretende desenvolver.': 'Send references, drawings, technical sheets or a description of the piece/collection you want to develop.',
    'Para pedir orçamento': 'For a quote request',
    'Envie tipo de peça, quantidades, materiais, tamanhos, imagens de referência e prazo desejado.': 'Send garment type, quantities, materials, sizes, reference images and desired deadline.',
    'Envie referências, quantidades e prazo': 'Send references, quantities and deadline',
    'Quanto mais claras forem as referências, mais rápido conseguimos orientar materiais, protótipos, acabamentos e produção.': 'The clearer the references are, the faster we can guide materials, prototypes, finishes and production.',
    'Enviar WhatsApp': 'Send WhatsApp',
    # paris
    'Apresentação Paris': 'Paris presentation',
    'Traços Fidalgos em Paris': 'Traços Fidalgos in Paris',
    'Uma apresentação clara da Traços Fidalgos para marcas, designers, boutiques e empresas que procuram um parceiro português de confeção premium, com rigor técnico, flexibilidade e acabamento cuidado.': 'A clear presentation of Traços Fidalgos for brands, designers, boutiques and companies looking for a Portuguese premium garment production partner, with technical rigour, flexibility and careful finishing.',
    'Descarregar livreto completo': 'Download full booklet',
    'Parceiro português de produção de moda para clientes exigentes.': 'Portuguese fashion production partner for demanding clients.',
    'A Traços Fidalgos é um atelier português em Perafita, Matosinhos, dedicado ao desenvolvimento e confeção de peças de vestuário e projetos têxteis para marcas, empresas e clientes profissionais.': 'Traços Fidalgos is a Portuguese atelier in Perafita, Matosinhos, dedicated to developing and manufacturing garments and textile projects for brands, companies and professional clients.',
    'Trabalhamos desde a leitura do briefing e prototipagem até à produção, acabamento, controlo de qualidade e preparação da peça final. O objetivo é simples: transformar ideias em produto com método, atenção ao detalhe e uma apresentação adequada ao mercado europeu.': 'We work from brief review and prototyping through production, finishing, quality control and preparation of the final piece. The goal is simple: turn ideas into product with method, attention to detail and presentation suited to the European market.',
    'O que fazemos': 'What we do',
    'Prototipagem e desenvolvimento': 'Prototyping and development',
    'Apoio na passagem da ideia, desenho, referência ou ficha técnica para uma peça física pronta a testar e ajustar.': 'Support in turning an idea, drawing, reference or technical sheet into a physical piece ready to test and adjust.',
    'Pequenas e médias séries': 'Small and medium series',
    'Produção flexível para marcas, boutiques, coleções cápsula e projetos que não precisam de volumes industriais enormes.': 'Flexible production for brands, boutiques, capsule collections and projects that do not require huge industrial volumes.',
    'Uniformes e peças premium': 'Uniforms and premium pieces',
    'Fardamento, peças personalizadas e projetos têxteis com imagem cuidada, consistência e acabamento profissional.': 'Uniforms, custom pieces and textile projects with careful image, consistency and professional finishing.',
    'Projetos têxteis especiais': 'Special textile projects',
    'Lenços, acessórios, peças sob medida, materiais delicados e propostas com identidade visual própria.': 'Scarves, accessories, bespoke pieces, delicate materials and proposals with their own visual identity.',
    'Valor': 'Value',
    'Por que trabalhar com a Traços Fidalgos': 'Why work with Traços Fidalgos',
    'Esta apresentação mostra, de forma direta, o que a empresa oferece: produção em Portugal, proximidade, flexibilidade, qualidade de confeção e acompanhamento direto.': 'This presentation shows directly what the company offers: production in Portugal, proximity, flexibility, sewing quality and direct follow-up.',
    'Produção em Portugal, perto dos principais mercados europeus.': 'Production in Portugal, close to the main European markets.',
    'Rigor técnico na construção, acabamentos e leitura dos materiais.': 'Technical rigour in construction, finishing and understanding of materials.',
    'Capacidade para peças delicadas, coleções cápsula, uniformes premium e projetos personalizados.': 'Capability for delicate pieces, capsule collections, premium uniforms and custom projects.',
    'Comunicação direta com uma equipa experiente, habituada a trabalhar com marcas e projetos exigentes.': 'Direct communication with an experienced team used to working with demanding brands and projects.',
    'Materiais': 'Materials',
    'Materiais, identidade e acabamento': 'Materials, identity and finishing',
    'O livreto Paris mostra diferentes áreas de trabalho: rendas e tecidos fluídos, peças com identidade, lenços personalizados, peças têxteis sob medida e propostas como polar diagonal 320 g/m². No site, estes temas passam a ser explicados como serviços e capacidades concretas, não apenas como páginas de apresentação.': 'The Paris booklet shows different areas of work: lace and fluid fabrics, pieces with identity, custom scarves, bespoke textile pieces and proposals such as 320 g/m² diagonal fleece. On the site, these themes are explained as concrete services and capabilities, not just presentation pages.',
    'Do conceito à peça final': 'From concept to final piece',
    'Briefing': 'Briefing',
    'Recebemos referências, desenhos, peças exemplo ou ficheiros técnicos.': 'We receive references, drawings, sample pieces or technical files.',
    'Protótipo': 'Prototype',
    'Desenvolvemos amostra e ajustamos proporções, materiais e acabamentos.': 'We develop a sample and adjust proportions, materials and finishes.',
    'Organizamos confeção, controlo e consistência de cada peça.': 'We organise sewing, control and consistency for each piece.',
    'Entrega': 'Delivery',
    'Preparamos o produto final com apresentação adequada ao cliente e ao mercado.': 'We prepare the final product with presentation suited to the client and the market.',
    'Quer desenvolver uma coleção, uniforme ou peça personalizada em Portugal?': 'Do you want to develop a collection, uniform or custom piece in Portugal?',
    'Envie-nos referências, quantidades aproximadas, materiais pretendidos e prazo. A equipa avalia o projeto e responde com o melhor caminho de produção.': 'Send us references, approximate quantities, desired materials and deadline. The team reviews the project and replies with the best production path.',
    'Descarregar livreto completo': 'Download full booklet',
    'Descarregar livreto': 'Download booklet',
    'Lenços, identidade e produção portuguesa': 'Scarves, identity and Portuguese production',
    'As imagens reforçam a ligação entre design têxtil, produção, apresentação e presente corporativo numa linguagem clara e premium.': 'The images reinforce the connection between textile design, production, presentation and corporate gifting in a clear, premium language.',
    # catalogue
    'Catálogos visuais organizados por categoria.': 'Visual catalogues organised by category.',
    'Peças, detalhes e referências selecionadas para mostrar materiais, formas, acabamentos e possibilidades de confeção.': 'Selected pieces, details and references showing materials, shapes, finishes and production possibilities.',
    'Peças, detalhes e materiais': 'Pieces, details and materials',
    'Detalhe, estrutura e sensibilidade aos materiais.': 'Detail, structure and material sensitivity.',
    'Uma seleção visual para conhecer formas, texturas, acabamentos e possibilidades de produção em Portugal.': 'A visual selection to explore shapes, textures, finishes and production possibilities in Portugal.',
    'As peças de moda exigem construção técnica, leitura das proporções, comportamento dos tecidos e acabamento cuidado. Esta galeria organiza referências visuais para mostrar detalhe, estrutura e capacidade de execução.': 'Fashion pieces require technical construction, understanding of proportions, fabric behaviour and careful finishing. This gallery organises visual references to show detail, structure and execution capability.',
    'Do livreto Paris': 'From the Paris booklet',
    'As páginas do livreto organizam o portfólio em torno de materiais delicados, peças com identidade, lenços/foulards personalizados, peças têxteis sob medida e propostas em polar diagonal. Esta seleção mostra a diversidade de projetos que a Traços Fidalgos pode desenvolver.': 'The booklet pages organise the portfolio around delicate materials, pieces with identity, custom scarves/foulards, bespoke textile pieces and diagonal fleece proposals. This selection shows the diversity of projects Traços Fidalgos can develop.',
    'As páginas do livreto organizam o portfólio em torno de materiais delicados, peças com identidade, lenços/foulards personalizados, peças têxteis sob medida e propostas em polar diagonal. Esta seleção mostra a diversidade de peças, materiais e acabamentos que podem ser desenvolvidos com a Traços Fidalgos.': 'The booklet pages organise the portfolio around delicate materials, pieces with identity, custom scarves/foulards, bespoke textile pieces and diagonal fleece proposals. This selection shows the diversity of pieces, materials and finishes that can be developed with Traços Fidalgos.',
    'Portfolio com leitura comercial e técnica.': 'Portfolio with commercial and technical reading.',
    'Falar sobre uma peça': 'Discuss a piece',
    'Vestidos & silhuetas': 'Dresses & silhouettes',
    'Vestidos, silhuetas femininas e peças especiais com movimento, proporção e acabamento premium.': 'Dresses, feminine silhouettes and special pieces with movement, proportion and premium finishing.',
    'Blusas & tops statement': 'Statement blouses & tops',
    'Blusas, camisas e tops com volume, laços, textura e construção diferenciada.': 'Blouses, shirts and tops with volume, ties, texture and distinctive construction.',
    'Tailoring & outerwear': 'Tailoring & outerwear',
    'Casacos, peças estruturadas, outerwear e propostas com leitura técnica.': 'Coats, structured pieces, outerwear and technically informed proposals.',
    'Rendas & transparências': 'Lace & transparencies',
    'Rendas, transparências e detalhes delicados que exigem precisão no corte e na confeção.': 'Lace, transparencies and delicate details that require precision in cutting and sewing.',
    'Saias, calças & coordenados': 'Skirts, trousers & coordinates',
    'Bases comerciais e coordenados para cápsulas, boutiques e private label.': 'Commercial bases and coordinated pieces for capsules, boutiques and private label.',
    'Atelier & processo': 'Atelier & process',
    'Bastidores, etiquetas, apresentação e detalhes de execução que reforçam o saber-fazer.': 'Behind the scenes, labels, presentation and execution details that reinforce know-how.',
    'Silhueta feminina premium': 'Premium feminine silhouette',
    'Blusa / top de coleção': 'Collection blouse / top',
    'Peça estruturada': 'Structured piece',
    'Renda e detalhe delicado': 'Lace and delicate detail',
    'Coordenado comercial': 'Commercial coordinate',
    'Detalhe de atelier': 'Atelier detail',
},
'fr': {
    **COMMON_FR,
    # atelier
    'Produção portuguesa com rigor técnico e sensibilidade estética.': 'Production portugaise avec rigueur technique et sensibilité esthétique.',
    'Desde 2017, a Traços Fidalgos trabalha com marcas e clientes que procuram confiança, detalhe e acabamento premium na produção europeia.': 'Depuis 2017, Traços Fidalgos travaille avec des marques et des clients qui recherchent fiabilité, détail et finition premium dans la production européenne.',
    'Quem somos': 'Qui nous sommes',
    'Atelier em Perafita, Matosinhos, com equipa experiente, capacidade técnica e acompanhamento próximo desde o briefing até à peça final.': 'Un atelier à Perafita, Matosinhos, avec une équipe expérimentée, une capacité technique et un accompagnement proche du brief à la pièce finale.',
    'Sobre nós': 'À propos',
    'Fundada em Portugal, preparada para a Europa.': 'Fondée au Portugal, prête pour l’Europe.',
    'A Traços Fidalgos, Unipessoal LDA é um atelier têxtil português fundado em 2017 em Perafita, Matosinhos. Desenvolvemos e confecionamos peças de vestuário e projetos têxteis com rigor técnico, acompanhamento próximo e sentido premium do detalhe.': 'Traços Fidalgos, Unipessoal LDA est un atelier textile portugais fondé en 2017 à Perafita, Matosinhos. Nous développons et confectionnons des vêtements et projets textiles avec rigueur technique, accompagnement proche et sens premium du détail.',
    'Technical rigour': 'Rigueur technique',
    'Construção, preparação técnica e acabamento consistentes.': 'Construction, préparation technique et finition cohérentes.',
    'Acompanhamento próximo': 'Accompagnement proche',
    'Acompanhamento próximo desde o briefing até à peça final.': 'Accompagnement proche du brief à la pièce finale.',
    'Parceiro europeu': 'Partenaire européen',
    'Produção portuguesa para marcas, empresas e projetos têxteis premium.': 'Production portugaise pour marques, entreprises et projets textiles premium.',
    'Por que trabalhar connosco?': 'Pourquoi travailler avec nous ?',
    'Parceiro fiável para projetos exigentes.': 'Un partenaire fiable pour projets exigeants.',
    'O livreto destaca produção portuguesa, comunicação direta, atenção a materiais, personalização para marcas e acompanhamento do conceito à peça final — uma proposta pensada para clientes europeus que procuram flexibilidade, discrição e acabamento consistente.': 'Le livret met en avant la production portugaise, la communication directe, l’attention aux matières, la personnalisation pour les marques et l’accompagnement du concept à la pièce finale — une proposition pensée pour des clients européens qui recherchent flexibilité, discrétion et finition régulière.',
    'O atelier como prova de confiança': 'L’atelier comme preuve de confiance',
    'As imagens de trabalho real mostram método, equipa e controlo: cada peça passa por mãos experientes antes de chegar ao cliente.': 'Les images de travail réel montrent méthode, équipe et contrôle : chaque pièce passe par des mains expérimentées avant d’arriver chez le client.',
    'Conhecer o processo': 'Découvrir le processus',
    # services
    'Do protótipo à produção.': 'Du prototype à la production.',
    'Apoiamos marcas em amostras, protótipos, cápsulas, marca própria e pequena/média produção.': 'Nous accompagnons les marques dans les échantillons, prototypes, capsules, marque propre et petite/moyenne production.',
    'Amostras': 'Échantillons',
    'Interpretação técnica, modelagem, corte, confeção e fitting.': 'Interprétation technique, patronage, coupe, confection et essayage.',
    'Cápsulas': 'Capsules',
    'Pequenas séries premium para boutiques, designers e marcas.': 'Petites séries premium pour boutiques, créateurs et marques.',
    'Produção': 'Production',
    'Produção europeia com controlo de qualidade e comunicação próxima.': 'Production européenne avec contrôle qualité et communication proche.',
    'Projetos especiais': 'Projets spéciaux',
    'Vestidos, blusas, tailoring, kimonos, lenços e peças detalhadas.': 'Robes, chemisiers, tailoring, kimonos, foulards et pièces détaillées.',
    'Our value': 'Notre valeur',
    'Precision, discretion and consistent finishing.': 'Précision, discrétion et finition régulière.',
    'We work as a production partner for fashion and textile projects that require adaptability, technical responsibility and careful presentation.': 'Nous travaillons comme partenaire de production pour les projets mode et textile qui exigent adaptabilité, responsabilité technique et présentation soignée.',
    'We support brands and companies in the development and production of garments, uniforms, promotional articles and personalised textile pieces.': 'Nous accompagnons les marques et entreprises dans le développement et la production de vêtements, uniformes, articles promotionnels et pièces textiles personnalisées.',
    'Serviços destacados no livreto': 'Services mis en avant dans le livret',
    'Mais do que confeção: desenvolvimento têxtil completo.': 'Plus que la confection : développement textile complet.',
    'Materiais delicados': 'Matières délicates',
    'Rendas, tecidos fluidos e matérias que exigem corte preciso, costura limpa e manuseamento técnico.': 'Dentelles, tissus fluides et matières qui exigent coupe précise, couture nette et manipulation technique.',
    'Peças com identidade': 'Pièces avec identité',
    'Peças personalizadas para marcas, boutiques, eventos e projetos profissionais.': 'Pièces personnalisées pour marques, boutiques, événements et projets professionnels.',
    'Lenços personalizados': 'Foulards personnalisés',
    'Desenvolvimento de foulards e acessórios têxteis com design, produção e acabamento coordenados.': 'Développement de foulards et accessoires textiles avec design, production et finition coordonnés.',
    'Polar diagonal 320 g/m²': 'Molleton diagonal 320 g/m²',
    'Propostas de vestuário em molleton/polar diagonal para peças confortáveis, estruturadas e comerciais.': 'Propositions de vêtements en molleton/polaire diagonal pour des pièces confortables, structurées et commerciales.',
    'Serviços com imagem, método e acabamento': 'Services avec image, méthode et finition',
    'Do protótipo à pequena produção, a apresentação também conta: etiquetas, packaging, fichas e acabamentos reforçam o valor de cada peça.': 'Du prototype à la petite production, la présentation compte aussi : étiquettes, packaging, fiches et finitions renforcent la valeur de chaque pièce.',
    # process/contact/paris/catalogue reuse via EN translations enough in FR below
    'Do briefing à peça final, com método e detalhe.': 'Du brief à la pièce finale, avec méthode et détail.',
    'Um processo visual e claro para marcas, empresas e projetos têxteis que precisam de acompanhamento técnico, protótipos bem resolvidos e produção cuidada em Portugal.': 'Un processus visuel et clair pour marques, entreprises et projets textiles qui ont besoin d’un accompagnement technique, de prototypes bien résolus et d’une production soignée au Portugal.',
    'Cada etapa tem uma função concreta.': 'Chaque étape a une fonction concrète.',
    'Não trabalhamos apenas por inspiração. Organizamos referências, materiais, medidas, acabamentos e prazos para que o cliente saiba em que fase está o projeto e o que precisa ser decidido antes da produção.': 'Nous ne travaillons pas seulement par inspiration. Nous organisons références, matières, mesures, finitions et délais afin que le client sache à quelle étape se trouve le projet et ce qui doit être décidé avant la production.',
    'Briefing e referências': 'Briefing et références',
    'Recebemos imagens, desenhos, peças exemplo, fichas técnicas ou uma descrição simples do que precisa ser desenvolvido. Nesta fase definimos objetivo, uso, quantidades, materiais e nível de acabamento.': 'Nous recevons images, dessins, pièces exemple, fiches techniques ou une description simple de ce qui doit être développé. À cette étape, nous définissons objectif, usage, quantités, matières et niveau de finition.',
    'Análise técnica': 'Analyse technique',
    'Avaliamos construção, proporções, tecido, detalhes, dificuldades de confeção e melhor caminho produtivo. Quando necessário, sugerimos ajustes para melhorar resultado, custo e viabilidade.': 'Nous évaluons construction, proportions, tissu, détails, difficultés de confection et meilleur parcours productif. Si nécessaire, nous suggérons des ajustements pour améliorer résultat, coût et faisabilité.',
    'Protótipo ou amostra': 'Prototype ou échantillon',
    'Desenvolvemos a primeira peça para testar caimento, estrutura, medidas, acabamentos e leitura visual. É a fase ideal para corrigir antes da produção.': 'Nous développons la première pièce pour tester tombé, structure, mesures, finitions et lecture visuelle. C’est l’étape idéale pour corriger avant la production.',
    'Preparação da produção': 'Préparation de la production',
    'Com a peça aprovada, organizamos materiais, sequência de confeção, instruções, controlo de qualidade e detalhes finais para manter consistência.': 'Une fois la pièce validée, nous organisons matières, séquence de confection, instructions, contrôle qualité et détails finaux pour maintenir la cohérence.',
    'Confeção e controlo': 'Confection et contrôle',
    'A produção é acompanhada com atenção aos acabamentos, proporções, etiquetas, passadoria e apresentação final.': 'La production est suivie avec attention aux finitions, proportions, étiquettes, repassage et présentation finale.',
    'Entrega e continuidade': 'Livraison et continuité',
    'Entregamos o projeto pronto e deixamos uma base clara para futuras reposições, novas cápsulas, ajustes ou desenvolvimento de outras peças.': 'Nous livrons le projet terminé et laissons une base claire pour de futurs réassorts, nouvelles capsules, ajustements ou développements d’autres pièces.',
    'Resultado': 'Résultat',
    'O que o cliente recebe': 'Ce que le client reçoit',
    'clareza sobre etapas e decisões': 'clarté sur les étapes et décisions',
    'acompanhamento próximo': 'accompagnement proche',
    'atenção aos materiais e acabamentos': 'attention aux matières et finitions',
    'produção em Portugal com responsabilidade técnica': 'production au Portugal avec responsabilité technique',
    'resultado adequado para marca, empresa ou projeto especial': 'résultat adapté à la marque, entreprise ou projet spécial',
    'Tem uma coleção, uniforme ou peça personalizada para desenvolver?': 'Vous avez une collection, un uniforme ou une pièce personnalisée à développer ?',
    'Envie-nos referências, quantidades aproximadas, materiais pretendidos e prazo. Respondemos com o melhor caminho para transformar a ideia numa peça real.': 'Envoyez-nous références, quantités approximatives, matières souhaitées et délai. Nous répondons avec le meilleur parcours pour transformer l’idée en pièce réelle.',
    'Vamos analisar o seu projeto?': 'Analysons votre projet ?',
    'Envie referências, desenhos, fichas técnicas ou uma descrição da peça/coleção que pretende desenvolver.': 'Envoyez références, dessins, fiches techniques ou une description de la pièce/collection que vous souhaitez développer.',
    'Para pedir orçamento': 'Pour demander un devis',
    'Envie tipo de peça, quantidades, materiais, tamanhos, imagens de referência e prazo desejado.': 'Envoyez type de pièce, quantités, matières, tailles, images de référence et délai souhaité.',
    'Envie referências, quantidades e prazo': 'Envoyez références, quantités et délai',
    'Quanto mais claras forem as referências, mais rápido conseguimos orientar materiais, protótipos, acabamentos e produção.': 'Plus les références sont claires, plus nous pouvons orienter rapidement matières, prototypes, finitions et production.',
    'Enviar WhatsApp': 'Envoyer WhatsApp',
    # paris/catalogue
    'Apresentação Paris': 'Présentation Paris', 'Traços Fidalgos em Paris': 'Traços Fidalgos à Paris',
    'Uma apresentação clara da Traços Fidalgos para marcas, designers, boutiques e empresas que procuram um parceiro português de confeção premium, com rigor técnico, flexibilidade e acabamento cuidado.': 'Une présentation claire de Traços Fidalgos pour marques, créateurs, boutiques et entreprises recherchant un partenaire portugais de confection premium, avec rigueur technique, flexibilité et finition soignée.',
    'Descarregar livreto completo': 'Télécharger le livret complet',
    'Parceiro português de produção de moda para clientes exigentes.': 'Partenaire portugais de production mode pour clients exigeants.',
    'A Traços Fidalgos é um atelier português em Perafita, Matosinhos, dedicado ao desenvolvimento e confeção de peças de vestuário e projetos têxteis para marcas, empresas e clientes profissionais.': 'Traços Fidalgos est un atelier portugais à Perafita, Matosinhos, dédié au développement et à la confection de vêtements et projets textiles pour marques, entreprises et clients professionnels.',
    'Trabalhamos desde a leitura do briefing e prototipagem até à produção, acabamento, controlo de qualidade e preparação da peça final. O objetivo é simples: transformar ideias em produto com método, atenção ao detalhe e uma apresentação adequada ao mercado europeu.': 'Nous travaillons depuis la lecture du brief et le prototypage jusqu’à la production, finition, contrôle qualité et préparation de la pièce finale. L’objectif est simple : transformer des idées en produit avec méthode, attention au détail et présentation adaptée au marché européen.',
    'O que fazemos': 'Ce que nous faisons',
    'Prototipagem e desenvolvimento': 'Prototypage et développement',
    'Apoio na passagem da ideia, desenho, referência ou ficha técnica para uma peça física pronta a testar e ajustar.': 'Accompagnement pour passer de l’idée, dessin, référence ou fiche technique à une pièce physique prête à tester et ajuster.',
    'Pequenas e médias séries': 'Petites et moyennes séries',
    'Produção flexível para marcas, boutiques, coleções cápsula e projetos que não precisam de volumes industriais enormes.': 'Production flexible pour marques, boutiques, collections capsules et projets ne nécessitant pas de grands volumes industriels.',
    'Uniformes e peças premium': 'Uniformes et pièces premium',
    'Fardamento, peças personalizadas e projetos têxteis com imagem cuidada, consistência e acabamento profissional.': 'Uniformes, pièces personnalisées et projets textiles avec image soignée, cohérence et finition professionnelle.',
    'Projetos têxteis especiais': 'Projets textiles spéciaux',
    'Lenços, acessórios, peças sob medida, materiais delicados e propostas com identidade visual própria.': 'Foulards, accessoires, pièces sur mesure, matières délicates et propositions avec identité visuelle propre.',
    'Valor': 'Valeur', 'Por que trabalhar com a Traços Fidalgos': 'Pourquoi travailler avec Traços Fidalgos',
    'Esta apresentação mostra, de forma direta, o que a empresa oferece: produção em Portugal, proximidade, flexibilidade, qualidade de confeção e acompanhamento direto.': 'Cette présentation montre directement ce que l’entreprise offre : production au Portugal, proximité, flexibilité, qualité de confection et accompagnement direct.',
    'Produção em Portugal, perto dos principais mercados europeus.': 'Production au Portugal, proche des principaux marchés européens.',
    'Rigor técnico na construção, acabamentos e leitura dos materiais.': 'Rigueur technique dans la construction, les finitions et la lecture des matières.',
    'Capacidade para peças delicadas, coleções cápsula, uniformes premium e projetos personalizados.': 'Capacité pour pièces délicates, collections capsules, uniformes premium et projets personnalisés.',
    'Comunicação direta com uma equipa experiente, habituada a trabalhar com marcas e projetos exigentes.': 'Communication directe avec une équipe expérimentée, habituée à travailler avec des marques et projets exigeants.',
    'Materiais': 'Matières', 'Materiais, identidade e acabamento': 'Matières, identité et finition',
    'O livreto Paris mostra diferentes áreas de trabalho: rendas e tecidos fluídos, peças com identidade, lenços personalizados, peças têxteis sob medida e propostas como polar diagonal 320 g/m². No site, estes temas passam a ser explicados como serviços e capacidades concretas, não apenas como páginas de apresentação.': 'Le livret Paris montre différents domaines de travail : dentelles et tissus fluides, pièces avec identité, foulards personnalisés, pièces textiles sur mesure et propositions comme le molleton diagonal 320 g/m². Sur le site, ces thèmes sont expliqués comme services et capacités concrètes, pas seulement comme pages de présentation.',
    'Do conceito à peça final': 'Du concept à la pièce finale',
    'Briefing': 'Briefing', 'Recebemos referências, desenhos, peças exemplo ou ficheiros técnicos.': 'Nous recevons références, dessins, pièces exemple ou fichiers techniques.',
    'Protótipo': 'Prototype', 'Desenvolvemos amostra e ajustamos proporções, materiais e acabamentos.': 'Nous développons un échantillon et ajustons proportions, matières et finitions.',
    'Organizamos confeção, controlo e consistência de cada peça.': 'Nous organisons confection, contrôle et cohérence de chaque pièce.',
    'Entrega': 'Livraison', 'Preparamos o produto final com apresentação adequada ao cliente e ao mercado.': 'Nous préparons le produit final avec une présentation adaptée au client et au marché.',
    'Quer desenvolver uma coleção, uniforme ou peça personalizada em Portugal?': 'Vous souhaitez développer une collection, un uniforme ou une pièce personnalisée au Portugal ?',
    'Envie-nos referências, quantidades aproximadas, materiais pretendidos e prazo. A equipa avalia o projeto e responde com o melhor caminho de produção.': 'Envoyez-nous références, quantités approximatives, matières souhaitées et délai. L’équipe évalue le projet et répond avec le meilleur parcours de production.',
    'Descarregar livreto completo': 'Télécharger le livret complet',
    'Descarregar livreto': 'Télécharger le livret',
    'Lenços, identidade e produção portuguesa': 'Foulards, identité et production portugaise',
    'As imagens reforçam a ligação entre design têxtil, produção, apresentação e presente corporativo numa linguagem clara e premium.': 'Les images renforcent le lien entre design textile, production, présentation et cadeau d’entreprise dans un langage clair et premium.',
    'Catálogos visuais organizados por categoria.': 'Catalogues visuels organisés par catégorie.',
    'Peças, detalhes e referências selecionadas para mostrar materiais, formas, acabamentos e possibilidades de confeção.': 'Pièces, détails et références sélectionnés pour montrer matières, formes, finitions et possibilités de confection.',
    'Peças, detalhes e materiais': 'Pièces, détails et matières',
    'Detalhe, estrutura e sensibilidade aos materiais.': 'Détail, structure et sensibilité aux matières.',
    'Uma seleção visual para conhecer formas, texturas, acabamentos e possibilidades de produção em Portugal.': 'Une sélection visuelle pour découvrir formes, textures, finitions et possibilités de production au Portugal.',
    'As peças de moda exigem construção técnica, leitura das proporções, comportamento dos tecidos e acabamento cuidado. Esta galeria organiza referências visuais para mostrar detalhe, estrutura e capacidade de execução.': 'Les pièces de mode exigent construction technique, lecture des proportions, comportement des tissus et finition soignée. Cette galerie organise des références visuelles pour montrer détail, structure et capacité d’exécution.',
    'Do livreto Paris': 'Du livret Paris',
    'As páginas do livreto organizam o portfólio em torno de materiais delicados, peças com identidade, lenços/foulards personalizados, peças têxteis sob medida e propostas em polar diagonal. Esta seleção mostra a diversidade de projetos que a Traços Fidalgos pode desenvolver.': 'Les pages du livret organisent le portfolio autour de matières délicates, pièces avec identité, foulards personnalisés, pièces textiles sur mesure et propositions en molleton diagonal. Cette sélection montre la diversité de projets que Traços Fidalgos peut développer.',
    'As páginas do livreto organizam o portfólio em torno de materiais delicados, peças com identidade, lenços/foulards personalizados, peças têxteis sob medida e propostas em polar diagonal. Esta seleção mostra a diversidade de peças, materiais e acabamentos que podem ser desenvolvidos com a Traços Fidalgos.': 'Les pages du livret organisent le portfolio autour de matières délicates, pièces avec identité, foulards personnalisés, pièces textiles sur mesure et propositions en molleton diagonal. Cette sélection montre la diversité de pièces, matières et finitions qui peuvent être développées avec Traços Fidalgos.',
    'Portfolio com leitura comercial e técnica.': 'Portfolio avec lecture commerciale et technique.',
    'Falar sobre uma peça': 'Parler d’une pièce',
    'Vestidos & silhuetas': 'Robes & silhouettes',
    'Vestidos, silhuetas femininas e peças especiais com movimento, proporção e acabamento premium.': 'Robes, silhouettes féminines et pièces spéciales avec mouvement, proportion et finition premium.',
    'Blusas & tops statement': 'Chemisiers & tops statement',
    'Blusas, camisas e tops com volume, laços, textura e construção diferenciada.': 'Chemisiers, chemises et tops avec volume, nœuds, texture et construction distinctive.',
    'Tailoring & outerwear': 'Tailoring & outerwear',
    'Casacos, peças estruturadas, outerwear e propostas com leitura técnica.': 'Vestes, pièces structurées, outerwear et propositions avec lecture technique.',
    'Rendas & transparências': 'Dentelles & transparences',
    'Rendas, transparências e detalhes delicados que exigem precisão no corte e na confeção.': 'Dentelles, transparences et détails délicats exigeant précision dans la coupe et la confection.',
    'Saias, calças & coordenados': 'Jupes, pantalons & coordonnés',
    'Bases comerciais e coordenados para cápsulas, boutiques e private label.': 'Bases commerciales et coordonnés pour capsules, boutiques et private label.',
    'Atelier & processo': 'Atelier & processus',
    'Bastidores, etiquetas, apresentação e detalhes de execução que reforçam o saber-fazer.': 'Coulisses, étiquettes, présentation et détails d’exécution qui renforcent le savoir-faire.',
    'Silhueta feminina premium': 'Silhouette féminine premium',
    'Blusa / top de coleção': 'Chemisier / top de collection',
    'Peça estruturada': 'Pièce structurée',
    'Renda e detalhe delicado': 'Dentelle et détail délicat',
    'Coordenado comercial': 'Coordonné commercial',
    'Detalhe de atelier': 'Détail d’atelier',
}}

TITLE_DESC = {
 'en': {
  'atelier': ('Atelier — Traços Fidalgos', 'Portuguese premium textile atelier in Perafita, Matosinhos.'),
  'servicos': ('Services — Traços Fidalgos', 'Services for samples, prototypes, private label, production and special pieces.'),
  'processo': ('Process — Traços Fidalgos', 'Work process for developing garments and collections in Portugal.'),
  'catalogos': ('Portfolio & Catalogues — Traços Fidalgos', 'Organised visual gallery of garments, finishes and fashion references produced by Traços Fidalgos.'),
  'paris': ('Paris Presentation — Traços Fidalgos', 'Traços Fidalgos Paris presentation material for B2B clients.'),
  'contacto': ('Contact — Traços Fidalgos', 'Traços Fidalgos contacts for quote requests and garment production projects.'),
  'alta-costura': ('Haute Couture — Traços Fidalgos', 'Traços Fidalgos catalogue category.'),
  'lencos': ('Scarves & Foulards — Traços Fidalgos', 'Traços Fidalgos catalogue category.'),
  'tailoring': ('Tailoring — Traços Fidalgos', 'Traços Fidalgos catalogue category.'),
 },
 'fr': {
  'atelier': ('Atelier — Traços Fidalgos', 'Atelier textile portugais premium à Perafita, Matosinhos.'),
  'servicos': ('Services — Traços Fidalgos', 'Services pour échantillons, prototypes, private label, production et pièces spéciales.'),
  'processo': ('Processus — Traços Fidalgos', 'Processus de travail pour le développement de vêtements et collections au Portugal.'),
  'catalogos': ('Portfolio & Catalogues — Traços Fidalgos', 'Galerie visuelle organisée de pièces, finitions et références mode produites par Traços Fidalgos.'),
  'paris': ('Présentation Paris — Traços Fidalgos', 'Matériel de présentation Traços Fidalgos Paris pour clients B2B.'),
  'contacto': ('Contact — Traços Fidalgos', 'Contacts Traços Fidalgos pour demandes de devis et projets de confection.'),
  'alta-costura': ('Haute Couture — Traços Fidalgos', 'Catégorie catalogue Traços Fidalgos.'),
  'lencos': ('Carrés & Foulards — Traços Fidalgos', 'Catégorie catalogue Traços Fidalgos.'),
  'tailoring': ('Tailoring — Traços Fidalgos', 'Catégorie catalogue Traços Fidalgos.'),
 }
}

def extract_main(txt):
    m = re.search(r'<main>.*?</main>', txt, re.S)
    if not m:
        raise ValueError('missing main')
    return m.group(0)

def replace_text(main, mapping):
    # Replace longer strings first to avoid partial replacements.
    for src in sorted(mapping, key=len, reverse=True):
        main = main.replace(src, mapping[src])
    return main

def route_assets(main, lang):
    main = main.replace('../assets/', '/assets/')
    for src, dst in ROUTES[lang]:
        main = main.replace(f'href="{src}', f'href="{dst}')
    # correct mailto subjects
    if lang == 'en':
        main = main.replace('subject=Pedido%20de%20or%C3%A7amento%20-%20Tra%C3%A7os%20Fidalgos', 'subject=Tra%C3%A7os%20Fidalgos%20project%20request')
    else:
        main = main.replace('subject=Pedido%20de%20or%C3%A7amento%20-%20Tra%C3%A7os%20Fidalgos', 'subject=Demande%20de%20devis%20-%20Tra%C3%A7os%20Fidalgos')
    return main

def replace_main(target, main):
    txt = target.read_text()
    txt = re.sub(r'<main>.*?</main>', main, txt, count=1, flags=re.S)
    return txt

def set_meta(txt, title, desc):
    txt = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', txt, count=1, flags=re.S)
    txt = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', txt, count=1)
    return txt

def sync():
    changed=[]
    for key, (pt_rel, en_rel, fr_rel) in PAGES.items():
        pt_main = extract_main((ROOT/pt_rel).read_text())
        for lang, rel in [('en', en_rel), ('fr', fr_rel)]:
            main = replace_text(pt_main, TRANSLATIONS[lang])
            main = route_assets(main, lang)
            target = ROOT/rel
            title, desc = TITLE_DESC[lang][key]
            new = set_meta(replace_main(target, main), title, desc)
            if new != target.read_text():
                target.write_text(new)
                changed.append(rel)
    for key, (pt_rel, en_rel, fr_rel) in DETAIL_PAGES.items():
        pt_main = extract_main((ROOT/pt_rel).read_text())
        for lang, rel in [('en', en_rel), ('fr', fr_rel)]:
            main = replace_text(pt_main, TRANSLATIONS[lang])
            main = route_assets(main, lang)
            target = ROOT/rel
            title, desc = TITLE_DESC[lang][key]
            new = set_meta(replace_main(target, main), title, desc)
            if new != target.read_text():
                target.write_text(new)
                changed.append(rel)
    print('synced i18n structure pages:', ', '.join(changed) if changed else 'no changes')

if __name__ == '__main__':
    sync()
