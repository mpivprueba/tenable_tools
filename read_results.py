"""
read_results.py

This module reads and displays the content of the myscan.csv file
exported from a Tenable.io scan. It shows a tabular view of the first rows
to facilitate quick review.

Usage from main.py:
  python main.py read_results
  
"""

import csv
import os

def read_results_csv(path="myscan.csv", row_limit=10):
    """
    Reads and displays the first rows of the myscan.csv file.

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
