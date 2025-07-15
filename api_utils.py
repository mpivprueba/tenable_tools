import requests
from config import ACCESS_KEY, SECRET_KEY, BASE_URL

# Generate request headers using access and secret keys
def get_headers():
    return {
        "X-ApiKeys": f"accessKey={ACCESS_KEY}; secretKey={SECRET_KEY};",
        "Content-Type": "application/json"
    }

# Retrieve list of available scans
def get_scan_list():
    url = f"{BASE_URL}/scans"
    response = requests.get(url, headers=get_headers())
    if response.status_code == 200:
        return response.json().get("scans", [])
    else:
        raise Exception(f"Failed to retrieve scans: {response.status_code}")

# Launch a scan using its ID
def launch_scan(scan_id):
    url = f"{BASE_URL}/scans/{scan_id}/launch"
    response = requests.post(url, headers=get_headers())
    if response.status_code == 200:
        print(f"Scan {scan_id} launched successfully.")
    else:
        print(f"Failed to launch scan: {response.status_code}")

# Export scan results in JSON format
def export_results(scan_id):
    url = f"{BASE_URL}/scans/{scan_id}/export"
    payload = {"format": "json"}
    response = requests.post(url, headers=get_headers(), json=payload)
    if response.status_code == 200:
        file_id = response.json().get("file")
        print(f"Export started. File ID: {file_id}")
        return file_id
    else:
        print(f"Failed to export results: {response.status_code}")