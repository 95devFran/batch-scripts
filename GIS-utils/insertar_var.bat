@echo off
setlocal enabledelayedexpansion

:: --------------------------------------------------------------
:: Descripción:
::   - Recorre todos los archivos `.js` desde la carpeta actual.
::   - Si un archivo no empieza por `var`, inserta al principio:
::         var <nombre_archivo> = 
::     convirtiéndolo en un js con la variable incluida.
::
:: Uso:
::   - Coloca este script en la carpeta raíz donde están los `.js`.
::   - Ejecuta con doble clic o desde CMD.
::
:: Precaución:
::   - El archivo se sobrescribe directamente. Haz copia si es necesario.
::
:: Autor: 95sFran
:: --------------------------------------------------------------

REM Recorre todos los archivos .js desde esta carpeta
for /R %%F in (*.js) do (
    REM Extraer nombre del archivo sin extensión
    set "filename=%%~nF"
    REM Comprobar si la primera línea empieza con "var"
    for /f "delims=" %%A in ('powershell -Command "Get-Content -TotalCount 1 -Path '%%F'"') do (
        set "firstline=%%A"
    )

    echo Procesando: %%F
    echo Primera línea: !firstline!

    echo !firstline! | findstr /b /c:"var " >nul
    if errorlevel 1 (
        echo Añadiendo 'var !filename! =' al principio
        powershell -Command ^
        "$content = Get-Content -Raw '%%F';" ^
        "$newContent = 'var !filename! = ' + $content;" ^
        "Set-Content -Encoding UTF8 '%%F' $newContent"
    ) else (
        echo Ya empieza por 'var', no se modifica.
    )
)

echo.
echo Listo.
pause
