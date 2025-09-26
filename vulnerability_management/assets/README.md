### Assets Module

The assets/ module provides functions to list, search, and export assets from Tenable.io.
It simplifies asset inventory management by wrapping Tenable.io API calls into reusable Python functions.

---

### Files in this module

list_assets.py → Retrieves all assets from Tenable.io.

search_assets.py → Searches for assets based on filters (e.g., hostname, IP, operating system).

export_assets.py → Exports asset inventory to CSV or JSON format.

---

## Requirements

This module depends on the following Python libraries (already included in requirements.txt):

requests
python-dotenv

---

## Install them with:

pip install -r requirements.txt

### Environment variables

The module requires API credentials and configuration stored in a .env file at the project root:

ACCESS_KEY=your_access_key
SECRET_KEY=your_secret_key
BASE_URL=https://cloud.tenable.com
Usage guide

### 1. List all assets

File: list_assets.py

from assets.list_assets import list_all_assets

assets = list_all_assets()
print(assets)

* Input: None.

* Output: A list of all assets in Tenable.io (as JSON objects).

### 2. Search for assets

File: search_assets.py

from assets.search_assets import search_assets

results = search_assets(filter_key="ipv4", filter_value="192.168.1.100")
print(results)

* Input: filter_key (field to filter by, e.g., "hostname", "ipv4", "os"), and filter_value (search term).

* Output: Filtered assets matching the criteria.

### 3. Export assets to a file

File: export_assets.py

from assets.export_assets import export_assets

file_path = export_assets(format="csv")
print(f"Assets exported to: {file_path}")

* Input: Export format (csv or json).

* Output: File path of the exported asset inventory.

---

## Example workflow

1. Retrieve all assets:

assets = list_all_assets()

2. Search for a specific host:

host = search_assets("hostname", "server01.company.com")

3. Export the full inventory:

report = export_assets("csv")

---

## Notes
* All functions automatically handle authentication using credentials from the .env file.

* Exported reports are saved in the exports/ directory.

* Includes error handling for invalid filters, empty results, or invalid credentials.

* The asset inventory reflects all scanned or imported assets in Tenable.io.