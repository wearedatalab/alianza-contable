# -*- coding: utf-8 -*-
"""Contenido de las 14 páginas interiores. Ejecutar:  python _pages.py"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _build import (ROOT, head_for, shell_top_for, SHELL_BOTTOM, CHK, ARR, checks,
                    crumbs, phead, steps, faq, faq_schema, service_schema, cta_band,
                    aside_card, service_page, otros_links)

PAGES = []   # (archivo, título, descripción, nav_current, imagen_og, schema, cuerpo)


# ==========================================================================
#  SERVICIO 01 · OUTSOURCING CONTABLE
# ==========================================================================
FAQ_OUT = [
    ("¿Cuánto cuesta el outsourcing contable en Bogotá?",
     "<p>Depende de tres cosas: el tamaño de la empresa, el volumen de documentos que se causan "
     "cada mes y las obligaciones que tenga a cargo. En el cotizador de la página de inicio puede "
     "estimar el rango en un minuto. El valor definitivo se acuerda después del diagnóstico "
     "gratuito, cuando ya conocemos su operación real.</p>"),
    ("¿Qué pasa con el contador que tengo hoy?",
     "<p>Coordinamos el empalme directamente con quien lleva la contabilidad en este momento: "
     "recibimos saldos, libros auxiliares y soportes, y verificamos que todo cuadre antes de "
     "asumir. Si prefiere que el proceso sea discreto hasta cerrar el acuerdo, también lo "
     "manejamos así.</p>"),
    ("¿Tengo que cambiar de software contable?",
     "<p>No necesariamente. Trabajamos sobre la plataforma que su empresa ya tiene licenciada. "
     "Si no tiene ninguna o la actual se quedó corta, le recomendamos alternativas y hacemos la "
     "implementación y la migración de saldos como parte del arranque.</p>"),
    ("¿Quién responde si llega una sanción?",
     "<p>El contrato define por escrito las responsabilidades de cada parte. Respondemos por los "
     "errores atribuibles a nuestra gestión. El cliente responde por la información y los "
     "soportes que entrega y por los hechos anteriores al inicio del servicio. Ese alcance queda "
     "claro antes de firmar, no después.</p>"),
    ("¿Puedo terminar el servicio cuando quiera?",
     "<p>Sí. El contrato fija un preaviso razonable y, al terminar, le entregamos la información "
     "contable completa y ordenada: libros oficiales, auxiliares, soportes digitales y saldos de "
     "cierre. Nunca retenemos la información de un cliente como forma de presión.</p>"),
]

PAGES.append((
    "outsourcing-contable.html",
    "Outsourcing contable en Bogotá | Alianza Contable",
    "Su departamento contable completo, operado por nosotros: causación, impuestos, nómina y "
    "estados financieros mensuales, con un contador líder asignado a su empresa.",
    "servicios", "img/srv-outsourcing.jpg",
    service_schema("Outsourcing contable",
                   "Tercerización del área contable para empresas en Bogotá.",
                   "outsourcing-contable.html") + "\n" + faq_schema(FAQ_OUT),
    service_page({
        "trail": [("Servicios", "index.html#servicios"), ("Outsourcing contable", None)],
        "h1": "Su departamento contable completo, sin tenerlo en nómina",
        "lead": "Causación, conciliaciones, impuestos, nómina y estados financieros mensuales. "
                "Un contador líder con nombre y teléfono, y un equipo detrás que conoce su "
                "operación.",
        "panel": [("Ideal para", "Empresas de 6 a 60 empleados"),
                  ("Entrega mensual", "Estados financieros, día 15"),
                  ("Desde", "$ 780.000 / mes"),
                  ("Arranque", "5 días hábiles")],
        "prose": """
<h2>Qué resuelve realmente</h2>
<p>Las pymes que nos llaman suelen estar en uno de tres puntos: el contador de planta renunció y
se llevó el conocimiento con él; la contabilidad la lleva alguien que además responde por
facturación, cartera y compras; o los estados financieros llegan tan tarde que ya no sirven para
decidir nada.</p>
<p>El outsourcing contable resuelve los tres a la vez. Su empresa deja de depender de una persona
y pasa a apoyarse en un equipo con procesos documentados, respaldo y un responsable con nombre
propio.</p>

<h3>Frente a un contador de planta</h3>
<p>Un contador interno no cuesta lo que dice el contrato. Sume prestaciones, parafiscales,
dotación, capacitación, licencias de software y el tiempo que alguien debe dedicar a
supervisarlo. Y aun así sigue siendo una sola persona: cuando se enferma, sale a vacaciones o
renuncia, la operación contable se detiene y los vencimientos no esperan.</p>
<blockquote>Con outsourcing su empresa nunca queda sin contabilidad: si el líder asignado se
ausenta, el respaldo ya conoce su operación y sus soportes.</blockquote>

