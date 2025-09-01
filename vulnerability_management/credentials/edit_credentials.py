"""
edit_credentials.py

This module provides a function to edit an existing credential by its UUID.
It sends a PUT request to the Tenable.io API, updating only the provided fields.
"""

from api_utils import get_headers  # Import function to get auth headers
from config import BASE_URL        # Import base API URL
import requests                    # HTTP client for API communication

def edit_credential(uuid, name=None, username=None, password=None, escalation_method=None, escalation_account=None, escalation_password=None, bin_directory=None):
    """
    Updates an existing SSH credential in Tenable.io.

    Args:
        uuid (str): UUID of the credential to update.
        name (str, optional): New name for the credential.
        username (str, optional): SSH username.
        password (str, optional): SSH password.
        escalation_method (str, optional): Privilege escalation method.
        escalation_account (str, optional): Escalation account.
        escalation_password (str, optional): Escalation password.
        bin_directory (str, optional): Binary directory for escalation.

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
    if username:
        settings["username"] = username
    if password:
        settings["password"] = password
    if escalation_method:
        settings["elevate_privileges_with"] = escalation_method
        # Add escalation details if applicable
        if escalation_method in ["sudo", "su", "su+sudo", "dzdo", "pbrun"]:
            if escalation_account:
                settings["escalation_account"] = escalation_account
            if escalation_password:
                settings["escalation_password"] = escalation_password
            if bin_directory:
                settings["bin_directory"] = bin_directory

    # Prepare payload with settings and optional new name
    payload = {
        "settings": settings
    }

    if name:
        payload["name"] = name

    # Send PUT request to update the credential
    response = requests.put(url, headers=get_headers(), json=payload)

    # Handle response
    if response.status_code == 200:
        print("Credential updated successfully.")
    else:
        print(f"Failed to edit credential. Status code: {response.status_code}")
        print(response.text)
