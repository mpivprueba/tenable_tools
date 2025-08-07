"""
lab_export_pdf.py

Este módulo permite exportar los resultados de un escaneo en formato PDF
desde Tenable.io utilizando la API.

Uso desde main.py:
  python main.py export_pdf <scan_id>
"""

import time
import requests
from config import BASE_URL
from api_utils import get_headers


def export_scan_to_pdf(scan_id):
    """
    Exporta un escaneo específico a formato PDF.

    Args:
        scan_id (int): ID del escaneo que se desea exportar.

    Returns:
        None. Guarda un archivo PDF en disco.
    """
    url = f"{BASE_URL}/scans/{scan_id}/export"

    # Definir el payload para exportar en formato PDF
    payload = {
        "format": "pdf",
        "chapters": "vuln_hosts_summary"
    }

    # Enviar solicitud de exportación
    response = requests.post(url, headers=get_headers(), json=payload)

    if response.status_code != 200:
        print(f"Error al solicitar la exportación. Código: {response.status_code}")
        return

    file_id = response.json()["file"]

    # Esperar hasta que el archivo esté listo para ser descargado
    status_url = f"{url}/{file_id}/status"
    download_url = f"{url}/{file_id}/download"

    for _ in range(10):  # Máximo 10 intentos
        status_response = requests.get(status_url, headers=get_headers())
        if status_response.json().get("status") == "ready":
            break
        time.sleep(2)
    else:
        print("El archivo PDF no estuvo listo a tiempo.")
        return

    # Descargar el archivo
    pdf_response = requests.get(download_url, headers=get_headers())
    if pdf_response.status_code == 200:
        filename = f"scan_{scan_id}.pdf"
        with open(filename, "wb") as f:
            f.write(pdf_response.content)
        print(f"Reporte PDF guardado como {filename}")
    else:
        print(f"No se pudo descargar el PDF. Código: {pdf_response.status_code}")
