# -*- coding: utf-8 -*-
"""Páginas institucionales, de conversión y legales + escritura final de todos los archivos.
Ejecutar:  python _pages2.py"""
import io
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _build import (ROOT, head_for, shell_top_for, SHELL_BOTTOM, CHK, ARR, checks,
                    crumbs, phead, steps, faq, faq_schema, cta_band)
from _pages import PAGES


# ==========================================================================
#  NOSOTROS
# ==========================================================================
def miembro(img, nombre, cargo, foco):
    return """<div class="member reveal">
  <div class="member-img"><img src="img/%s.jpg" alt="%s, %s" loading="lazy" width="768" height="1024"></div>
  <div><b>%s</b><span>%s</span><span class="cred">%s</span></div>
</div>""" % (img, nombre, cargo, nombre, cargo, foco)


NOSOTROS = phead(
    [("Nosotros", None)],
    "Una firma pequeña, a propósito",
    "Somos contadores públicos, abogados y administradores que decidieron no crecer más rápido "
    "de lo que pueden responder. Cada cliente tiene un líder asignado que conoce su empresa por "
    "dentro, no un número de ticket.",
    [("Sede", "Calle 70 No. 69i - 28, Bogotá"),
     ("Equipo", "Contadores con tarjeta profesional"),
     ("Enfoque", "Pyme establecida y emprendimiento"),
     ("Cobertura", "Bogotá y resto del país")]
) + """

<section class="section">
  <div class="wrap">
    <div class="duo duo-even">
      <div class="reveal">
        <p class="eyebrow">La firma</p>
        <h2>Contabilidad que se puede explicar</h2>
        <p class="lead">Brindamos soluciones a personas y empresas en el área contable, financiera,
          jurídica, tributaria y administrativa. Esa es la descripción formal. La práctica es más
          simple: hacemos que los números de su empresa estén al día y que usted entienda qué
          dicen.</p>
        <p>Trabajamos sobre todo con pymes bogotanas de entre 6 y 60 empleados y con emprendedores
          que están formalizando su negocio. No somos la firma más grande de la ciudad y no
          pretendemos serlo: preferimos un número de clientes que podamos atender con un
          responsable con nombre propio para cada uno.</p>
        <p>Cuando un cliente crece por encima de lo que podemos atender bien, se lo decimos y
          ayudamos a encontrar la firma adecuada. Ha pasado tres veces y volvería a pasar.</p>
      </div>
      <div class="reveal" data-d="1">
        <div class="rounded" style="border:1px solid var(--line)">
          <img src="img/oficina.jpg" alt="Oficina de Alianza Contable en Bogotá" loading="lazy"
               width="1024" height="768" style="width:100%%;height:auto">
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section paper-2">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Cómo trabajamos</p>
      <h2>Tres compromisos que se pueden verificar</h2>
      <p class="lead">No son valores de pared. Cada uno se traduce en algo concreto que usted puede
        exigir y comprobar mes a mes.</p>
    </div>
    <div class="grid g-3">
      <article class="card reveal">
        <div class="icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M17 20v-2a4 4 0 00-4-4H6a4 4 0 00-4 4v2" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><circle cx="9.5" cy="7" r="3.5" stroke="currentColor" stroke-width="1.7"/><path d="M19 8v6M22 11h-6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg></div>
        <h3>Acompañamiento</h3>
        <p>Un contador líder asignado, con nombre, correo y teléfono directo. Una reunión mensual
          para revisar los números juntos. Usted nunca va a tener que explicar su empresa desde
          cero a una persona distinta.</p>
      </article>
      <article class="card reveal" data-d="1">
        <div class="icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M12 2.5l7.5 3v6c0 4.6-3.1 8.4-7.5 9.8-4.4-1.4-7.5-5.2-7.5-9.8v-6l7.5-3z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M8.8 12l2.3 2.3 4.3-4.6" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        <h3>Responsabilidad</h3>
        <p>Fechas de entrega fijas y alertas antes de cada vencimiento, no después. Si algo se nos
          pasa, lo asumimos y se lo decimos nosotros primero. El alcance de la responsabilidad de
          cada parte queda por escrito en el contrato.</p>
      </article>
      <article class="card reveal" data-d="2">
        <div class="icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none"><rect x="4" y="10.5" width="16" height="10" rx="2.2" stroke="currentColor" stroke-width="1.7"/><path d="M8 10.5V7.2a4 4 0 018 0v3.3" stroke="currentColor" stroke-width="1.7"/><circle cx="12" cy="15.4" r="1.4" fill="currentColor"/></svg></div>
        <h3>Confidencialidad</h3>
        <p>La información de clientes y proveedores se trata bajo protocolo estricto y acuerdo de
          confidencialidad firmado. Acceso restringido por rol, respaldos cifrados y entrega
          ordenada de todo si algún día decide irse.</p>
      </article>
    </div>
  </div>
</section>

<section class="section dark">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">El equipo</p>
      <h2>Quién va a responder por su contabilidad</h2>
      <p class="lead">Cada perfil incluye el número de tarjeta profesional, verificable en el
        registro público de la Junta Central de Contadores.</p>
    </div>
    <div class="grid g-4">
      %s%s%s%s
    </div>
    <p class="note mt-3"><span class="demo-tag">Perfiles de ejemplo</span>
      Los nombres, cargos y números de tarjeta profesional los aporta Alianza Contable antes de
      publicar. La estructura de la ficha ya queda lista.</p>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <div class="sec-head reveal" style="margin-bottom:22px">
        <p class="eyebrow">Nuestro método</p>
        <h2>Lo mismo para todos los clientes, sin excepción</h2>
      </div>
      %s
    </div>
    <aside class="sticky-aside">
      <div class="aside-card">
        <h4>Lo que puede exigirnos</h4>
        %s
        <a class="btn btn-primary mt-2" href="agende-su-diagnostico.html" style="width:100%%">
          Agende su diagnóstico</a>
      </div>
    </aside>
  </div>
</section>

""" % (
    miembro("team-1", "Nombre de la socia", "Socia directora", "Contadora pública · T. P. por confirmar"),
    miembro("team-2", "Nombre del director", "Director tributario", "Contador público · T. P. por confirmar"),
    miembro("team-3", "Nombre de la líder", "Líder de nómina y cumplimiento", "Contadora pública · T. P. por confirmar"),
    miembro("team-4", "Nombre del gerente", "Gerente de auditoría", "Contador público · T. P. por confirmar"),
    steps([
        ("Diagnóstico antes de cotizar",
         "No cotizamos a ciegas. Primero miramos el estado real de la contabilidad y le "
         "entregamos un informe con lo que encontramos, incluso si al final no nos contrata."),
        ("Alcance por escrito",
         "Qué hacemos, qué no hacemos, qué necesitamos de usted y en qué fechas. Sin zonas "
         "grises que después se conviertan en cobros adicionales."),
        ("Un responsable con nombre",
         "Un contador líder asignado y un respaldo que también conoce su operación. Nunca va a "
         "quedar sin interlocutor."),
        ("Salida ordenada",
         "Si algún día decide irse, entregamos libros, auxiliares, soportes digitales y saldos "
         "de cierre. La información es suya."),
    ]),
    checks([
        "Estados financieros el día 15 de cada mes",
        "Aviso antes de cada vencimiento",
        "Respuesta en menos de 24 horas hábiles",
        "Reunión mensual de revisión",
        "Tarjeta profesional verificable",
        "Acuerdo de confidencialidad firmado",
    ]),
) + cta_band(
    "¿Conversamos treinta minutos?",
    "Sin costo y sin compromiso. Revisamos el estado de su contabilidad y le decimos con "
    "franqueza si le servimos o no.")

