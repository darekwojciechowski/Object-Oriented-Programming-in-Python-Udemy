'''
Ćwiczenie 3
Podana jest klasa Vehicle, która posiada trzy atrybuty:

    brand
    color
    year

Utwórz klasę Car, która dziedziczy po klasie Vehicle. Następnie nadpisz metodę __init__() tak, aby klasa Car w konstruktorze przyjmowała cztery argumenty i ustawiała je odpowiednio jako atrybuty instancji:

    brand
    color
    year
    horsepower

Następnie utwórz poniższe instancje odpowiednio dla klas Vehicle i Car:
    o nazwie vehicle i wartościach atrybutów kolejno: 'Tesla', 'red', 2020
    o nazwie car i wartościach atrybutów kolejno: 'Tesla', 'red', 2020, 300

W odpowiedzi wydrukuj wartość atrybutu __dict__ instancji vehicle oraz car.

Oczekiwany wynik:

    {'brand': 'Tesla', 'color': 'red', 'year': 2020}
    {'brand': 'Tesla', 'color': 'red', 'year': 2020, 'horsepower': 300}
'''

class Vehicle:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year
 
 
class Car(Vehicle):
    def __init__(self, brand, color, year, horsepower):
        super().__init__(brand, color, year)
        self.horsepower = horsepower
 
 
vehicle = Vehicle('Tesla', 'red', 2020)
print(vehicle.__dict__)       
 
car = Car('Tesla', 'red', 2020, 300)
print(car.__dict__)