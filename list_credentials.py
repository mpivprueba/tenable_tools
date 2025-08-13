"""
list_credentials.py

The function list_credentials fetches the credentials and prints a summary
including name, UUID, type, username, and privilege escalation method.
"""

from api_utils import get_headers
from config import BASE_URL
import requests

def list_credentials():
    """
    Retrieves and displays all registered credentials from Tenable.io.
    """

    url = f"{BASE_URL}/credentials"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        data = response.json()
        print("Registered credentials:\n")
        for cred in data.get("credentials", []):
            name = cred.get("name", "No name")
            uuid = cred.get("uuid", "No UUID")
            type_ = cred.get("type", {}).get("name", "No type")
            settings = cred.get("settings", {})
            username = settings.get("username", "No user")
            escalation = settings.get("elevate_privileges_with", "No escalation method")
            print(f"- {name} | UUID: {uuid} | Type: {type_} | User: {username} | Escalation: {escalation}")
    else:
        print(f"Error listing credentials. Status code: {response.status_code}")
        print(response.text)