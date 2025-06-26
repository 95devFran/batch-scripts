import os
import shutil

# Rutas
ruta_municipios = "P:/GRUPOS/IAA/05_I_AGUA/ABASTECIMIENTO/05XXXX_AT_SOAR_PERTE/01_AT_TTEC/0105_PLAN_GIS/010501_EN_PROCESO/MUNICIPIOS_GIS"
ruta_salida = "K:/abascos"

# Asegurar que la carpeta de salida existe
os.makedirs(ruta_salida, exist_ok=True)

print("Iniciando copia de capas ABASCO...\n")

# Recorremos carpetas de municipios
for municipio in os.listdir(ruta_municipios):
    carpeta_capas = os.path.join(ruta_municipios, municipio, "CAPAS")

    if not os.path.isdir(carpeta_capas):
        continue

    print(f"Procesando municipio: {municipio}")

    contador = 1  # Para distinguir múltiples archivos por municipio

    for archivo in os.listdir(carpeta_capas):
        if archivo.startswith("ABASCO") and archivo.endswith(".shp"):
            nombre_base = f"ABASCO_{municipio.lower()}_{contador}"
            contador += 1

            base_sin_ext = os.path.splitext(archivo)[0]
            print(f"  ➜ Copiando {archivo} como {nombre_base}.shp")

            for ext in [".shp", ".dbf", ".shx", ".prj", ".cpg"]:
                archivo_completo = base_sin_ext + ext
                origen = os.path.join(carpeta_capas, archivo_completo)
                if os.path.exists(origen):
                    destino = os.path.join(ruta_salida, nombre_base + ext)
                    shutil.copy2(origen, destino)

print("Proceso terminado. Todas las capas ABASCO han sido copiadas.")
