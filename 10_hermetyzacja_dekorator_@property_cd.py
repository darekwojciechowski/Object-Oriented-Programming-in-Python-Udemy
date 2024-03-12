#   Dekorator @property - c. d.

class Phone:

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        print('getting...')
        return self._price

    @price.setter
    def price(self, value):
        print('setting...')
        if isinstance(value, (int, float)):
            if value > 0:
                self._price = value
            else:
                raise ValueError('The price attribute must be positive.')
        else:
            raise TypeError('The price attribute must be an int or float value.')        

Phone.__dict__

phone = Phone(2000)
phone.price

phone.price = -1000
phone.price = 'fsds'

phone.price = 4000