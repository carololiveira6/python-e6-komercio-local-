from flask import Flask, jsonify, request
from flask_cors import CORS
from komercio import json_products

app = Flask(__name__)
CORS(app)

@app.route('/products')
def list_products():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page')
    # pagenation = json_products.query.paginate(page=page, per_page=per_page)

    return jsonify(json_products))

@app.route('/products/<product_id>')
def get_product(product_id):
    for product in json_products:
        if product['id'] == int(product_id):
            return product
    return ('', 404)