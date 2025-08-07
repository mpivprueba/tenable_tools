"""
webapp_scan_basic.py

Crea y lanza un escaneo web básico sobre http://demo.testfire.net usando el template estándar 'webapp'.
"""

import requests
from config import BASE_URL, ACCESS_KEY, SECRET_KEY

def crear_webapp_scan_basico():
    headers = {
        "Content-Type": "application/json",
        "X-ApiKeys": f"accessKey={ACCESS_KEY}; secretKey={SECRET_KEY}"
    }

    # UUID del template "webapp"
    template_uuid = "c3cbcd46-329f-a9ed-1077-554f8c2af33d0d44f09d736969bf"

    payload = {
        "uuid": template_uuid,
        "settings": {
            "name": "Demo WebApp Scan Básico",
            "description": "Escaneo web a http://demo.testfire.net",
            "enabled": True,
            "text_targets": "http://demo.testfire.net"
        }
    }

    url = f"{BASE_URL}/scans"
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("Escaneo web básico creado exitosamente.")
        scan_id = response.json().get("scan", {}).get("id")
        print(f"Scan ID: {scan_id}")
    else:
        print(f"Error al crear el escaneo: {response.status_code}")
        print(response.text)
