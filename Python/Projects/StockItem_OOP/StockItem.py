class StockItem:
    __longName = ""
    __shortName = ""
    __price = 0.0

    def __init__(self, longName, shortName, price):
        self.longName = longName
        self.shortName = shortName
        self.price = price
    
    def getPrice(self):
        return self.__price 
    
    def setPrice(self, newPrice):
        if newPrice >= 0:
            self.price = newPrice 
        elif newPrice < 0:
            raise ValueError('newPrice cannot be negative')

    def getShortName(self):
        return self.__shortName

    def setShortName(self, newShortName):
        self.__shortName = newShortName
    
    def setLongName(self, newLongName):
        self.__longName = newLongName

    def getLongName(self):
        return self.__longName

    
    