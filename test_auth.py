import requests
from config import ACCESS_KEY, SECRET_KEY, BASE_URL

headers = {
    "X-ApiKeys": f"accessKey={ACCESS_KEY}; secretKey={SECRET_KEY};",
    "Content-Type": "application/json"
}

url = f"{BASE_URL}/scans"
response = requests.get(url, headers=headers)
print("Status Code:", response.status_code)
print("Response Body:", response.text)