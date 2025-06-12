@echo off
setlocal enabledelayedexpansion

:: --------------------------------------------------------------
:: Descripción:
::   - Elimina todos los archivos con extensión .qmd recursivamente.
::   - Renombra archivos .geojson a .js en todas las subcarpetas.
::
:: Uso:
::   - Coloca este archivo en la carpeta raíz donde se encuentran
::     los archivos a procesar.
::   - Ejecuta con doble clic o desde la terminal de Windows.
::
:: Precaución:
::   - Esta operación es destructiva (borra archivos .qmd).
::     Se recomienda hacer una copia de seguridad en caso de querer mantenerlos.
::
:: Autor: 95devFran
:: --------------------------------------------------------------

REM Recorre todas las carpetas desde la actual
for /R %%F in (*.qmd) do (
    echo Eliminando: %%F
    del "%%F"
)

for /R %%F in (*.geojson) do (
    set "file=%%~dpnF"
    echo Renombrando: %%F → !file!.js
    ren "%%F" "*.js"
)

echo.
echo Operación completada.
pause
