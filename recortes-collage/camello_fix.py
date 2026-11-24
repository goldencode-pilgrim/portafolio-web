# -*- coding: utf-8 -*-
"""Camello v5: quita el boton del carrusel por inpainting y extrae con rembg."""
from pathlib import Path
import json

import cv2
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


img = cv2.imread(str(FUENTES / "camello.jpg"))  # BGR
h_img, w_img = img.shape[:2]

# mascara del boton: pixeles claros (circulo blanco) en la zona del pecho
zona = np.zeros((h_img, w_img), np.uint8)
reg = img[355:445, 155:235]
claros = (reg[:, :, 0] > 150) & (reg[:, :, 1] > 150) & (reg[:, :, 2] > 150)
zona[355:445, 155:235] = (claros * 255).astype(np.uint8)
zona = cv2.dilate(zona, np.ones((7, 7), np.uint8), iterations=1)
print("pixeles a inpintar:", int((zona > 0).sum()))

limpio = cv2.inpaint(img, zona, 5, cv2.INPAINT_TELEA)

# vista de control de la zona reparada
cv2.imwrite(str(BASE / "_control_inpaint.png"), limpio[280:470, 100:227])

src = Image.fromarray(cv2.cvtColor(limpio, cv2.COLOR_BGR2RGB))
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