<h3>Lo que no hacemos</h3>
<p>No firmamos estados financieros que no podamos sustentar, no presentamos declaraciones con
información incompleta y no registramos operaciones sin soporte. Si algo de eso aparece durante
el diagnóstico, se lo decimos antes de firmar el contrato, aunque implique perder el negocio.</p>
""",
        "resumen": "Su departamento contable completo, operado por un equipo externo con un "
                   "responsable asignado.",
        "desde": "$ 780.000",
        "val": "outsourcing-contable",
        "incluye_t": "Todo lo que su área contable tiene que hacer cada mes",
        "incluye_lead": "Un solo servicio cubre la operación completa. Sin cobros sorpresa por "
                        "actividades que cualquier contabilidad necesita.",
        "incluye": [
            "Causación de compras, ventas y gastos",
            "Conciliaciones bancarias mensuales",
            "Liquidación y presentación de IVA",
            "Retención en la fuente y ReteICA",
            "Nómina, seguridad social y nómina electrónica",
            "Facturación electrónica y documento soporte",
            "Estados financieros mensuales",
            "Control de activos fijos y depreciación",
            "Análisis y evaluación de cartera",
            "Certificados de ingresos y retenciones",
        ],
        "img": "srv-outsourcing",
        "img_alt": "Contador de Alianza Contable operando la contabilidad de un cliente",
        "proceso_t": "Cuatro pasos, sin sorpresas en el camino",
        "proceso": [
            ("Diagnóstico y empalme",
             "Revisamos el estado real de la contabilidad, los saldos por conciliar y las "
             "obligaciones pendientes. Le entregamos un informe con lo que encontramos antes de "
             "que firme nada."),
            ("Migración y puesta a punto",
             "Cargamos saldos iniciales, parametrizamos el plan de cuentas y dejamos la "
             "plataforma operando con su información. Si viene de otra firma, coordinamos el "
             "empalme documento por documento."),
            ("Operación mensual",
             "Usted envía los soportes por el canal que prefiera. Nosotros causamos, conciliamos, "
             "liquidamos y presentamos. Le avisamos antes de cada vencimiento, no después."),
            ("Informe y reunión",
             "El día 15 recibe los estados financieros del mes anterior y un resumen en lenguaje "
             "claro. Una vez al mes revisamos juntos qué muestran los números y qué conviene "
             "ajustar."),
        ],
        "faq": FAQ_OUT,
        "otros": otros_links("outsourcing-contable.html"),
    })
))


# ==========================================================================
#  SERVICIO 02 · ASESORÍA TRIBUTARIA
# ==========================================================================
FAQ_TRIB = [
    ("Me llegó un requerimiento de la DIAN. ¿Qué hago?",
     "<p>Lo primero es no dejar vencer el término de respuesta, que suele ser corto y perentorio. "
     "Envíenos el documento el mismo día que lo reciba: revisamos qué le están pidiendo, qué "
     "soportes existen y preparamos la respuesta dentro del plazo. Responder tarde o no responder "
     "convierte un requerimiento en una liquidación oficial.</p>"),
    ("¿La planeación tributaria es legal?",
     "<p>Sí, siempre que se base en la aplicación correcta de la norma y no en ocultar hechos "
     "económicos. Planear es elegir, entre alternativas legítimas, la que genera menor carga "
     "impositiva: régimen, forma societaria, momento de la deducción, beneficios a los que "
     "efectivamente tiene derecho. Lo que no hacemos es simular operaciones.</p>"),
    ("¿Puedo corregir una declaración ya presentada?",
     "<p>Sí. La ley permite corregir, con reglas y plazos distintos según si la corrección aumenta "
     "o disminuye el impuesto a cargo. Corregir de forma voluntaria casi siempre sale mucho más "
     "barato que esperar a que la administración lo detecte. Revisamos su caso y le decimos si "
     "conviene corregir y con qué sanción reducida.</p>"),
    ("¿Atienden impuestos distritales de Bogotá?",
     "<p>Sí. Además de los impuestos nacionales, manejamos ICA, ReteICA, avisos y tableros y las "
     "declaraciones ante la Secretaría Distrital de Hacienda, incluida la clasificación correcta "
     "de actividades, que es donde más empresas terminan pagando de más.</p>"),
    ("¿Trabajan con empresas que ya tienen contador?",
     "<p>Con frecuencia. Muchas empresas mantienen su contabilidad interna y nos contratan solo "
     "para la parte tributaria: planeación anual, revisión previa a declarar y defensa ante "
     "requerimientos. Es un servicio que convive sin problema con su equipo actual.</p>"),
]

PAGES.append((
    "asesoria-tributaria.html",
    "Asesoría tributaria en Bogotá | Alianza Contable",
    "Planeación de impuestos, revisión antes de declarar y respuesta a requerimientos de la DIAN "
    "y la Secretaría de Hacienda de Bogotá.",
    "servicios", "img/srv-tributaria.jpg",
    service_schema("Asesoría tributaria",
                   "Planeación tributaria y atención de requerimientos para empresas en Bogotá.",
                   "asesoria-tributaria.html") + "\n" + faq_schema(FAQ_TRIB),
    service_page({
        "trail": [("Servicios", "index.html#servicios"), ("Asesoría tributaria", None)],
        "h1": "Pague lo que le corresponde. Ni un peso de más, ni una sanción de más.",
        "lead": "Planeación de impuestos, revisión antes de presentar y acompañamiento cuando la "
                "DIAN o la Secretaría de Hacienda tocan la puerta.",
        "panel": [("Ideal para", "Empresas con carga tributaria relevante"),
                  ("Modalidad", "Mensual o por caso puntual"),
                  ("Desde", "$ 520.000 / mes"),
                  ("Requerimientos", "Respuesta dentro del término legal")],
        "prose": """
