"""
lab_schedule_scan.py

Provides functions to schedule and launch scans in Tenable.io using the API.

- programar_scan: Schedules a scan with a given cron-like recurrence rule.
- lanzar_scan: Launches a scan immediately.

"""

from api_utils import get_headers  # Import function to get authentication headers
from config import BASE_URL        # Import base API URL
import requests                    # HTTP client for API requests

def programar_scan(scan_id, cron_expression="FREQ=DAILY;INTERVAL=1"):
    """
    Schedules a scan in Tenable.io with a specified recurrence rule.

    Args:
        scan_id (int or str): The ID of the scan to schedule.
        cron_expression (str): Recurrence rule in RFC 5545 RRULE format (default: daily).

    Returns:
        None. Prints success or error messages.
    """

    headers = get_headers()

    # Retrieve full scan information to check if scheduling is allowed
    url_info = f"{BASE_URL}/scans/{scan_id}"
    r = requests.get(url_info, headers=headers)

    if r.status_code != 200:
        print(f"Failed to get information for scan {scan_id}. Status code: {r.status_code}")
        return

    scan_info = r.json()

    if scan_info.get("enabled") is False:
        print(f"Scan {scan_id} is disabled and cannot be launched or scheduled.")
        return

    # Check if the scan supports scheduling
    if "schedule" not in scan_info or not scan_info["schedule"]:
        print(f"Scan {scan_id} does not support scheduling. Attempting to launch immediately...")
        lanzar_scan(scan_id)
        return

    # Prepare the scheduling payload with recurrence rules
    url_schedule = f"{BASE_URL}/scans/{scan_id}/schedule"
    payload = {
        "enabled": True,
        "schedule": {
            "rrules": cron_expression
        }
    }

    response = requests.put(url_schedule, headers=headers, json=payload)

    if response.status_code == 200:
        print(f"Scan {scan_id} scheduled successfully.")
    else:
        try:
            mensaje = response.json().get("error", "Failed to set schedule.")
        except Exception:
            mensaje = "Unknown error."
        print(f"Error scheduling scan {scan_id}. Status code: {response.status_code}. Details: {mensaje}")

def lanzar_scan(scan_id):
    """
    Launches a scan immediately in Tenable.io.

    Args:
        scan_id (int or str): The ID of the scan to launch.

    Returns:
        None. Prints success or error messages.
    """

    url = f"{BASE_URL}/scans/{scan_id}/launch"
    response = requests.post(url, headers=get_headers())

    if response.status_code == 200:
        print(f"Scan {scan_id} launched successfully.")
    else:
        try:
            mensaje = response.json().get("error", "Failed to launch scan.")
        except Exception:
            mensaje = "Unknown error."
        print(f"Error launching scan {scan_id}. Status code: {response.status_code}. Details: {mensaje}")
