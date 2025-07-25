# Tenable Tools — Gestión Automatizada en Tenable.io

Este proyecto ofrece una interfaz en Python para interactuar con la API de Tenable.io, permitiendo la gestión de activos, credenciales, políticas y escaneos desde la terminal. Está diseñado para ser modular, seguro y eficiente, facilitando la automatización y el monitoreo de vulnerabilidades en entornos empresariales.

## Características principales

- Crear, editar y eliminar credenciales SSH
- Listar activos registrados con hostname e IP
- Gestionar escaneos: crear, programar y exportar resultados
- Visualizar templates, escáneres y políticas disponibles
- Exportar datos en formato `.nessus`
- Acceso por línea de comandos mediante `main.py`

## Requisitos

- Python 3.8 o superior
- Cuenta activa en Tenable.io
- Claves `ACCESS_KEY` y `SECRET_KEY` generadas desde el portal de Tenable.io
- Acceso a Internet

## Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/mpivprueba/tenable_tools.git
cd tenable_tools

---

### 2. Crear un entorno virtual (Opcional)

python -m venv venv
source venv/bin/activate       # En Linux/macOS
venv\Scripts\activate          # En Windows

---

### 3. Instala las dependencias: Crea un archivo requirements.txt con este contenido

requests
python-dotenv

# Instala las dependencias ejecutando:

pip install -r requirements.txt

---

## Configuracion:

## Crea un archivo .env en la raíz del proyecto con las credenciales de Tenable.io:

ACCESS_KEY=tu_access_key_aqui
SECRET_KEY=tu_secret_key_aqui
BASE_URL=https://cloud.tenable.com

---

## Estructura del proyecto

tenable_tools/
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── config.py
├── api_utils.py
├── create_credentials.py
├── edit_credentials.py
├── delete_credentials.py
├── list_credentials.py
├── list_credential_names.py
├── list_credential_types.py
├── extract_credential_ids.py
├── show_type_config.py
├── create_policy.py
├── create_scan.py
├── list_templates.py
├── list_scanners.py
├── lab_asset_inventory.py
├── lab_schedule_scan.py
├── lab_scan_list.py
├── lab_vuln_export.py
├── test_auth.py

---

## Comandos disponibles
### Desde la terminal, ejecuta main.py seguido de cualquiera de estos comandos:
### 1. Escaneos

python main.py scans                             # Listar escaneos disponibles
python main.py export                            # Exportar escaneo finalizado
python main.py export <scan_id>                  # Exportar escaneo por ID
python main.py schedule <scan_id>                # Programar escaneo por ID
python main.py create_scan                       # Crear escaneo interactivo

### 2. Activos
python main.py assets                         # Listar activos registrados

### 3. Credenciales
python main.py create_credential <name> <user> <password> <elevation_method> [account][elevation_password] [bin_directory]
python main.py edit_credential <uuid> [name] 
python main.py delete_credential <uuid>

---