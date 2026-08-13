# -*- coding: utf-8 -*-
"""
Generador de las páginas interiores de alianza-contable.

index.html es la plantilla canónica escrita a mano. Este script lee de ella
el <head>, la barra superior, la navegación, el pie y los flotantes, y compone
las 14 páginas restantes con el mismo armazón. Así el shell nunca se desincroniza.

Uso:  python _build.py
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()

# --------------------------------------------------------------------------
# 1. Extracción del armazón desde index.html
# --------------------------------------------------------------------------
HEAD = SRC[:SRC.index("</head>")] + "</head>\n"
SHELL_TOP = SRC[SRC.index("<body>"):SRC.index('<main id="main">') + len('<main id="main">')]
SHELL_BOTTOM = SRC[SRC.index("</main>"):]


def head_for(title, desc, slug, image="img/hero.jpg", schema=None):
    h = HEAD
    h = h.replace("<title>Outsourcing contable en Bogotá | Alianza Contable</title>",
                  "<title>%s</title>" % title)
    h = re.sub(r'<meta name="description" content="[^"]*">',
               '<meta name="description" content="%s">' % desc, h, count=1)
    h = h.replace('<link rel="canonical" href="https://alianzacontable.com/">',
                  '<link rel="canonical" href="https://alianzacontable.com/%s">' % slug)
    h = re.sub(r'<meta property="og:title" content="[^"]*">',
               '<meta property="og:title" content="%s">' % title, h, count=1)
    h = re.sub(r'<meta property="og:description" content="[^"]*">',
               '<meta property="og:description" content="%s">' % desc, h, count=1)
    h = h.replace('<meta property="og:url" content="https://alianzacontable.com/">',
                  '<meta property="og:url" content="https://alianzacontable.com/%s">' % slug)
    h = h.replace('<meta property="og:image" content="https://alianzacontable.com/img/hero.jpg">',
                  '<meta property="og:image" content="https://alianzacontable.com/%s">' % image)
    if schema:
        h = h.replace("</head>", schema + "\n</head>")
    return h


def shell_top_for(current):
    """Marca en la navegación el ítem activo de la página."""
    s = SHELL_TOP.replace('<li class="current"><a href="index.html">',
                          '<li><a href="index.html">')
    if current == "servicios":
        s = s.replace('<li>\n          <a href="#" aria-haspopup="true">Servicios',
                      '<li class="current">\n          <a href="#" aria-haspopup="true">Servicios')
    elif current:
        s = s.replace('<li><a href="%s">' % current, '<li class="current"><a href="%s">' % current)
    return s


# --------------------------------------------------------------------------
# 2. Piezas reutilizables
# --------------------------------------------------------------------------
CHK = ('<svg width="15" height="15" viewBox="0 0 16 16" fill="none"><path d="M3 8.4l3.2 3.2L13 5" '
       'stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>')
ARR = ('<svg width="15" height="15" viewBox="0 0 16 16" fill="none"><path d="M2.5 8h11m-4.5-4.5L13.5 8 9 12.5" '
       'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')
SEP = ('<svg width="11" height="11" viewBox="0 0 16 16" fill="none"><path d="M6 3.5L10.5 8 6 12.5" '
       'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def checks(items, cls="checks"):
    li = "".join('<li>%s %s</li>' % (CHK, i) for i in items)
    return '<ul class="%s">%s</ul>' % (cls, li)


def crumbs(trail):
    """trail: lista de (texto, href) — el último sin href."""
    out = ['<a href="index.html">Inicio</a>']
    for txt, href in trail:
        out.append(SEP)
        out.append('<a href="%s">%s</a>' % (href, txt) if href
                   else '<span aria-current="page">%s</span>' % txt)
    return '<nav class="crumbs" aria-label="Ruta de navegación">%s</nav>' % "".join(out)


def phead(trail, h1, lead, panel=None, panel_title="En resumen"):
    right = ""
    if panel:
        rows = "".join('<li><span>%s</span><b>%s</b></li>' % (k, v) for k, v in panel)
        right = ('<div class="phead-panel reveal" data-d="1">'
                 '<p class="kicker" style="color:#7F98AA;margin-bottom:10px">%s</p>'
                 '<ul>%s</ul></div>' % (panel_title, rows))
    return """<section class="phead dark">
  <div class="wrap">
    %s
    <div class="phead-grid">
      <div class="reveal">
        <h1>%s</h1>
        <p class="lead">%s</p>
      </div>
      %s
    </div>
  </div>
