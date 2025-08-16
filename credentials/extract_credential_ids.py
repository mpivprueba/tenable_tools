"""
extract_credential_ids.py 

This module defines a function that fetches available credential types from the Tenable.io API
and prints their IDs along with visible names.

"""

from api_utils import get_headers  # Import function to get authentication headers
from config import BASE_URL        # Import base URL for Tenable.io API
import requests                    # HTTP client for API calls
import json                       # JSON parsing (optional, response.json() used)

def extraer_ids_de_credenciales():
    """
    Retrieves and prints valid credential type IDs and their visible names.

    Makes a GET request to the /credentials/types endpoint and outputs each
    credential type's ID and name grouped by main categories.

    Returns:
        None. Prints the list or error message.
    """

    # Construct URL for credential types endpoint
    url = f"{BASE_URL}/credentials/types"

    # Perform GET request to fetch credential types
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        datos = response.json()

        print("Available credential types (valid IDs):")

        # Iterate through each main credential group
        for grupo in datos.get("credentials", []):
            tipos = grupo.get("types", [])
            for tipo in tipos:
                tipo_id = tipo.get("id")
                tipo_nombre = tipo.get("name", "Unnamed")
                if tipo_id:
                    print(f"- {tipo_id}  (Visible name: {tipo_nombre})")
    else:
        print(f"Failed to retrieve credential types. Status code: {response.status_code}")
        print(response.text)
