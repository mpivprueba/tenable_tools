from api_utils import get_headers
from config import BASE_URL
import requests

def list_scanners():
    url = f"{BASE_URL}/scanners"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        scanners = response.json().get("scanners", [])
        print("Available scanners:\n")
        for scanner in scanners:
            name = scanner.get("name", "Unnamed")
            scanner_id = scanner.get("id", "No ID")
            status = scanner.get("status", "Unknown")
            print(f"- {name} | ID: {scanner_id} | Status: {status}")
    else:
        print(f"Error retrieving scanners. Status code: {response.status_code}")
        print(response.text)