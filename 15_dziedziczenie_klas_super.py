class Vehicle:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


class Car(Vehicle):

    def __init__(self, brand, year, horsepower):
        super().__init__(brand, year)
        self.horsepower = horsepower        

v1 = Vehicle('Tesla', 2020)
v1.__dict__

c1 = Car('Tesla', 2020, 306)
c1.__dict__