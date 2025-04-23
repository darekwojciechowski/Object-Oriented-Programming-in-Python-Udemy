class Vehicle:

    def __init__(self, category=None):
        self.category = category if category else 'land'

    def __repr__(self):
        return f"{self.__class__.__name__}(category='{self.category}')"


class LandVehicle(Vehicle):
    pass


class AirVehicle(Vehicle):
    pass


vehicles = [Vehicle(), LandVehicle(), AirVehicle('air')]
vehicles
