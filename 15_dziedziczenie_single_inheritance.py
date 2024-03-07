'''
Pojedyncze dziedziczenie - Single Inheritance
Vehicle:
LandVehicle
AirVehicle
WaterVehicle
'''
class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class AirVehicle(Vehicle):
    pass


class WaterVehicle(Vehicle):
    pass


vehicles = [Vehicle(), LandVehicle(), AirVehicle(), WaterVehicle()]

vehicles

help(issubclass)

issubclass(Vehicle, object)

issubclass(LandVehicle, Vehicle), issubclass(AirVehicle, Vehicle), issubclass(WaterVehicle, Vehicle)

issubclass(WaterVehicle, object)