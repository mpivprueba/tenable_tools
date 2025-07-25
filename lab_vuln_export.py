"""
lab_vuln_export.py

Exports completed scan results from Tenable.io in .nessus format.

The export_vulnerabilities function exports scan results by a given scan ID,
or by the first completed scan if no ID is provided. It waits for the export file
to be ready and then downloads and saves it locally.
"""

from api_utils import get_scan_list, export_results
from config import BASE_URL, ACCESS_KEY, SECRET_KEY
import requests
import time

def export_vulnerabilities(scan_id=None):
    """
    Export scan results for a specified scan ID, or the first completed scan if none given.
    Saves the exported results as a .nessus file.

    Args:
        scan_id (int or None): ID of the scan to export. Defaults to None.

    Returns:
        None. Prints status messages indicating success or failure.
    """

    headers = {
        "Content-Type": "application/json",
        "X-ApiKeys": f"accessKey={ACCESS_KEY}; secretKey={SECRET_KEY};"
    }

    # If no scan ID provided, select the first completed scan
    if scan_id is None:
        scans = get_scan_list()
        scans_finalizados = [s for s in scans if s.get("status") == "completed"]
        if not scans_finalizados:
            print("No completed scans available.")
            return
        scan_id = scans_finalizados[0]['id']

    print(f"Exporting scan ID: {scan_id}")
    export_id = export_results(scan_id)
    if not export_id:
        print("Failed to initiate export.")
        return

    # Wait for the export file to be ready (up to ~30 seconds)
    status_url = f"{BASE_URL}/scans/{scan_id}/export/{export_id}/status"
    for _ in range(15):
        r = requests.get(status_url, headers=headers)
        if r.status_code == 200 and r.json().get("status") == "ready":
            break
        time.sleep(2)
    else:
        print("Export file is not ready after waiting.")
        return

    # Download the exported file
    download_url = f"{BASE_URL}/scans/{scan_id}/export/{export_id}/download"
    r = requests.get(download_url, headers=headers)
    if r.status_code == 200:
        contenido = r.text
        nombre_archivo = f"export_scan_{scan_id}.nessus"
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(contenido)
        print(f"File saved as {nombre_archivo}")
    else:
        print(f"Error downloading results: {r.status_code}")