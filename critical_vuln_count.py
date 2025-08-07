"""
critical_vuln_count.py

This script reads 'myscan.csv' and counts the number of vulnerabilities
with severity or risk marked as critical.
"""

import csv
import os

def contar_vulnerabilidades_criticas():
    archivo = "myscan.csv"
    if not os.path.exists(archivo):
        print("No se encontró el archivo: myscan.csv")
        return

    total_criticas = 0
    try:
        with open(archivo, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                risk = row.get("Risk", "").strip().lower()
                severity = row.get("Severity", "").strip().lower()

                if "critical" in risk or severity == "4" or severity == "critical":
                    total_criticas += 1

        print(f"Total de vulnerabilidades críticas encontradas: {total_criticas}")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
