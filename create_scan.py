from api_utils import get_headers
from config import BASE_URL
import requests

def create_scan_interactive():
    print("\n=== Create New Scan ===")
    name = input("Scan name: ").strip()
    template_uuid = input("Template UUID: ").strip()
    targets = input("Targets (comma-separated IPs or domains): ").strip()
    credentials_uuid = input("Credential UUID (leave blank if none): ").strip()
    scanner_id = input("Scanner ID (e.g. 641464): ").strip()

    settings = {
        "name": name,
        "enabled": True,
        "launch": "ON_DEMAND",
        "scanner_id": int(scanner_id),
        "text_targets": targets,
        "uuid": template_uuid
    }

    if credentials_uuid:
        settings["credentials"] = {
            "host": {
                "SSH": {
                    "id": credentials_uuid
                }
            }
        }

    payload = {
        "uuid": template_uuid,
        "settings": settings
    }

    url = f"{BASE_URL}/scans"
    response = requests.post(url, headers=get_headers(), json=payload)

    if response.status_code in [200, 201]:
        scan_id = response.json().get("scan", {}).get("id", "N/A")
        print(f"\nScan created successfully. ID: {scan_id}")
    else:
        print(f"\nError creating scan. Status code: {response.status_code}")
        print(response.text)