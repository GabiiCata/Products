from flask import Flask, jsonify

app = Flask (__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True,port=4000)
