from api_utils import get_headers
from config import BASE_URL
import requests
import json

def extraer_ids_de_credenciales():
    url = f"{BASE_URL}/credentials/types"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        datos = response.json()

        print("Tipos de credenciales disponibles (IDs válidos):")

        # Recorrer cada grupo principal
        for grupo in datos.get("credentials", []):
            tipos = grupo.get("types", [])
            for tipo in tipos:
                tipo_id = tipo.get("id")
                tipo_nombre = tipo.get("name", "Sin nombre")
                if tipo_id:
                    print(f"- {tipo_id}  (Nombre visible: {tipo_nombre})")
    else:
        print(f"No se pudieron obtener los tipos. Código: {response.status_code}")
        print(response.text)