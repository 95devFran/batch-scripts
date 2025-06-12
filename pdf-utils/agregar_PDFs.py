"""

Descripción: Inserta un archivo PDF como primera página de otro PDF.
Uso común: Para añadir portadas, hojas de presentación u otras páginas iniciales a documentos PDF.
"""

from PyPDF2 import PdfMerger

def insertar_pdf_primera_pagina(pdf_principal, pdf_a_insertar, archivo_salida):
    """
    Inserta un PDF como la primera página de otro PDF.

    :param pdf_principal: Ruta del PDF principal.
    :param pdf_a_insertar: Ruta del PDF que se va a insertar al principio.
    :param archivo_salida: Ruta del archivo PDF de salida.
    """
    merger = PdfMerger()

    # Añadir primero el PDF que se quiere como primera página
    merger.append(pdf_a_insertar)

    # Añadir después el PDF principal (el resto del documento)
    merger.append(pdf_principal)

    # Guardar el resultado
    merger.write(archivo_salida)
    merger.close()

    print(f"PDF actualizado con éxito: {archivo_salida}")


# 👉 Ejemplo de uso:
# Sustituye las rutas por archivos reales cuando vayas a probarlo
pdf_principal = "documento_principal.pdf"
pdf_a_insertar = "portada.pdf"
archivo_salida = "documento_con_portada.pdf"

# Ejecutar la función
insertar_pdf_primera_pagina(pdf_principal, pdf_a_insertar, archivo_salida)
