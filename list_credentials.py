from api_utils import get_headers
from config import BASE_URL
import requests

def listar_credenciales():
    url = f"{BASE_URL}/credentials"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        datos = response.json()
        print("Credenciales registradas:\n")
        for cred in datos.get("credentials", []):
            nombre = cred.get("name", "Sin nombre")
            uuid = cred.get("uuid", "Sin UUID")
            tipo = cred.get("type", {}).get("name", "Sin tipo")
            settings = cred.get("settings", {})
            usuario = settings.get("username", "Sin usuario")
            metodo = settings.get("elevate_privileges_with", "Sin método")
            print(f"- {nombre} | UUID: {uuid} | Tipo: {tipo} | Usuario: {usuario} | Elevación: {metodo}")
    else:
        print(f"Error al listar credenciales. Código: {response.status_code}")
        print(response.text)