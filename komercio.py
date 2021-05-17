from services.request_processor import get_products
from services.json_processor import populate_json, get_json_data
from json import dump, load


URL = 'https://gitlab.com/-/snippets/2118021/raw/master/komercio.py'

JSON_FILEPATH = 'data/lista_de_produtos.json'

products = get_products(URL)
populate_json(JSON_FILEPATH, products)

json_products = get_json_data(JSON_FILEPATH)

def populate_json(filepath: str, data: list):
    with open(filepath, 'w') as file:
        dump(data, file, indent=2)

def get_json_data(filepath: str) -> list:
    with open(filepath, 'r') as file:
        return load(file)