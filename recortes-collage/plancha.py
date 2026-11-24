# -*- coding: utf-8 -*-
"""Plancha de recorte A4 a tamano real, con medidas leidas de los PNG finales."""
from pathlib import Path

from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

BASE = Path(__file__).resolve().parent
DPI = 300.0
PX_CM = DPI / 2.54

ELEMENTOS = [
    ("03-campanario-iglesia.png", "Campanario iglesia"),
    ("01-estatua-virgen.png", "Estatua Virgen (halo + capitel)"),
    ("02-estatua-virgen-con-columna.png", "Estatua con columna (variante)"),
    ("04-torre-kairouan.png", "Torre del fondo (Kairouan)"),
    ("05-camello.png", "Camello"),
]

medidas = {}
for archivo, _ in ELEMENTOS:
    with Image.open(BASE / archivo) as im:
        medidas[archivo] = (im.width / PX_CM, im.height / PX_CM)

c = canvas.Canvas(str(BASE / "plancha-recorte-A4-tamano-real.pdf"), pagesize=A4)
W, H = A4
MARGEN = 0.7
TOP = H / cm - MARGEN - 0.75

c.setTitle("Plancha de recorte a tamano real - Cuadro Raul (lienzo 65 x 81 cm)")
c.setFont("Helvetica", 6.5)
c.setFillColorRGB(0.35, 0.35, 0.35)
c.drawString(MARGEN * cm, (H / cm - 0.45) * cm,
             "PLANCHAS DE RECORTE A TAMAÑO REAL - imprimir al 100 % (sin 'ajustar a pagina') - lienzo final 65 x 81 cm")


def fmt(v):
    return f"{v:.1f}".replace(".", ",")


def coloca(archivo, x_cm, y_top_cm, etiqueta):
    ancho, alto = medidas[archivo]
    y = y_top_cm - alto
    c.drawImage(str(BASE / archivo), x_cm * cm, y * cm, width=ancho * cm, height=alto * cm, mask="auto")
    c.saveState()
    c.setStrokeColorRGB(0.65, 0.65, 0.65)
    c.setDash(2, 3)
    c.setLineWidth(0.4)
    c.roundRect((x_cm - 0.25) * cm, (y - 0.25) * cm, (ancho + 0.5) * cm, (alto + 0.5) * cm, 5)
    c.restoreState()
    c.setFont("Helvetica", 6.5)
    c.setFillColorRGB(0.25, 0.25, 0.25)
    c.drawCentredString((x_cm + ancho / 2) * cm, (y - 0.5) * cm, etiqueta)
    return y - 0.8


w_camp = medidas["03-campanario-iglesia.png"][0]
w_est = medidas["01-estatua-virgen.png"][0]
XA = MARGEN
XB = XA + w_camp + 1.0
XC = XB + w_est + 1.0

y_sig_a = coloca("03-campanario-iglesia.png", XA, TOP,
                 f"Campanario iglesia - {fmt(medidas['03-campanario-iglesia.png'][1])} x {fmt(w_camp)} cm")
coloca("01-estatua-virgen.png", XB, TOP,
       f"Estatua Virgen - {fmt(medidas['01-estatua-virgen.png'][1])} x {fmt(medidas['01-estatua-virgen.png'][0])} cm")
coloca("02-estatua-virgen-con-columna.png", XB, 16.6,
       f"Variante con columna - {fmt(medidas['02-estatua-virgen-con-columna.png'][1])} x {fmt(medidas['02-estatua-virgen-con-columna.png'][0])} cm")
coloca("04-torre-kairouan.png", XC, TOP,
       f"Torre fondo - {fmt(medidas['04-torre-kairouan.png'][1])} x {fmt(medidas['04-torre-kairouan.png'][0])} cm")
coloca("05-camello.png", XC, 16.6,
       f"Camello - {fmt(medidas['05-camello.png'][1])} x {fmt(medidas['05-camello.png'][0])} cm")

# regla de comprobacion de 10 cm
REG_Y = 1.7
c.setStrokeColorRGB(0, 0, 0)
c.setLineWidth(0.5)
c.line(XA * cm, REG_Y * cm, (XA + 10) * cm, REG_Y * cm)
for i in range(11):
    x = (XA + i) * cm
    c.line(x, REG_Y * cm, x, (REG_Y + (0.28 if i % 5 == 0 else 0.16)) * cm)
c.setFont("Helvetica", 6.5)
c.setFillColorRGB(0.25, 0.25, 0.25)
c.drawString(XA * cm, (REG_Y - 0.45) * cm,
             "Regla de control: debe medir 10 cm exactos con una regla tras imprimir al 100 %.")
c.drawString(XA * cm, (REG_Y + 0.45) * cm,
             "Sugerencia: la franja oscura de tejados y el bloque gris de la peana se recortan a mano.")

c.save()
print("PDF regenerado con medidas finales:")
for archivo, _ in ELEMENTOS:
    ancho, alto = medidas[archivo]
    print(f"  {archivo}: {alto:.1f} x {ancho:.1f} cm")
