class Smartphone:
    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, value):
        self._price = value


smartphone = Smartphone(3499)
print(smartphone.get_price())
smartphone.set_price(3999)
print(smartphone.get_price())