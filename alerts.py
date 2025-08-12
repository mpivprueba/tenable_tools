"""
alerts.py

Provides alerting functionality for Tenable.io scans.
Checks for critical vulnerabilities in one or more scans and sends an email alert.
"""
from api_utils import get_headers
from config import (BASE_URL, EMAIL_FROM, EMAIL_TO, EMAIL_SERVER, EMAIL_PORT, EMAIL_USER, EMAIL_PASS)
import requests
import smtplib
from email.mime.text import MIMEText


class Alerts:
    @staticmethod
    def critical_vulns(*scan_ids):
        """
        Checks provided scan IDs for critical vulnerabilities and sends an email if any are found.

        Args:
            *scan_ids: One or more scan IDs to check.

        Returns:
            None. Prints results and sends email if vulnerabilities are found.
        """
        if not scan_ids:
            print("No scan IDs provided.")
            return

        found = []

        for scan_id in scan_ids:
            url = f"{BASE_URL}/scans/{scan_id}"
            try:
                response = requests.get(url, headers=get_headers(), timeout=15)
            except requests.RequestException as e:
                print(f"Error connecting to Tenable.io for scan {scan_id}: {e}")
                continue

            if response.status_code == 200:
                scan_data = response.json()
                vulns = scan_data.get("vulnerabilities", [])
                
                for vuln in vulns:
                    # Tenable uses severity as integer: 0=Info, 1=Low, 2=Medium, 3=High, 4=Critical
                    if vuln.get("severity") == 4:
                        found.append((scan_id, vuln.get("plugin_name", "No name")))
            else:
                print(f"Error retrieving scan {scan_id}. Code: {response.status_code}")
                continue

        if found:
            body = "\n".join([f"Scan ID: {sid} - {name}" for sid, name in found])
            msg = MIMEText(body, "plain", "utf-8")
            msg["Subject"] = "Critical Vulnerability Alert"
            msg["From"] = EMAIL_FROM
            msg["To"] = EMAIL_TO

            try:
                with smtplib.SMTP(EMAIL_SERVER, EMAIL_PORT) as server:
                    server.starttls()
                    server.login(EMAIL_USER, EMAIL_PASS)
                    server.send_message(msg)
                print("Alert sent successfully by email.")
            except Exception as e:
                print(f"Failed to send email alert: {e}")
        else:
            print("No critical vulnerabilities found.")
