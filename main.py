import sys

def mostrar_ayuda():
    print("Uso:")
    print("  python main.py scans                 # Lista escaneos disponibles")
    print("  python main.py activos               # Lista activos detectados")
    print("  python main.py export [scan_id]      # Exporta escaneo por ID (opcional)")
    print("  python main.py schedule <scan_id>    # Programa escaneo por ID")

if len(sys.argv) < 2:
    mostrar_ayuda()
    sys.exit(1)

if sys.argv[1] == "scans":
    from lab_scan_list import mostrar_scans
    mostrar_scans()

elif sys.argv[1] == "activos":
    from lab_asset_inventory import listar_activos
    listar_activos()

elif sys.argv[1] == "export":
    from lab_vuln_export import export_vulnerabilities
    if len(sys.argv) >= 3:
        export_vulnerabilities(scan_id=int(sys.argv[2]))
    else:
        export_vulnerabilities()

elif sys.argv[1] == "schedule":
    from lab_schedule_scan import programar_scan
    if len(sys.argv) >= 3:
        programar_scan(scan_id=int(sys.argv[2]))
    else:
        print("Debes proporcionar un ID de escaneo para programar.")
else:
    mostrar_ayuda()