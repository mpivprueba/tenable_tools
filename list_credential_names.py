from api_utils import get_headers
from config import BASE_URL
import requests
import json

def listar_nombres_tipos():
    url = f"{BASE_URL}/credentials/types"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        respuesta = response.json()
        print("Respuesta completa recibida desde la API:")
        print(json.dumps(respuesta, indent=4))
    else:
        print(f"No se pudieron obtener los tipos. Código: {response.status_code}")
        print(response.text)