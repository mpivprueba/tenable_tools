"""
main.py - Tenable.io CLI Utility

This script serves as a command-line interface (CLI) for managing and interacting
with the Tenable.io API. It provides users with access to scan, asset, credential,
and policy management features, using various subcommands.

"""

import sys

def show_help():
    """
    Display CLI usage instructions for all supported commands.
    Called when no arguments are passed or an unknown command is used.
    """
    print("Usage:")
    print("  python main.py scans                                 # List available scans")
    print("  python main.py assets                                # List detected assets")
    print("  python main.py export [scan_id]                      # Export scan by ID (optional)")
    print("  python main.py schedule <scan_id>                    # Schedule scan by ID")
    print("  python main.py create_credential <name> <user> <password> <elevation_method> [account] [elevation_password] [bin_directory]")
    print("  python main.py edit_credential <uuid> [name] [user] [password] [method] [account] [elevation_password] [bin_directory]")
    print("  python main.py delete_credential <uuid>")
    print("  python main.py list_credentials                      # Show all registered credentials")
    print("  python main.py credential_types                      # Show available credential types")
    print("  python main.py credential_names                      # List valid credential type names")
    print("  python main.py credential_ids                        # Extract valid credential type IDs")
    print("  python main.py credential_config <type>              # Show expected config for credential type")
    print("  python main.py create_policy <name> <template_uuid> [targets] [credentials_uuid]")
    print("  python main.py list_templates                        # List available scan templates")
    print("  python main.py create_scan <name> <template_uuid> <targets> [credentials_uuid]")
    print("  python main.py list_scanners                         # List available scanners")
    print("  python main.py critical_vulns <scan_id> [...]        # Enviar correo si hay vulnerabilidades críticas")
    print("  python main.py generate_assets_report                # Exporta activos en CSV")
    print("  python main.py generate_untagged_report              # Exporta activos sin etiquetas")
    print("  python main.py generate_tags_summary                 # Muestra resumen de etiquetas")
    print("  python main.py generate_vulns_report [scan_id...]    # Exporta reporte de vulnerabilidades")
    
# Check if a command was provided
if len(sys.argv) < 2:
    show_help()
    sys.exit(1)

# Get the command from arguments
command = sys.argv[1]

# Command dispatching using if-elif structure

if command == "scans":
    from lab_scan_list import mostrar_scans
    mostrar_scans()

elif command == "assets":
    from lab_asset_inventory import listar_activos
    listar_activos()

elif command == "export":
    from lab_vuln_export import export_vulnerabilities
    # scan_id is optional
    if len(sys.argv) >= 3:
        export_vulnerabilities(scan_id=int(sys.argv[2]))
    else:
        export_vulnerabilities()

elif command == "schedule":
    from lab_schedule_scan import programar_scan
    if len(sys.argv) >= 3:
        programar_scan(scan_id=int(sys.argv[2]))
    else:
        print("You must provide a scan ID to schedule.")

elif command == "create_credential":
    from create_credentials import crear_credencial
    if len(sys.argv) >= 6:
        # Required parameters
        name = sys.argv[2]
        user = sys.argv[3]
        password = sys.argv[4]
        method = sys.argv[5]
        # Optional parameters
        account = sys.argv[6] if len(sys.argv) > 6 else None
        elevation_password = sys.argv[7] if len(sys.argv) > 7 else None
        bin_dir = sys.argv[8] if len(sys.argv) > 8 else None

        crear_credencial(name, user, password, method, account, elevation_password, bin_dir)
    else:
        print("Usage: create_credential <name> <user> <password> <elevation_method> [account] [elevation_password] [bin_directory]")

elif command == "edit_credential":
    from edit_credentials import editar_credencial
    if len(sys.argv) >= 3:
        # Required parameter
        uuid = sys.argv[2]
        # Optional fields
        name = sys.argv[3] if len(sys.argv) > 3 else None
        user = sys.argv[4] if len(sys.argv) > 4 else None
        password = sys.argv[5] if len(sys.argv) > 5 else None
        method = sys.argv[6] if len(sys.argv) > 6 else None
        account = sys.argv[7] if len(sys.argv) > 7 else None
        elevation_password = sys.argv[8] if len(sys.argv) > 8 else None
        bin_dir = sys.argv[9] if len(sys.argv) > 9 else None

        editar_credencial(uuid, name, user, password, method, account, elevation_password, bin_dir)
    else:
        print("Usage: edit_credential <uuid> [name] [user] [password] [method] [account] [elevation_password] [bin_directory]")

elif command == "delete_credential":
    from delete_credentials import eliminar_credencial
    if len(sys.argv) >= 3:
        eliminar_credencial(sys.argv[2])
    else:
        print("Usage: delete_credential <uuid>")

elif command == "list_credentials":
    from list_credentials import listar_credenciales
    listar_credenciales()

elif command == "credential_types":
    from list_credential_types import listar_tipos_credenciales
    listar_tipos_credenciales()

elif command == "credential_names":
    from list_credential_names import listar_nombres_tipos
    listar_nombres_tipos()

elif command == "credential_ids":
    from extract_credential_ids import extraer_ids_de_credenciales
    extraer_ids_de_credenciales()

elif command == "credential_config":
    from show_type_config import mostrar_configuracion_tipo
    if len(sys.argv) >= 3:
        mostrar_configuracion_tipo(sys.argv[2])
    else:
        print("Usage: credential_config <type>")

elif command == "create_policy":
    from create_policy import create_policy
    if len(sys.argv) >= 4:
        name = sys.argv[2]
        template_uuid = sys.argv[3]
        # Optional arguments
        targets = sys.argv[4] if len(sys.argv) > 4 else ""
        credentials_uuid = sys.argv[5] if len(sys.argv) > 5 else None
        create_policy(name, template_uuid, targets, credentials_uuid)
    else:
        print("Usage: create_policy <name> <template_uuid> [targets] [credentials_uuid]")

elif command == "list_templates":
    from list_templates import list_templates
    list_templates()

elif command == "create_scan":
    from create_scan import create_scan_interactive
    create_scan_interactive()

elif command == "list_scanners":
    from list_scanners import list_scanners
    list_scanners()

elif command == "critical_vulns":
    from alerts import alerts
    scan_ids = [int(arg) for arg in sys.argv[2:]] if len(sys.argv) > 2 else []
    alerts.critical_vulns(*scan_ids)

elif command == "generate_assets_report":
    from assets_reports import assets
    assets().report()

elif command == "generate_untagged_report":
    from assets_reports import assets
    assets().untagged()

elif command == "generate_tags_summary":
    from tags import tags
    tags().summary()

elif command == "generate_vulns_report":
    from vulnerabilities_reports import vulnerabilities
    scan_ids = [int(arg) for arg in sys.argv[2:]] if len(sys.argv) > 2 else []
    vulnerabilities().report(*scan_ids)
else:
    # Unknown command fallback
    show_help()
