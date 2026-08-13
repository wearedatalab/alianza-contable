# -*- coding: utf-8 -*-
"""Genera las imagenes del rediseno Alianza Contable via fal.ai FLUX dev."""
import json, os, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

ENV = r"C:\Users\donju\Desktop\Webs\videos-secuenciales\.env"
OUT = r"C:\Users\donju\Desktop\Webs\alianza-contable\img"
KEY = os.environ.get("FAL_KEY")
if not KEY and os.path.exists(ENV):
    with open(ENV, encoding="utf-8") as f:
        for line in f:
            if line.startswith("FAL_KEY="):
                KEY = line.strip().split("=", 1)[1]
if not KEY:
    sys.exit("FAL_KEY no encontrada")

STYLE = ("editorial corporate photography, colombian professionals in bogota, "
         "soft natural window light, calm confident composed mood, restrained color "
         "palette of deep navy blue, warm sand and paper tones with subtle sage green "
         "accents, shot on 50mm f2.0, medium depth of field, authentic documentary feel, "
         "muted realistic colors, film grain, no text, no letters, no numbers, "
         "no logos, no watermarks, no signage")

IMAGES = [
    # ---- hero (retrato vertical junto al titular) ----
    ("hero", 896, 1152,
     "portrait of a composed colombian woman accountant in her late 30s wearing a navy "
     "blazer over a cream blouse, standing with arms lightly crossed in a bright modern "
     "accounting firm office in bogota, large window with soft city light behind her, "
     "warm wooden desk and plants softly blurred, quiet authority, subtle warm smile, "
     + STYLE),

    # ---- nosotros / equipo ----
    ("equipo", 1344, 896,
     "small team of four colombian accounting professionals reviewing documents together "
     "around a light wooden meeting table in a modern bogota office, two women and two men "
     "in smart business casual, engaged collaborative conversation, laptops and paper "
     "folders on the table, large windows with soft daylight, plants, " + STYLE),
    ("oficina", 1024, 768,
     "interior of a calm modern accounting firm office in bogota, empty light wooden desks, "
     "navy blue accent wall, tall windows with sheer curtains diffusing morning light, "
     "green plants, minimal architecture, warm neutral tones, no people, " + STYLE),

    # ---- servicios (6) ----
    ("srv-outsourcing", 1024, 768,
     "colombian accountant man in his 40s working focused at a clean desk with two monitors "
     "in a modern office, papers organized in neat stacks, calm concentration, morning light, "
     + STYLE),
    ("srv-tributaria", 1024, 768,
     "two colombian professionals in a serious focused discussion over printed documents at "
     "a meeting table, one pointing at a page, navy and sand tones, tall window light, "
     + STYLE),
    ("srv-fiscal", 1024, 768,
     "colombian woman auditor in her 50s wearing glasses carefully reviewing a thick binder "
     "of documents at a desk, magnifier and pen nearby, precise methodical atmosphere, "
     "soft side light, " + STYLE),
    ("srv-renta", 1024, 768,
     "colombian accountant sitting across a desk from a client couple in a warm office, "
     "explaining calmly with open hands, reassuring atmosphere, folders on desk, " + STYLE),
    ("srv-constitucion", 1024, 768,
     "young colombian entrepreneur woman shaking hands with an advisor in a bright modern "
     "office, signing folder on the table, hopeful new beginning atmosphere, " + STYLE),
    ("srv-emprendedores", 1024, 768,
     "young colombian entrepreneur man in a casual shirt working on a laptop at a small "
     "wooden table in a bright coworking space in bogota, coffee cup, plants, relaxed "
     "focused energy, " + STYLE),

    # ---- industrias (3) ----
    ("ind-salud", 1024, 768,
     "administrative manager of a small private medical clinic in bogota reviewing paperwork "
     "at a reception desk, clean clinical interior softly blurred, calm professional, "
     + STYLE),
    ("ind-construccion", 1024, 768,
     "colombian construction company manager wearing a white hard hat and safety vest "
     "reviewing plans on a tablet at a building site office in bogota, structural concrete "
     "background softly blurred, late afternoon light, " + STYLE),
    ("ind-comercio", 1024, 768,
     "owner of a small colombian retail store checking inventory on a tablet behind the "
     "counter, warm shop interior with shelves softly blurred, friendly entrepreneurial "
     "energy, " + STYLE),

    # ---- retratos equipo (4) ----
    ("team-1", 768, 1024,
     "professional portrait of a colombian woman in her late 40s, senior partner of an "
     "accounting firm, elegant navy blazer, short dark hair with subtle grey, confident "
     "warm expression, modern office softly blurred behind, " + STYLE),
    ("team-2", 768, 1024,
     "professional portrait of a colombian man in his mid 50s, tax director, light blue "
     "shirt and dark blazer no tie, glasses, calm authoritative expression, office "
     "background softly blurred, " + STYLE),
    ("team-3", 768, 1024,
     "professional portrait of a colombian woman in her early 30s, payroll and compliance "
     "lead, cream blouse, natural curly hair, approachable confident smile, bright office "
     "softly blurred, " + STYLE),
    ("team-4", 768, 1024,
     "professional portrait of a colombian man in his 30s, audit manager, dark grey shirt, "
     "short beard, thoughtful serious expression, modern office softly blurred, " + STYLE),

    # ---- testimonios (avatares cuadrados) ----
    ("tst-1", 640, 640,
     "close portrait of a colombian woman in her 40s, administrative manager of a small "
     "company, simple blouse, natural warm smile, plain office background blurred, "
     + STYLE),
    ("tst-2", 640, 640,
     "close portrait of a colombian man in his 50s, owner of a family manufacturing "
     "business, casual shirt, honest direct gaze, workshop softly blurred behind, "
     + STYLE),
    ("tst-3", 640, 640,
     "close portrait of a young colombian woman in her late 20s, startup founder, casual "
     "knit sweater, bright optimistic expression, coworking space blurred, " + STYLE),

    # ---- diagnostico / cta ancho ----
    ("diagnostico", 1344, 768,
     "colombian accountant and a small business owner sitting side by side at a table "
     "looking at a laptop together in a bright modern office, collaborative advisory "
     "moment, coffee cups, notebook, soft daylight from a large window, " + STYLE),

    # ---- recursos / blog (3) ----
    ("post-1", 1024, 640,
     "neat stack of organized document folders and a fountain pen on a light wooden desk "
     "in a modern office, shallow depth of field, soft morning light, no people, " + STYLE),
    ("post-2", 1024, 640,
     "colombian professional woman standing at a window in an office holding a tablet, "
     "thoughtful expression looking out at bogota cityscape softly blurred, " + STYLE),
    ("post-3", 1024, 640,
     "close up of hands of a colombian accountant using a calculator next to printed "
     "documents on a clean desk, warm side light, shallow depth of field, " + STYLE),

    # ---- contacto / mapa ambiente ----
    ("contacto", 1024, 768,
     "welcoming reception area of a modern professional services office in bogota, light "
     "wooden counter, navy accent wall, plants, soft daylight, no people, no signage, "
     + STYLE),
]


