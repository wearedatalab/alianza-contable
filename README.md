# Alianza Contable — rediseño web

Propuesta de rediseño de **alianzacontable.com** (firma de outsourcing contable, Bogotá),
construida sobre la arquitectura definida en `Propuesta_Alianza_Contable_Web_2026.pptx`.

Sitio estático autónomo: HTML + CSS + JS, sin dependencias ni backend.

## Cómo verlo

```bash
npx -y http-server alianza-contable -p 8812 -c-1
```

Registrado también en `.claude/launch.json` como `alianza-contable` (puerto 8812).

## Arquitectura (14 páginas + 1 plantilla de artículo)

| Página | Archivo |
|---|---|
| Inicio | `index.html` |
| Nosotros | `nosotros.html` |
| Outsourcing contable | `outsourcing-contable.html` |
| Asesoría tributaria | `asesoria-tributaria.html` |
| Asesoría fiscal y revisoría | `asesoria-fiscal.html` |
| Declaración de renta | `declaracion-de-renta.html` |
| Constitución de empresa | `constitucion-de-empresa.html` |
| Contabilidad para emprendedores | `contabilidad-para-emprendedores.html` |
| Por industria | `por-industria.html` |
| Recursos y normativa | `recursos.html` |
| Artículo (plantilla) | `articulo-caracteristicas-outsourcing-contable.html` |
| Agende su diagnóstico | `agende-su-diagnostico.html` |
| Contáctenos | `contacto.html` |
| Política de tratamiento de datos | `politica-de-datos.html` |
| Términos y condiciones | `terminos-y-condiciones.html` |

## Sistema de diseño

Concepto **«Cifras que sostienen decisiones»**: precisión de libro contable — numeración
tabular, tinta azul profunda, verde de conformidad y superficies limpias sin textura.

- **Color:** navy `#0B2A41` y verde `#55BB53`, extraídos del sitio y el logo actuales.
  Papel cálido `#F7F5F0` en lugar de blanco clínico. `--green-700` y `--text-3` son
  variantes **oscurecidas para texto**: todo el sitio pasa WCAG AA (auditado por script).
- **Tipografía:** Fraunces (títulos), Inter (texto), IBM Plex Mono (etiquetas y cifras).
- **Todo el sistema vive en `css/site.css`**, organizado en 27 bloques numerados.

## Los cinco vacíos del mercado, resueltos en el sitio

La propuesta identificó cinco cosas que ninguna de las seis firmas de Bogotá analizadas
ofrece. Las cinco están implementadas:

1. **Agendamiento real** — `agende-su-diagnostico.html`: selector de día y hora con
   disponibilidad simulada de forma determinista.
2. **Precios visibles** — tarifas «desde» por perfil de empresa y en cada servicio.
3. **Herramientas gratuitas** — cotizador de outsourcing y consulta de vencimientos DIAN
   por último dígito del NIT (inicio y `recursos.html`).
4. **Segmentación por industria** — `por-industria.html`: salud, construcción y comercio.
5. **Resultados con cifras** — barra de confianza y paneles de datos por servicio.

## Cumplimiento y honestidad de la maqueta

- **Ley 1581 de 2012:** casilla de autorización expresa en cada formulario, banner de
  cookies con registro de consentimiento en `localStorage`, y las dos páginas legales.
  Los textos legales son **modelo, pendientes de validación por el abogado de la firma**;
  cada página lo advierte en un aviso visible.
- **Datos estructurados:** 29 bloques JSON-LD válidos — `AccountingService` en las 15
  páginas, `Service` en las 6 de servicio, `FAQPage` en 7 y `BlogPosting` en el artículo.
- **Nada inventado se presenta como real.** Cifras, tarifas, testimonios, perfiles del
  equipo, logos de clientes y fechas de la DIAN llevan la etiqueta `.demo-tag`
  («Formato de ejemplo», «Por confirmar»…). La propuesta señaló testimonios falsos en el
  sitio actual como hallazgo crítico; aquí los testimonios son plantillas marcadas.
- Franja fija abajo a la izquierda: «Propuesta de rediseño · DataLab 2026 · prototipo sin
  backend». Se elimina borrando el `div.demo-ribbon` de `index.html` y reconstruyendo.

## Pendientes de la firma antes de publicar

Razón social y NIT · coordenadas y horario reales · cifras de la barra de confianza ·
tarifas definitivas · nombres y tarjetas profesionales del equipo · testimonios y logos
autorizados · calendario oficial DIAN vigente · mapa de Google.

## Generación

`index.html` es la **plantilla canónica escrita a mano**. Las otras 14 páginas se generan
tomando de ella el `<head>`, la barra superior, la navegación, el pie y los flotantes, de
modo que el armazón nunca se desincroniza.

```bash
python _pages2.py     # regenera las 14 páginas interiores
```

- `_build.py` — extrae el armazón de `index.html` y define los componentes reutilizables
  (`phead`, `steps`, `faq`, `cta_band`, `service_page`, schemas…).
- `_pages.py` — contenido de las 6 páginas de servicio.
- `_pages2.py` — contenido institucional, de conversión y legal + escritura de archivos.
- `_gen_images.py` — genera las 24 imágenes con fal.ai (FLUX dev). Ya ejecutado; el script
  omite las que existan.

**Si edita el `<head>`, la navegación o el pie, hágalo en `index.html` y vuelva a ejecutar
`python _pages2.py`.** Editar una página interior a mano se pierde en la siguiente
generación.
