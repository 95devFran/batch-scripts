#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Extraer páginas específicas de un PDF

Este script permite extraer un rango o páginas específicas de un archivo PDF
y guardar esas páginas en un nuevo PDF.

Requisitos:
 - Python 3.x
 - pypdf (pip install pypdf)

Uso:
 - Modifica las variables `ruta_pdf_entrada`, `paginas_a_extraer` y `ruta_pdf_salida`.
"""

from pypdf import PdfReader, PdfWriter

# Ruta del PDF de entrada
ruta_pdf_entrada = "ruta/a/tu/archivo.pdf"

# Lista de páginas a extraer (empezando en 1, ej: [1, 3, 5] o un rango)
paginas_a_extraer = [1, 2, 3]  # páginas 1, 2 y 3

# Ruta del PDF resultante
ruta_pdf_salida = "ruta/a/tu/archivo_extraido.pdf"

# Leer el PDF de entrada
reader = PdfReader(ruta_pdf_entrada)
writer = PdfWriter()

# Agregar las páginas indicadas
for num_pagina in paginas_a_extraer:
    # Restar 1 porque las páginas en pypdf son 0-indexadas
    writer.add_page(reader.pages[num_pagina - 1])

# Guardar el nuevo PDF con las páginas extraídas
with open(ruta_pdf_salida, "wb") as f_out:
    writer.write(f_out)

print(f"Páginas {paginas_a_extraer} extraídas correctamente a {ruta_pdf_salida}")
