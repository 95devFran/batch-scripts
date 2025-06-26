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
