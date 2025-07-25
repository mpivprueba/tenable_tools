"""
lab_asset_inventory.py

Queries the registered assets in Tenable.io and securely displays their hostnames and IPs.
"""

from api_utils import get_headers  # Import function to get authentication headers
from config import BASE_URL        # Import base URL for Tenable.io API
import requests                    # HTTP client for API requests

def listar_activos():
    """
    Retrieves assets from Tenable.io and prints their hostnames and IP addresses.

    Returns:
        list: A list of asset dictionaries returned by the API, or empty list if failed.
    """

    # Endpoint URL to fetch assets
    url = f"{BASE_URL}/assets"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        activos = response.json().get("assets", [])
        for a in activos:
            # Safely process hostname field, which may be list or string
            raw_nombre = a.get("hostname")
            if isinstance(raw_nombre, list):
                nombre = ", ".join(str(n) for n in raw_nombre)
            elif isinstance(raw_nombre, str):
                nombre = raw_nombre
            else:
                nombre = "Unnamed"

            # Safely process IPv4 addresses, which may be list or string
            raw_ips = a.get("ipv4", [])
            if isinstance(raw_ips, list):
                ip_texto = ", ".join(str(ip) for ip in raw_ips)
            elif isinstance(raw_ips, str):
                ip_texto = raw_ips
            else:
                ip_texto = "Unavailable"

            # Print formatted asset information
            print(f"{str(nombre):<30} | IP: {ip_texto}")
        return activos
    else:
        print(f"Failed to retrieve assets: {response.status_code}")
        return []
