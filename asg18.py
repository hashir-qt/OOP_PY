class Product:
    def __init__(self, price):
        self._price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self._price = value
    
    @price.deleter
    def price(self):
        del self._price

# Test
p = Product(100)
print(p.price)  # Output: 100
p.price = 150
print(p.price)  # Output: 150
del p.price
try:
    print(p.price)  # Raises AttributeError
except AttributeError:
    print("Price attribute deleted")