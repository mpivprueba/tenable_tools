"""
webapp_scan.py

Creates and launches a Web Application Scan (WAS) for demo.testfire.net
using the Tenable.io API.

"""

from config import BASE_URL, ACCESS_KEY, SECRET_KEY
import requests
import json

def launch_webapp_scan():
    headers = {
        "Content-Type": "application/json",
        "X-ApiKeys": f"accessKey={ACCESS_KEY}; secretKey={SECRET_KEY};"
    }

    url = f"{BASE_URL}/was/v2/scans"

    payload = {
        "uuid": "ab4bacd8-7f3f-11eb-9439-ff49a6f4d4b9",  # WAS template UUID
        "settings": {
            "name": "Demo WAS Scan",
            "description": "Scan against demo.testfire.net using WAS template",
            "target": "http://demo.testfire.net"
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 201:
        print("Web App Scan created successfully.")
        print(f"Scan ID: {response.json().get('id')}")
    else:
        print(f"Failed to create scan: {response.status_code}")
        print(response.text)