PAGES.append((
    "nosotros.html",
    "Nosotros | Alianza Contable, firma contable en Bogotá",
    "Equipo de contadores públicos, abogados y administradores en Bogotá. Un líder asignado por "
    "cliente, tarjeta profesional verificable y confidencialidad por contrato.",
    "nosotros.html", "img/equipo.jpg", None, NOSOTROS
))


# ==========================================================================
#  POR INDUSTRIA
# ==========================================================================
def industria(anchor, num, titulo, img, alt, lead, riesgos, entregables, invert=False):
    cols = "duo-b" if not invert else "duo-a"
    foto = """<div class="reveal"%s>
      <div class="rounded" style="border:1px solid var(--line)">
        <img src="img/%s.jpg" alt="%s" loading="lazy" width="1024" height="768"
             style="width:100%%;height:auto">
      </div>
    </div>""" % (' data-d="1"' if not invert else "", img, alt)
    texto = """<div class="reveal"%s>
      <p class="eyebrow">Sector %s</p>
      <h2>%s</h2>
      <p class="lead">%s</p>
      <div class="grid g-2 mt-3" style="gap:26px">
        <div>
          <p class="kicker mb-2">Dónde se complica</p>
          %s
        </div>
        <div>
          <p class="kicker mb-2">Qué entregamos</p>
          %s
        </div>
      </div>
    </div>""" % (' data-d="1"' if invert else "", num, titulo, lead,
                 checks(riesgos), checks(entregables))
    inner = (texto + foto) if not invert else (foto + texto)
    return """<section class="section%s" id="%s">
  <div class="wrap">
    <div class="duo %s">
      %s
    </div>
  </div>
</section>""" % (" bg-white" if invert else "", anchor, cols, inner)


INDUSTRIA = phead(
    [("Por industria", None)],
    "Su sector tiene sus propias trampas contables",
    "La contabilidad de una IPS no se parece a la de una constructora, y ninguna de las dos se "
    "parece a la de un comercio. Trabajamos con el plan de cuentas, los indicadores y los riesgos "
    "propios de cada sector.",
    [("Sectores con práctica propia", "Salud, construcción y comercio"),
     ("Otros sectores", "Se evalúan en el diagnóstico"),
     ("Qué cambia", "Plan de cuentas e indicadores"),
     ("Qué no cambia", "El precio del diagnóstico: gratuito")]
) + """
<section class="section-sm">
  <div class="wrap">
    <p class="note reveal">De las seis firmas contables de Bogotá que analizamos, ninguna segmenta
      su oferta por sector económico. Hay páginas por ciudad y por tamaño de empresa, pero el
      sector —que es lo que de verdad cambia la contabilidad— nadie lo trabaja.</p>
  </div>
</section>
""" + industria(
    "salud", "01", "Salud: IPS, consultorios y prestadores",
    "ind-salud", "Administración de una clínica en Bogotá",
    "Facturar a una EPS no es facturar. Entre la radicación, la glosa, la respuesta y el pago "
    "pueden pasar meses, y la contabilidad tiene que reflejar esa realidad sin inflar ingresos "
    "que todavía no son ciertos.",
    ["Glosas que nunca se conciliaron",
     "Cartera con EPS envejecida sin provisión",
     "Ingresos reconocidos antes de la auditoría de cuentas",
     "Retenciones especiales del sector aplicadas mal"],
    ["Conciliación de radicado contra glosa y pago",
     "Provisión de cartera por edades reales",
     "Reconocimiento de ingreso por evento auditado",
     "Indicadores de rotación de cartera por EPS"]
) + industria(
    "construccion", "02", "Construcción, obra civil y consorcios",
    "ind-construccion", "Gerente de obra revisando planos en un proyecto en Bogotá",
    "El resultado de una constructora no se lee mes a mes: se lee por proyecto. Si la contabilidad "
    "no separa costos por obra, el estado de resultados dice muy poco y las decisiones se toman a "
    "ciegas.",
    ["Costos sin centro de costo por proyecto",
     "Anticipos registrados como ingreso",
     "Consorcios y uniones temporales sin contabilidad propia",
     "Retención de garantía olvidada en la cartera"],
    ["Contabilidad por centro de costo y por obra",
     "Reconocimiento por grado de avance",
     "Contabilidad separada del consorcio o la UT",
     "Control de anticipos, amortización y garantías"],
    invert=True
) + industria(
    "comercio", "03", "Comercio, distribución y servicios",
    "ind-comercio", "Propietaria de un comercio revisando su inventario",
    "El margen real de un comercio casi nunca es el que el dueño cree. Sin control de inventario y "
    "sin separar líneas de producto, la contabilidad muestra una utilidad que no distingue lo que "
    "gana de lo que pierde.",
    ["Inventario que no cuadra con el sistema",
     "IVA mal liquidado en ventas mixtas",
     "Faltantes de caja sin registrar",
     "Márgenes calculados sin costear el flete ni la merma"],
    ["Control de inventario y kárdex conciliado",
     "Liquidación de IVA por tipo de bien y servicio",
     "Arqueos de caja periódicos",
     "Margen real por línea de producto"]
) + """
<section class="section paper-2">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Comparación</p>
      <h2>Qué cambia de un sector a otro</h2>
      <p class="lead">Mismo servicio, distinta ejecución. Esto es lo que ajustamos según la
        industria de su empresa.</p>
    </div>
    <div class="table-wrap reveal">
      <table class="tbl">
        <thead><tr>
          <th>Aspecto</th><th>Salud</th><th>Construcción</th><th>Comercio y servicios</th>
        </tr></thead>
        <tbody>
          <tr><td><b>Unidad de análisis</b></td><td>Contrato y EPS</td><td>Proyecto u obra</td><td>Línea de producto</td></tr>
          <tr><td><b>Reconocimiento del ingreso</b></td><td>Evento auditado</td><td>Grado de avance</td><td>Entrega del bien</td></tr>
          <tr><td><b>Riesgo principal</b></td><td>Glosa y cartera</td><td>Sobrecosto de obra</td><td>Merma de inventario</td></tr>
          <tr><td><b>Indicador que vigilamos</b></td><td>Rotación de cartera</td><td>Costo real contra presupuesto</td><td>Margen por línea</td></tr>
          <tr><td><b>Frecuencia de informe</b></td><td>Mensual</td><td>Por corte de obra</td><td>Mensual</td></tr>
        </tbody>
      </table>
    </div>
    <p class="note mt-2">¿Su sector no aparece? Trabajamos también con transporte, educación,
      tecnología y manufactura. En el diagnóstico definimos qué ajustes necesita su operación.</p>
  </div>
</section>

""" + cta_band(
    "Cuéntenos en qué sector está",
    "En treinta minutos le decimos qué debería estar midiendo su contabilidad y hoy no está "
    "midiendo.")