<h2>Dos frentes distintos, un mismo equipo</h2>
<p>La asesoría tributaria tiene un lado preventivo y uno reactivo, y la mayoría de las empresas
solo descubre que necesitaba el primero cuando ya está viviendo el segundo.</p>

<h3>Antes: planear y revisar</h3>
<p>Revisamos cómo está estructurada su operación desde el punto de vista fiscal: régimen,
responsabilidades inscritas en el RUT, tratamiento de deducciones, beneficios a los que tiene
derecho y no está usando, y los puntos donde la empresa está expuesta. Antes de cada
presentación, un segundo par de ojos revisa la declaración.</p>

<h3>Después: responder y defender</h3>
<p>Si llega un requerimiento ordinario, un emplazamiento o un pliego de cargos, preparamos la
respuesta dentro del término, con los soportes que la sustentan. Cuando corresponde, evaluamos si
conviene corregir de forma voluntaria con sanción reducida en lugar de discutir.</p>
<blockquote>Un requerimiento que se deja vencer no desaparece: se convierte en una liquidación
oficial de revisión, con sanción e intereses.</blockquote>

<h3>Información exógena</h3>
<p>Buena parte de los requerimientos nacen de un cruce de exógena que no coincide. Por eso
revisamos su información antes de reportarla y la conciliamos con lo que terceros reportaron
sobre usted.</p>
""",
        "resumen": "Planeación tributaria, revisión previa a declarar y defensa ante "
                   "requerimientos de la DIAN.",
        "desde": "$ 520.000",
        "val": "asesoria-tributaria",
        "incluye_t": "Del calendario a la defensa, todo el frente tributario",
        "incluye_lead": "Cubrimos impuestos nacionales y distritales, y acompañamos el proceso "
                        "completo si la administración abre una revisión.",
        "incluye": [
            "Planeación tributaria anual",
            "Liquidación de impuestos nacionales",
            "ICA, ReteICA y avisos y tableros",
            "Revisión previa a cada presentación",
            "Información exógena nacional y distrital",
            "Respuesta a requerimientos y emplazamientos",
            "Evaluación de correcciones voluntarias",
            "Solicitudes de devolución y compensación",
            "Conceptos tributarios por escrito",
            "Acompañamiento en visitas de fiscalización",
        ],
        "img": "srv-tributaria",
        "img_alt": "Profesionales revisando obligaciones tributarias de una empresa",
        "proceso_t": "Así entramos en su operación tributaria",
        "proceso": [
            ("Radiografía fiscal",
             "Revisamos RUT, responsabilidades inscritas, declaraciones de los últimos periodos "
             "abiertos y el estado de cuenta ante la DIAN. Le mostramos dónde está expuesto."),
            ("Plan del año",
             "Definimos el calendario de la empresa, quién entrega qué y en qué fecha, y las "
             "decisiones fiscales que conviene tomar antes de que termine el periodo."),
            ("Revisión antes de presentar",
             "Ninguna declaración sale sin una segunda revisión. Es el control que evita la "
             "corrección costosa tres meses después."),
            ("Defensa si hace falta",
             "Si llega un requerimiento, asumimos la respuesta con los soportes y dentro del "
             "término. Le explicamos en lenguaje claro qué está en juego y qué opciones tiene."),
        ],
        "faq": FAQ_TRIB,
        "otros": otros_links("asesoria-tributaria.html"),
    })
))


# ==========================================================================
#  SERVICIO 03 · ASESORÍA FISCAL Y REVISORÍA
# ==========================================================================
FAQ_FISC = [
    ("¿Mi empresa está obligada a tener revisor fiscal?",
     "<p>Están obligadas todas las sociedades por acciones y las sucursales de compañías "
     "extranjeras. Además, cualquier sociedad cuyos activos brutos al cierre del año anterior "
     "superen los 5.000 salarios mínimos o cuyos ingresos brutos superen los 3.000, según el "
     "parágrafo del artículo 13 de la Ley 43 de 1990. Si no sabe si los superó, lo verificamos "
     "con usted sin costo.</p>"),
    ("¿Cuál es la diferencia entre revisoría fiscal y auditoría?",
     "<p>La revisoría fiscal es una figura de la ley colombiana: es permanente, la elige la "
     "asamblea, y el revisor dictamina los estados financieros y responde ante el Estado, los "
     "socios y terceros. La auditoría es un encargo contractual, con alcance y duración que "
     "define quien la contrata. Una empresa puede necesitar las dos, por razones distintas.</p>"),
    ("¿Pueden ser mi contador y mi revisor fiscal a la vez?",
     "<p>No, y ninguna firma seria debería ofrecerlo. La revisoría fiscal exige independencia "
     "frente a quien prepara la contabilidad. Si llevamos su contabilidad, no podemos ser sus "
     "revisores, y al contrario. Cuando se da el caso, le ayudamos a encontrar una firma "
     "independiente.</p>"),
    ("¿Cuánto dura una auditoría?",
     "<p>Depende del alcance. Una auditoría de estados financieros de una pyme suele tomar entre "
     "tres y seis semanas de trabajo de campo. Una revisión limitada a un ciclo concreto —compras, "
     "nómina, inventarios— puede resolverse en dos. El cronograma se acuerda antes de empezar.</p>"),
    ("Un banco me pide estados financieros dictaminados. ¿Eso qué es?",
     "<p>Son estados financieros acompañados del dictamen de un contador público independiente que "
     "opina sobre si presentan razonablemente la situación de la empresa. Es lo que bancos, "
     "inversionistas y procesos de due diligence suelen exigir. Emitimos ese dictamen cuando "
     "actuamos como auditores externos.</p>"),
]

PAGES.append((
    "asesoria-fiscal.html",
    "Revisoría fiscal y auditoría en Bogotá | Alianza Contable",
    "Revisoría fiscal para sociedades obligadas por ley y auditoría independiente de estados "
    "financieros para bancos, socios y procesos de due diligence.",
    "servicios", "img/srv-fiscal.jpg",
    service_schema("Revisoría fiscal y auditoría",
                   "Revisoría fiscal y auditoría externa independiente en Bogotá.",
                   "asesoria-fiscal.html") + "\n" + faq_schema(FAQ_FISC),
    service_page({
        "trail": [("Servicios", "index.html#servicios"), ("Asesoría fiscal y revisoría", None)],
        "h1": "Revisoría fiscal y auditoría independiente",
        "lead": "Para sociedades que superaron los topes de ley y para empresas a las que un "
                "banco, un socio o un inversionista les está pidiendo estados financieros "
                "dictaminados.",
        "panel": [("Ideal para", "Sociedades obligadas y empresas en due diligence"),
                  ("Figura", "Revisoría fiscal o auditoría externa"),
                  ("Desde", "$ 1.520.000 / mes"),
                  ("Dictamen", "Sobre estados financieros anuales")],
        "prose": """
