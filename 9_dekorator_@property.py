"""
Demonstrates using the @property decorator to create getter and setter methods
for a class attribute. Allows accessing the attribute like a normal attribute 
while running custom code when getting and setting.
"""
class Phone:

    def __init__(self, price):
        self._price = price

    def price(self):
        print('getting...')
        return self._price

    price = property(fget=price)

class Phone:

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        print('getting...')
        return self._price

Phone.__dict__

phone = Phone(2000)
phone.__dict__

phone.price
phone.price = 1000

del phone.price