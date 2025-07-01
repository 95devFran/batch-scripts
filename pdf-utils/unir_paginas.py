#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unir automáticamente todos los archivos PDF de una carpeta en un único documento.

Requisitos:
    - Python 3.x
    - pypdf (instalar con: pip install pypdf)

Autor: 95sFran (https://github.com/95devFran)
Modificado por ChatGPT para unión automática por carpeta.
"""

import os
from pypdf import PdfReader, PdfWriter

# Ruta de la carpeta que contiene los PDF a unir
carpeta_pdfs = r"RUTA/PDFs"

# Ruta de salida del PDF combinado
ruta_salida = r"RUTA/DE/SALIDA/.pdf"

# Obtener lista de archivos PDF en la carpeta, ordenados alfabéticamente
rutas_pdfs = [
    os.path.join(carpeta_pdfs, archivo)
    for archivo in sorted(os.listdir(carpeta_pdfs))
    if archivo.lower().endswith(".pdf")
]

# Verificar que se encontraron PDFs
if not rutas_pdfs:
    print("No se encontraron archivos PDF en la carpeta indicada.")
    exit(1)

# Crear el objeto escritor de PDF
pdf_writer = PdfWriter()

# Leer y agregar cada página de cada archivo PDF en orden
for ruta_pdf in rutas_pdfs:
    print(f"Añadiendo: {ruta_pdf}")
    reader = PdfReader(ruta_pdf)
    for page in reader.pages:
        pdf_writer.add_page(page)

# Guardar el PDF combinado
with open(ruta_salida, "wb") as f_out:
    pdf_writer.write(f_out)

print(f"\nPDFs unidos correctamente. Archivo guardado en:\n{ruta_salida}")
