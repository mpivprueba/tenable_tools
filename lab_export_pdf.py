"""
lab_export_pdf.py

This module allows exporting scan results in PDF format
from Tenable.io using the API.

Usage from main.py:
  python main.py export_pdf <scan_id>
"""

import time
import requests
from config import BASE_URL
from api_utils import get_headers


def export_scan_to_pdf(scan_id):
    """
    Exports a specific scan to PDF format.

    Args:
        scan_id (int): ID of the scan to export.

    Returns:
        None. Saves a PDF file to disk.
    """
    url = f"{BASE_URL}/scans/{scan_id}/export"

    # Define the payload to export in PDF format
    payload = {
        "format": "pdf",
        "chapters": "vuln_hosts_summary"
    }

    # Send export request
    response = requests.post(url, headers=get_headers(), json=payload)

    if response.status_code != 200:
        print(f"Error requesting export. Status code: {response.status_code}")
        return

    file_id = response.json()["file"]

    # Wait until the file is ready for download
    status_url = f"{url}/{file_id}/status"
    download_url = f"{url}/{file_id}/download"

    for _ in range(10):  # Maximum 10 attempts
        status_response = requests.get(status_url, headers=get_headers())
        if status_response.json().get("status") == "ready":
            break
        time.sleep(2)
    else:
        print("PDF file was not ready in time.")
        return

    # Download the file
    pdf_response = requests.get(download_url, headers=get_headers())
    if pdf_response.status_code == 200:
        filename = f"scan_{scan_id}.pdf"
        with open(filename, "wb") as f:
            f.write(pdf_response.content)
        print(f"PDF report saved as {filename}")
    else:
        print(f"Failed to download PDF. Status code: {pdf_response.status_code}")