<h2>Cuándo aparece esta necesidad</h2>
<p>Casi siempre por una de tres razones: la sociedad cruzó los topes de activos o ingresos y quedó
obligada a nombrar revisor fiscal; un banco condicionó el crédito a estados financieros
dictaminados; o entró un inversionista que quiere una lectura independiente de las cifras antes
de poner dinero.</p>

<h3>Revisoría fiscal</h3>
<p>Es una figura permanente creada por la ley colombiana. El revisor fiscal lo elige la asamblea,
vigila que la sociedad cumpla las normas, que la contabilidad se lleve conforme a la técnica, que
exista un control interno razonable, y dictamina los estados financieros. Responde ante el Estado,
los socios y terceros.</p>

<h3>Auditoría externa</h3>
<p>Es un encargo con alcance definido por quien la contrata. Puede ser sobre los estados
financieros completos o sobre un ciclo específico: compras, inventarios, nómina, tesorería.
Termina con un informe de hallazgos y recomendaciones concretas, no con una lista de generalidades.</p>

<blockquote>La independencia no es un formalismo: quien prepara la contabilidad no puede
auditarla. Si llevamos sus libros, no podemos ser sus revisores fiscales.</blockquote>

<h3>Qué recibe además del dictamen</h3>
<p>Un informe de control interno con los hallazgos ordenados por riesgo y con recomendaciones
aplicables. La mayoría de nuestros clientes de auditoría dice que ese documento le resultó más
útil que el dictamen mismo.</p>
""",
        "resumen": "Revisoría fiscal permanente o auditoría externa independiente, con dictamen "
                   "e informe de control interno.",
        "desde": "$ 1.520.000",
        "val": "asesoria-fiscal",
        "incluye_t": "El alcance de un encargo serio",
        "incluye_lead": "Trabajo de campo documentado, papeles de trabajo archivados y un informe "
                        "que se puede defender ante quien lo pregunte.",
        "incluye": [
            "Dictamen sobre estados financieros",
            "Evaluación del sistema de control interno",
            "Verificación del cumplimiento tributario",
            "Revisión de aportes a seguridad social",
            "Pruebas selectivas por ciclo de negocio",
            "Arqueos, inventarios y confirmaciones",
            "Informe de hallazgos priorizados por riesgo",
            "Asistencia a asamblea y junta directiva",
            "Comunicaciones obligatorias a organismos de control",
            "Papeles de trabajo archivados y disponibles",
        ],
        "img": "srv-fiscal",
        "img_alt": "Auditora revisando documentación de una empresa cliente",
        "proceso_t": "Cómo se ejecuta el encargo",
        "proceso": [
            ("Aceptación y evaluación de independencia",
             "Antes de aceptar verificamos que no exista incompatibilidad. Definimos por escrito "
             "el alcance, el equipo asignado y los honorarios."),
            ("Planeación y evaluación de riesgos",
             "Entendemos el negocio, identificamos los ciclos críticos y definimos las pruebas. "
             "Aquí se decide dónde vale la pena mirar a fondo."),
            ("Trabajo de campo",
             "Pruebas de recorrido, muestreo, confirmaciones con terceros, arqueos e inventarios. "
             "Todo queda soportado en papeles de trabajo."),
            ("Informe y dictamen",
             "Presentamos hallazgos ordenados por riesgo, con recomendaciones concretas, y "
             "emitimos el dictamen. Lo sustentamos ante junta directiva o asamblea si se requiere."),
        ],
        "faq": FAQ_FISC,
        "otros": otros_links("asesoria-fiscal.html"),
    })
))


# ==========================================================================
#  SERVICIO 04 · DECLARACIÓN DE RENTA
# ==========================================================================
FAQ_RENTA = [
    ("¿Estoy obligado a declarar renta este año?",
     "<p>Los topes de patrimonio, ingresos, consumos con tarjeta, compras y consignaciones se "
     "actualizan cada año en UVT mediante decreto. No basta con recordar lo del año pasado. "
     "Revisamos su caso concreto contra los topes vigentes y le decimos si está obligado, sin "
     "costo y sin compromiso.</p>"),
    ("¿Qué pasa si no declaré y estaba obligado?",
     "<p>Se genera sanción por extemporaneidad, que aumenta por cada mes de retraso, más "
     "intereses de mora. Presentar de forma voluntaria antes de que la DIAN lo requiera reduce "
     "significativamente la sanción. Cuanto antes se corrija, menos cuesta.</p>"),
    ("¿Por qué revisan la exógena antes de declarar?",
     "<p>Porque la DIAN ya sabe buena parte de lo que usted va a declarar: bancos, empleadores y "
     "comercios reportaron sus operaciones. Si su declaración no coincide con esa información, el "
     "cruce automático genera el requerimiento. Comparamos ambas fuentes antes de presentar.</p>"),
    ("¿Qué documentos debo reunir?",
     "<p>Certificado de ingresos y retenciones, certificados bancarios y de inversiones, "
     "certificados de deudas, escrituras y avalúos de inmuebles, tarjeta de propiedad de "
     "vehículos, y los soportes de deducciones: medicina prepagada, intereses de vivienda, "
     "dependientes y aportes voluntarios. Le enviamos la lista completa al agendar.</p>"),
    ("¿Atienden personas naturales o solo empresas?",
     "<p>Las dos. Para personas naturales manejamos la cédula tributaria completa: rentas de "
     "trabajo, de capital, no laborales, dividendos y ganancias ocasionales. Para sociedades, la "
     "declaración de renta y complementarios junto con sus anexos.</p>"),
]

PAGES.append((
    "declaracion-de-renta.html",
    "Declaración de renta en Bogotá | Alianza Contable",
    "Declaración de renta para personas naturales y sociedades, con revisión previa de la "
    "información exógena para evitar requerimientos posteriores.",
    "servicios", "img/srv-renta.jpg",
    service_schema("Declaración de renta",
                   "Preparación y presentación de la declaración de renta en Bogotá.",
                   "declaracion-de-renta.html") + "\n" + faq_schema(FAQ_RENTA),
    service_page({
        "trail": [("Servicios", "index.html#servicios"), ("Declaración de renta", None)],
        "h1": "Su declaración de renta, revisada antes de presentarla",
        "lead": "Personas naturales y sociedades. Cruzamos su información con la exógena que la "
                "DIAN ya tiene sobre usted, para que no le llegue un requerimiento seis meses "
                "después.",
        "panel": [("Ideal para", "Personas naturales y sociedades"),
                  ("Incluye", "Cruce con información exógena"),
                  ("Desde", "$ 380.000 por declaración"),
                  ("Plazo", "Según el calendario DIAN vigente")],
        "prose": """
