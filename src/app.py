from products import products
from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from bson import json_util

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/pythonmongodb'

mongo = PyMongo(app)


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"})


@app.route('/products', methods=['GET'])
def getProducts():
    prods = mongo.db.products.find()
    response = json_util.dumps(prods)
    return Response(response, mimetype='application/json')


@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = mongo.db.products.find_one({'name': product_name})
    response = json_util.dumps(productsFound)
    return Response(response, mimetype='application/json')


@app.route('/products',  methods=['POST'])
def addProduct():
    if request.json['name']:
        new_product = {
            "name": request.json["name"],
            "price": request.json["price"],
            "quantity": request.json["quantity"]
        }

        id = mongo.db.products.insert(new_product)

        response = {
            'id': str(id),
            'name': new_product["name"],
            'price': new_product["price"],
            'quantity': new_product["quantity"]
        }
        return response
    else:
        return not_found()


@app.route('/products/<string:product_name>',  methods=['PUT'])
def editProduct(product_name):

    name = request.json['name']
    price = request.json['price']
    quantity = request.json['quantity']

    mongo.db.products.update_one({'name': product_name}, { "$set": {
        'name': name,
        'price': price,
        'quantity': quantity
    }})

    return jsonify(
        {
            "message": "product updated"
        }
    )



@app.route('/products/<string:product_name>',  methods=['DELETE'])
def deleteProduct(product_name):
    mongo.db.products.delete_one({'name': product_name})
    response = jsonify(
        {"message": "Product " + product_name + " was deleted successfuly"})
    return response


@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        'response': 'Resourse Not Found :' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True, port=4000)
