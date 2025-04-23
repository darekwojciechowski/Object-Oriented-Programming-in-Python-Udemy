#   207. Klasy abstrakcyjne - przykład

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def show_activity(self):
        pass


class Plane(Vehicle):

    def show_activity(self):
        print(f'{self.__class__.__name__} -> I can fly.')


class Car(Vehicle):

    def show_activity(self):
        print(f'{self.__class__.__name__} -> I can drive.')


vehicles = [Plane(), Car()]
for vehicle in vehicles:
    vehicle.show_activity()