<h2>El error más común no es calcular mal</h2>
<p>Es declarar sin mirar antes qué información tiene la DIAN sobre usted. Bancos, empleadores,
comercios, notarías y fondos ya reportaron sus operaciones en la información exógena. Si lo que
usted declara no coincide con eso, el cruce automático genera un requerimiento, aunque su cifra
sea la correcta.</p>
<p>Por eso el primer paso de este servicio es descargar y leer su información exógena. Después
declaramos.</p>

<h3>Personas naturales</h3>
<p>El sistema cedular obliga a clasificar correctamente cada ingreso: rentas de trabajo, de
capital, no laborales, dividendos y ganancias ocasionales. Una clasificación equivocada puede
costarle más impuesto del que le corresponde, o abrirle una discusión que no tenía por qué existir.
Revisamos además las deducciones a las que sí tiene derecho y que mucha gente no aplica.</p>

<h3>Sociedades</h3>
<p>Declaración de renta y complementarios con sus anexos, conciliación fiscal, y verificación de
que las cifras concuerden con los estados financieros y con lo reportado durante el año.</p>

<blockquote>Presentar de forma voluntaria antes de que la DIAN requiera reduce la sanción de
manera sustancial. Esperar nunca sale más barato.</blockquote>

<h3>Fechas de vencimiento</h3>
<p>Los plazos cambian cada año por decreto y dependen de los últimos dígitos de su NIT o cédula.
Consulte la herramienta de vencimientos en la
<a href="index.html#cotizar">página de inicio</a> y confirme siempre contra el calendario oficial
vigente de la DIAN.</p>
""",
        "resumen": "Preparación, revisión contra exógena y presentación de su declaración de "
                   "renta, para personas naturales y sociedades.",
        "desde": "$ 380.000",
        "val": "declaracion-de-renta",
        "incluye_t": "Qué hacemos antes de oprimir «presentar»",
        "incluye_lead": "El valor del servicio no está en llenar el formulario: está en todo lo "
                        "que se revisa antes.",
        "incluye": [
            "Verificación de la obligación de declarar",
            "Descarga y lectura de información exógena",
            "Cruce entre exógena y sus soportes",
            "Clasificación cedular de los ingresos",
            "Revisión de deducciones aplicables",
            "Depuración de patrimonio y deudas",
            "Cálculo de ganancias ocasionales",
            "Elaboración y presentación electrónica",
            "Generación del recibo de pago",
            "Archivo digital de soportes por si hay revisión",
        ],
        "img": "srv-renta",
        "img_alt": "Asesor contable explicando la declaración de renta a sus clientes",
        "proceso_t": "De la cita a la declaración presentada",
        "proceso": [
            ("Cita y lista de documentos",
             "Agenda una cita y recibe por correo la lista exacta de documentos que necesitamos "
             "según su caso. Nada genérico."),
            ("Descarga de exógena",
             "Consultamos qué reportaron terceros sobre usted durante el año y lo comparamos con "
             "los soportes que nos entregó."),
            ("Depuración y cálculo",
             "Clasificamos ingresos, aplicamos las deducciones a las que tiene derecho y "
             "calculamos el impuesto. Le mostramos el resultado antes de presentar."),
            ("Presentación y archivo",
             "Presentamos electrónicamente, generamos el recibo de pago y le entregamos el "
             "expediente digital completo, listo por si algún día hay revisión."),
        ],
        "faq": FAQ_RENTA,
        "otros": otros_links("declaracion-de-renta.html"),
    })
))


# ==========================================================================
#  SERVICIO 05 · CONSTITUCIÓN DE EMPRESA
# ==========================================================================
FAQ_CONST = [
    ("¿SAS, persona natural o qué me conviene?",
     "<p>Depende de cuánto riesgo asume, si tendrá socios, qué tan grande espera que sea la "
     "facturación y qué tipo de clientes va a atender. La SAS es la figura más usada en Colombia "
     "porque separa su patrimonio personal del de la empresa y es flexible en estatutos, pero no "
     "siempre es lo más conveniente para un negocio que apenas está probando. Lo definimos en la "
     "primera reunión.</p>"),
    ("¿Cuánto se demora todo el trámite?",
     "<p>Con la documentación completa, entre una y dos semanas hábiles. La matrícula en cámara "
     "de comercio suele resolverse en pocos días; lo que más suele demorar es la asignación de "
     "cita para la firma electrónica y la habilitación de facturación.</p>"),
    ("¿Cuánto cuesta constituir una empresa?",
     "<p>Hay dos rubros distintos: nuestros honorarios y los derechos que cobra la Cámara de "
     "Comercio de Bogotá, que dependen del capital que se registre y se actualizan cada año. Le "
     "entregamos el desglose completo antes de empezar, para que no haya sorpresas.</p>"),
    ("¿Me ayudan a abrir la cuenta bancaria?",
     "<p>Preparamos el paquete de documentos que los bancos piden —certificado de existencia, RUT, "
     "estatutos, composición accionaria— y lo acompañamos en el proceso. La aprobación de la "
     "cuenta depende del banco, no de nosotros.</p>"),
    ("¿Qué obligaciones tengo desde el primer mes?",
     "<p>Depende de las responsabilidades que queden inscritas en el RUT. Como mínimo: facturar "
     "electrónicamente, llevar contabilidad y presentar las declaraciones que le correspondan. Al "
     "cerrar la constitución le entregamos su calendario de obligaciones personalizado.</p>"),
]

PAGES.append((
    "constitucion-de-empresa.html",
    "Constitución de empresa en Bogotá | Alianza Contable",
    "Constituya su SAS o sociedad en Bogotá: tipo societario, cámara de comercio, RUT, firma "
    "electrónica y habilitación de facturación electrónica.",
    "servicios", "img/srv-constitucion.jpg",
    service_schema("Constitución de empresa",
                   "Constitución de sociedades y formalización de negocios en Bogotá.",
                   "constitucion-de-empresa.html") + "\n" + faq_schema(FAQ_CONST),
    service_page({
        "trail": [("Servicios", "index.html#servicios"), ("Constitución de empresa", None)],
        "h1": "De la idea a la sociedad constituida, en dos semanas",
        "lead": "Tipo societario, estatutos, cámara de comercio, RUT, firma electrónica y "
                "facturación habilitada. Termina con la empresa lista para emitir su primera "
                "factura, no con una carpeta de trámites a medias.",
        "panel": [("Ideal para", "Emprendedores y negocios que se formalizan"),
                  ("Tiempo", "1 a 2 semanas hábiles"),
                  ("Honorarios desde", "$ 890.000 pago único"),
                  ("Aparte", "Derechos de cámara de comercio")],
        "prose": """
