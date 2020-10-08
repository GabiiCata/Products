from flask import Flask, jsonify, request

app = Flask (__name__)

from products import products

@app.route('/ping' , methods=['GET'])
def ping():
    return jsonify({"message":"pong"})

@app.route('/products' , methods=['GET'])
def getProducts():
    return jsonify( {"products": products} )

@app.route('/products/<string:product_name>')
def getProduct( product_name ):
    productsFound = [product for product in products if product['name']== product_name]
    if (len(productsFound) > 0 ):
        return jsonify ( {"product" : productsFound[0]} )
    return jsonify ( {'message' : 'product not found'})


@app.route('/products',  methods=['POST'] )
def addProduct ():
    new_product = {
        "name" : request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"]
    }

    products.append ( new_product )
    return jsonify ({'message': 'Product added succesfuly',"product" : products})

if __name__ == '__main__':
    app.run(debug=True,port=4000)
