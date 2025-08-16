"""
webapp_scan_basic.py

Creates and launches a basic web scan on http://demo.testfire.net using the standard 'webapp' template.

"""

import requests
from config import BASE_URL, ACCESS_KEY, SECRET_KEY

def create_basic_webapp_scan():
    headers = {
        "Content-Type": "application/json",
        "X-ApiKeys": f"accessKey={ACCESS_KEY}; secretKey={SECRET_KEY}"
    }

    # UUID of the "webapp" template
    template_uuid = "c3cbcd46-329f-a9ed-1077-554f8c2af33d0d44f09d736969bf"

    payload = {
        "uuid": template_uuid,
        "settings": {
            "name": "Demo Basic WebApp Scan",
            "description": "Web scan on http://demo.testfire.net",
            "enabled": True,
            "text_targets": "http://demo.testfire.net"
        }
    }

    url = f"{BASE_URL}/scans"
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("Basic web scan created successfully.")
        scan_id = response.json().get("scan", {}).get("id")
        print(f"Scan ID: {scan_id}")
    else:
        print(f"Failed to create scan: {response.status_code}")
        print(response.text)
