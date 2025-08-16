"""
tags.py

The 'tags' class extracts tag information from assets and generates an exportable summary.

"""

from api_utils import get_headers
from config import BASE_URL
import requests
import csv

class tags:
    def summary(self):
        """
        Summarizes detected tags on assets and exports the result to 'tag_summary.csv'.
        Also creates 'untagged_assets.csv' to list assets without tags.
        """
        url = f"{BASE_URL}/assets"
        response = requests.get(url, headers=get_headers())

        if response.status_code == 200:
            assets = response.json().get("assets", [])
            print("Number of assets received:", len(assets))

            tag_counts = {}
            untagged_assets = []

            for a in assets:
                asset_id = a.get("id", "No ID")
                asset_name = a.get("name", "No name")
                asset_ip = a.get("ipv4", "") or a.get("ipv6", "") or ""
                tags_list = a.get("tags", [])

                print(f"Asset {asset_id} has {len(tags_list)} tags")

                if not tags_list:
                    untagged_assets.append([asset_id, asset_name, asset_ip])

                for t in tags_list:
                    value = t.get("value", "No tag")
                    tag_counts[value] = tag_counts.get(value, 0) + 1

            # Export tag summary
            with open("tag_summary.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Tag", "Count"])
                for tag, count in tag_counts.items():
                    writer.writerow([tag, count])
            print("Tag summary exported to 'tag_summary.csv'")

            # Export untagged assets
            with open("untagged_assets.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "IP"])
                for asset in untagged_assets:
                    writer.writerow(asset)
            print("Untagged assets exported to 'untagged_assets.csv'")

            # Print summary in console
            if tag_counts:
                print("\nConsole summary:")
                for tag, count in tag_counts.items():
                    print(f"{tag}: {count}")
            else:
                print("No tags detected on assets.")
        else:
            print(f"Error fetching assets: {response.status_code}")
