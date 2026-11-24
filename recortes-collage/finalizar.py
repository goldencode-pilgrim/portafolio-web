# -*- coding: utf-8 -*-
"""Pasada final: campanario (barra cruz + limpieza base) y camello (parche correcto)."""
from pathlib import Path
import json

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from rembg import remove, new_session

BASE = Path(__file__).resolve().parent
FUENTES = BASE / "fuentes"
DPI = 300.0
PX_CM = DPI / 2.54

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


# ---------------------------------------------------------------- 03 campanario
im = Image.open(BASE / "tmp-03a.png").convert("RGBA")
arr = np.array(im)

# 1) borrar la mancha oscura de tejado en la esquina inferior izquierda
arr[1860:, :102, 3] = 0
# 2) borrar los restos de la varilla entre la cruz y la bola del remate
arr[28:97, :, 3] = 0
im = Image.fromarray(arr)

# 3) dibujar la varilla uniendo cruz y bola con sus centros reales
a_top = np.array(im)[0:35, :, 3].astype(float)
a_ball = np.array(im)[92:128, :, 3].astype(float)
x_cross = float((np.arange(im.width) * a_top.sum(axis=0)).sum() / max(a_top.sum(), 1))
x_ball = float((np.arange(im.width) * a_ball.sum(axis=0)).sum() / max(a_ball.sum(), 1))
d = ImageDraw.Draw(im)
d.line([(x_cross, 26), (x_ball, 102)], fill=(105, 105, 105, 255), width=6)
im.save(BASE / "03-campanario-iglesia.png", dpi=(DPI, DPI))
print(json.dumps({"archivo": "03-campanario-iglesia.png", "ancho_cm": round(im.width / PX_CM, 1),
                  "alto_cm": round(im.height / PX_CM, 1),
                  "x_cruz": round(x_cross), "x_bola": round(x_ball)}, ensure_ascii=False))

# ---------------------------------------------------------------- 05 camello
src = Image.open(FUENTES / "camello.jpg").convert("RGB")
# boton del carrusel en (166,380)-(204,420); lo tapamos con pelaje de debajo
x0, y0, x1, y1, off = 166, 380, 204, 420, 46
src.paste(src.crop((x0, y0 + off, x1, y1 + off)), (x0, y0))
src = src.crop((12, 118, 227, 478))
out = remove(src, session=session, post_process_mask=True)
b = out.split()[3].getbbox()
if b:
    out = out.crop(b)
dpi_ef = round(out.height / (8.0 / 2.54))
alfa = out.split()[3].filter(ImageFilter.MinFilter(3))
out.putalpha(alfa)
out = fill_holes(out)
h2 = round(8.0 * PX_CM)
w2 = max(1, round(out.width * h2 / out.height))
out = out.resize((w2, h2), Image.LANCZOS)
out = out.filter(ImageFilter.UnsharpMask(radius=1.6, percent=60, threshold=2))
out.save(BASE / "05-camello.png", dpi=(DPI, DPI))
print(json.dumps({"archivo": "05-camello.png", "ancho_cm": round(w2 / PX_CM, 1),
                  "alto_cm": round(h2 / PX_CM, 1), "dpi_efectivo": dpi_ef}, ensure_ascii=False))
