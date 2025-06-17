# -*- coding: utf-/ -*-
"""
Este srcipt recorre recursivamente una carpeta base para localizr archivos que contengan una palabra concreta en su nombre.
No importa si es mayúcula o minúscula. Por cada archivo encontrado extrae el nombre de carpeta donde se encuentra (hay que
designar el index que corresponde a esa carpeta) y genera una lista en un archivo txt, que guarda en la ruta de salida que 
especificamos.

Uso:
    - Desde la terminal (python <Nombre_del_script>.py) --> Recomendable
    - Desde la consola de Python en QGIS 

Requisitos:
    -Pyhton 3.x
"""

import os

# Ruta base donde buscar los archivos
ruta_base = r"ruta/a/tus/archivos"

# Ruta de salida donde se generará en txt
ruta_salida = r"ruta/de/salida"

#Para almacenar el nombre de la carpeta cuyo nombre queremos averiguar:
nombres_municipios = set()

# Recorrido recursivo de todas las carpetas y archivos
for root, dirs, files in os.walk(ruta_base):
    for file in files:
        if "cad" in file.lower():
            partes = os.path.normpath(root).split(os.sep)
            if len(partes) >= 2:
                municipio = partes[-2]  #El index que nos interese en función de la carpeta
                nombres_municipios.add(municipio)

# Escribir sobre el txt los resultados obtenidos de la búqueda
with open(ruta_salida, 'w', encoding='utf-8') as f:
    for nombre in sorted(nombres_municipios):
        f.write(nombre + '\n')

print(f"Se han guardado {len(nombres_municipios)} resultados en: {ruta_salida}")
