"""
assets_reports.py

The class assets provides methods to export asset data and generate reports on untagged assets.
"""

from api_utils import get_headers
from config import BASE_URL
import requests
import csv

class assets:
    def report(self):
        """
        Exports all assets to 'assets_report.csv'.
        """
        url = f"{BASE_URL}/assets"
        response = requests.get(url, headers=get_headers())

        if response.status_code == 200:
            data = response.json().get("assets", [])
            with open("assets_report.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Nombre", "IP", "Etiquetas"])

                for item in data:
                    asset_id = item.get("id", "")
                    name = item.get("hostname", "")
                    ip = item.get("ip", "")
                    tags = ", ".join(tag.get("value", "") for tag in item.get("tags", []))
                    writer.writerow([asset_id, name, ip, tags])
            print("Reporte de activos exportado.")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    def untagged(self):
        """
        Exports assets without any tags to 'untagged_assets.csv'.
        """
        url = f"{BASE_URL}/assets"
        response = requests.get(url, headers=get_headers())

        if response.status_code == 200:
            data = response.json().get("assets", [])
            untagged = [a for a in data if not a.get("tags")]

            if not untagged:
                print("Todos los activos tienen etiquetas.")
                return

            with open("untagged_assets.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Nombre", "IP"])
                for item in untagged:
                    writer.writerow([item.get("id", ""), item.get("hostname", ""), item.get("ip", "")])
            print("Activos sin etiquetas exportados.")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)