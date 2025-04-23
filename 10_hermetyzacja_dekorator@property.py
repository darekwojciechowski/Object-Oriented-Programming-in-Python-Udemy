#   Dekorator @property

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

phone.price = 1000