PAGES.append((
    "por-industria.html",
    "Contabilidad por sector: salud, construcción y comercio | Alianza Contable",
    "Contabilidad especializada por industria en Bogotá: IPS y prestadores de salud, "
    "constructoras y consorcios, comercio y distribución.",
    "por-industria.html", "img/ind-construccion.jpg", None, INDUSTRIA
))


# ==========================================================================
#  RECURSOS
# ==========================================================================
def post_card(href, img, alt, cat, tiempo, titulo, resumen, delay=""):
    return """<a class="post reveal"%s href="%s">
  <div class="post-img"><img src="img/%s.jpg" alt="%s" loading="lazy" width="1024" height="640"></div>
  <div class="post-body">
    <p class="post-meta"><span class="cat">%s</span> · <span>%s</span></p>
    <h3>%s</h3>
    <p>%s</p>
  </div>
</a>""" % (delay, href, img, alt, cat, tiempo, titulo, resumen)


RECURSOS = phead(
    [("Recursos y normativa", None)],
    "Lo que cambia, y a usted le toca",
    "Normativa contable y tributaria explicada sin jerga, herramientas de consulta y las fechas "
    "que no puede dejar pasar. Publicamos cuando hay algo útil que decir, no para llenar un "
    "calendario editorial.",
    [("Temas", "Tributario, laboral, pymes"),
     ("Herramienta", "Consulta de vencimientos"),
     ("Frecuencia", "Mensual"),
     ("Autoría", "Equipo de la firma")]
) + """
<section class="section">
  <div class="wrap">
    <div class="grid g-3">
      %s
      %s
      %s
    </div>
    <p class="note mt-3"><span class="demo-tag">Contenido de ejemplo</span>
      El sitio publicado migra las entradas existentes de alianzacontable.com y las actualiza.
      La redacción de contenido editorial nuevo no está incluida en la propuesta de desarrollo.</p>
  </div>
</section>

<section class="section paper-2">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Herramienta de consulta</p>
      <h2>¿Cuándo vencen sus obligaciones?</h2>
      <p class="lead">Elija el último dígito de su NIT y vea las próximas fechas límite ante
        la DIAN.</p>
    </div>
    <div class="tool reveal">
      <div class="duo duo-dian">
        <div>
          <div class="field">
            <label>Último dígito del NIT</label>
            <div class="dian-grid" id="dian-grid" role="group" aria-label="Último dígito del NIT"></div>
            <span class="hint">Sin el dígito de verificación.</span>
          </div>
        </div>
        <div class="dian-out" id="dian-out" hidden></div>
      </div>
    </div>
  </div>
</section>

""" % (
    post_card("articulo-caracteristicas-outsourcing-contable.html", "post-1",
              "Carpetas de documentos contables organizadas sobre un escritorio",
              "Outsourcing", "6 min de lectura",
              "Características de un buen outsourcing contable",
              "Siete señales que separan a una firma que le resuelve de una que solo le entrega "
              "un balance tarde."),
    post_card("recursos.html", "post-2",
              "Profesional mirando la ciudad desde una oficina en Bogotá",
              "Tributario", "4 min de lectura",
              "Calendario tributario: las fechas que no puede dejar pasar",
              "Cómo leer el calendario de la DIAN según el último dígito de su NIT y qué hacer "
              "si ya se le pasó una fecha.", ' data-d="1"'),
    post_card("recursos.html", "post-3",
              "Manos de un contador usando una calculadora junto a documentos",
              "Pymes", "5 min de lectura",
              "Cuánto cuesta realmente tener un contador de planta",
              "Salario, prestaciones, software, capacitación y vacaciones: la cuenta completa "
              "frente a tercerizar el área.", ' data-d="2"'),
) + cta_band(
    "¿Tiene una duda concreta?",
    "En el diagnóstico gratuito puede preguntar lo que quiera sobre su situación contable o "
    "tributaria. Sin costo y sin compromiso.")

PAGES.append((
    "recursos.html",
    "Recursos y normativa contable | Alianza Contable",
    "Normativa contable y tributaria explicada sin jerga, consulta de vencimientos DIAN por "
    "último dígito del NIT y publicaciones del equipo.",
    "recursos.html", "img/post-1.jpg", None, RECURSOS
))


# ==========================================================================
#  ARTÍCULO
# ==========================================================================
ART_SCHEMA = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting",
 "headline":"Características de un buen outsourcing contable",
 "description":"Siete señales que distinguen a una firma de outsourcing contable que resuelve de una que solo entrega un balance tarde.",
 "image":"https://alianzacontable.com/img/post-1.jpg",
 "author":{"@type":"Organization","name":"Alianza Contable"},
 "publisher":{"@type":"Organization","name":"Alianza Contable",
   "logo":{"@type":"ImageObject","url":"https://alianzacontable.com/img/logo.svg"}},
 "mainEntityOfPage":"https://alianzacontable.com/articulo-caracteristicas-outsourcing-contable.html"}
