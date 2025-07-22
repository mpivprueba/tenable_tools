from api_utils import get_headers
from config import BASE_URL
import requests

def editar_credencial(uuid, nombre=None, usuario=None, contraseña=None, metodo_escalacion=None, cuenta_escalacion=None, clave_escalacion=None, directorio_bin=None):
    url = f"{BASE_URL}/credentials/{uuid}"

    settings = {
        "auth_method": "password"  # ← obligatorio para credenciales SSH con contraseña
    }

    if usuario:
        settings["username"] = usuario
    if contraseña:
        settings["password"] = contraseña
    if metodo_escalacion:
        settings["elevate_privileges_with"] = metodo_escalacion
        if metodo_escalacion in ["sudo", "su", "su+sudo", "dzdo", "pbrun"]:
            if cuenta_escalacion:
                settings["escalation_account"] = cuenta_escalacion
            if clave_escalacion:
                settings["escalation_password"] = clave_escalacion
            if directorio_bin:
                settings["bin_directory"] = directorio_bin

    payload = {
        "settings": settings
    }

    if nombre:
        payload["name"] = nombre

    response = requests.put(url, headers=get_headers(), json=payload)

    if response.status_code == 200:
        print("Credencial actualizada correctamente.")
    else:
        print(f"Error al editar credencial. Código: {response.status_code}")
        print(response.text)