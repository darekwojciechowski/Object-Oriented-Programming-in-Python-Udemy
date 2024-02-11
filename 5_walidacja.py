class Phone:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self._price

    def set_price(self, value):
        if isinstance(value, (int, float)):
            if value > 0:
                self._price = value
            else:
                raise ValueError('The price attribute must be positive.')
        else:
            raise TypeError('The price attribute must be an int or float value.')

phone = Phone(2000)
print(phone.get_price())
#phone.set_price(-100)
#print(phone.set_price('apple'))

print(phone.__dict__)
phone = Phone('appple')
phone.get_price()
