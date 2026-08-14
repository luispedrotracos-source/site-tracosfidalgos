from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER

ROOT=Path(__file__).parent
OUT=ROOT/'assets/downloads/manual-marca-tracos-fidalgos.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
font_b='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
font_s='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
pdfmetrics.registerFont(TTFont('DejaVu',font)); pdfmetrics.registerFont(TTFont('DejaVu-Bold',font_b)); pdfmetrics.registerFont(TTFont('DejaVuSerif-Bold',font_s))

W,H=A4
cream=colors.HexColor('#F8F3EA'); ink=colors.HexColor('#15110E'); gold=colors.HexColor('#C5A15A'); muted=colors.HexColor('#6F6254'); sand=colors.HexColor('#E9DDC8')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle('CoverTitle', fontName='DejaVuSerif-Bold', fontSize=34, leading=38, textColor=cream, alignment=TA_CENTER, spaceAfter=14))
styles.add(ParagraphStyle('CoverSub', fontName='DejaVu', fontSize=13, leading=18, textColor=colors.HexColor('#E6D8B8'), alignment=TA_CENTER))
styles.add(ParagraphStyle('H1x', fontName='DejaVuSerif-Bold', fontSize=24, leading=29, textColor=ink, spaceAfter=10))
styles.add(ParagraphStyle('H2x', fontName='DejaVu-Bold', fontSize=14, leading=18, textColor=gold, spaceBefore=10, spaceAfter=6))
styles.add(ParagraphStyle('Bodyx', fontName='DejaVu', fontSize=9.5, leading=14, textColor=ink, spaceAfter=6))
styles.add(ParagraphStyle('BigQuote', fontName='DejaVuSerif-Bold', fontSize=17, leading=23, textColor=ink, alignment=TA_CENTER, backColor=colors.HexColor('#EFE5D4'), borderPadding=12, spaceAfter=10))
styles.add(ParagraphStyle('Smallx', fontName='DejaVu', fontSize=8, leading=11, textColor=muted))

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(cream); canvas.rect(0,0,W,H,fill=1,stroke=0)
    canvas.setStrokeColor(gold); canvas.setLineWidth(0.8); canvas.line(18*mm, H-14*mm, W-18*mm, H-14*mm)
    canvas.setFont('DejaVu',7); canvas.setFillColor(muted); canvas.drawString(18*mm, 10*mm, 'Traços Fidalgos — Manual de Marca · Portugal & Europa')
    canvas.drawRightString(W-18*mm, 10*mm, str(doc.page))
    canvas.restoreState()

def cover(canvas, doc):
    canvas.saveState(); canvas.setFillColor(ink); canvas.rect(0,0,W,H,fill=1,stroke=0)
    # logo circle
    canvas.setFillColor(gold); canvas.circle(W/2, H-82*mm, 26*mm, fill=1, stroke=0)
    canvas.setFillColor(ink); canvas.setFont('DejaVuSerif-Bold',34); canvas.drawCentredString(W/2, H-88*mm, 'TF')
    canvas.setFillColor(cream); canvas.setFont('DejaVuSerif-Bold',30); canvas.drawCentredString(W/2, H-128*mm, 'TRAÇOS FIDALGOS')
    canvas.setStrokeColor(gold); canvas.line(52*mm, H-138*mm, W-52*mm, H-138*mm)
    canvas.setFont('DejaVu',12); canvas.setFillColor(colors.HexColor('#E6D8B8'))
    canvas.drawCentredString(W/2, H-150*mm, 'Confeção Premium em Portugal · Fashion Production Partner')
    canvas.drawCentredString(W/2, H-158*mm, 'Manual de marca e posicionamento internacional')
    canvas.setFont('DejaVu',8); canvas.drawCentredString(W/2, 24*mm, 'Website · redes sociais · folhetos · feira · packaging · comunicação B2B')
    canvas.restoreState()

story=[Spacer(1,1), PageBreak()]

def add_title(t, sub=None):
    story.append(Paragraph(t, styles['H1x']))
    if sub: story.append(Paragraph(sub, styles['Bodyx']))
    story.append(Spacer(1,4))

