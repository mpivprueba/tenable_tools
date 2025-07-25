"""
edit_credentials.py

This module provides a function to edit an existing credential by its UUID.
It sends a PUT request to the Tenable.io API, updating only the provided fields.

"""

from api_utils import get_headers  # Import function to get auth headers
from config import BASE_URL        # Import base API URL
import requests                    # HTTP client for API communication

def editar_credencial(uuid, nombre=None, usuario=None, contraseña=None, metodo_escalacion=None, cuenta_escalacion=None, clave_escalacion=None, directorio_bin=None):
    """
    Updates an existing SSH credential in Tenable.io.

    Args:
        uuid (str): UUID of the credential to update.
        nombre (str, optional): New name for the credential.
        usuario (str, optional): SSH username.
        contraseña (str, optional): SSH password.
        metodo_escalacion (str, optional): Privilege escalation method.
        cuenta_escalacion (str, optional): Escalation account.
        clave_escalacion (str, optional): Escalation password.
        directorio_bin (str, optional): Binary directory for escalation.

    Returns:
        None. Prints the result of the update operation.
    """

    # Construct the URL for updating the specified credential
    url = f"{BASE_URL}/credentials/{uuid}"

    # Base settings dictionary with mandatory auth method
    settings = {
        "auth_method": "password"  # Required for SSH credentials using password
    }

    # Update fields if provided
    if usuario:
        settings["username"] = usuario
    if contraseña:
        settings["password"] = contraseña
    if metodo_escalacion:
        settings["elevate_privileges_with"] = metodo_escalacion
        # Add escalation details if applicable
        if metodo_escalacion in ["sudo", "su", "su+sudo", "dzdo", "pbrun"]:
            if cuenta_escalacion:
                settings["escalation_account"] = cuenta_escalacion
            if clave_escalacion:
                settings["escalation_password"] = clave_escalacion
            if directorio_bin:
                settings["bin_directory"] = directorio_bin

    # Prepare payload with settings and optional new name
    payload = {
        "settings": settings
    }

    if nombre:
        payload["name"] = nombre

    # Send PUT request to update the credential
    response = requests.put(url, headers=get_headers(), json=payload)

    # Handle response
    if response.status_code == 200:
        print("Credencial actualizada correctamente.")
    else:
        print(f"Error al editar credencial. Código: {response.status_code}")
        print(response.text)
