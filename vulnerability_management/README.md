# Tenable.io CLI Utility

This project provides a command-line interface (CLI) for managing and interacting
with Tenable.io. It allows users to list scans, manage assets and credentials,
create policies, launch scans, export results, and generate reports.

This README serves as a step-by-step guide for clients to set up, configure,
and use the CLI effectively.

## Project Overview

The utility allows you to perform tasks such as:

- Listing and scheduling scans
- Exporting scan results in CSV and PDF formats
- Managing credentials and policies
- Generating reports on assets, untagged assets, and vulnerabilities
- Launching Web Application Security (WAS) scans

All functionality is accessible via the `main.py` CLI script.

## Project Structure

tenable_tools/
├── main.py                # CLI entry point
├── config.py              # Global configuration (API keys, base URL)
├── api_utils.py           # Helper functions for API requests
├── assets/                # Asset management scripts
├── vulnerabilities/       # Vulnerability export, reports, and analysis
├── scans/                 # Scan management (create, schedule, list)
├── credentials/           # Credential management (create, edit, delete, list)
├── policies/              # Policy creation and templates
├── webapp/                # Web application scanning scripts
└── README.md              # This file

# Installation

## Step 1: Prerequisites

Before starting, ensure you have:

- **Python 3.10 or higher** installed
- **pip** (Python package manager)
- An **active Tenable.io account** with API access
- Internet connection
1. Clone the repository:

## Step 2: Clone the Repository

Open a terminal or command prompt and run:

bash
git clone <repository_url>
cd tenable_tools

## Step 3: Create a Virtual Environment (Optional but Recommended)

python -m venv venv

* Activate the environment:

Windows:
venv\Scripts\activate

Linux / macOS:
source venv/bin/activate

## Step 4: Install Required Python Libraries
All dependencies are listed in requirements.txt. Install them with:

pip install -r requirements.txt

Dependencies included:

-requests – For making HTTP requests to Tenable.io API
-python-dotenv – For reading .env configuration files
-tabulate – Optional, for nicely formatted table outputs
-smtplib (built-in Python library) – For sending email notifications
-email (built-in Python library) – For composing email messages
-Any other libraries included in requirements.txt

Verify installation by running:

pip list

You should see all required packages installed.

## Step 5: Configure Environment Variables

Create a .env file in the project root with the following content:

# Tenable.io API credentials
ACCESS_KEY=<your_access_key>
SECRET_KEY=<your_secret_key>
BASE_URL=https://cloud.tenable.com

# Email configuration for alerts and notifications
EMAIL_FROM=<sender_email_address>
EMAIL_TO=<recipient_email_address>
EMAIL_SERVER=<smtp_server>
EMAIL_PORT=<smtp_port>
EMAIL_USER=<smtp_user>
EMAIL_PASS=<smtp_password>

Explanation of variables:

ACCESS_KEY / SECRET_KEY: API credentials from Tenable.io
BASE_URL: Base URL for Tenable.io API (default: https://cloud.tenable.com)
EMAIL_FROM: Sender email for notifications
EMAIL_TO: Recipient email for alerts
EMAIL_SERVER: SMTP server (e.g., smtp.office365.com)
EMAIL_PORT: SMTP port (e.g., 587 for TLS)
EMAIL_USER: Email username
EMAIL_PASS: Email password or app-specific password

## Step 6: Run the CLI

Test the setup by running the CLI:

python main.py

This will display a list of all available commands and usage instructions.

Example commands:

python main.py scans
python main.py generate_assets_report
python main.py critical_vulns <scan_id>


## Step 7: Next Steps

Once the environment is ready:

*Explore module-specific commands:
    -scans/ – Manage and schedule scans
    -assets/ – Export assets, generate reports, and view tags
    -credentials/ – Create, edit, delete, and list credentials
    -policies/ – Create and list scan policies
    -vulnerabilities/ – Export vulnerabilities and generate reports
    -webapp/ – Launch Web Application Scans (WAS)

Each module will have its own detailed README with examples and explanations.