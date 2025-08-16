# Scans Module - Tenable.io

## Description
The `scans` module provides functionalities for managing and interacting with Tenable.io scans.  
It allows users to list available scans, create new scans, schedule scans, and export scan results in CSV or PDF formats.

---

## Requirements
- Python 3.10+
- Libraries:
  - `requests`
  - `csv`
  - `os`
- Environment variables in `.env`:
  - `ACCESS_KEY`
  - `SECRET_KEY`
  - `BASE_URL`
  - `EMAIL_FROM`
  - `EMAIL_TO`
  - `EMAIL_SERVER`
  - `EMAIL_PORT`
  - `EMAIL_USER`
  - `EMAIL_PASS`

---

## Functions

### 1. `show_scans()`
**Description:**  
Retrieves and displays all available scans in Tenable.io.  

**Arguments:**  
- None  

**Returns:**  
- `None` (Prints scan IDs, names, and statuses to the console)  

**Example:**

from scans.list_scans import show_scans

show_scans()

# CLI Usage:

python main.py scans

### 2. create_scan_interactive()
**Description:** 
Guides the user interactively to create a new scan using a scan template.

**Arguments:**  
- None (inputs are requested interactively)

**Returns:**  
- None (Outputs scan creation confirmation and ID to the console)

**Example:**
from scans.create_scan import create_scan_interactive

create_scan_interactive()


CLI Usage:

python main.py create_scan

### 3. schedule_scan(scan_id)
**Description:** 
Schedules an existing scan to run immediately or at a specified time.

**Arguments:** 
- scan_id (int): The ID of the scan to schedule

**Returns:**  
- None (Prints confirmation of scheduled scan)

**Example:**
from scans.scans_schedule import schedule_scan

schedule_scan(scan_id=1234)

CLI Usage:
python main.py schedule 1234

### 4. list_scanners()
**Description:** 
Lists all scanners registered in Tenable.io, including name, ID, and status.

**Arguments:** 
- None

**Returns:**  
- None (Prints scanner details to console)

**Example:**

from scans.list_scanners import list_scanners

list_scanners()


CLI Usage:
python main.py list_scanners

### 5. export_scan_to_pdf(scan_id)
**Description:** 
Exports scan results to PDF format and saves it locally.

**Arguments:** 
- scan_id (int): The ID of the scan to export

**Returns:**  
- None (Saves a PDF file named scan_<scan_id>.pdf)

**Example:**
from scans.results_export_pdf import export_scan_to_pdf

export_scan_to_pdf(scan_id=1234)


CLI Usage:
python main.py export_pdf 1234


### Notes
- Always verify that the scan_id exists before scheduling or exporting a scan.
- PDF export may take several seconds; ensure the download completes before proceeding.
- Use descriptive names for scans to make identification easier in large environments.