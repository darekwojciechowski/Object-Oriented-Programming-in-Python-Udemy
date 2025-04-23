class Vehicle:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_details(self):
        return f'Calling from... {self.__class__.__name__}.'


class Car(Vehicle):

    def __init__(self, brand, year, horsepower):
        super().__init__(brand, year)
        self.horsepower = horsepower

    def show_details(self):
        result = super().show_details()
        return result + f'\nCalling from derived class... {self}'


c1 = Car('Tesla', 2020, 306)
c1.__dict__

c1.show_details()

print(c1.show_details())