add_title('1. Essência da marca', 'A Traços Fidalgos deve ser percebida como um parceiro português de produção de moda — técnico, flexível, discreto e premium — capaz de servir Portugal e marcas europeias.')
story += [Paragraph('Frase-mãe da marca', styles['H2x']), Paragraph('Confeção premium em Portugal para marcas, empresas e projetos têxteis exigentes.', styles['BigQuote'])]

phrase_table=[['Idioma','Frase-mãe'],['Português','Confeção premium em Portugal para marcas, empresas e projetos têxteis exigentes.'],['Inglês','Portuguese fashion production partner for brands, companies and textile projects.'],['Francês','Partenaire portugais de confection mode pour marques, entreprises et projets textiles.']]
t=Table(phrase_table, colWidths=[30*mm,130*mm]); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),ink),('TEXTCOLOR',(0,0),(-1,0),cream),('FONTNAME',(0,0),(-1,0),'DejaVu-Bold'),('FONTNAME',(0,1),(-1,-1),'DejaVu'),('FONTSIZE',(0,0),(-1,-1),8.5),('GRID',(0,0),(-1,-1),0.4,sand),('BACKGROUND',(0,1),(-1,-1),colors.white),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)])); story.append(t); story.append(Spacer(1,8))

add_title('2. Posicionamento por mercado')
story += [Paragraph('<b>Portugal:</b> comunicar “confeção premium”, “marcas e empresas”, “projetos têxteis”, “fardamento premium”, “peças personalizadas” e “acabamento cuidado”.', styles['Bodyx']), Paragraph('<b>Europa:</b> comunicar “Portuguese fashion production partner”, “nearshore production”, “technical rigour”, “flexible small/medium series”, “premium finishing” e “European sourcing”.', styles['Bodyx'])]

story.append(Paragraph('Assim comunica bem para todos', styles['H2x']))
comm=[['Público','O que deve entender imediatamente'],['Marcas portuguesas','“Podem produzir a minha coleção.”'],['Empresas','“Podem desenvolver fardamento premium ou peças personalizadas.”'],['Designers','“Podem ajudar em protótipos, peças especiais e pequenas séries.”'],['Boutiques','“Podem criar cápsulas comerciais com imagem premium.”'],['Clientes internacionais','“É um production partner em Portugal.”'],['Agentes comerciais','“É uma empresa B2B clara, vendável e confiável.”']]
t=Table(comm,colWidths=[48*mm,112*mm]); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),gold),('TEXTCOLOR',(0,0),(-1,0),ink),('FONTNAME',(0,0),(-1,0),'DejaVu-Bold'),('FONTNAME',(0,1),(-1,-1),'DejaVu'),('FONTSIZE',(0,0),(-1,-1),8.5),('GRID',(0,0),(-1,-1),0.4,sand),('BACKGROUND',(0,1),(-1,-1),colors.white),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)])); story += [t, PageBreak()]

add_title('3. Sistema de logotipo', 'A máquina de costura deve sair de uso como símbolo principal. O monograma TF passa a ser a assinatura oficial, com versões para Portugal e Europa.')
story.append(Paragraph('TF · TRAÇOS FIDALGOS', styles['BigQuote']))
story += [Paragraph('<b>Versão principal:</b> TF + Traços Fidalgos + Confeção Premium em Portugal / Fashion Production Partner.', styles['Bodyx']), Paragraph('<b>Versão reduzida:</b> monograma TF para Instagram, favicon, etiquetas pequenas, marca d’água e cantos de fotografia.', styles['Bodyx']), Paragraph('<b>Regra:</b> usar sempre uma versão oficial. Evitar misturar máquina de costura, fitas antigas, logotipos improvisados e textos diferentes no mesmo suporte.', styles['Bodyx'])]

