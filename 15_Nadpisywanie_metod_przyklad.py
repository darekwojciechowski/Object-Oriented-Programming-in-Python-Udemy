class Vehicle:

    def __init__(self, category=None):
        self.category = category if category else 'land'

    def __repr__(self):
        return f"{self.__class__.__name__}(category='{self.category}')"

    def display_info(self):
        print(f'Vehicle category: {self.category}')

    def show_activity(self):
        print(f'{self} -> Moving...')


class LandVehicle(Vehicle): 

    def display_info(self):
        print(f'LandVehicle category: {self.category}')

    def show_activity(self):
        print(f'{self} -> Driving...')        


class AirVehicle(Vehicle):
    
    def show_activity(self):
        print(f'{self} -> Flying...')    

vehicles = [Vehicle(), LandVehicle(), AirVehicle('air')]
vehicles

for vehicle in vehicles:
    vehicle.show_activity()