</script>"""

ARTICULO = """<section class="phead dark">
  <div class="wrap">
    %s
    <div class="phead-grid">
      <div class="reveal">
        <p class="post-meta" style="color:#7F98AA;margin-bottom:16px">
          <span style="color:var(--mint)">Outsourcing</span> · <span>6 min de lectura</span>
          · <span>Actualizado en agosto de 2026</span></p>
        <h1>Características de un buen outsourcing contable</h1>
        <p class="lead">Contratar una firma contable es delegar algo que, si sale mal, le cuesta
          dinero y tranquilidad. Estas son las señales que conviene revisar antes de firmar.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <article class="prose reveal">
      <img src="img/post-1.jpg" alt="Carpetas de documentos contables organizadas sobre un escritorio"
           width="1024" height="640" style="width:100%%;height:auto;margin-top:0">

      <p>Las empresas de asesoría contable en Bogotá ofrecen una gama amplia de servicios: desde la
      elaboración de estados financieros y la asesoría fiscal hasta la optimización de procesos
      financieros. El problema no es encontrar una firma. Es distinguir cuál de todas va a
      responder cuando llegue un requerimiento un viernes a las cinco de la tarde.</p>

      <p>Después de años recibiendo empresas que vienen de otras firmas, identificamos siete
      señales que se repiten. Ninguna es sofisticada; todas son verificables antes de firmar.</p>

      <h2 id="s1">1. Le hacen un diagnóstico antes de cotizar</h2>
      <p>Una firma que le cotiza por teléfono, sin haber visto un solo saldo, está cotizando un
      promedio. Cuando entre a la operación y encuentre dos años de conciliaciones pendientes,
      o le renegocia el precio o hace el trabajo mal. Un diagnóstico previo protege a las dos
      partes.</p>

      <h2 id="s2">2. Hay un responsable con nombre propio</h2>
      <p>«El equipo» no responde llamadas. Pregunte quién va a ser el contador líder de su cuenta,
      cuál es su número de tarjeta profesional y a qué teléfono se le puede escribir. Si la
      respuesta es un correo genérico de contacto, ya sabe cómo va a ser el servicio.</p>

      <blockquote>Si no le pueden decir el nombre de quien va a llevar su contabilidad, es porque
      todavía no lo han decidido.</blockquote>

      <h2 id="s3">3. El alcance está por escrito, con lo que no incluye</h2>
      <p>Los contratos que solo enumeran lo incluido son los que después generan cobros
      adicionales. Un contrato serio dice también qué queda fuera: revisoría fiscal, atención de
      requerimientos, elaboración de exógena, reprocesos por información entregada tarde. Pida esa
      lista.</p>

      <h2 id="s4">4. Le avisan antes del vencimiento, no después</h2>
      <p>Es la diferencia más práctica entre una firma que opera con proceso y una que opera con
      urgencias. Pregunte con cuántos días de anticipación le van a pedir la información y qué
      pasa si usted la entrega tarde. Una firma con proceso ya tiene esa respuesta.</p>

      <h2 id="s5">5. Los informes se entienden sin ser contador</h2>
      <p>Un estado de resultados en formato de exportación no es un informe. Si después de leer el
      cierre del mes usted no sabe si el negocio ganó o perdió, y por qué, el trabajo está
      incompleto. Pida ver un ejemplo del informe mensual que entregan a otros clientes.</p>

      <h2 id="s6">6. Tienen una política clara de confidencialidad</h2>
      <p>Su información contable incluye datos de clientes, proveedores y empleados. Pregunte quién
      del equipo tiene acceso, dónde se almacenan los soportes, si hay acuerdo de confidencialidad
      firmado y qué pasa con la información el día que usted decida terminar el servicio.</p>

      <h2 id="s7">7. La salida está definida desde el principio</h2>
      <p>Es la señal que casi nadie revisa y la que más problemas causa. Un buen contrato define
      qué le entregan si algún día se va: libros oficiales, auxiliares, soportes digitales, saldos
      de cierre y en qué plazo. Una firma que se incomoda con esa pregunta le está diciendo algo.</p>

      <h2 id="cierre">En resumen</h2>
      <p>El outsourcing contable bien hecho reduce costos, mejora la precisión de la información y
      garantiza el cumplimiento fiscal. Pero eso no viene por el hecho de tercerizar: viene de
      tercerizar con una firma que tenga proceso, responsable asignado y reglas claras. Las siete
      señales anteriores se pueden verificar en una sola reunión, antes de firmar nada.</p>
    </article>

    <aside class="sticky-aside">
      <div class="aside-card mb-2">
        <h4>En esta página</h4>
        <ul class="footer-links">
          <li><a href="#s1" style="color:var(--text-2)">1. Diagnóstico antes de cotizar</a></li>
          <li><a href="#s2" style="color:var(--text-2)">2. Responsable con nombre</a></li>
          <li><a href="#s3" style="color:var(--text-2)">3. Alcance por escrito</a></li>
          <li><a href="#s4" style="color:var(--text-2)">4. Aviso antes del vencimiento</a></li>
          <li><a href="#s5" style="color:var(--text-2)">5. Informes que se entienden</a></li>
          <li><a href="#s6" style="color:var(--text-2)">6. Confidencialidad</a></li>
          <li><a href="#s7" style="color:var(--text-2)">7. Salida definida</a></li>
        </ul>
      </div>
      <div class="aside-card">
        <h4>Ponga a prueba estas siete</h4>
        <p style="font-size:.9rem;color:var(--text-2);margin-bottom:16px">Agende el diagnóstico y
          pregúntenos las siete. Si fallamos en alguna, no nos contrate.</p>
        <a class="btn btn-primary" href="agende-su-diagnostico.html" style="width:100%%">
          Agende su diagnóstico</a>
      </div>
    </aside>
  </div>
</section>

<section class="section paper-2">
  <div class="wrap">
    <div class="sec-head reveal"><p class="eyebrow">Siga leyendo</p>
      <h2>Otras publicaciones</h2></div>
    <div class="grid g-3">
      %s
      %s
      %s
    </div>
  </div>
</section>

