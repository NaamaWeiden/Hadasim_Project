# from flask import Flask,jsonify,request
# from flask_cors import CORS
#
# app = Flask(__name__)
# CORS(app)
#
# from CONTROLLER.supplier_controller import *
# from CONTROLLER.product_controller import *
# from CONTROLLER.invitation_controller import *
# from CONTROLLER.supplier_products_controller import *
#
# if __name__ == '__main__':
#     print("Registered Routes:")
#     app.run(port=5000, debug=True)

from server import app
from CONTROLLER.supplier_controller import *
from CONTROLLER.product_controller import *
from CONTROLLER.invitation_controller import *
from CONTROLLER.supplier_products_controller import *

if __name__ == '__main__':
    print("Registered Routes:")
    print(app.url_map)

    app.run(port=5000, debug=True)
