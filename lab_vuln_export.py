"""
lab_vuln_export.py

Exporta resultados de escaneos finalizados en formato .nessus.
"""

from api_utils import get_scan_list, export_results
from config import BASE_URL, ACCESS_KEY, SECRET_KEY
import requests
import time

def export_vulnerabilities(scan_id=None):
    """
    Exporta los resultados del escaneo por ID (si se proporciona), o del primero finalizado.
    Guarda el archivo en formato .nessus.
    """
    headers = {
        "Content-Type": "application/json",
        "X-ApiKeys": f"accessKey={ACCESS_KEY}; secretKey={SECRET_KEY};"
    }

    if scan_id is None:
        scans = get_scan_list()
        scans_finalizados = [s for s in scans if s.get("status") == "completed"]
        if not scans_finalizados:
            print("No hay escaneos finalizados disponibles.")
            return
        scan_id = scans_finalizados[0]['id']

    print(f"Exportando escaneo ID: {scan_id}")
    export_id = export_results(scan_id)
    if not export_id:
        print("No se pudo iniciar la exportación.")
        return

    # Esperar que el archivo esté listo
    status_url = f"{BASE_URL}/scans/{scan_id}/export/{export_id}/status"
    for _ in range(15):
        r = requests.get(status_url, headers=headers)
        if r.status_code == 200 and r.json().get("status") == "ready":
            break
        time.sleep(2)
    else:
        print("El archivo aún no está listo después de esperar.")
        return

    # Descargar el archivo
    download_url = f"{BASE_URL}/scans/{scan_id}/export/{export_id}/download"
    r = requests.get(download_url, headers=headers)
    if r.status_code == 200:
        contenido = r.text
        nombre_archivo = f"export_scan_{scan_id}.nessus"
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(contenido)
        print(f"Archivo guardado como {nombre_archivo}")
    else:
        print(f"Error al descargar resultados: {r.status_code}")