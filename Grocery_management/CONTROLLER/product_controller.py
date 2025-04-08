from flask import Flask,request, jsonify
from server import app
from DTO.Products import Products
import STORE.products_store as ps

@app.route('/add_product', methods=['POST'])
def add_product():
    try:
        data = request.json
        product = Products(
            product_name=data['product_name'],
            price_per_item=data['price_per_item'],
            minimum_for_sale=data['minimum_for_sale']
        )
        is_inserted = ps.add_product(product)
        if is_inserted:
            return jsonify({'message': 'Product inserted successfully'}), 200
        else:
            return jsonify({'error': 'Product not inserted'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/get_products_by_supplier', methods=['GET'])
def get_products_by_supplier():
    try:
        company_name = request.args.get('company_name')
        products = ps.get_products_by_supplier(company_name)
        return jsonify(products), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/get_minimum_for_sale', methods=['GET'])
def get_minimum_for_sale():
    try:
        product_name = request.args.get('product_name')
        minimum_for_sale = ps.get_minimum_for_sale(product_name)
        return jsonify({"minimum_for_sale": minimum_for_sale}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/calculate_total_payment', methods=['GET'])
def calculate_total_payment():
    try:
        product_name = request.args.get('product_name')
        quantity = int(request.args.get('quantity'))
        total_payment = ps.calculate_total_payment(product_name, quantity)
        return jsonify({"total_payment": total_payment}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