def gen(item):
    name, w, h, prompt = item
    dest = os.path.join(OUT, name + ".jpg")
    if os.path.exists(dest) and os.path.getsize(dest) > 20000:
        return name, "ya existe"
    body = json.dumps({
        "prompt": prompt,
        "image_size": {"width": w, "height": h},
        "num_inference_steps": 30,
        "guidance_scale": 3.5,
        "num_images": 1,
        "enable_safety_checker": True,
        "output_format": "jpeg",
    }).encode()
    for attempt in range(3):
        try:
            req = urllib.request.Request(
                "https://fal.run/fal-ai/flux/dev", data=body,
                headers={"Authorization": "Key " + KEY,
                         "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=300) as r:
                data = json.loads(r.read())
            url = data["images"][0]["url"]
            with urllib.request.urlopen(url, timeout=180) as r, open(dest, "wb") as f:
                f.write(r.read())
            return name, "ok %d KB" % (os.path.getsize(dest) // 1024)
        except Exception as e:
            if attempt == 2:
                return name, "ERROR: %r" % e
            time.sleep(4 * (attempt + 1))


with ThreadPoolExecutor(max_workers=4) as ex:
    futs = [ex.submit(gen, it) for it in IMAGES]
    for fu in as_completed(futs):
        n, st = fu.result()
        print("[%s] %s" % (n, st), flush=True)
print("LISTO")
