"""
show_type_config.py

The function `show_type_config` fetches all credential types and prints detailed
configuration info (field name, ID, required status, and possible values) for the specified type ID.

"""

from api_utils import get_headers
from config import BASE_URL
import requests

def show_type_config(type_id):
    """
    Prints expected configuration fields for a given credential type ID.

    Args:
        type_id (str): Credential type identifier.

    Returns:
        None. Prints configuration details or error messages.
    """
    url = f"{BASE_URL}/credentials/types"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        data = response.json()
        print(f"Expected configuration for type '{type_id}':\n")

        for group in data.get("credentials", []):
            for credential_type in group.get("types", []):
                if credential_type.get("id") == type_id:
                    for field in credential_type.get("configuration", []):
                        name = field.get("name", "Unnamed")
                        field_id = field.get("id")
                        required = field.get("required", False)
                        options = field.get("options") if "options" in field else "Free text"
                        print(f"- {field_id} ({name}) → {'Required' if required else 'Optional'} | Values: {options}")
                    return
        print("Type not found.")
    else:
        print(f"Error fetching types. Status code: {response.status_code}")
        print(response.text)