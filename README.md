# Tenable Tools
---

## Overview

Tenable Tools is a comprehensive cybersecurity solution suite focused on exposure management, designed to help [MPIV Partners](https://mpivpartners.com/) clients identify, assess, and prioritize vulnerabilities in their systems before they can be exploited by attackers.

The core objective of Tenable is to enable businesses and organizations to answer a critical question: "Are we exposed and at risk?" To achieve this, its unified platform, Tenable One, aims to unify security visibility across the modern attack surface, encompassing IT infrastructure, cloud environments, operational technology (OT), identities, and applications.

---

## Modules/Tools Included

* Vulnerability Management - Comprehensive vulnerability management

* Coming Soon: More specialized tools for the Tenable ecosystem

---

## Global Technology Stack

* [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
* [![Tenable API](https://img.shields.io/badge/Tenable_API-v2-orange.svg)](https://developer.tenable.com/)
* [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

---

## Installation and Global Configuration

### Prerequisites

* Python 3.8 or higher

* Active Tenable Vulnerability Management account

* [Tenable.io](https://www.tenable.com/products/vulnerability-management/) API credentials

---

## Step-by-Step Installation

1. Create virtual environment (recommended):

* Create virtual environment
python -m venv venv

*  Activate on Windows
venv\Scripts\activate

*  Activate on Linux/macOS
source venv/bin/activate

2. Install dependencies:

pip install -r requirements.txt

3. Configure Tenable credentials:

Generate API keys in [Tenable Vulnerability Management](https://cloud.tenable.com/tio/app.html#/login)

Create .env file in project root:

* Tenable.io API credentials

ACCESS_KEY=your_access_key_here
SECRET_KEY=your_secret_key_here
BASE_URL=https://cloud.tenable.com

4. Verify installation:

python main.py

---

# Project Structure

```
tenable_tools/
├── vulnerability_management/          # First tool - Vulnerability Management
│   ├── assets/                        # Asset management
│   ├── credentials/                   # Credentials handling
│   ├── policies/                      # Scan policies
│   ├── scans/                         # Scan execution and management
│   ├── tests/                         # Test suite
│   ├── vulnerabilities/               # Vulnerability analysis
│   ├── webapp/                        # Main web interface
│   └── README.md                      # Module-specific documentation
├── README.md                          # This file
└── [future_tools]/                    # Upcoming modules
```
---

## Available Modules

* [Vulnerability Management](https://github.com/mpivprueba/tenable_tools/tree/main/vulnerability_management) - Comprehensive vulnerability and asset management

---

## License
This project is licensed under the Apache License 2.0. See the LICENSE file for details.