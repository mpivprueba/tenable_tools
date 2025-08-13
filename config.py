"""
config.py 

This module loads the necessary configuration variables for authenticating and interacting
with the Tenable.io API. It uses environment variables, optionally loaded from a `.env` file,
to securely manage sensitive information such as API credentials.

"""
import os # For accessing environment variables.
from dotenv import load_dotenv #To load variables from a .env file into the environment.

load_dotenv()

ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
BASE_URL   = os.getenv("BASE_URL", "https://cloud.tenable.com")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_SERVER = os.getenv("EMAIL_SERVER")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")