add_title('4. Paleta e tipografia')
color_data=[['Cor','HEX','Uso'],['Charcoal','#15110E','texto, fundos premium, contraste'],['Ivory','#F8F3EA','fundo editorial, leveza, papel'],['Soft Gold','#C5A15A','detalhes, linhas, destaques, monograma F'],['Warm Sand','#E9DDC8','fundos secundários, caixas e folhetos'],['Muted Taupe','#6F6254','texto secundário e legendas']]
t=Table(color_data,colWidths=[38*mm,34*mm,88*mm]); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),ink),('TEXTCOLOR',(0,0),(-1,0),cream),('FONTNAME',(0,0),(-1,0),'DejaVu-Bold'),('FONTNAME',(0,1),(-1,-1),'DejaVu'),('FONTSIZE',(0,0),(-1,-1),8.5),('GRID',(0,0),(-1,-1),0.4,sand),('BACKGROUND',(0,1),(-1,-1),colors.white),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)])); story.append(t)
story += [Paragraph('<b>Tipografia:</b> serif elegante para títulos institucionais e monograma; sans-serif limpa para textos comerciais, fichas técnicas e posts.', styles['Bodyx'])]

add_title('5. Direção visual')
story += [Paragraph('Fotografia real, clara e premium: bastidores, mãos, costura, etiquetas, manequins, textura dos materiais, peças em ambiente limpo, fundos neutros e luz suave. Evitar imagens demasiado artificiais, filtros fortes e composição confusa.', styles['Bodyx'])]
# Image strip
imgs=[ROOT/'assets/portfolio/treated/tf-042.webp',ROOT/'assets/portfolio/treated/tf-053.webp',ROOT/'assets/book/paris/book-page-02.webp']
row=[]
for im in imgs:
    if im.exists(): row.append(Image(str(im), width=48*mm, height=64*mm))
if row: story.append(Table([row], colWidths=[52*mm]*len(row)))
story.append(PageBreak())

add_title('6. Tom de voz')
story += [Paragraph('<b>Tom:</b> técnico, discreto, confiante, premium e direto. Falar como parceiro de produção, não como loja de roupa.', styles['Bodyx']), Paragraph('<b>Evitar:</b> “luxo” exagerado, promessas sem prova, linguagem demasiado artesanal/local, ou foco exclusivo em alta costura/fardamento.', styles['Bodyx']), Paragraph('<b>Usar:</b> rigor técnico, flexibilidade, acabamento premium, produção portuguesa, small/medium series, marcas europeias, projetos têxteis personalizados.', styles['Bodyx'])]

add_title('7. Aplicações')
apps=[['Canal','Orientação'],['Instagram/LinkedIn','Monograma TF no avatar; posts com fundos ivory/charcoal, fotos reais, frases curtas e provas concretas.'],['Folhetos e feira','Usar tagline internacional, QR para site, imagens de portfólio e chamada clara para reunião/orçamento.'],['Site','PT focado em “confeção premium em Portugal”; EN/FR focados em production partner europeu.'],['Caixas e packaging','Monograma TF em dourado/charcoal; frase curta; evitar excesso de informação.'],['Fichas técnicas/orçamentos','Versão institucional limpa, dados da empresa, contacto, termos claros e visual legível.']]
t=Table(apps,colWidths=[42*mm,118*mm]); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),ink),('TEXTCOLOR',(0,0),(-1,0),cream),('FONTNAME',(0,0),(-1,0),'DejaVu-Bold'),('FONTNAME',(0,1),(-1,-1),'DejaVu'),('FONTSIZE',(0,0),(-1,-1),8.2),('GRID',(0,0),(-1,-1),0.4,sand),('BACKGROUND',(0,1),(-1,-1),colors.white),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)])); story.append(t)
story += [Spacer(1,8), Paragraph('Traços Fidalgos · Rua 9 de Julho 1277, 4455-508 Perafita · geralt.fidalgos@gmail.com · +351 96 31 94 111', styles['Smallx'])]

doc=SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=18*mm, leftMargin=18*mm, topMargin=20*mm, bottomMargin=18*mm)
doc.build(story, onFirstPage=cover, onLaterPages=header_footer)
print(OUT)