""" % (
    crumbs([("Recursos", "recursos.html"), ("Características de un buen outsourcing contable", None)]),
    post_card("recursos.html", "post-2", "Profesional mirando la ciudad desde una oficina en Bogotá",
              "Tributario", "4 min de lectura",
              "Calendario tributario: las fechas que no puede dejar pasar",
              "Cómo leer el calendario de la DIAN según el último dígito de su NIT."),
    post_card("recursos.html", "post-3", "Manos de un contador usando una calculadora",
              "Pymes", "5 min de lectura", "Cuánto cuesta realmente tener un contador de planta",
              "La cuenta completa frente a tercerizar el área.", ' data-d="1"'),
    post_card("outsourcing-contable.html", "srv-outsourcing", "Contador operando una contabilidad",
              "Servicio", "Ver página", "Outsourcing contable en Bogotá",
              "Qué incluye, cómo funciona el empalme y desde cuánto cuesta.", ' data-d="2"'),
) + cta_band()

PAGES.append((
    "articulo-caracteristicas-outsourcing-contable.html",
    "Características de un buen outsourcing contable | Alianza Contable",
    "Siete señales verificables que distinguen a una firma de outsourcing contable que resuelve "
    "de una que solo entrega un balance tarde.",
    "recursos.html", "img/post-1.jpg", ART_SCHEMA, ARTICULO
))


# ==========================================================================
#  AGENDE SU DIAGNÓSTICO
# ==========================================================================
FAQ_AG = [
    ("¿El diagnóstico tiene algún costo?",
     "<p>No. Es una reunión de treinta minutos, sin costo y sin compromiso de contratación. Al "
     "final le entregamos por escrito lo que encontramos, sea que nos contrate o no.</p>"),
    ("¿Qué necesito tener listo?",
     "<p>Nada obligatorio. Si tiene a mano el RUT, el último balance y las declaraciones del año "
     "en curso, la reunión rinde mucho más. Si no los tiene, igual conversamos y le decimos qué "
     "conseguir.</p>"),
    ("¿Es presencial o virtual?",
     "<p>Como prefiera. Virtual por videollamada, presencial en nuestra oficina de la Calle 70 o "
     "en su empresa si está en Bogotá. Lo indica en el formulario.</p>"),
    ("¿Me van a llamar a vender?",
     "<p>Le vamos a decir qué encontramos y cuánto costaría resolverlo. Si su caso no es para "
     "nosotros, se lo decimos en la misma reunión y le sugerimos a quién acudir. No insistimos "
     "después.</p>"),
]

AGENDA = phead(
    [("Agende su diagnóstico", None)],
    "Elija el día y la hora que le sirva",
    "Treinta minutos para revisar el estado real de su contabilidad, identificar lo que está en "
    "riesgo y decirle cuánto costaría ponerlo al día. Sin costo y sin compromiso.",
    [("Duración", "30 minutos"),
     ("Costo", "Sin costo"),
     ("Modalidad", "Virtual o presencial"),
     ("Confirmación", "El mismo día por correo")]
) + """
<section class="section">
  <div class="wrap">
    <div class="tool reveal">
      <div class="tool-head">
        <div>
          <p class="eyebrow" style="margin-bottom:10px">Paso 1 de 2</p>
          <h3>Escoja fecha y hora</h3>
          <p>Disponibilidad de lunes a viernes. Los horarios ocupados aparecen tachados.</p>
        </div>
        <span class="demo-tag">Disponibilidad simulada</span>
      </div>

      <div class="field">
        <label>Día</label>
        <div class="days" id="agenda-days" role="group" aria-label="Días disponibles"></div>
      </div>

      <div class="field">
        <label id="agenda-slots-label" hidden>Hora</label>
        <div class="slots" id="agenda-slots" role="group" aria-label="Horarios disponibles" hidden></div>
      </div>

      <div class="form-ok show" id="agenda-picked" hidden style="margin-top:4px"></div>
    </div>

    <div class="tool reveal mt-3">
      <div class="tool-head">
        <div>
          <p class="eyebrow" style="margin-bottom:10px">Paso 2 de 2</p>
          <h3>Sus datos</h3>
          <p>Con esto preparamos la reunión antes de que empiece. Nadie más va a usar esta
            información.</p>
        </div>
      </div>

      <form data-demo novalidate>
        <input type="hidden" name="cita" id="agenda-value">
        <div class="form-grid">
          <div class="field"><label for="ag-n">Nombre completo *</label>
            <input class="input" id="ag-n" name="nombre" required autocomplete="name"></div>
          <div class="field"><label for="ag-e">Empresa</label>
            <input class="input" id="ag-e" name="empresa" autocomplete="organization"></div>
          <div class="field"><label for="ag-c">Correo electrónico *</label>
            <input class="input" id="ag-c" name="correo" type="email" required autocomplete="email"></div>
          <div class="field"><label for="ag-t">Teléfono o WhatsApp *</label>
            <input class="input" id="ag-t" name="telefono" type="tel" required autocomplete="tel"></div>
          <div class="field"><label for="ag-s">Servicio de interés</label>
            <select class="input" id="ag-s" name="servicio">
              <option value="">Todavía no lo tengo claro</option>
              <option value="outsourcing-contable">Outsourcing contable</option>
              <option value="asesoria-tributaria">Asesoría tributaria</option>
              <option value="asesoria-fiscal">Asesoría fiscal y revisoría</option>
              <option value="declaracion-de-renta">Declaración de renta</option>
              <option value="constitucion-de-empresa">Constitución de empresa</option>
              <option value="contabilidad-para-emprendedores">Contabilidad para emprendedores</option>
            </select></div>
          <div class="field"><label for="ag-m">Modalidad</label>
            <select class="input" id="ag-m" name="modalidad">
              <option>Videollamada</option>
              <option>Presencial en su oficina (Calle 70)</option>
              <option>Presencial en mi empresa</option>
            </select></div>
          <div class="field full"><label for="ag-msg">¿Qué le preocupa hoy de su contabilidad?</label>
            <textarea class="input" id="ag-msg" name="mensaje" rows="4"
              placeholder="Por ejemplo: el contador renunció, tengo declaraciones vencidas, un banco me pide estados financieros…"></textarea></div>
          <div class="field full">
            <label class="consent"><input type="checkbox" required>
              <span>Autorizo de manera previa, expresa e informada a Alianza Contable el
              tratamiento de mis datos personales para atender esta solicitud, conforme a la
              <a href="politica-de-datos.html">política de tratamiento de datos</a> y a la
              Ley 1581 de 2012. *</span></label>
          </div>
        </div>
        <button class="btn btn-primary btn-lg mt-1" type="submit">Confirmar la cita %s</button>
        <p class="note mt-1">Le confirmamos por correo el mismo día hábil. * Campos obligatorios.</p>
      </form>

      <div class="form-ok">
        <span class="tick" style="width:22px;height:22px">%s</span>
        <div><b>Solicitud registrada</b>
          <p>Este sitio es un prototipo de diseño: no se envió ninguna información. En el sitio
            publicado, aquí llegaría la confirmación de la cita al correo y una notificación al
            equipo comercial.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section paper-2">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Qué pasa en esos 30 minutos</p>
      <h2>Sin presentación corporativa, sin rodeos</h2>
    </div>
    %s
  </div>
</section>

<section class="section">
  <div class="wrap wrap-narrow">
    <div class="sec-head reveal" style="margin-bottom:24px">
      <p class="eyebrow">Antes de agendar</p>
      <h2>Preguntas rápidas</h2>
    </div>
    %s
  </div>
