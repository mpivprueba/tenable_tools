"""
lab_scan_list.py

Muestra la lista de escaneos disponibles en Tenable.io, ordenados por ID.
"""

from api_utils import get_scan_list

def mostrar_scans():
    scans = get_scan_list()
    if not scans:
        print("No se encontraron escaneos.")
        return

    # Ordenar escaneos por ID ascendente
    scans_ordenados = sorted(scans, key=lambda s: s.get("id", 0))

    print("Escaneos disponibles (ordenados por ID):")
    for scan in scans_ordenados:
        scan_id = scan.get("id", "N/A")
        nombre = scan.get("name", "Sin nombre")
        estado = scan.get("status", "Desconocido")
        print(f"- ID: {scan_id} | Nombre: {nombre} | Estado: {estado}")