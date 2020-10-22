from database_mongo import Mongo

# si se recibe el string 'mongo' por parametro instancia el objeto Mongo
class DatabaseFactory ():
    def getDatabase( self ):
        if self == "mongo":
            return Mongo()
