import requests
from config import ACCESS_KEY, SECRET_KEY, BASE_URL

# Genera encabezados para autenticación con Tenable.io
def get_headers():
    return {
        "X-ApiKeys": f"accessKey={ACCESS_KEY}; secretKey={SECRET_KEY};",
        "Content-Type": "application/json"
    }

# Obtiene la lista de escaneos disponibles
def get_scan_list():
    url = f"{BASE_URL}/scans"
    response = requests.get(url, headers=get_headers())
    if response.status_code == 200:
        return response.json().get("scans", [])
    else:
        raise Exception(f"Failed to retrieve scans: {response.status_code}")

# Lanza un escaneo por ID
def launch_scan(scan_id):
    url = f"{BASE_URL}/scans/{scan_id}/launch"
    response = requests.post(url, headers=get_headers())
    if response.status_code == 200:
        print(f"Scan {scan_id} launched successfully.")
    else:
        print(f"Failed to launch scan: {response.status_code}")

# Exporta resultados del escaneo en formato .nessus
def export_results(scan_id):
    url = f"{BASE_URL}/scans/{scan_id}/export"
    payload = {
    "format": "nessus",
    "chapters": "vulnerabilities"  # ← ahora como string, no lista
}
    response = requests.post(url, headers=get_headers(), json=payload)
    if response.status_code == 200:
        file_id = response.json().get("file")
        print(f"Export started. File ID: {file_id}")
        return file_id
    else:
        mensaje = response.json().get("error", "Exportación no permitida o escaneo incompleto.")
        print(f"Failed to export results: {response.status_code} – {mensaje}")
        return None