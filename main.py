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
    print("  python main.py critical_vulns <scan_id> [...]        # Send alert if critical vulnerabilities found")
    print("  python main.py generate_assets_report                # Export assets to CSV")
    print("  python main.py generate_untagged_report              # Export untagged assets")
    print("  python main.py generate_tags_summary                 # Show tags summary")
    print("  python main.py generate_vulns_report [scan_id...]    # Export vulnerability report")
    print("  python main.py export_pdf <scan_id>                  # Export scan results to PDF")
    print("  python main.py read_results                          # Read myscan.csv file")
    print("  python main.py critical_vulns_count                  # Count critical vulnerabilities")
    print("  python main.py webapp_scan                           # Launch WAS scan on demo.testfire.net")
    print("  python main.py webapp_scan_basic                     # Create basic WebApp scan on demo.testfire.net")

# Check if a command was provided
if len(sys.argv) < 2:
    show_help()
    sys.exit(1)

# Get the command from arguments
command = sys.argv[1]

# Command dispatching using if-elif structure

if command == "scans":
    from lab_scan_list import show_scans
    show_scans()

elif command == "assets":
    from lab_asset_inventory import list_assets
    list_assets()

elif command == "export":
    from lab_vuln_export import export_vulnerabilities
    # scan_id is optional
    if len(sys.argv) >= 3:
        export_vulnerabilities(scan_id=int(sys.argv[2]))
    else:
        export_vulnerabilities()

elif command == "schedule":
    from lab_schedule_scan import schedule_scan
    if len(sys.argv) >= 3:
        schedule_scan(scan_id=int(sys.argv[2]))
    else:
        print("You must provide a scan ID to schedule.")

elif command == "create_credential":
    from create_credentials import create_credential
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

        create_credential(name, user, password, method, account, elevation_password, bin_dir)
    else:
        print("Usage: create_credential <name> <user> <password> <elevation_method> [account] [elevation_password] [bin_directory]")

elif command == "edit_credential":
    from edit_credentials import edit_credential
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

        edit_credential(uuid, name, user, password, method, account, elevation_password, bin_dir)
    else:
        print("Usage: edit_credential <uuid> [name] [user] [password] [method] [account] [elevation_password] [bin_directory]")

elif command == "delete_credential":
    from delete_credentials import delete_credential
    if len(sys.argv) >= 3:
        delete_credential(sys.argv[2])
    else:
        print("Usage: delete_credential <uuid>")

elif command == "list_credentials":
    from list_credentials import list_credentials
    list_credentials()

elif command == "credential_types":
    from list_credential_types import list_credential_types
    list_credential_types()

elif command == "credential_names":
    from list_credential_names import list_credential_names
    list_credential_names()

elif command == "credential_ids":
    from extract_credential_ids import extract_credential_ids
    extract_credential_ids()

elif command == "credential_config":
    from show_type_config import show_type_config
    if len(sys.argv) >= 3:
        show_type_config(sys.argv[2])
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
    from alerts import Alerts
    if len(sys.argv) > 2:
        scan_ids = sys.argv[2:]
        Alerts.critical_vulns(*scan_ids)
    else:
        print("Usage: python main.py critical_vulns <scan_id> [scan_id...]")

elif command == "generate_assets_report":
    from assets_reports import Assets
    Assets().report()

elif command == "generate_untagged_report":
    from assets_reports import Assets
    Assets().untagged()

elif command == "generate_tags_summary":
    from tags import Tags
    Tags().summary()

elif command == "generate_vulns_report":
    from vulnerabilities_reports import Vulnerabilities
    scan_ids = [int(arg) for arg in sys.argv[2:]] if len(sys.argv) > 2 else []
    Vulnerabilities().report(*scan_ids)

elif command == "export_pdf":
    from lab_export_pdf import export_scan_to_pdf
    if len(sys.argv) >= 3:
        export_scan_to_pdf(int(sys.argv[2]))
    else:
        print("You must provide the scan_id to export to PDF.")

elif command == "read_results":
    from read_results import read_results_csv
    read_results_csv()

elif command == "critical_vulns_count":
    from critical_vuln_count import count_critical_vulnerabilities
    count_critical_vulnerabilities()

elif command == "webapp_scan":
    from webapp_scan import launch_webapp_scan
    launch_webapp_scan()

elif command == "webapp_scan_basic":
    from webapp_scan_basic import create_basic_webapp_scan
    create_basic_webapp_scan()

else:
    # Unknown command fallback
    show_help()
