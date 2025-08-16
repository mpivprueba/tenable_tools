"""
vulnerabilities_read_scan_results.py

Reads and displays the content of a scan export CSV (myscan.csv) from Tenable.io.
Shows a tabular view of the first rows for quick review.
"""

import csv
import os

def read_scan_results(path="myscan.csv", row_limit=10):
    """
    Reads and displays the first rows of the scan CSV file.

    Args:
        path (str): Path to the CSV file to read.
        row_limit (int): Number of rows to display (default is 10).

    Returns:
        None. Prints rows from the CSV.
    """
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return

    try:
        with open(path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            headers = next(reader, [])
            print(" | ".join(headers))
            print("-" * 80)
            for i, row in enumerate(reader):
                print(" | ".join(row))
                if i + 1 >= row_limit:
                    break
    except Exception as e:
        print(f"Error reading CSV file: {e}")
