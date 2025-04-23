class Laptop:

    def __init__(self, brand, code, wholesale_price):
        self.brand = brand
        self._code = code
        self.__wholesale_price = wholesale_price

    def info(self):
        print(self.brand)
        print(self._code)
        print(self.__wholesale_price)


laptop = Laptop('Apple', '0043', 3000)
laptop.info()
