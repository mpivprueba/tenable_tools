from api_utils import get_headers
from config import BASE_URL
import requests

def list_templates():
    url = f"{BASE_URL}/editor/scan/templates"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        data = response.json()
        templates = data.get("templates", [])
        print("Available scan templates:\n")
        for template in templates:
            name = template.get("name", "Unnamed")
            uuid = template.get("uuid", "No UUID")
            print(f"- {name} | UUID: {uuid}")
    else:
        print(f"Error retrieving templates. Status code: {response.status_code}")
        print(response.text)