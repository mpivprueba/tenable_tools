# # Tenable Tools - MPIV Automation Suite

* [![MPIV Developed](https://img.shields.io/badge/Developed%20by-MPIV-orange.svg)](https://mpivpartners.com)

* [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

* [![Tenable API](https://img.shields.io/badge/Tenable_API-v2-orange.svg)](https://developer.tenable.com/)

* [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

---

## MPIV Automation Tools for Tenable

This repository contains a comprehensive suite of **automation tools and scripts developed by [MPIV Partners](https://mpivpartners.com/)** to help our clients maximize their Tenable investment through simplified API interactions, automated workflows, and standardized security processes.

## Why MPIV Automation?

As Tenable experts and implementation partners, we've packaged our proven methodologies into reusable tools that:

- **Reduce operational overhead** by automating repetitive tasks
- **Ensure consistency** across vulnerability management processes  
- **Accelerate time-to-value** from your Tenable deployment
- **Provide enterprise-grade reporting** for compliance and audits

---

## Modules/Tools Included

* Vulnerability Management - Comprehensive vulnerability management

* Coming Soon: More specialized tools for the Tenable ecosystem

## Coming Soon from MPIV
- **Compliance Reporting Engine** - Automated regulatory compliance reports
- **Remediation Workflow Manager** - Ticketing and patch management integration
- **Cloud Security Posture** - Multi-cloud environment security assessment

---

## Global Technology Stack

* [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

* [![Tenable API](https://img.shields.io/badge/Tenable_API-v2-orange.svg)](https://developer.tenable.com/)

* [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

---

## Installation and Global Configuration

### Prerequisites

* Python 3.8 or higher - [Download here](https://www.python.org/downloads/)

* Active Tenable Vulnerability Management account - With API access enabled

* [Tenable.io](https://www.tenable.com/products/vulnerability-management/) API credentials

---

## Installation Guide

### Step 1: Setup Environment

```bash
# Create isolated Python environment
python -m venv tenable-env

# Activate it
# Windows:
tenable-env\Scripts\activate
# Linux/Mac:
source tenable-env/bin/activate
```
### Step 2: Install MPIV Tools

```bash
# Install all required dependencies
pip install -r requirements.txt
```

### Step 3: Configure Your Tenable Connection

```bash
# Create configuration file
echo 'ACCESS_KEY=your_actual_access_key_here' > .env
echo 'SECRET_KEY=your_actual_secret_key_here' >> .env
echo 'BASE_URL=https://cloud.tenable.com' >> .env
```

### Step 4: Verify Setup

```bash
# Test your installation
python main.py --help
```

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

## License & Support

**Apache 2.0 License** - Chosen by MPIV to provide maximum flexibility for our clients while protecting intellectual property.

### MPIV Support
This tool is actively maintained by **MPIV's Cybersecurity Practice**. 

**Need assistance?** Contact our team:
- **Email**: security@mpivpartners.com
- **Website**: [mpivpartners.com](https://mpivpartners.com)
- **Technical Support**: Open an issue in this repository

---