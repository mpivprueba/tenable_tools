# Scans Module

The `scans/` module provides functions to create, launch, monitor, and export network and web application scans using the Tenable.io API.  
It is designed to simplify the vulnerability assessment process by abstracting the complexity of direct API calls.

---

## Files in this module

- `scan_launcher.py` → Creates and launches a network vulnerability scan.  
- `scan_status.py` → Monitors the status of a scan until it completes.  
- `scan_export.py` → Exports scan results in CSV or PDF format.  
- `webapp_scan.py` → Creates and launches a Web Application Scan (WAS).  

---

## Requirements

This module depends on the following Python libraries (already included in `requirements.txt`):

bash
requests
python-dotenv

## Install them with:

pip install -r requirements.txt

### Environment variables

The module requires API credentials and configuration stored in a .env file at the project root:

ACCESS_KEY=your_access_key
SECRET_KEY=your_secret_key
BASE_URL=https://cloud.tenable.com
Usage guide

### 1. Launch a network scan
File: scan_launcher.py

from scans.scan_launcher import launch_scan

scan_id = launch_scan("My Network Scan", ["192.168.1.1", "192.168.1.2"])
print(f"Scan launched with ID: {scan_id}")

* Input: Scan name and list of target IPs.
* Output: scan_id (unique identifier in Tenable.io).

### 2. Monitor scan status
File: scan_status.py

from scans.scan_status import check_scan_status

status = check_scan_status(scan_id=1234)
print(f"Current status: {status}")

* Input: scan_id.
* Output: Current scan status (running, completed, paused).

### 3. Export scan results
File: scan_export.py

from scans.scan_export import export_scan_results

export_file = export_scan_results(scan_id=1234, format="csv")
print(f"Scan results exported to: {export_file}")
* Input: scan_id, export format (csv or pdf).
* Output: File path of exported report.

### 4. Launch a Web Application Scan (WAS)
File: webapp_scan.py

from scans.webapp_scan import launch_webapp_scan

scan_id = launch_webapp_scan("Web Scan", "http://demo.testfire.net")
print(f"Web Application Scan launched with ID: {scan_id}")
* Input: Scan name and target URL.
* Output: scan_id for the WAS.

## Example workflow

1. Launch a network scan:

scan_id = launch_scan("Office Network", ["10.0.0.1"])

2. Check the scan status:

status = check_scan_status(scan_id)

3. Export results once completed:

report = export_scan_results(scan_id, "pdf")

4. Launch a web application scan:

was_id = launch_webapp_scan("Corporate Portal", "https://intranet.company.com")

## Notes
* The module automatically handles authentication with the Tenable.io API using credentials from the .env file.

* Exported reports are saved in the exports/ directory.

* Includes error handling for common issues (invalid API keys, scan not found, etc.).

* Web Application Scans (WAS) require a Tenable.io WAS license.