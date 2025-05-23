# Property Decorators: @property, @setter, and @deleter
# Assignment: Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.


class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        self.__price = price
        
    @price.deleter
    def price(self):
        del self.__price
        print("Price deleted")


p1 = Product(100)
print(p1.price)
p1.price = 200
print(p1.price)
del p1.price
# print(p1.price) # Uncommenting this line will raise an AttributeError since the price has been deleted