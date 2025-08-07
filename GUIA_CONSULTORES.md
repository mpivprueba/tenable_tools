GUÍA DE DESARROLLO Y DOCUMENTACIÓN PARA CONSULTORES – TENABLE.IO PROJECT

Este documento establece el estándar que deben seguir los desarrolladores y consultores para mantener la consistencia, calidad y funcionalidad en el proyecto Tenable.io.

------------------------------------------------------------

ESTRUCTURA DEL PROYECTO

Los scripts Python están organizados en el directorio principal tenable_tools/

tenable_tools/
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── config.py
├── api_utils.py
├── create_credentials.py
├── edit_credentials.py
├── delete_credentials.py
├── list_credentials.py
├── list_credential_names.py
├── list_credential_types.py
├── extract_credential_ids.py
├── show_type_config.py
├── create_policy.py
├── create_scan.py
├── list_templates.py
├── list_scanners.py
├── lab_asset_inventory.py
├── lab_schedule_scan.py
├── lab_scan_list.py
├── lab_vuln_export.py
├── test_auth.py

------------------------------------------------------------

NOMBRAMIENTO DE ARCHIVOS

- Usa snake_case para nombres de archivo.
- Prefijo lab_ para scripts de laboratorio.
- Sufijos descriptivos como _basic, _extended, _advanced para variantes.

Ejemplos:
- lab_webapp_scan.py
- lab_read_results.py
- lab_critical_vuln_count.py

------------------------------------------------------------

ESTÁNDARES DE COMENTARIOS Y DOCUMENTACIÓN

1. Docstring principal del archivo

Debe ir al inicio del archivo:

"""
lab_example.py

Este script permite realizar X tarea mediante la API de Tenable.io.
"""

2. Docstring por función

def nombre_funcion(param1, param2):
    """
    Explicación clara de lo que hace la función.

    Args:
        param1 (tipo): Qué representa.
        param2 (tipo): Qué representa.

    Returns:
        tipo: Qué devuelve o acción que realiza.
    """

3. Comentarios dentro del código

Usa # para aclarar bloques de código complejos:

# Esperar hasta que el archivo esté listo para descarga
for _ in range(10):
    ...

------------------------------------------------------------

INTEGRACIÓN DE NUEVAS FUNCIONALIDADES

Paso 1: Crear el nuevo archivo

- Guarda como lab_nueva_funcionalidad.py
- Usa docstrings y comentarios
- Utiliza funciones auxiliares de api_utils.py y constantes de config.py

Paso 2: Modificar main.py

Agrega el comando dentro del bloque principal:

elif command == "nombre_comando":
    from lab_nombre_funcionalidad import nombre_funcion
    nombre_funcion()

Paso 3: Registrar el comando en show_help()

def show_help():
    ...
    print("  python main.py nombre_comando              # Breve descripción de la funcionalidad")

Paso 4: Agregar al README.md

Incluye una sección como:

## Ejecutar análisis de vulnerabilidades críticas

Comando:

------------------------------------------------------------
python main.py critical_vulns_count


Este comando exporta el último escaneo y cuenta las vulnerabilidades con severidad crítica.

------------------------------------------------------------

CHECKLIST ANTES DE HACER COMMIT

- [ ] El archivo tiene docstring inicial
- [ ] Todas las funciones están documentadas
- [ ] Se agregó la funcionalidad a main.py
- [ ] El comando fue registrado en show_help()
- [ ] El README.md incluye la nueva funcionalidad
- [ ] Pruebas realizadas localmente sin errores

------------------------------------------------------------

BUENAS PRÁCTICAS

- Usar nombres descriptivos para variables y funciones.
- Validar todos los scan_id, template_uuid o credential_uuid.
- Manejar errores con bloques try/except claros.
- Evitar duplicar funciones ya existentes en api_utils.py.

------------------------------------------------------------

EJEMPLO DE NUEVA FUNCIÓN

def example_function(scan_id):
    """
    Obtiene información básica del escaneo.

    Args:
        scan_id (int): ID del escaneo.

    Returns:
        None. Muestra información por consola.
    """
    try:
        response = requests.get(...)
        if response.status_code == 200:
            print(response.json())
        else:
            print("Error:", response.status_code)
    except Exception as e:
        print("Exception:", str(e))

------------------------------------------------------------

NOTA FINAL

Todo el equipo debe seguir esta guía para asegurar compatibilidad, claridad y mantenibilidad del código. No se aprobarán contribuciones que no cumplan con este formato.



