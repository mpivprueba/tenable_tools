# DEVELOPMENT AND DOCUMENTATION GUIDE FOR CONSULTANTS – TENABLE.IO PROJECT

This guide defines the standards developers and consultants must follow to ensure consistency, quality, and maintainability in the Tenable.io project.

---

## PROJECT STRUCTURE

All Python scripts are organized under the main `tenable_tools/` directory:


tenable_tools/
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── config.py
├── api_utils.py
├── create_credentials.py
├── edit_credentials.py
├── delete_credentials.py
├── list_credentials.py
├── list_credential_names.py
├── list_credential_types.py
├── extract_credential_ids.py
├── show_type_config.py
├── create_policy.py
├── create_scan.py
├── list_templates.py
├── list_scanners.py
├── asset_inventory.py
├── schedule_scan.py
├── scan_list.py
├── vulnerabilities.py
├── webapp_scan.py
├── read_results.py
├── critical_vuln_count.py
├── tags.py
├── export_pdf.py
├── test_auth.py

------------------------------------------------------------

## FILE NAMING CONVENTIONS

- Use **snake_case** for all file names.
- Prefix experimental or lab scripts with `lab_`.
- Use descriptive suffixes for variants: `_basic`, `_extended`, `_advanced`.

**Examples:**

- `webapp_scan.py`  
- `read_results.py`  
- `critical_vuln_count.py`  

---

## COMMENTING AND DOCUMENTATION STANDARDS

### 1. File-level docstring

At the beginning of each file:

```python
"""
read_results.py

This script reads and displays the first rows of the CSV export from a Tenable.io scan.
"""

2. Function-level docstring

def fetch_scan(scan_id, include_details=False):
    """
    Retrieves basic or detailed information about a specific scan.

    Args:
        scan_id (int): The unique ID of the scan.
        include_details (bool): If True, include detailed host and plugin information.

    Returns:
        dict: Scan information returned by the API.
    """
3. Inline comments

Use # to clarify complex or critical code blocks:

# Wait until the export file is ready for download
for _ in range(10):
    ...

------------------------------------------------------------

ADDING NEW FUNCTIONALITY

Step 1: Create a new module

Save as lab_new_feature.py (or an appropriate descriptive name).
Include file-level docstring and inline comments.
Use helper functions from api_utils.py and constants from config.py.

Step 2: Modify main.py
Add the command in the main dispatcher block:

elif command == "new_command":
    from lab_new_feature import new_function
    new_function()

Step 3: Update show_help()
Register the command and provide a brief description:

def show_help():
    ...
    print("  python main.py new_command              # Brief description of the functionality")

Step 4: Update README.md

Include a section describing the new command:

## Execute Critical Vulnerability Analysis

Command:

python main.py critical_vulns_count

Description:

This command exports the latest scan and counts vulnerabilities marked as critical.

------------------------------------------------------------

PRE-COMMIT CHECKLIST

 File contains a top-level docstring

 All functions are properly documented

 Functionality added to main.py

 Command registered in show_help()

 README.md updated with the new feature

 Successfully tested locally without errors

------------------------------------------------------------

BEST PRACTICES

-Use descriptive names for variables and functions.
-Validate all scan_id, template_uuid, and credential_uuid inputs.
-Handle errors using clear try/except blocks.
-Avoid duplicating existing functions available in api_utils.py.

------------------------------------------------------------

EXAMPLE FUNCTION

def example_function(scan_id):
    """
    Fetches basic information about a scan.

    Args:
        scan_id (int): ID of the scan.

    Returns:
        None. Outputs scan information to the console.
    """
    try:
        response = requests.get(f"{BASE_URL}/scans/{scan_id}", headers=get_headers())
        if response.status_code == 200:
            print(response.json())
        else:
            print("Error:", response.status_code)
    except Exception as e:
        print("Exception:", str(e))

------------------------------------------------------------

FINAL NOTE

All team members must follow this guide to ensure code compatibility, clarity, and maintainability. Contributions that do not comply with these standards will not be approved.



