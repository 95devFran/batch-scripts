#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unir múltiples archivos PDF en un único documento

Este script toma varias rutas de archivos PDF y los une en un solo archivo de salida,
manteniendo el orden especificado.

Requisitos:
    - Python 3.x
    - pypdf (instalar con: pip install pypdf)

Autor: 95sFran (https://github.com/95sFran)
"""

from pypdf import PdfReader, PdfWriter

# Lista de rutas de los PDFs a unir (modificar con tus propios archivos)
rutas_pdfs = [
    r"RUTA/AL/ARCHIVO/hoja1.pdf",
    r"RUTA/AL/ARCHIVO/hoja2.pdf",
    r"RUTA/AL/ARCHIVO/hoja3.pdf",
    r"RUTA/AL/ARCHIVO/hoja4.pdf"
]

# Ruta del archivo PDF de salida
ruta_salida = r"RUTA/DE/SALIDA/documento_unido.pdf"

# Crear el objeto escritor de PDF
pdf_writer = PdfWriter()

# Leer y agregar cada página de cada archivo PDF en orden
for ruta_pdf in rutas_pdfs:
    reader = PdfReader(ruta_pdf)
    for page in reader.pages:
        pdf_writer.add_page(page)

# Guardar el PDF combinado
with open(ruta_salida, "wb") as f_out:
    pdf_writer.write(f_out)

print(f"PDFs unidos correctamente. Archivo guardado en: {ruta_salida}")
