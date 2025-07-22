from api_utils import get_headers
from config import BASE_URL
import requests

def eliminar_credencial(uuid):
    url = f"{BASE_URL}/credentials/{uuid}"
    response = requests.delete(url, headers=get_headers())

    if response.status_code == 200:
        print(f"Credencial eliminada correctamente.")
    else:
        print(f"Error al eliminar credencial. Código: {response.status_code}")
        print(response.text)