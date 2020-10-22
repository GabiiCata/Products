from database import *
from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from jproperties import Properties
from bson import json_util

class Mongo ( Database ):

    mongo = None 

    def config ( self , app ):
        app.config['MONGO_URI'] = 'mongodb://localhost/pythonmongodb'
        self.mongo = PyMongo(app)


    def hablar ( self ):
        return ( "Esta es la base de mongo !")

    def getProducts(self):
        prods = self.mongo.db.products.find()
        response = json_util.dumps(prods)
        return Response(response, mimetype='application/json')


    def getProduct(self):
        pass


    def addProduct(self):
        pass



    def editProduct(self):
        pass



    def deleteProduct(self):
        pass

