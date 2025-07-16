# 🚀 Tenable Tools – Integración con API de Tenable.io

Este proyecto permite interactuar con la API de Tenable.io utilizando Python. Incluye módulos para gestionar escaneos, listar activos, exportar vulnerabilidades y programar tareas, todo desde la terminal.

---

## 📁 Estructura del proyecto

- `config.py`: Configuración con claves de acceso y URL base
- `api_utils.py`: Funciones reutilizables para interacción con la API
- `main.py`: Controlador principal que ejecuta módulos desde consola
- `lab_asset_inventory.py`: Lista activos con IP y hostname
- `lab_vuln_export.py`: Exporta vulnerabilidades filtradas por severidad
- `lab_schedule_scan.py`: Programa escaneos automáticos
- `test_auth.py`: Prueba la autenticación API
- `test_asset_inventory.py`: Verifica funcionalidad de lab_asset_inventory

---

## 🧪 Requisitos

- Python 3.x
- Cuenta activa en Tenable.io
- Claves de acceso (`ACCESS_KEY`, `SECRET_KEY`) configuradas en `config.py`

---

## 💻 Cómo ejecutar

1. Clona el repositorio:
   ```bash
   git clone https://github.com/mpivprueba/tenable_tools.git
   cd tenable_tools