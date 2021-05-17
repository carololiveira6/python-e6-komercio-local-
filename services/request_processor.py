import requests

def get_products(url: str) -> list:
    response = requests.get(url)

    return response.json()