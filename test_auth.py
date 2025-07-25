"""
test_auth.py - Simple script to fetch and print the list of scans from the Tenable.io API.

It uses API keys and base URL from configuration and sends an authenticated GET request
to retrieve scan data, then prints the HTTP status code and response body.


"""

import requests
from config import ACCESS_KEY, SECRET_KEY, BASE_URL

# Prepare HTTP headers with API authentication keys
headers = {
    "X-ApiKeys": f"accessKey={ACCESS_KEY}; secretKey={SECRET_KEY};",
    "Content-Type": "application/json"
}

# Endpoint URL for retrieving scans
url = f"{BASE_URL}/scans"

# Perform the GET request to fetch scans
response = requests.get(url, headers=headers)

# Output the status code and raw response text
print("Status Code:", response.status_code)
print("Response Body:", response.text)