<h2>Formalizarse mal sale caro después</h2>
<p>Constituir una empresa es un trámite. Constituirla bien es una decisión: el tipo societario, el
capital que registra, las responsabilidades que inscribe en el RUT y el código de actividad
económica que elige van a determinar cuántos impuestos paga y qué obligaciones asume desde el
primer mes.</p>
<p>Vemos con frecuencia empresas que quedaron inscritas con responsabilidades que no les
correspondían, o con un código CIIU equivocado que les generó una tarifa de ICA más alta durante
años. Corregirlo después toma tiempo y dinero.</p>

<h3>Qué definimos antes de radicar</h3>
<ul>
  <li>El tipo societario que corresponde a su riesgo, sus socios y su proyección.</li>
  <li>El capital autorizado, suscrito y pagado, y qué implica cada cifra.</li>
  <li>Los estatutos: objeto social, administración, reparto de utilidades y salida de socios.</li>
  <li>El código de actividad económica correcto, que define su tarifa de ICA.</li>
  <li>Las responsabilidades del RUT que realmente le aplican.</li>
</ul>

<blockquote>Un código de actividad económica mal elegido puede costarle una tarifa de ICA más alta
durante todos los años en que nadie lo revise.</blockquote>

<h3>Y después de constituir</h3>
<p>La empresa nueva necesita llevar contabilidad desde el día uno. Si quiere, seguimos con el plan
de <a href="contabilidad-para-emprendedores.html">contabilidad para emprendedores</a>; si prefiere
manejarlo internamente, le dejamos el calendario de obligaciones y la parametrización lista.</p>
""",
        "resumen": "Constitución completa de su sociedad, desde el tipo societario hasta la "
                   "primera factura electrónica emitida.",
        "desde": "$ 890.000",
        "val": "constitucion-de-empresa",
        "incluye_t": "Todo el trámite, de principio a fin",
        "incluye_lead": "Nos encargamos de la gestión completa. Usted solo firma lo que tiene que "
                        "firmar.",
        "incluye": [
            "Asesoría en tipo societario",
            "Redacción de estatutos a la medida",
            "Consulta y reserva de nombre",
            "Matrícula en Cámara de Comercio de Bogotá",
            "Inscripción del RUT ante la DIAN",
            "Definición de responsabilidades tributarias",
            "Firma electrónica de la sociedad",
            "Habilitación de facturación electrónica",
            "Registro de libros y de accionistas",
            "Calendario de obligaciones del primer año",
        ],
        "img": "srv-constitucion",
        "img_alt": "Emprendedora firmando los documentos de constitución de su empresa",
        "proceso_t": "Dos semanas, cuatro momentos",
        "proceso": [
            ("Reunión de definición",
             "Una hora para entender el negocio, los socios y la proyección. De ahí sale el tipo "
             "societario, el capital y el objeto social."),
            ("Estatutos y radicación",
             "Redactamos los estatutos, verificamos disponibilidad del nombre y radicamos ante la "
             "Cámara de Comercio de Bogotá."),
            ("RUT y firma electrónica",
             "Inscribimos el RUT con las responsabilidades que corresponden y gestionamos el "
             "instrumento de firma electrónica ante la DIAN."),
            ("Facturación y entrega",
             "Habilitamos la facturación electrónica, dejamos la numeración autorizada y le "
             "entregamos el expediente completo con su calendario de obligaciones."),
        ],
        "faq": FAQ_CONST,
        "otros": otros_links("constitucion-de-empresa.html"),
    })
))


# ==========================================================================
#  SERVICIO 06 · CONTABILIDAD PARA EMPRENDEDORES
# ==========================================================================
FAQ_EMP = [
    ("Facturo muy poco. ¿De verdad necesito contador?",
     "<p>Si está constituido como sociedad, sí: la obligación de llevar contabilidad no depende de "
     "cuánto facture. Si opera como persona natural, depende de su régimen y de sus ingresos. En "
     "cualquier caso, empezar bien cuesta mucho menos que arreglar dos años de desorden después.</p>"),
    ("¿Qué pasa si un mes no tuve movimiento?",
     "<p>Igual hay que presentar las declaraciones a las que esté obligado, aunque sean en ceros. "
     "No presentar una declaración en ceros genera sanción por extemporaneidad exactamente igual "
     "que no presentar una con impuesto a cargo.</p>"),
    ("¿El plan de entrada tiene permanencia mínima?",
     "<p>No. Puede terminar cuando quiera con el preaviso pactado, y al salir le entregamos la "
     "información contable completa y ordenada. Tampoco hay penalidad por subir al plan de "
     "outsourcing completo cuando el negocio crezca.</p>"),
    ("¿Cuándo debo pasarme al plan completo?",
     "<p>Cuando contrate empleados, cuando el volumen de documentos supere lo que el plan cubre, o "
     "cuando necesite estados financieros mensuales para un banco o un inversionista. Se lo "
     "decimos nosotros cuando lo veamos, no esperamos a que se dé cuenta solo.</p>"),
    ("¿Me ayudan con la facturación electrónica?",
     "<p>Sí. Dejamos habilitada la facturación, la numeración autorizada y le enseñamos a emitir. "
     "Es lo primero que hacemos, porque sin factura válida no hay ingreso deducible para su "
     "cliente ni soporte para usted.</p>"),
]

PAGES.append((
    "contabilidad-para-emprendedores.html",
    "Contabilidad para emprendedores en Bogotá | Alianza Contable",
    "Plan de entrada para negocios que apenas arrancan: lo mínimo legal bien hecho, a un costo "
    "que un emprendimiento sí puede sostener.",
    "servicios", "img/srv-emprendedores.jpg",
    service_schema("Contabilidad para emprendedores",
                   "Plan contable de entrada para emprendimientos y negocios nuevos en Bogotá.",
                   "contabilidad-para-emprendedores.html") + "\n" + faq_schema(FAQ_EMP),
    service_page({
        "trail": [("Servicios", "index.html#servicios"),
                  ("Contabilidad para emprendedores", None)],
        "h1": "El plan de entrada para el negocio que apenas arranca",
        "lead": "Lo mínimo legal, bien hecho, a un costo que un emprendimiento sí puede sostener. "
                "Sin pagar por servicios que todavía no necesita.",
        "panel": [("Ideal para", "Negocios con menos de 40 documentos al mes"),
                  ("Sin", "Permanencia mínima"),
                  ("Desde", "$ 420.000 / mes"),
                  ("Incluye", "Facturación electrónica habilitada")],
        "prose": """
