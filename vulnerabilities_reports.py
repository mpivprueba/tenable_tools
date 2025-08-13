"""
vulnerabilities_reports.py

The vulnerabilities class generates a detailed vulnerability report by scan ID and exports it to a CSV file.

"""

from api_utils import get_headers
from config import BASE_URL
import requests
import csv

class vulnerabilities:
    def report(self, *scan_ids):
        """
        Exports vulnerabilities for provided scan IDs to 'vulnerabilities_report.csv'.
        If no IDs are provided, retrieves all scans.

        Args:
            scan_ids (int): Optional list of scan IDs to report on.

        Returns:
            None. Creates a CSV file with vulnerability data.
        """
        results = []

        ids_to_use = list(scan_ids) if scan_ids else self.get_all_scan_ids()

        for scan_id in ids_to_use:
            url = f"{BASE_URL}/scans/{scan_id}"
            response = requests.get(url, headers=get_headers())

            if response.status_code == 200:
                vulns = response.json().get("vulnerabilities", [])
                for v in vulns:
                    results.append([
                        scan_id,
                        v.get("plugin_name", ""),
                        v.get("severity", ""),
                        v.get("description", "")
                    ])
            else:
                print(f"Error with scan {scan_id}")

        with open("vulnerabilities_report.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Scan ID", "Name", "Severity", "Description"])
            writer.writerows(results)

        print("Vulnerabilities report exported.")

    def get_all_scan_ids(self):
        """
        Retrieves all scan IDs available in Tenable.io.

        Returns:
            list: List of scan IDs or empty list if retrieval fails.
        """
        url = f"{BASE_URL}/scans"
        response = requests.get(url, headers=get_headers())
        if response.status_code == 200:
            return [s.get("id") for s in response.json().get("scans", [])]
        else:
            return []