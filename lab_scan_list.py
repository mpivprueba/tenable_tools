"""
lab_scan_list.py

Displays the list of available scans in Tenable.io, sorted by scan ID.
"""

from api_utils import get_scan_list  # Import function to retrieve scan list from API

def show_scans():
    """
    Retrieves and prints the list of scans from Tenable.io sorted by ascending ID.

    If no scans are found, prints an appropriate message.
    """

    scans = get_scan_list()
    if not scans:
        print("No scans found.")
        return

    # Sort scans by their ID in ascending order
    sorted_scans = sorted(scans, key=lambda s: s.get("id", 0))

    print("Available scans (sorted by ID):")
    for scan in sorted_scans:
        scan_id = scan.get("id", "N/A")
        name = scan.get("name", "Unnamed")
        status = scan.get("status", "Unknown")
        print(f"- ID: {scan_id} | Name: {name} | Status: {status}")