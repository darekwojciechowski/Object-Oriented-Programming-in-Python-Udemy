'''
Ćwiczenie 2
Zaimplementowane są poniższe klasy:

    Vehicle
    LandVehicle
    AirVehicle

Zdefiniuj metodę specjalną __repr__() w klasie Vehicle, która będzie zwracać formalną reprezentację obiektów klas: Vehicle, LandVehicle oraz AirVehicle.

Przykład:

    [IN]: instances = [Vehicle(), LandVehicle(), AirVehicle()]
    [IN]: for instance in instances:
    [IN]:     print(instance)

    [OUT]: Vehicle(category='land vehicle')
    [OUT]: LandVehicle(category='land vehicle')
    [OUT]: AirVehicle(category='air vehicle')
'''


class Vehicle:
    def __init__(self, category=None):
        self.category = category if category else 'land vehicle'

    def __repr__(self):
        return f"{self.__class__.__name__}(category='{self.category}')"


class LandVehicle(Vehicle):
    pass


class AirVehicle(Vehicle):
    def __init__(self, category=None):
        self.category = category if category else 'air vehicle'


instances = [Vehicle(), LandVehicle(), AirVehicle()]

for instance in instances:
    print(instance)
