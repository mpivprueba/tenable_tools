"""
lab_asset_inventory.py

Consulta los activos registrados en Tenable.io y muestra hostname e IPs de forma segura.
"""

from api_utils import get_headers
from config import BASE_URL
import requests

def listar_activos():
    """
    Recupera activos desde Tenable.io y muestra hostname e IPs.
    """
    url = f"{BASE_URL}/assets"
    response = requests.get(url, headers=get_headers())

    if response.status_code == 200:
        activos = response.json().get("assets", [])
        for a in activos:
            # Procesar el hostname de forma segura
            raw_nombre = a.get("hostname")
            if isinstance(raw_nombre, list):
                nombre = ", ".join(str(n) for n in raw_nombre)
            elif isinstance(raw_nombre, str):
                nombre = raw_nombre
            else:
                nombre = "Sin nombre"

            # Procesar la IP de forma segura
            raw_ips = a.get("ipv4", [])
            if isinstance(raw_ips, list):
                ip_texto = ", ".join(str(ip) for ip in raw_ips)
            elif isinstance(raw_ips, str):
                ip_texto = raw_ips
            else:
                ip_texto = "No disponible"

            print(f"{str(nombre):<30} | IP: {ip_texto}")
        return activos
    else:
        print(f"Error al obtener activos: {response.status_code}")
        return []