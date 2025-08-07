"""
read_results.py

Este módulo permite leer y visualizar el contenido del archivo myscan.csv
exportado desde un escaneo de Tenable.io. Muestra una vista tabular de las
primeras filas del archivo para facilitar la revisión rápida.

Uso desde main.py:
  python main.py read_results
"""

import csv
import os


def leer_resultados_csv(ruta="myscan.csv", limite_filas=10):
    """
    Lee y muestra las primeras filas del archivo myscan.csv.

    Args:
        ruta (str): Ruta al archivo CSV a leer.
        limite_filas (int): Número de filas a mostrar (por defecto 10).

    Returns:
        None. Imprime filas del CSV.
    """
    if not os.path.exists(ruta):
        print(f"No se encontró el archivo: {ruta}")
        return

    try:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            encabezados = next(lector, [])
            print(" | ".join(encabezados))
            print("-" * 80)
            for i, fila in enumerate(lector):
                print(" | ".join(fila))
                if i + 1 >= limite_filas:
                    break
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
