class Laptop:

    brand = 'Apple'
    _usdpln = 4.0
    __trade_margin = 0.3

    def __init__(self, net_price):
        self.net_price = net_price

    def __convert_price(price):
        return price * Laptop._usdpln * (1 + Laptop.__trade_margin)

    def display_price_pln(self):
        print(Laptop.__convert_price(self.net_price))


Laptop.__dict__

laptop = Laptop(3000)
laptop.display_price_pln()

#   Laptop.__convert_price(400)
