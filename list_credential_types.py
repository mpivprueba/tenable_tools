"""
list_credential_types.py

The function listar_tipos_credenciales retrieves the credential types data and
prints the entire JSON response for inspection.

"""

from api_utils import get_headers
from config import BASE_URL
import requests
import json

def listar_tipos_credenciales():
    """
    Retrieves all credential types from Tenable.io API and prints the full JSON response.

    Useful for inspecting the detailed structure and fields of available credential types.

    """

    url = f"{BASE_URL}/credentials/types"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        respuesta = response.json()

        # Print full response structure in a readable format
        print("Full response received:")
        print(json.dumps(respuesta, indent=4))
    else:
        print(f"Failed to retrieve credential types. Status code: {response.status_code}")
        print(response.text)