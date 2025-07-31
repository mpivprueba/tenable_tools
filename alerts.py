"""
alerts.py

The function alerts.critical_vulns checks for critical vulnerabilities in provided scan IDs and sends an email alert.
"""

from api_utils import get_headers
from config import BASE_URL, EMAIL_FROM, EMAIL_TO, EMAIL_SERVER, EMAIL_PORT, EMAIL_USER, EMAIL_PASS
import requests
import smtplib
from email.mime.text import MIMEText

class alerts:
    @staticmethod
    def critical_vulns(*scan_ids):
        """
        Scans provided scan IDs for critical vulnerabilities and sends an email if any are found.
        """
        found = []

        for scan_id in scan_ids:
            url = f"{BASE_URL}/scans/{scan_id}"
            response = requests.get(url, headers=get_headers())

            if response.status_code == 200:
                vulns = response.json().get("vulnerabilities", [])
                for vuln in vulns:
                    if vuln.get("severity") == "critical":
                        found.append((scan_id, vuln.get("plugin_name", "No name")))
            else:
                print(f"Error retrieving scan {scan_id}. Code: {response.status_code}")

        if found:
            body = "\n".join([f"Scan ID: {sid} - {name}" for sid, name in found])
            msg = MIMEText(body)
            msg["Subject"] = "Alerta de Vulnerabilidades Críticas"
            msg["From"] = EMAIL_FROM
            msg["To"] = EMAIL_TO

            server = smtplib.SMTP(EMAIL_SERVER, EMAIL_PORT)
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)
            server.quit()

            print("Alerta enviada por correo.")
        else:
            print("No se encontraron vulnerabilidades críticas.")