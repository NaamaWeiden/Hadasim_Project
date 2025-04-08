from flask import Flask,jsonify, request

from DTO.Products import Products
from server import app
from DTO.supplier import supplier
import STORE.supplier_store as ss

@app.route('/add_supplier', methods=['POST'])
def register_supplier():
    data = request.json
    print("Received supplier data:", data)

    # יצירת אובייקט ספק עם נתונים
    new_supplier = supplier(
        company_name=data["company_name"],
        phone_num=data["phone_num"],
        worker_name=data["worker_name"],
        products=[Products(product['product_name'], product['price_per_item'], product['minimum_for_sale']) for product in data["products"]]
    )

    # קריאה לפונקציה של הסטור
    is_inserted = ss.add_supplier(new_supplier)
    if is_inserted:
        return jsonify({'message': 'Supplier and products inserted successfully'}), 200
    else:
        return jsonify({'error': 'Failed to insert supplier'}), 404


@app.route('/get_suppliers', methods=['GET'])
def get_suppliers():
    try:
        suppliers = ss.get_all_suppliers_names()
        return jsonify(suppliers), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
