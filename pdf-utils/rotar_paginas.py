#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Rotar todas las páginas de un PDF

Este script rota todas las páginas de un PDF un ángulo específico (90, 180 o 270 grados).

Requisitos:
 - Python 3.x
 - pypdf (pip install pypdf)

Uso:
 - Modifica las variables `ruta_pdf_entrada`, `grados_rotacion` y `ruta_pdf_salida`.
"""

from pypdf import PdfReader, PdfWriter

# Ruta del PDF de entrada
ruta_pdf_entrada = "ruta/a/tu/archivo.pdf"

# Ángulo de rotación (solo 90, 180 o 270)
grados_rotacion = 90

# Ruta del PDF resultante
ruta_pdf_salida = "ruta/a/tu/archivo_rotado.pdf"

reader = PdfReader(ruta_pdf_entrada)
writer = PdfWriter()

# Rotar cada página
for page in reader.pages:
    page.rotate_clockwise(grados_rotacion)
    writer.add_page(page)

# Guardar el PDF rotado
with open(ruta_pdf_salida, "wb") as f_out:
    writer.write(f_out)

print(f"Todas las páginas rotadas {grados_rotacion}° y guardadas en {ruta_pdf_salida}")
