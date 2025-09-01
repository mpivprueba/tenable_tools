"""
list_assets.py

Queries the registered assets in Tenable.io and securely displays their hostnames and IP addresses.
"""

import requests
from config import BASE_URL
from api_utils import get_headers


def list_assets():
    """
    Retrieves assets from Tenable.io and prints their hostnames and IP addresses.

    Returns:
        list: A list of asset dictionaries returned by the API, or an empty list if the request failed.
    """
    url = f"{BASE_URL}/assets"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        assets = response.json().get("assets", [])
        for asset in assets:
            # Process hostname safely
            raw_name = asset.get("hostname")
            if isinstance(raw_name, list):
                name = ", ".join(str(n) for n in raw_name)
            elif isinstance(raw_name, str):
                name = raw_name
            else:
                name = "Unnamed"

            # Process IPv4 addresses safely
            raw_ips = asset.get("ipv4", [])
            if isinstance(raw_ips, list):
                ip_text = ", ".join(str(ip) for ip in raw_ips)
            elif isinstance(raw_ips, str):
                ip_text = raw_ips
            else:
                ip_text = "Unavailable"

            # Print formatted asset information
            print(f"{name:<30} | IP: {ip_text}")
        return assets
    else:
        print(f"Failed to retrieve assets: {response.status_code}")
        return []
