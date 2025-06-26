"""
Este script recorre una estructura de carpetas (accediendo a las distintas subcarpetas) que contiene archivos con la extensión que queremos encontrar.
Dentro de cada carpeta, busca archivos cuyo nombre:
  - Empiece por un nombre concreto, o conjunto de caracteres específico.
  - O empiece por un nombre general de interés.

Lógica:
- Si encuentra un archivo cuyo nombre coincide con el establecido por nosotros (sin importar tildes o mayúsculas), lo selecciona.
- Si no, selecciona los que empiezan por el nombre general de interés.
- Copia esos archivos (junto a sus archivos auxiliares en caso de tenerlos) en una carpeta de destino.
"""


import os
import shutil

# Rutas
ruta_directorio = "Ruta/al/directorio/archivos"
ruta_salida = "Ruta/de/salida"

# Asegurar que la carpeta de salida existe
os.makedirs(ruta_salida, exist_ok=True)

print("Iniciando copia de los archivos...\n")

# Recorremos carpetas de la ruta del directorio deseado
for archivo in os.listdir(ruta_directorio):
    carpeta_archivos = os.path.join(ruta_directorio, archivo, "ARCHIVOS")

    if not os.path.isdir(carpeta_archivos):
        continue

    print(f"Procesando municipio: {archivo}")

    contador = 1  # Para distinguir múltiples archivos por cada carpeta

    for archivos in os.listdir(carpeta_archivos):
        if archivos.startswith("NOMBRE QUE QUEREMOS") and archivos.endswith("EXTENSIÓN QUE NOS INTERESA"):
            nombre_base = f"ARCHIVO_{archivo.lower()}_{contador}"
            contador += 1

            base_sin_ext = os.path.splitext(archivos)[0]
            print(f"  ➜ Copiando {archivos} como {nombre_base}.shp")

            for ext in [".shp", ".dbf", ".shx", ".prj", ".cpg"]:
                archivo_completo = base_sin_ext + ext
                origen = os.path.join(carpeta_archivos, archivo_completo)
                if os.path.exists(origen):
                    destino = os.path.join(ruta_salida, nombre_base + ext)
                    shutil.copy2(origen, destino)

print("Proceso terminado. Todos los archivos han sido copiados.")