</section>
""" % (
    ARR,
    '<svg width="12" height="12" viewBox="0 0 16 16" fill="none"><path d="M3 8.4l3.2 3.2L13 5" '
    'stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    steps([
        ("Nos cuenta dónde está parado",
         "Diez minutos. Qué hace la empresa, quién lleva hoy la contabilidad, qué le preocupa y "
         "qué lo hizo buscar una firma."),
        ("Revisamos lo que tenga a mano",
         "RUT, último balance, declaraciones del año. Con eso identificamos vencimientos "
         "pendientes, riesgos abiertos y lo que está costando de más."),
        ("Le decimos qué encontramos",
         "En lenguaje claro, con lo urgente separado de lo importante. Se lo dejamos por escrito "
         "aunque no nos contrate."),
        ("Y cuánto costaría resolverlo",
         "Un rango cerrado, no un «depende». Si su caso no es para nosotros, se lo decimos ahí "
         "mismo y le sugerimos a quién acudir."),
    ]),
    faq(FAQ_AG),
)

PAGES.append((
    "agende-su-diagnostico.html",
    "Agende su diagnóstico contable gratuito en Bogotá | Alianza Contable",
    "Treinta minutos sin costo para revisar el estado real de su contabilidad, identificar riesgos "
    "y saber cuánto costaría ponerla al día. Elija día y hora.",
    "agende-su-diagnostico.html", "img/diagnostico.jpg", faq_schema(FAQ_AG), AGENDA
))


# ==========================================================================
#  CONTACTO
# ==========================================================================
CONTACTO = phead(
    [("Contáctenos", None)],
    "Hablemos",
    "Escríbanos, llámenos o pase por la oficina. Respondemos todos los mensajes en menos de "
    "24 horas hábiles, incluso los que terminan en un «no somos los indicados para esto».",
    [("Dirección", "Calle 70 No. 69i - 28"),
     ("Teléfonos", "310 300 3711 · 300 649 7974"),
     ("Correo", "info@alianzacontable.com"),
     ("Horario", "Lunes a viernes, 8:00 a 18:00")]
) + """
<section class="section">
  <div class="wrap split">
    <div class="tool reveal">
      <div class="tool-head">
        <div><h3>Envíenos un mensaje</h3>
          <p>Cuéntenos brevemente qué necesita y le respondemos con una propuesta de siguiente
            paso, no con un folleto.</p></div>
      </div>
      <form data-demo novalidate>
        <div class="form-grid">
          <div class="field"><label for="c-n">Nombre completo *</label>
            <input class="input" id="c-n" name="nombre" required autocomplete="name"></div>
          <div class="field"><label for="c-emp">Empresa</label>
            <input class="input" id="c-emp" name="empresa" autocomplete="organization"></div>
          <div class="field"><label for="c-e">Correo electrónico *</label>
            <input class="input" id="c-e" name="correo" type="email" required autocomplete="email"></div>
          <div class="field"><label for="c-t">Teléfono o WhatsApp *</label>
            <input class="input" id="c-t" name="telefono" type="tel" required autocomplete="tel"></div>
          <div class="field full"><label for="c-s">Servicio de interés</label>
            <select class="input" id="c-s" name="servicio">
              <option value="">Seleccione una opción</option>
              <option value="outsourcing-contable">Outsourcing contable</option>
              <option value="asesoria-tributaria">Asesoría tributaria</option>
              <option value="asesoria-fiscal">Asesoría fiscal y revisoría</option>
              <option value="declaracion-de-renta">Declaración de renta</option>
              <option value="constitucion-de-empresa">Constitución de empresa</option>
              <option value="contabilidad-para-emprendedores">Contabilidad para emprendedores</option>
              <option value="otro">Otro asunto</option>
            </select></div>
          <div class="field full"><label for="c-m">Mensaje *</label>
            <textarea class="input" id="c-m" name="mensaje" rows="5" required></textarea></div>
          <div class="field full">
            <label class="consent"><input type="checkbox" required>
              <span>Autorizo de manera previa, expresa e informada a Alianza Contable el
              tratamiento de mis datos personales para atender esta solicitud, conforme a la
              <a href="politica-de-datos.html">política de tratamiento de datos</a> y a la
              Ley 1581 de 2012. *</span></label>
          </div>
        </div>
        <button class="btn btn-primary btn-lg mt-1" type="submit">Enviar mensaje %s</button>
        <p class="note mt-1">* Campos obligatorios.</p>
      </form>
      <div class="form-ok">
        <span class="tick" style="width:22px;height:22px">%s</span>
        <div><b>Mensaje registrado</b>
          <p>Este sitio es un prototipo de diseño: no se envió ninguna información. En el sitio
            publicado, el mensaje llegaría al correo de la firma y quedaría registrado con la
            fecha de la autorización de datos.</p></div>
      </div>
    </div>

    <aside class="sticky-aside">
      <div class="aside-card mb-2">
        <h4>Datos de contacto</h4>
        <ul class="footer-contact" style="color:var(--text-2)">
          <li><svg width="15" height="15" viewBox="0 0 16 16" fill="none" style="color:var(--green-700)"><path d="M8 1.6c2.5 0 4.5 2 4.5 4.5 0 3.2-4.5 8.3-4.5 8.3S3.5 9.3 3.5 6.1C3.5 3.6 5.5 1.6 8 1.6z" stroke="currentColor" stroke-width="1.4"/><circle cx="8" cy="6.1" r="1.6" stroke="currentColor" stroke-width="1.4"/></svg>
            <span><b style="color:var(--navy)">Calle 70 No. 69i - 28</b>Bogotá D. C., Colombia</span></li>
          <li><svg width="15" height="15" viewBox="0 0 16 16" fill="none" style="color:var(--green-700)"><path d="M5.2 2.3l1.5 2.6-1.3 1.3c.6 1.3 1.8 2.5 3.1 3.1l1.3-1.3 2.6 1.5v2.3c0 .6-.5 1.1-1.1 1C6.2 12.3 3.4 9.5 2.1 4.3c-.1-.6.4-1.1 1-1.1h2.1z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg>
            <span><a href="tel:+573103003711" style="color:var(--navy);font-weight:600">310 300 3711</a><a href="tel:+573006497974" style="color:var(--text-2)">300 649 7974</a></span></li>
          <li><svg width="15" height="15" viewBox="0 0 16 16" fill="none" style="color:var(--green-700)"><rect x="1.6" y="3.2" width="12.8" height="9.6" rx="1.6" stroke="currentColor" stroke-width="1.4"/><path d="M2 4.4l6 4 6-4" stroke="currentColor" stroke-width="1.4"/></svg>
            <span><a href="mailto:info@alianzacontable.com" style="color:var(--text-2)">info@alianzacontable.com</a></span></li>
          <li><svg width="15" height="15" viewBox="0 0 16 16" fill="none" style="color:var(--green-700)"><circle cx="8" cy="8" r="6.4" stroke="currentColor" stroke-width="1.4"/><path d="M8 4.4V8l2.4 1.6" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
            <span><b style="color:var(--navy)">Lunes a viernes</b>8:00 a. m. – 6:00 p. m.</span></li>
        </ul>
        <a class="btn btn-primary mt-1" href="https://wa.me/573103003711" rel="noopener" style="width:100%%">
          Escribir por WhatsApp</a>
      </div>

      <div class="aside-card" style="padding:0;overflow:hidden">
        <div style="position:relative;aspect-ratio:4/3;background:var(--paper-2)">
          <img src="img/contacto.jpg" alt="Recepción de la oficina de Alianza Contable en Bogotá"
               loading="lazy" width="1024" height="768"
               style="width:100%%;height:100%%;object-fit:cover">
        </div>
        <div style="padding:18px 20px">
          <p class="kicker mb-2">Cómo llegar</p>
          <p style="font-size:.875rem;color:var(--text-2);margin-bottom:14px">Barrio Santa Sofía,
            cerca de la Avenida Boyacá con Calle 70. Parqueadero en la zona.</p>
          <p class="note"><span class="demo-tag">Pendiente</span> El sitio publicado incluye el
            mapa interactivo de Google con la ubicación exacta verificada.</p>
        </div>
      </div>
    </aside>
  </div>
