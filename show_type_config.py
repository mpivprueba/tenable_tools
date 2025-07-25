"""
show_type_config.py

The function `mostrar_configuracion_tipo` fetches all credential types and prints detailed
configuration info (field name, ID, required status, and possible values) for the specified type ID.

"""

from api_utils import get_headers
from config import BASE_URL
import requests
import json

def mostrar_configuracion_tipo(tipo_id):
    """
    Prints expected configuration fields for a given credential type ID.

    Returns:
        None. Prints configuration details or error messages.
    """
    url = f"{BASE_URL}/credentials/types"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        datos = response.json()
        print(f"Configuración esperada para el tipo '{tipo_id}':\n")

        for grupo in datos.get("credentials", []):
            for tipo in grupo.get("types", []):
                if tipo.get("id") == tipo_id:
                    for campo in tipo.get("configuration", []):
                        nombre = campo.get("name", "Sin nombre")
                        identificador = campo.get("id")
                        requerido = campo.get("required", False)
                        valores = campo.get("options") if "options" in campo else "Libre"
                        print(f"- {identificador} ({nombre}) → {'Requerido' if requerido else 'Opcional'} | Valores: {valores}")
                    return
        print("Tipo no encontrado.")
    else:
        print(f"Error al consultar tipos. Código: {response.status_code}")
        print(response.text)