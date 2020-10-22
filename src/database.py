import abc

class Database(abc.ABC):

    @abc.abstractmethod
    def config( self ):
        pass

    @abc.abstractmethod
    def hablar( self ):
        pass

    @abc.abstractmethod
    def getProducts(self):
        pass

    @abc.abstractmethod
    def getProduct(self):
        pass

    @abc.abstractmethod
    def addProduct(self):
        pass


    @abc.abstractmethod
    def editProduct(self):
        pass


    @abc.abstractmethod
    def deleteProduct(self):
        pass