</section>

<section class="section paper-2">
  <div class="wrap">
    <div class="grid g-3">
      <article class="card reveal">
        <div class="icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.7"/><path d="M12 7.5v5l3 2" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg></div>
        <h3>Menos de 24 horas</h3>
        <p>Es el tiempo máximo que nos damos para responder un mensaje en día hábil. Si su caso es
          urgente, llame: contestamos el teléfono.</p>
      </article>
      <article class="card reveal" data-d="1">
        <div class="icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M12 2.5l7.5 3v6c0 4.6-3.1 8.4-7.5 9.8-4.4-1.4-7.5-5.2-7.5-9.8v-6l7.5-3z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg></div>
        <h3>Su información está protegida</h3>
        <p>Lo que nos escriba se usa solo para atender su solicitud. No compartimos datos con
          terceros ni los usamos para campañas que usted no haya autorizado.</p>
      </article>
      <article class="card reveal" data-d="2">
        <div class="icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M4 6.5h16M4 12h16M4 17.5h10" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg></div>
        <h3>Respuesta con contenido</h3>
        <p>No respondemos con un folleto. Le decimos qué entendimos de su caso y cuál sería el
          siguiente paso concreto, aunque ese paso no nos incluya.</p>
      </article>
    </div>
  </div>
</section>

""" % (
    ARR,
    '<svg width="12" height="12" viewBox="0 0 16 16" fill="none"><path d="M3 8.4l3.2 3.2L13 5" '
    'stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
) + cta_band(
    "¿Prefiere que hablemos con calma?",
    "Agende una reunión de treinta minutos en el horario que le sirva, en vez de intentar "
    "coordinar por correo.")

PAGES.append((
    "contacto.html",
    "Contáctenos | Alianza Contable, Bogotá",
    "Calle 70 No. 69i - 28, Bogotá. Teléfonos 310 300 3711 y 300 649 7974. "
    "info@alianzacontable.com. Respondemos en menos de 24 horas hábiles.",
    "contacto.html", "img/contacto.jpg", None, CONTACTO
))


# ==========================================================================
#  LEGALES
# ==========================================================================
AVISO_LEGAL = """<div class="card reveal" style="border-color:#EFDFB4;background:#FBF3DD;margin-bottom:34px">
  <div class="flex gap-1" style="align-items:flex-start">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" style="color:#9A7B22;flex:none;margin-top:2px">
      <circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.7"/>
      <path d="M12 7.6v5.2" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/>
      <circle cx="12" cy="16.4" r="1.1" fill="currentColor"/></svg>
    <div>
      <b style="display:block;color:#7A6118;font-size:.95rem;margin-bottom:5px">Texto modelo, pendiente de validación jurídica</b>
      <p style="font-size:.87rem;color:#7A6118;margin:0">Este documento es una estructura de
      referencia elaborada por DataLab como parte de la propuesta de rediseño. Cumple con lo que
      exige la Ley 1581 de 2012 y el Decreto 1074 de 2015 en cuanto a contenido mínimo, pero
      <b>debe ser revisado y adoptado por el abogado de Alianza Contable</b> antes de publicarse.
      Los campos marcados como «por confirmar» los completa la firma.</p>
    </div>
  </div>
</div>"""

POLITICA = phead(
    [("Política de tratamiento de datos", None)],
    "Política de tratamiento de la información",
    "Cómo recolectamos, usamos, almacenamos y protegemos los datos personales que usted nos "
    "entrega, conforme a la Ley 1581 de 2012 y sus decretos reglamentarios."
) + """
<section class="section">
  <div class="wrap wrap-narrow">
    %s
    <article class="prose reveal" style="max-width:none">
      <h2>1. Responsable del tratamiento</h2>
      <ul>
        <li><b>Razón social:</b> Alianza Contable <span class="demo-tag">Por confirmar</span></li>
        <li><b>NIT:</b> <span class="demo-tag">Por confirmar</span></li>
        <li><b>Domicilio:</b> Calle 70 No. 69i - 28, Bogotá D. C., Colombia</li>
        <li><b>Correo de contacto:</b> info@alianzacontable.com</li>
        <li><b>Teléfono:</b> 310 300 3711</li>
      </ul>

      <h2>2. Datos que recolectamos</h2>
      <p>A través de los formularios de este sitio recolectamos: nombre completo, nombre de la
      empresa, correo electrónico, número de teléfono, servicio de interés y el contenido del
      mensaje que usted decida escribir. En el marco de la prestación del servicio contable
      podemos recibir además información financiera y tributaria de la empresa y datos de sus
      empleados, clientes y proveedores.</p>
      <p>No recolectamos datos sensibles a través del sitio web. Si en el desarrollo del servicio
      resulta necesario tratar datos de esa naturaleza, se solicitará autorización específica y
      se informará que no existe obligación de autorizar su tratamiento.</p>

      <h2>3. Finalidades del tratamiento</h2>
      <ul>
        <li>Atender solicitudes de información, cotización y agendamiento de citas.</li>
        <li>Prestar los servicios contables, tributarios y de auditoría contratados.</li>
        <li>Cumplir obligaciones legales, contables y tributarias a cargo de la firma.</li>
        <li>Enviar comunicaciones relacionadas con el servicio contratado.</li>
        <li>Enviar información comercial, únicamente si el titular lo autoriza de forma separada.</li>
        <li>Elaborar estadísticas internas de uso del sitio en forma agregada y anónima.</li>
      </ul>

      <h2>4. Autorización del titular</h2>
      <p>La autorización se obtiene de manera previa, expresa e informada mediante la casilla de
      aceptación que acompaña cada formulario del sitio. Se conserva registro de la fecha, la hora
      y el medio por el cual se otorgó, como prueba del consentimiento.</p>

      <h2>5. Derechos del titular</h2>
      <p>De acuerdo con el artículo 8 de la Ley 1581 de 2012, usted tiene derecho a:</p>
      <ul>
        <li>Conocer, actualizar y rectificar sus datos personales.</li>
        <li>Solicitar prueba de la autorización otorgada.</li>
        <li>Ser informado sobre el uso que se ha dado a sus datos.</li>
        <li>Presentar quejas ante la Superintendencia de Industria y Comercio.</li>
        <li>Revocar la autorización y solicitar la supresión de sus datos, cuando no exista un
        deber legal o contractual que obligue a conservarlos.</li>
        <li>Acceder de forma gratuita a los datos que hayan sido objeto de tratamiento.</li>
      </ul>

      <h2>6. Cómo ejercer sus derechos</h2>
      <p>Escriba a <a href="mailto:info@alianzacontable.com">info@alianzacontable.com</a> con el
      asunto «Protección de datos personales», indicando su nombre, documento de identidad, el
      derecho que desea ejercer y un canal de respuesta.</p>
      <p>Las consultas se atienden en un término máximo de diez días hábiles, prorrogable por cinco
      días más. Los reclamos se atienden en un término máximo de quince días hábiles, prorrogable
      por ocho días más, conforme a los artículos 14 y 15 de la Ley 1581 de 2012.</p>

      <h2>7. Seguridad de la información</h2>
      <p>Aplicamos medidas técnicas, humanas y administrativas razonables para proteger la
      información: acceso restringido por rol, copias de seguridad, cifrado en tránsito mediante
      certificado TLS y acuerdos de confidencialidad firmados por todo el personal.</p>

      <h2>8. Transferencia y transmisión de datos</h2>
      <p>No vendemos ni cedemos datos personales a terceros con fines comerciales. Podemos
      compartir información con proveedores tecnológicos que actúan como encargados del
      tratamiento —correo electrónico, alojamiento del sitio y plataformas contables— bajo
      contratos que los obligan a mantener el mismo nivel de protección.</p>

      <h2>9. Cookies</h2>
      <p>El sitio utiliza cookies propias y de terceros con fines analíticos. Al ingresar, se
      muestra un aviso que permite aceptarlas todas o limitarlas a las estrictamente necesarias
      para el funcionamiento. Puede modificar su decisión en cualquier momento desde la
      configuración de su navegador.</p>

      <h2>10. Vigencia</h2>
      <p>Esta política rige a partir de su publicación. Las bases de datos se conservarán mientras
      exista relación contractual y durante los términos que exija la ley para efectos contables,
      tributarios y de responsabilidad profesional.</p>
      <p class="note">Última actualización: <span class="demo-tag">Por confirmar</span></p>
    </article>
  </div>
