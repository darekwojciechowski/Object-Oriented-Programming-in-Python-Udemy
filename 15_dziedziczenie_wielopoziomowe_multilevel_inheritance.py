#   Dziedziczenie wielopoziomowe - Multilevel Inheritance

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
        return result + f'\nCalling from derived class... {self.__class__.__name__}.'


class RacingCar(Car):
    
    def show_details(self):
        result = super().show_details() 
        return result + f'\nCalling from... {self.__class__.__name__}.'    