# -*- coding: utf-8 -*-
"""
Este script recorre una carpeta para localizar todos los archivos con extensión .dbf.
Por cada archivo encontrado:
    - Lo abre y lo convierte en una tabla, la cual guarda en formato excel (.xlsx) con el mismo nombre que el archivo original.
    - Todos los archivos Excel se guardan en una subcarpeta llamada 'excel' dentro de la carpeta de entrada.

Soporta caracteres especiales mediante la codificación adecuada (ej: latin1). Si da error relativo a la codificación, conviene conocer cuál usa y 
aplicarla en el 'encoding = x' de la variable "tabla".

Uso:
    - Desde la terminal: python convertir_a_excel.py
    - También puede usarse desde entornos como QGIS o VSCode con Python 3.x

Requisitos:
    - Python 3.x
    - Librerías: dbfread, pandas, openpyxl.
                |_ En caso de no tenerlas instaladas ---> pip install dbfread pandas openpyxl
"""

import os
import pandas as pd
from dbfread import DBF

# Ruta a la carpeta con los .dbf
carpeta_dbf = "K:/dbfs"

# Crear la carpeta de salida
carpeta_salida = os.path.join(carpeta_dbf, "excel_output")
os.makedirs(carpeta_salida, exist_ok=True)

# Recorrer todos los archivos .dbf
for archivo in os.listdir(carpeta_dbf):
    if archivo.lower().endswith('.dbf'):
        ruta_dbf = os.path.join(carpeta_dbf, archivo)
        nombre_base = os.path.splitext(archivo)[0]
        ruta_excel = os.path.join(carpeta_salida, f"{nombre_base}.xlsx")

        # Leer archivo DBF
        tabla = DBF(ruta_dbf, load=True, encoding='latin1')
        df = pd.DataFrame(iter(tabla))

        # Guardar como excel
        df.to_excel(ruta_excel, index=False)
        print(f"Guardado: {ruta_excel}")
