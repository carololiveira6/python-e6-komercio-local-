from services.request_processor import get_products
from services.json_processor import populate_json, get_json_data

URL = 'https://gitlab.com/-/snippets/2118021/raw/master/komercio.py'

JSON_FILEPATH = 'data/lista_de_produtos.json'

products = get_products(URL)
populate_json(JSON_FILEPATH, products)

json_products = get_json_data(JSON_FILEPATH)
