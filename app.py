from flask import Flask, jsonify, request
from flask_cors import CORS
from komercio import json_products
from paginator import pagination

app = Flask(__name__)
CORS(app)

@app.route('/products')
def list_products():
    page = request.args.get('page')
    per_page = request.args.get('per_page')

    pagenated = pagination(json_products, per_page, page)

    return jsonify(pagenated)

@app.route('/products/<product_id>')
def get_product(product_id):
    for product in json_products:
        if product['id'] == int(product_id):
            return product
    return ('', 404)