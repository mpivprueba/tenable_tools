from api_utils import get_headers
from config import BASE_URL
import requests

def crear_credencial(nombre, usuario, contraseña, metodo_escalacion="Nothing", cuenta_escalacion=None, clave_escalacion=None, directorio_bin=None):
    url = f"{BASE_URL}/credentials"

    settings = {
        "username": usuario,
        "auth_method": "password",
        "password": contraseña,
        "port": 22,
        "elevate_privileges_with": metodo_escalacion
    }

    # Agregar campos según el método de escalación
    if metodo_escalacion in ["sudo", "su", "su+sudo", "dzdo", "pbrun"]:
        if cuenta_escalacion:
            settings["escalation_account"] = cuenta_escalacion
        if clave_escalacion:
            settings["escalation_password"] = clave_escalacion
        if directorio_bin:
            settings["bin_directory"] = directorio_bin

    payload = {
        "name": nombre,
        "type": "SSH",
        "category": "host",
        "settings": settings
    }

    response = requests.post(url, headers=get_headers(), json=payload)

    if response.status_code in [200, 201]:
        cred_id = response.json().get("id", "N/A")
        print(f"Credencial creada correctamente. ID: {cred_id}")
    else:
        print(f"Error al crear credencial. Código: {response.status_code}")
        print("Respuesta completa del servidor:")
        print(response.text)