# Main script for testing API functions

from api_utils import get_scan_list, launch_scan, export_results

# Display available scans
scans = get_scan_list()
for scan in scans:
    print(f"ID: {scan['id']} - Name: {scan['name']}")

# Launch and export first available scan
scan_id = scans[0]['id'] if scans else None
if scan_id:
    launch_scan(scan_id)
    export_results(scan_id)
else:
    print("No scans available.")