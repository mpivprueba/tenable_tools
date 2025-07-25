"""
list_credential_names.py

The function listar_nombres_tipos sends a GET request to the credentials types endpoint
and prints the full JSON response with pretty formatting.

"""

from api_utils import get_headers
from config import BASE_URL
import requests
import json

def listar_nombres_tipos():
    """
    Fetches all credential types from Tenable.io API and prints the complete JSON response.

    This helps in understanding all available credential type names and their structure.

    """

    url = f"{BASE_URL}/credentials/types"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        respuesta = response.json()
        print("Full response received from the API:")
        print(json.dumps(respuesta, indent=4))
    else:
        print(f"Failed to retrieve credential types. Status code: {response.status_code}")
        print(response.text)
