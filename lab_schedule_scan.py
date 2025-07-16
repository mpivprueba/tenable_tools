from api_utils import get_headers
from config import BASE_URL
import requests

def programar_scan(scan_id, cron_expression="FREQ=DAILY;INTERVAL=1"):
    headers = get_headers()

    # Consultar información completa del escaneo
    url_info = f"{BASE_URL}/scans/{scan_id}"
    r = requests.get(url_info, headers=headers)

    if r.status_code != 200:
        print(f"No se pudo obtener información del escaneo {scan_id}. Código: {r.status_code}")
        return

    scan_info = r.json()

    if scan_info.get("enabled") is False:
        print(f"El escaneo {scan_id} está deshabilitado y no se puede lanzar ni programar.")
        return

    if "schedule" not in scan_info or not scan_info["schedule"]:
        print(f"El escaneo {scan_id} no admite programación. Intentando lanzar directamente...")
        lanzar_scan(scan_id)
        return

    url_schedule = f"{BASE_URL}/scans/{scan_id}/schedule"
    payload = {
        "enabled": True,
        "schedule": {
            "rrules": cron_expression
        }
    }

    response = requests.put(url_schedule, headers=headers, json=payload)

    if response.status_code == 200:
        print(f"Escaneo {scan_id} programado correctamente.")
    else:
        try:
            mensaje = response.json().get("error", "No se pudo configurar la programación.")
        except Exception:
            mensaje = "Error desconocido."
        print(f"Error al programar escaneo {scan_id}. Código: {response.status_code}. Detalle: {mensaje}")

def lanzar_scan(scan_id):
    url = f"{BASE_URL}/scans/{scan_id}/launch"
    response = requests.post(url, headers=get_headers())

    if response.status_code == 200:
        print(f"Escaneo {scan_id} lanzado correctamente.")
    else:
        try:
            mensaje = response.json().get("error", "No se pudo lanzar el escaneo.")
        except Exception:
            mensaje = "Error desconocido."
        print(f"Error al lanzar escaneo {scan_id}. Código: {response.status_code}. Detalle: {mensaje}")