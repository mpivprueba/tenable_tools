"""
tags.py

La clase 'tags' extrae información de etiquetas desde los activos y genera un resumen exportable.
"""

from api_utils import get_headers
from config import BASE_URL
import requests
import csv

class tags:
    def summary(self):
        """
        Resume las etiquetas detectadas en los activos y exporta el resultado a 'tag_summary.csv'.
        También crea 'untagged_assets.csv' para listar activos sin etiquetas.
        """
        url = f"{BASE_URL}/assets"
        response = requests.get(url, headers=get_headers())

        if response.status_code == 200:
            assets = response.json().get("assets", [])
            print("Cantidad de activos recibidos:", len(assets))

            tag_counts = {}
            untagged_assets = []

            for a in assets:
                asset_id = a.get("id", "Sin ID")
                asset_name = a.get("name", "Sin nombre")
                asset_ip = a.get("ipv4", "") or a.get("ipv6", "") or ""
                tags_list = a.get("tags", [])

                print(f"Activo {asset_id} tiene {len(tags_list)} etiquetas")

                if not tags_list:
                    untagged_assets.append([asset_id, asset_name, asset_ip])

                for t in tags_list:
                    value = t.get("value", "Sin etiqueta")
                    tag_counts[value] = tag_counts.get(value, 0) + 1

            # Exportar resumen de etiquetas
            with open("tag_summary.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Etiqueta", "Cantidad"])
                for tag, count in tag_counts.items():
                    writer.writerow([tag, count])
            print("Resumen de etiquetas exportado en 'tag_summary.csv'")

            # Exportar activos sin etiquetas
            with open("untagged_assets.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Nombre", "IP"])
                for asset in untagged_assets:
                    writer.writerow(asset)
            print("Activos sin etiquetas exportados en 'untagged_assets.csv'")

            # Imprimir en consola
            if tag_counts:
                print("\nResumen en consola:")
                for tag, count in tag_counts.items():
                    print(f"{tag}: {count}")
            else:
                print("No se detectaron etiquetas en los activos.")
        else:
            print(f"Error al obtener activos: {response.status_code}")