</section>
""" % AVISO_LEGAL

PAGES.append((
    "politica-de-datos.html",
    "Política de tratamiento de datos personales | Alianza Contable",
    "Cómo Alianza Contable recolecta, usa, almacena y protege los datos personales, conforme a la "
    "Ley 1581 de 2012 y sus decretos reglamentarios.",
    None, "img/oficina.jpg", None, POLITICA
))


TERMINOS = phead(
    [("Términos y condiciones", None)],
    "Términos y condiciones de uso",
    "Las reglas bajo las cuales se ofrece este sitio web y el alcance de la información publicada "
    "en él."
) + """
<section class="section">
  <div class="wrap wrap-narrow">
    %s
    <article class="prose reveal" style="max-width:none">
      <h2>1. Titular del sitio</h2>
      <p>Este sitio web es operado por Alianza Contable
      <span class="demo-tag">Razón social y NIT por confirmar</span>, con domicilio en la
      Calle 70 No. 69i - 28 de Bogotá D. C., Colombia.</p>

      <h2>2. Aceptación</h2>
      <p>El acceso y uso de este sitio implica la aceptación plena de estos términos. Si no está
      de acuerdo con alguno de ellos, le pedimos abstenerse de utilizarlo.</p>

      <h2>3. Alcance de la información publicada</h2>
      <p>El contenido de este sitio tiene carácter informativo y general. <b>No constituye asesoría
      contable, tributaria, jurídica ni financiera</b> aplicable a un caso particular, y no
      sustituye el análisis profesional de la situación concreta de una persona o empresa.</p>
      <p>Las cifras, tarifas, rangos y calendarios que aparecen en las herramientas del sitio son
      estimaciones de referencia. No constituyen una oferta comercial vinculante ni una
      certificación de fechas oficiales. Los plazos tributarios definitivos son los que fija la
      DIAN mediante decreto para cada año gravable.</p>

      <h2>4. Herramientas de cálculo y consulta</h2>
      <p>El cotizador de servicios y la consulta de vencimientos se ofrecen como apoyo orientativo.
      El valor final de cualquier servicio se acuerda por escrito tras el diagnóstico, y las fechas
      de vencimiento deben verificarse siempre contra la normativa vigente. Alianza Contable no
      responde por decisiones tomadas exclusivamente con base en estas herramientas.</p>

      <h2>5. Propiedad intelectual</h2>
      <p>Los textos, imágenes, marcas, logotipos y elementos de diseño de este sitio son propiedad
      de Alianza Contable o se utilizan con autorización de sus titulares. Se prohíbe su
      reproducción total o parcial sin consentimiento previo y escrito.</p>

      <h2>6. Enlaces a sitios de terceros</h2>
      <p>El sitio puede contener enlaces a páginas externas, como las de la DIAN o la Cámara de
      Comercio de Bogotá. Alianza Contable no controla ni responde por el contenido, las políticas
      de privacidad o la disponibilidad de esos sitios.</p>

      <h2>7. Disponibilidad del servicio</h2>
      <p>Procuramos mantener el sitio disponible de forma permanente, pero no garantizamos que esté
      libre de interrupciones por mantenimiento, fallas técnicas o causas ajenas a nuestro control.</p>

      <h2>8. Tratamiento de datos personales</h2>
      <p>El uso de los formularios está sujeto a la
      <a href="politica-de-datos.html">política de tratamiento de datos personales</a>, que forma
      parte integral de estos términos.</p>

      <h2>9. Modificaciones</h2>
      <p>Alianza Contable puede actualizar estos términos en cualquier momento. La versión vigente
      es siempre la publicada en esta página, con su fecha de actualización.</p>

      <h2>10. Ley aplicable y jurisdicción</h2>
      <p>Estos términos se rigen por la ley colombiana. Cualquier controversia derivada de su
      interpretación o aplicación se someterá a los jueces competentes de la ciudad de Bogotá D. C.</p>
      <p class="note">Última actualización: <span class="demo-tag">Por confirmar</span></p>
    </article>
  </div>
</section>
""" % AVISO_LEGAL

PAGES.append((
    "terminos-y-condiciones.html",
    "Términos y condiciones de uso | Alianza Contable",
    "Reglas de uso del sitio web de Alianza Contable y alcance de la información publicada en él.",
    None, "img/oficina.jpg", None, TERMINOS
))


# ==========================================================================
#  ESCRITURA
# ==========================================================================
for archivo, titulo, desc, current, og, schema, cuerpo in PAGES:
    html = (head_for(titulo, desc, archivo, og, schema)
            + shell_top_for(current) + "\n"
            + cuerpo + "\n"
            + SHELL_BOTTOM)
    with open(os.path.join(ROOT, archivo), "w", encoding="utf-8") as f:
        f.write(html)
    print("  %-52s %6.1f KB" % (archivo, len(html.encode("utf-8")) / 1024))

print("\n%d páginas generadas." % len(PAGES))
