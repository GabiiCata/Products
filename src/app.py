from flask import Flask, jsonify, request, Response
from bson import json_util
from database_factory import DatabaseFactory
from jproperties import Properties
import sys

configs = Properties()

with open('app-config.properties', 'rb') as config_file:
    configs.load(config_file)


database = DatabaseFactory.getDatabase( configs.get("database").data )

app = Flask(__name__)

database.config ( app )


@app.route('/',  methods=['GET'])
def index():
    return database.hablar()




@app.route('/products', methods=['GET'])
def getProducts():
    return database.getProducts()



# handler de error
@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        'response': 'Resourse Not Found :' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response

# inicia el server 
if __name__ == '__main__':
    app.run(debug=True, port=4000)

