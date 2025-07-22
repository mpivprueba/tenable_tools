from api_utils import get_headers
from config import BASE_URL
import requests

def create_policy(name, template_uuid, targets="", credentials_uuid=None):
    url = f"{BASE_URL}/editor/scan"

    settings = {
        "name": name,
        "enabled": True,
        "launch": "ON_DEMAND",
        "scanner_id": "1",  # ID por defecto del escáner en Tenable.io
        "policy_id": "",    # Se puede dejar vacío si se usa template_uuid
        "text_targets": targets,
        "target_network_uuid": "",  # Opcional, puede omitirse si no se usa segmentación
        "description": f"Policy created via API for {name}"
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

    response = requests.post(url, headers=get_headers(), json=payload)

    if response.status_code in [200, 201]:
        policy_uuid = response.json().get("uuid", "N/A")
        print(f"Policy created successfully. UUID: {policy_uuid}")
    elif response.status_code == 403:
        print("Forbidden: Your API key may lack permission to create policies.")
        print("Check if your user role is Administrator and that your API scope includes write access.")
    else:
        print(f"Error creating policy. Status code: {response.status_code}")
        print(response.text)