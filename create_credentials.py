"""
create_credentials.py

This module contains a function to create SSH credentials by sending a POST request
to the Tenable.io API credentials endpoint. It supports optional privilege escalation
methods and related parameters.
"""

from api_utils import get_headers  # Function to generate authenticated headers
from config import BASE_URL        # Base URL for Tenable.io API
import requests                    # HTTP client for API calls

def create_credential(name, username, password, escalation_method="Nothing", escalation_account=None, escalation_password=None, bin_directory=None):
    """
    Creates an SSH credential in Tenable.io.

    Args:
        name (str): Credential name.
        username (str): SSH username.
        password (str): SSH password.
        escalation_method (str, optional): Privilege escalation method. Defaults to "Nothing".
        escalation_account (str, optional): Account used for privilege escalation.
        escalation_password (str, optional): Password for escalation account.
        bin_directory (str, optional): Path to escalation binary.

    Returns:
        None. Prints the result of the creation operation.
    """

    # Construct API endpoint URL for credentials creation
    url = f"{BASE_URL}/credentials"

    # Define basic SSH credential settings
    settings = {
        "username": username,
        "auth_method": "password",
        "password": password,
        "port": 22,
        "elevate_privileges_with": escalation_method
    }

    # Add escalation fields if the method requires them
    if escalation_method in ["sudo", "su", "su+sudo", "dzdo", "pbrun"]:
        if escalation_account:
            settings["escalation_account"] = escalation_account
        if escalation_password:
            settings["escalation_password"] = escalation_password
        if bin_directory:
            settings["bin_directory"] = bin_directory

    # Prepare the payload with all credential data
    payload = {
        "name": name,
        "type": "SSH",
        "category": "host",
        "settings": settings
    }

    # Perform POST request to create the credential
    response = requests.post(url, headers=get_headers(), json=payload)

    # Check response status and print results
    if response.status_code in [200, 201]:
        cred_id = response.json().get("id", "N/A")
        print(f"Credential created successfully. ID: {cred_id}")
    else:
        print(f"Failed to create credential. Status code: {response.status_code}")
        print("Full server response:")
        print(response.text)