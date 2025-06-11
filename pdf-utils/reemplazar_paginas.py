#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Reemplazar una página específica en un archivo PDF

Este script toma un archivo PDF original y reemplaza una página específica
(por defecto la página 4) por una nueva desde otro archivo PDF.
Ideal para actualizaciones sin rehacer todo el documento.

Requisitos:
    - Python 3.x
    - pypdf (instalar con: pip install pypdf)

Autor: 95sFran (https://github.com/95sFran)
"""

from pypdf import PdfReader, PdfWriter

# Rutas de los archivos de entrada y salida (modificar según sea necesario)
ruta_original = r"RUTA/AL/ARCHIVO/original.pdf"
ruta_pagina_nueva = r"RUTA/AL/ARCHIVO/nueva_pagina.pdf"
ruta_salida = r"RUTA/DE/SALIDA/pdf_modificado.pdf"

# Cargar los archivos PDF
original_pdf = PdfReader(ruta_original)
pagina_nueva_pdf = PdfReader(ruta_pagina_nueva)

# Crear el nuevo PDF combinando páginas
output = PdfWriter()

# Agregar las primeras 3 páginas del PDF original (índices 0–2)
for i in range(3):
    output.add_page(original_pdf.pages[i])

# Insertar la nueva página en la posición 4
output.add_page(pagina_nueva_pdf.pages[0])

# Agregar el resto de las páginas del original (desde la página 5 en adelante)
for i in range(4, len(original_pdf.pages)):
    output.add_page(original_pdf.pages[i])

# Guardar el archivo PDF resultante
with open(ruta_salida, "wb") as f:
    output.write(f)

print(f"Página 4 reemplazada correctamente. Archivo guardado en: {ruta_salida}")
