from flask import request, jsonify
from server import app
from DTO.supplier_products import SupplierProducts
import STORE.supplier_products_store as store

@app.route('/add_supplier_product', methods=['POST'])
def add_supplier_product():
    try:
        data = request.json
        supplier_product = SupplierProducts(
            company_name=data['company_name'],
            product_name=data['product_name']
        )
        is_inserted = store.add_supplier_product(supplier_product)
        if is_inserted:
            return jsonify({'message': 'Connection added successfully'}), 200
        else:
            return jsonify({'error': 'Failed to add connection'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400
