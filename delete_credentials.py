"""
delete_credentials.py 

This module provides a function to delete a credential by its UUID
using the Tenable.io API.

"""

from api_utils import get_headers  # Import function to get authentication headers
from config import BASE_URL        # Import base URL for Tenable.io API
import requests                    # HTTP client for API calls

def eliminar_credencial(uuid):
    """
    Deletes a credential from Tenable.io by its UUID.

    Args:
        uuid (str): UUID of the credential to delete.

    Returns:
        None. Prints the result of the deletion operation.
    """

    # Construct the URL for deleting the specified credential
    url = f"{BASE_URL}/credentials/{uuid}"

    # Send DELETE request to the API
    response = requests.delete(url, headers=get_headers())

    # Check response status and print the outcome
    if response.status_code == 200:
        print(f"Credencial eliminada correctamente.")
    else:
        print(f"Error al eliminar credencial. Código: {response.status_code}")
        print(response.text)
