import os
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from tenable.io import TenableIO
from config import ACCESS_KEY, SECRET_KEY, EMAIL_FROM, EMAIL_TO, EMAIL_SERVER, EMAIL_PORT, EMAIL_USER, EMAIL_PASS

# Inicializar cliente Tenable
tio = TenableIO(ACCESS_KEY, SECRET_KEY)

def generate_csv_report():
    filename = "high_and_critical_last7days.csv"
    seven_days_ago = (datetime.utcnow() - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%S")

    # Crear exportación con filtros soportados
    export = tio.exports.vulns(
        filters=[
            {"filter": "severity", "operator": "eq", "value": "high"},
            {"filter": "severity", "operator": "eq", "value": "critical"},
            {"filter": "last_seen", "operator": "gte", "value": seven_days_ago}
        ],
        format="csv"
    )

    # Descargar CSV
    with open(filename, "wb") as f:
        for chunk in tio.exports.download(export["file"]):
            f.write(chunk)

    print(f"CSV report generated: {filename}")
    return filename

def send_email(attachment_path):
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_FROM
        msg["To"] = EMAIL_TO
        msg["Subject"] = "High & Critical Vulnerabilities Report (Last 7 Days)"
        msg.attach(MIMEText("Attached is the latest High & Critical vulnerabilities report (last 7 days).", "plain"))

        with open(attachment_path, "rb") as f:
            part = MIMEApplication(f.read(), Name=os.path.basename(attachment_path))
            part["Content-Disposition"] = f'attachment; filename="{os.path.basename(attachment_path)}"'
            msg.attach(part)

        with smtplib.SMTP(EMAIL_SERVER, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)

        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    csv_file = generate_csv_report()
    send_email(csv_file)