</section>""" % (crumbs(trail), h1, lead, right)


def steps(items, dark=False):
    out = []
    for i, (t, d) in enumerate(items, 1):
        out.append('<div class="step reveal"><div class="step-n">%02d</div>'
                   '<div><h3>%s</h3><p>%s</p></div></div>' % (i, t, d))
    return '<div class="steps">%s</div>' % "".join(out)


def faq(items):
    out = []
    for i, (q, a) in enumerate(items, 1):
        out.append('<details class="reveal"><summary><span class="num">%02d</span>%s'
                   '<span class="pm"></span></summary>'
                   '<div class="acc-body">%s</div></details>' % (i, q, a))
    return '<div class="acc">%s</div>' % "".join(out)


def faq_schema(items):
    ent = []
    for q, a in items:
        plain = re.sub(r"<[^>]+>", "", a).replace('"', "'").strip()
        ent.append('{"@type":"Question","name":"%s","acceptedAnswer":'
                   '{"@type":"Answer","text":"%s"}}' % (q.replace('"', "'"), plain))
    return ('<script type="application/ld+json">\n{"@context":"https://schema.org",'
            '"@type":"FAQPage","mainEntity":[%s]}\n</script>' % ",".join(ent))


def service_schema(name, desc, slug):
    return ('<script type="application/ld+json">\n{"@context":"https://schema.org",'
            '"@type":"Service","name":"%s","serviceType":"%s",'
            '"description":"%s","url":"https://alianzacontable.com/%s",'
            '"areaServed":{"@type":"City","name":"Bogotá"},'
            '"provider":{"@type":"AccountingService","name":"Alianza Contable",'
            '"@id":"https://alianzacontable.com/#organizacion"}}\n</script>'
            % (name, name, desc, slug))


def cta_band(title="Treinta minutos, sin costo y sin compromiso",
             text=("Revisamos el estado real de su contabilidad, le decimos qué está en riesgo "
                   "y cuánto costaría ponerlo al día. Si no le servimos, se lo decimos en la "
                   "misma reunión."),
             btn="Agende su diagnóstico"):
    return """<section class="cta-band dark">
  <div class="wrap">
    <div class="reveal">
      <p class="eyebrow">Siguiente paso</p>
      <h2>%s</h2>
      <p>%s</p>
    </div>
    <div class="btn-row reveal" data-d="1">
      <a class="btn btn-primary btn-lg" href="agende-su-diagnostico.html">%s %s</a>
      <a class="btn btn-outline btn-lg" href="https://wa.me/573103003711" rel="noopener">WhatsApp</a>
    </div>
  </div>
</section>""" % (title, text, btn, ARR)


def aside_card(resumen, desde, servicio_val):
    return """<aside class="sticky-aside">
  <div class="aside-card">
    <h4>En una línea</h4>
    <p style="font-family:var(--f-display);font-size:1.12rem;line-height:1.4;color:var(--navy);
       letter-spacing:-.014em;margin-bottom:18px">%s</p>
    <div style="padding:14px 0;border-top:1px solid var(--line-soft);border-bottom:1px solid var(--line-soft);
         margin-bottom:18px">
      <span class="kicker">Desde</span>
      <div style="font-family:var(--f-display);font-size:1.75rem;font-weight:600;color:var(--navy);
           letter-spacing:-.03em;font-variant-numeric:tabular-nums;line-height:1.1;margin-top:4px">%s</div>
      <span class="note">mensual, antes de IVA · <span class="demo-tag">Ejemplo</span></span>
    </div>
    <a class="btn btn-primary" href="agende-su-diagnostico.html?servicio=%s" style="width:100%%">
      Agende su diagnóstico</a>
    <a class="btn btn-outline btn-sm mt-1" href="tel:+573103003711" style="width:100%%">
      Llamar al 310 300 3711</a>
    <p class="note mt-2" style="text-align:center">Respuesta en menos de 24 horas hábiles.</p>
  </div>
</aside>""" % (resumen, desde, servicio_val)


# --------------------------------------------------------------------------
# 3. Plantilla de página de servicio
# --------------------------------------------------------------------------
def service_page(c):
    incluye_left = checks(c["incluye"][:len(c["incluye"]) // 2 + len(c["incluye"]) % 2])
    incluye_right = checks(c["incluye"][len(c["incluye"]) // 2 + len(c["incluye"]) % 2:])
    return """%(phead)s

<section class="section">
  <div class="wrap split">
    <div class="prose reveal">
      %(prose)s
    </div>
    %(aside)s
  </div>
</section>

<section class="section paper-2">
  <div class="wrap">
    <div class="duo duo-a">
      <div class="reveal">
        <p class="eyebrow">Qué incluye</p>
        <h2>%(incluye_t)s</h2>
        <p class="lead">%(incluye_lead)s</p>
        <div class="grid g-2 mt-2" style="gap:0 30px">%(inc_l)s%(inc_r)s</div>
      </div>
      <div class="reveal" data-d="1">
        <div class="rounded" style="border:1px solid var(--line)">
          <img src="img/%(img)s.jpg" alt="%(img_alt)s" loading="lazy" width="1024" height="768"
               style="width:100%%;height:auto">
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Cómo trabajamos</p>
      <h2>%(proceso_t)s</h2>
    </div>
    %(steps)s
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <div class="sec-head reveal" style="margin-bottom:24px">
        <p class="eyebrow">Preguntas frecuentes</p>
        <h2>Lo que nos preguntan antes de contratar</h2>
      </div>
      %(faq)s
    </div>
    <aside class="sticky-aside">
      <div class="aside-card">
        <h4>Otros servicios</h4>
        <ul class="footer-links" style="margin-bottom:4px">%(otros)s</ul>
      </div>
    </aside>
  </div>
</section>

%(cta)s
""" % {
        "phead": phead(c["trail"], c["h1"], c["lead"], c["panel"]),
        "prose": c["prose"],
        "aside": aside_card(c["resumen"], c["desde"], c["val"]),
        "incluye_t": c["incluye_t"],
        "incluye_lead": c["incluye_lead"],
        "inc_l": incluye_left,
        "inc_r": incluye_right,
        "img": c["img"],
        "img_alt": c["img_alt"],
        "proceso_t": c["proceso_t"],
        "steps": steps(c["proceso"]),
        "faq": faq(c["faq"]),
        "otros": c["otros"],
        "cta": cta_band(),
    }


SERVICIOS = [
    ("outsourcing-contable.html", "Outsourcing contable"),
    ("asesoria-tributaria.html", "Asesoría tributaria"),
    ("asesoria-fiscal.html", "Asesoría fiscal y revisoría"),
    ("declaracion-de-renta.html", "Declaración de renta"),
    ("constitucion-de-empresa.html", "Constitución de empresa"),
    ("contabilidad-para-emprendedores.html", "Contabilidad para emprendedores"),
]


def otros_links(actual):
    return "".join('<li><a href="%s">%s</a></li>' % (h, t)
                   for h, t in SERVICIOS if h != actual)
