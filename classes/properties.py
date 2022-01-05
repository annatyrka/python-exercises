# How to for example ensure that our products don't have negative price
class Product:
    def __init__(self, price):
        self.price = price

    @property               # this is to hide the function when calling on an object
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative.')
        self.__price = value


product = Product(2)
product = Product(-10)
print(product.price)
