"""
create_scan.py 

This module provides a function to interactively create a new scan in Tenable.io.
It prompts the user for scan details, constructs the request payload, and sends
a POST request to the Tenable.io scans endpoint.

"""

from api_utils import get_headers  # Import function to generate auth headers
from config import BASE_URL        # Import base API URL
import requests                    # HTTP client for API communication

def create_scan_interactive():
    """
    Interactively prompts the user for scan parameters and creates a scan in Tenable.io.

    User inputs required:
        - Scan name
        - Template UUID
        - Targets (comma-separated IPs or domains)
        - Credential UUID (optional)
        - Scanner ID (numeric)

    Sends a POST request to create the scan and prints the outcome.
    """

    print("\n=== Create New Scan ===")
    name = input("Scan name: ").strip()
    template_uuid = input("Template UUID: ").strip()
    targets = input("Targets (comma-separated IPs or domains): ").strip()
    credentials_uuid = input("Credential UUID (leave blank if none): ").strip()
    scanner_id = input("Scanner ID (e.g. 641464): ").strip()

    # Build the settings dictionary for the scan
    settings = {
        "name": name,
        "enabled": True,
        "launch": "ON_DEMAND",
        "scanner_id": int(scanner_id),
        "text_targets": targets,
        "uuid": template_uuid
    }

    # Add credentials if provided
    if credentials_uuid:
        settings["credentials"] = {
            "host": {
                "SSH": {
                    "id": credentials_uuid
                }
            }
        }

    # Construct the payload for the API request
    payload = {
        "uuid": template_uuid,
        "settings": settings
    }

    # API endpoint for creating scans
    url = f"{BASE_URL}/scans"
    response = requests.post(url, headers=get_headers(), json=payload)

    # Handle API response
    if response.status_code in [200, 201]:
        scan_id = response.json().get("scan", {}).get("id", "N/A")
        print(f"\nScan created successfully. ID: {scan_id}")
    else:
        print(f"\nError creating scan. Status code: {response.status_code}")
        print(response.text)
