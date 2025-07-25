"""
create_credentials.py 

This module contains a function to create SSH credentials by sending a POST request
to the Tenable.io API credentials endpoint. It supports optional privilege escalation
methods and related parameters.

"""

from api_utils import get_headers  # Function to generate authenticated headers
from config import BASE_URL        # Base URL for Tenable.io API
import requests                    # HTTP client for API calls

def crear_credencial(nombre, usuario, contraseña, metodo_escalacion="Nothing", cuenta_escalacion=None, clave_escalacion=None, directorio_bin=None):
    """
    Creates an SSH credential in Tenable.io.

    Args:
        nombre (str): Credential name.
        usuario (str): SSH username.
        contraseña (str): SSH password.
        metodo_escalacion (str, optional): Privilege escalation method. Defaults to "Nothing".
        cuenta_escalacion (str, optional): Account used for privilege escalation.
        clave_escalacion (str, optional): Password for escalation account.
        directorio_bin (str, optional): Path to escalation binary.

    Returns:
        None. Prints the result of the creation operation.
    """

    # Construct API endpoint URL for credentials creation
    url = f"{BASE_URL}/credentials"

    # Define basic SSH credential settings
    settings = {
        "username": usuario,
        "auth_method": "password",
        "password": contraseña,
        "port": 22,
        "elevate_privileges_with": metodo_escalacion
    }

    # Add escalation fields if the method requires them
    if metodo_escalacion in ["sudo", "su", "su+sudo", "dzdo", "pbrun"]:
        if cuenta_escalacion:
            settings["escalation_account"] = cuenta_escalacion
        if clave_escalacion:
            settings["escalation_password"] = clave_escalacion
        if directorio_bin:
            settings["bin_directory"] = directorio_bin

    # Prepare the payload with all credential data
    payload = {
        "name": nombre,
        "type": "SSH",
        "category": "host",
        "settings": settings
    }

    # Perform POST request to create the credential
    response = requests.post(url, headers=get_headers(), json=payload)

    # Check response status and print results
    if response.status_code in [200, 201]:
        cred_id = response.json().get("id", "N/A")
        print(f"Credencial creada correctamente. ID: {cred_id}")
    else:
        print(f"Error al crear credencial. Código: {response.status_code}")
        print("Respuesta completa del servidor:")
        print(response.text)
