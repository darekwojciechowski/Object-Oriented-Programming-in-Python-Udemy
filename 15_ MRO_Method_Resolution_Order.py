#   MRO - Method Resolution Order

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


help(Plane)

Plane.mro()

Truck.__mro__
