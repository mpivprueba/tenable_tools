"""
create_policy.py 

This module provides a function to create a scan policy in Tenable.io using a scan template UUID.
It supports setting targets and optional credentials for authenticated scanning.

"""

from api_utils import get_headers  # Import function to get authentication headers
from config import BASE_URL        # Import base URL for Tenable.io API
import requests                    # HTTP client for API requests

def create_policy(name, template_uuid, targets="", credentials_uuid=None):
    """
    Creates a new scan policy in Tenable.io.

    Args:
        name (str): Name of the new policy.
        template_uuid (str): UUID of the scan template to base the policy on.
        targets (str, optional): Comma-separated list of target IPs or hostnames. Defaults to empty string.
        credentials_uuid (str, optional): UUID of credentials to attach to the policy.

    Returns:
        None. Prints the result of the creation operation.
    """

    # Construct the API URL for creating/editing scans/policies
    url = f"{BASE_URL}/editor/scan"

    # Build the settings dictionary for the policy configuration
    settings = {
        "name": name,
        "enabled": True,
        "launch": "ON_DEMAND",       # Scan runs on demand, not scheduled
        "scanner_id": "1",           # Default scanner ID in Tenable.io
        "policy_id": "",             # Leave empty to use the template_uuid directly
        "text_targets": targets,     # Targets to scan
        "target_network_uuid": "",   # Optional segmentation UUID, empty if unused
        "description": f"Policy created via API for {name}"
    }

    # Attach credentials if provided
    if credentials_uuid:
        settings["credentials"] = {
            "host": {
                "SSH": {
                    "id": credentials_uuid
                }
            }
        }

    # Complete payload including the template UUID and settings
    payload = {
        "uuid": template_uuid,
        "settings": settings
    }

    # Send POST request to create the policy
    response = requests.post(url, headers=get_headers(), json=payload)

    # Handle the API response
    if response.status_code in [200, 201]:
        policy_uuid = response.json().get("uuid", "N/A")
        print(f"Policy created successfully. UUID: {policy_uuid}")
    elif response.status_code == 403:
        print("Forbidden: Your API key may lack permission to create policies.")
        print("Check if your user role is Administrator and that your API scope includes write access.")
    else:
        print(f"Error creating policy. Status code: {response.status_code}")
        print(response.text)
