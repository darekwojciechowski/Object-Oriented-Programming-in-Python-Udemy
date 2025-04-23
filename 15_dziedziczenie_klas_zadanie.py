#   15 dziedziczenie klas zadanie

'''
Zadanie
Zaimplementuj poniższą hierarchię klas:

Vehicle
    LandVehicle
        Bike
        Car
        Truck
    AirVehicle
        Plane
        Helicopter
    WaterVehicle
'''


class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class Bike(LandVehicle):
    pass


class Car(LandVehicle):
    pass


class Truck(LandVehicle):
    pass


class AirVehicle(Vehicle):
    pass


class Plane(AirVehicle):
    pass


class Helicopter(AirVehicle):
    pass


class WaterVehicle(Vehicle):
    pass


issubclass(Bike, Vehicle), issubclass(Car, Vehicle), issubclass(Truck, Vehicle)

issubclass(Bike, LandVehicle), issubclass(
    Car, LandVehicle), issubclass(Truck, LandVehicle)

issubclass(Bike, AirVehicle), issubclass(
    Car, WaterVehicle), issubclass(Truck, LandVehicle)

issubclass(Bike, (LandVehicle, AirVehicle))
