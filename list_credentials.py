"""
list_credentials.py 

The function listar_credenciales fetches the credentials and prints a summary
including name, UUID, type, username, and privilege escalation method.

"""

from api_utils import get_headers
from config import BASE_URL
import requests

def listar_credenciales():
    """
    Retrieves and displays all registered credentials from Tenable.io.

    """

    url = f"{BASE_URL}/credentials"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        datos = response.json()
        print("Registered credentials:\n")
        for cred in datos.get("credentials", []):
            nombre = cred.get("name", "No name")
            uuid = cred.get("uuid", "No UUID")
            tipo = cred.get("type", {}).get("name", "No type")
            settings = cred.get("settings", {})
            usuario = settings.get("username", "No user")
            metodo = settings.get("elevate_privileges_with", "No escalation method")
            print(f"- {nombre} | UUID: {uuid} | Type: {tipo} | User: {usuario} | Escalation: {metodo}")
    else:
        print(f"Error listing credentials. Status code: {response.status_code}")
        print(response.text)