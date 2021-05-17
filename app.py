from flask import Flask, jsonify
from flask_cors import CORS
from komercio import json_products
app = Flask(__name__)
CORS(app)

@app.route('/products')
def list_products():
    return jsonify(json_products)

# @app.route('/products/<product_id')
# def get_product():
#     pass