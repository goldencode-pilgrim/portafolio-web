# -*- coding: utf-8 -*-
"""
Extrae los edificios del collage "Cuadro Raul", quita el fondo y los escala
a tamano real de impresion sobre un lienzo de 65 x 81 cm.

Alturas objetivo (medidas sobre el boceto 723x1280 -> lienzo 65x81 cm):
  - Estatua de la Virgen (figura con halo): ~8,5 cm  -> recorte figura+capitel = 10,7 cm
  - Estatua con columna (variante de peana):        13,4 cm
  - Campanario/iglesia gris (a su lado):            20,0 cm (incl. franja de tejados de la base)
  - Torre de ladrillo del fondo (Kairouan):         11,0 cm (con el porche de arcos de la base)
  - Camello (asoma por la derecha):                  8,0 cm

Salida: PNG a 300 DPI con fondo transparente (dpi embebido en el archivo)
        + plancha A4 en PDF a escala real (imprimir al 100 %).
"""
from pathlib import Path
import json

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from rembg import remove, new_session

BASE = Path(__file__).resolve().parent
FUENTES = BASE / "fuentes"
DPI = 300.0
PX_CM = DPI / 2.54  # 118.11 px por cm

print("Cargando modelo de recorte de fondos (u2net)...")
session = new_session("u2net")


def fill_holes(im: Image.Image) -> Image.Image:
    """Rellena agujeros internos de la mascara (p. ej. ojivas de la torre)."""
    binaria = im.split()[3].point(lambda v: 255 if v > 100 else 0)
    w, h = binaria.size
    pad = Image.new("L", (w + 2, h + 2), 0)
    pad.paste(binaria, (1, 1))
    ImageDraw.floodfill(pad, (0, 0), 128)  # inunda el exterior
    arr = np.array(pad)[1:-1, 1:-1]
    alfa = np.array(im.split()[3])
    alfa[arr == 0] = 255  # todo lo que no es exterior = objeto
    im.putalpha(Image.fromarray(alfa))
    return im


def extraer(src: str, caja, salida: str, alto_cm: float, gris: bool = False) -> dict:
    im = Image.open(FUENTES / src).convert("RGB").crop(caja)
    out = remove(im, session=session, post_process_mask=True)

    caja_alfa = out.split()[3].getbbox()
    if caja_alfa:
        out = out.crop(caja_alfa)

    dpi_efectivo = round(out.height / (alto_cm / 2.54))

    # erosiona 1 px el contorno para eliminar halos del cielo
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

    return {
        "archivo": salida,
        "ancho_cm": round(w2 / PX_CM, 1),
        "alto_cm": round(h2 / PX_CM, 1),
        "dpi_efectivo_fuente": dpi_efectivo,
    }


# (fuente, caja (x0, y0, x1, y1) en px de la foto original, archivo, alto cm, escala de grises)
TAREAS = [
    ("virgen-campanario.jpg", (40, 82, 280, 468),   "01-estatua-virgen.png",             10.7, False),
    ("virgen-campanario.jpg", (40, 82, 280, 565),   "02-estatua-virgen-con-columna.png", 13.4, False),
    ("virgen-campanario.jpg", (278, 12, 502, 772),  "03-campanario-iglesia.png",         20.0, True),
    ("torre-kairouan.jpg",    (170, 30, 505, 748),  "04-torre-kairouan.png",             11.0, False),
    ("camello.jpg",           (12, 118, 256, 478),  "05-camello.png",                     8.0, False),
]

resultados = []
for fuente, caja, salida, alto_cm, gris in TAREAS:
    print(f"Procesando {salida} ...")
    resultados.append(extraer(fuente, caja, salida, alto_cm, gris))

for r in resultados:
    print(json.dumps(r, ensure_ascii=False))

# ---------------------------------------------------------------- plancha PDF
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

por_archivo = {r["archivo"]: r for r in resultados}
ANCHO = {k: v["ancho_cm"] for k, v in por_archivo.items()}

c = canvas.Canvas(str(BASE / "plancha-recorte-A4-tamano-real.pdf"), pagesize=A4)
W, H = A4  # 21 x 29.7 cm
MARGEN = 0.7
TOP = H / cm - MARGEN - 0.55  # deja hueco para el titulo

c.setTitle("Plancha de recorte - tamano real (Cuadro Raul)")
c.setFont("Helvetica", 6.5)
c.setFillColorRGB(0.35, 0.35, 0.35)
c.drawString(MARGEN * cm, (H / cm - 0.42) * cm,
             "PLANCHAS DE RECORTE A TAMANO REAL - imprimir al 100 % (sin 'ajustar a pagina') - lienzo final 65 x 81 cm")


def coloca(archivo: str, x_cm: float, y_top_cm: float, etiqueta: str):
    ancho = ANCHO[archivo]
    alto = por_archivo[archivo]["alto_cm"]
    y = y_top_cm - alto
    c.drawImage(str(BASE / archivo), x_cm * cm, y * cm, width=ancho * cm, height=alto * cm, mask="auto")
    # caja de corte discontinua
    c.saveState()
    c.setStrokeColorRGB(0.65, 0.65, 0.65)
    c.setDash(2, 3)
    c.setLineWidth(0.4)
    c.roundRect((x_cm - 0.25) * cm, (y - 0.25) * cm, (ancho + 0.5) * cm, (alto + 0.5) * cm, 5)
    c.restoreState()
    c.setFont("Helvetica", 6.5)
    c.setFillColorRGB(0.25, 0.25, 0.25)
    c.drawCentredString((x_cm + ancho / 2) * cm, (y - 0.52) * cm, etiqueta)
    return y - 0.75  # siguiente y_top disponible


XA = MARGEN
XB = XA + ANCHO["03-campanario-iglesia.png"] + 1.0
XC = XB + ANCHO["01-estatua-virgen.png"] + 1.0

coloca("03-campanario-iglesia.png", XA, TOP, "Campanario iglesia - 20,0 x 5,9 cm aprox")
coloca("01-estatua-virgen.png", XB, TOP, "Estatua Virgen (figura+capitel) - 10,7 cm alto")
coloca("02-estatua-virgen-con-columna.png", XB, 16.6, "Variante: estatua con columna - 13,4 cm alto")
coloca("04-torre-kairouan.png", XC, TOP, "Torre fondo (Kairouan) - 11,0 cm alto")
coloca("05-camello.png", XC, 16.6, "Camello - 8,0 cm alto")

# regla de comprobacion de 10 cm (bajo el campanario, zona libre)
REG_Y = 3.6
c.setStrokeColorRGB(0, 0, 0)
c.setLineWidth(0.5)
c.line(XA * cm, REG_Y * cm, (XA + 10) * cm, REG_Y * cm)
for i in range(11):
    x = (XA + i) * cm
    c.line(x, REG_Y * cm, x, (REG_Y + (0.28 if i % 5 == 0 else 0.16)) * cm)
c.setFont("Helvetica", 6.5)
c.drawString(XA * cm, (REG_Y - 0.42) * cm, "Regla de control: 10 cm exactos tras imprimir (medela con una regla)")
c.drawString(XA * cm, (REG_Y + 0.48) * cm, "Si mide 10 cm, el resto de elementos tambien estan a tamano real.")

c.save()
print("PDF generado: plancha-recorte-A4-tamano-real.pdf")
