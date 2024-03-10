class Vehicle:
    
    year = 2010

    def info(self):
        print(f'{self.__class__.__name__} from {Vehicle.year}.')


class Car(Vehicle):
    
    year = 2020
    
vehicles = [Vehicle(), Car()]
for vehicle in vehicles:
    vehicle.info()


class Vehicle:
    
    year = 2010

    def info(self):
        print(f'{self.__class__.__name__} from {type(self).year}.')


class Car(Vehicle):
    
    year = 2020


vehicles = [Vehicle(), Car()]
for vehicle in vehicles:
    vehicle.info()

