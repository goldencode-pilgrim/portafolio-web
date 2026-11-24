# -*- coding: utf-8 -*-
"""Segunda pasada: corrige halo, cruz, base del campanario y el boton del camello."""
from pathlib import Path
import json
import shutil

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from rembg import remove, new_session

BASE = Path(__file__).resolve().parent
FUENTES = BASE / "fuentes"
DPI = 300.0
PX_CM = DPI / 2.54

print("Cargando modelo u2net...")
session = new_session("u2net")


def fill_holes(im: Image.Image) -> Image.Image:
    binaria = im.split()[3].point(lambda v: 255 if v > 100 else 0)
    w, h = binaria.size
    pad = Image.new("L", (w + 2, h + 2), 0)
    pad.paste(binaria, (1, 1))
    ImageDraw.floodfill(pad, (0, 0), 128)
    arr = np.array(pad)[1:-1, 1:-1]
    alfa = np.array(im.split()[3])
    alfa[arr == 0] = 255
    im.putalpha(Image.fromarray(alfa))
    return im


def extraer(src, caja, salida, alto_cm, gris=False, erosion=True, parche=None):
    im = Image.open(FUENTES / src).convert("RGB")
    if parche:  # (x0,y0,x1,y1, desplazamiento_y) clona la franja de abajo encima
        x0, y0, x1, y1, off = parche
        im.paste(im.crop((x0, y0 + off, x1, y1 + off)), (x0, y0))
    im = im.crop(caja)
    out = remove(im, session=session, post_process_mask=True)
    b = out.split()[3].getbbox()
    if b:
        out = out.crop(b)
    dpi_ef = round(out.height / (alto_cm / 2.54))
    if erosion:
        alfa = out.split()[3].filter(ImageFilter.MinFilter(3))
        out.putalpha(alfa)
    out = fill_holes(out)
    if gris:
        out = out.convert("LA").convert("RGBA")
    h2 = round(alto_cm * PX_CM)
    w2 = max(1, round(out.width * h2 / out.height))
    out = out.resize((w2, h2), Image.LANCZOS)
    out = out.filter(ImageFilter.UnsharpMask(radius=1.6, percent=60, threshold=2))
    out.save(BASE / salida, dpi=(DPI, DPI))
    return {"archivo": salida, "ancho_cm": round(w2 / PX_CM, 1), "alto_cm": round(h2 / PX_CM, 1),
            "dpi_efectivo": dpi_ef}


# 1) Estatua con halo: recorte del archivo 02 justo bajo el capitel (conserva el halo intacto)
im02 = Image.open(BASE / "02-estatua-virgen-con-columna.png")
corte = im02.crop((0, 0, im02.width, 1250))
corte.save(BASE / "01-estatua-virgen.png", dpi=(DPI, DPI))
print(json.dumps({"archivo": "01-estatua-virgen.png", "ancho_cm": round(corte.width / PX_CM, 1),
                  "alto_cm": round(corte.height / PX_CM, 1)}, ensure_ascii=False))

# 2) Campanario: dos variantes, sin erosion para que la cruz quede unida al remate
print("Campanario variante A...")
r_a = extraer("virgen-campanario.jpg", (278, 12, 502, 688), "tmp-03a.png", 17.8, gris=True, erosion=False)
print(json.dumps(r_a, ensure_ascii=False))
print("Campanario variante B...")
r_b = extraer("virgen-campanario.jpg", (312, 12, 502, 688), "tmp-03b.png", 17.8, gris=True, erosion=False)
print(json.dumps(r_b, ensure_ascii=False))

# 3) Torre de Kairouan sin erosion (prueba para conservar el remate de la cupula)
print("Torre variante sin erosion...")
r_t = extraer("torre-kairouan.jpg", (170, 30, 505, 748), "tmp-04b.png", 11.0, erosion=False)
print(json.dumps(r_t, ensure_ascii=False))

# 4) Camello: parche sobre el boton '>' del carrusel antes de quitar el fondo
print("Camello con parche...")
r_c = extraer("camello.jpg", (12, 118, 256, 478), "05-camello.png", 8.0,
              erosion=True, parche=(198, 368, 250, 412, 46))
print(json.dumps(r_c, ensure_ascii=False))
