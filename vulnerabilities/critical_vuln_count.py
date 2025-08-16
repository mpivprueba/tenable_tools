"""
critical_vuln_count.py

This script reads 'myscan.csv' and counts the number of vulnerabilities
with severity or risk marked as critical.
"""

import csv
import os

def count_critical_vulnerabilities():
    filename = "myscan.csv"
    if not os.path.exists(filename):
        print("File not found: myscan.csv")
        return

    total_critical = 0
    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                risk = row.get("Risk", "").strip().lower()
                severity = row.get("Severity", "").strip().lower()

                if "critical" in risk or severity == "4" or severity == "critical":
                    total_critical += 1

        print(f"Total critical vulnerabilities found: {total_critical}")
    except Exception as e:
        print(f"Error reading the file: {e}")