"""
lab_vuln_export.py

Exports completed scan results from Tenable.io in CSV format.

The export_vulnerabilities function exports scan results by a given scan ID,
or by the first completed scan if no ID is provided. It waits for the export file
to be ready and then downloads and saves it locally.
"""

from api_utils import get_scan_list
from config import BASE_URL, ACCESS_KEY, SECRET_KEY
import requests
import time

def export_vulnerabilities(scan_id=None):
    """
    Export scan results for a specified scan ID, or the first completed scan if none given.
    Saves the exported results as a CSV file.

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

    print(f">> Exporting scan ID: {scan_id}")

    # 1. Request export in CSV format
    export_url = f"{BASE_URL}/scans/{scan_id}/export"
    payload = {
        "format": "csv",
        "reportContents": {
            "csvColumns": [
                "plugin_id", "severity", "plugin_name", "host", "protocol", "port"
            ]
        }
    }

    r = requests.post(export_url, headers=headers, json=payload)
    if r.status_code != 200:
        print(f"Error initiating export: {r.status_code}")
        return

    export_id = r.json().get("file")
    if not export_id:
        print("No export file ID received.")
        return

    # 2. Wait until export is ready
    status_url = f"{BASE_URL}/scans/{scan_id}/export/{export_id}/status"
    for _ in range(15):
        r = requests.get(status_url, headers=headers)
        if r.status_code == 200 and r.json().get("status") == "ready":
            break
        time.sleep(2)
    else:
        print("Export file is not ready after waiting.")
        return

    # 3. Download the CSV file
    download_url = f"{BASE_URL}/scans/{scan_id}/export/{export_id}/download"
    r = requests.get(download_url, headers=headers)
    if r.status_code == 200:
        with open("myscan.csv", "w", encoding="utf-8") as f:
            f.write(r.text)
        print("myscan.csv exportado correctamente.")
    else:
        print(f"Error downloading CSV file: {r.status_code}")