<h2>El problema del emprendedor con la contabilidad</h2>
<p>Las firmas contables suelen cotizarle a un negocio nuevo lo mismo que a una empresa mediana,
porque el proceso interno es el mismo. El resultado es previsible: el emprendedor decide que la
contabilidad puede esperar, y a los dos años llega con obligaciones vencidas y sanciones
acumuladas.</p>
<p>Este plan existe para romper eso. Cubre lo que la ley exige y lo que el negocio realmente usa
en su primer año, y nada más.</p>

<h3>Qué sí necesita un negocio nuevo</h3>
<ul>
  <li>Facturar electrónicamente, con numeración autorizada y sin errores de forma.</li>
  <li>Presentar a tiempo las declaraciones que le correspondan, incluso en ceros.</li>
  <li>Saber cuánto está ganando de verdad, no cuánto entró a la cuenta.</li>
  <li>Tener los soportes ordenados por si algún día hay revisión.</li>
</ul>

<h3>Qué todavía no necesita</h3>
<p>Estados financieros bajo NIIF plenas, revisoría fiscal, planeación tributaria compleja ni
informes gerenciales semanales. Cuando llegue el momento, se lo decimos y subimos el plan.</p>

<blockquote>Empezar bien cuesta una fracción de lo que cuesta arreglar dos años de desorden
contable, con sanciones incluidas.</blockquote>
""",
        "resumen": "Contabilidad mensual, impuestos y facturación electrónica para negocios en "
                   "su primer año, sin permanencia mínima.",
        "desde": "$ 420.000",
        "val": "contabilidad-para-emprendedores",
        "incluye_t": "Lo esencial, sin relleno",
        "incluye_lead": "Un plan pensado para un volumen de hasta 40 documentos mensuales. Si lo "
                        "supera, se lo avisamos antes de cobrarle de más.",
        "incluye": [
            "Contabilidad mensual del negocio",
            "Facturación electrónica habilitada",
            "Liquidación de IVA cuando aplique",
            "Retención en la fuente cuando aplique",
            "Declaraciones en ceros si no hubo movimiento",
            "Informe mensual simplificado de resultados",
            "Conciliación bancaria",
            "Archivo digital de soportes",
            "Alertas antes de cada vencimiento",
            "Una asesoría al mes por videollamada",
        ],
        "img": "srv-emprendedores",
        "img_alt": "Emprendedor trabajando en un espacio de coworking en Bogotá",
        "proceso_t": "Empezar toma menos de una semana",
        "proceso": [
            ("Diagnóstico corto",
             "Media hora para entender qué vende, cómo cobra y qué obligaciones tiene inscritas "
             "en el RUT."),
            ("Puesta a punto",
             "Habilitamos facturación electrónica, ordenamos lo que exista de meses anteriores y "
             "dejamos el archivo digital montado."),
            ("Rutina mensual",
             "Usted nos envía los soportes; nosotros contabilizamos, declaramos y le mandamos el "
             "informe simplificado."),
            ("Crecer cuando toque",
             "Cuando el volumen o la nómina lo justifiquen, le proponemos pasar al outsourcing "
             "completo. Sin penalidad y sin migración traumática."),
        ],
        "faq": FAQ_EMP,
        "otros": otros_links("contabilidad-para-emprendedores.html"),
    })
))

print("Servicios definidos: %d" % len(PAGES))
