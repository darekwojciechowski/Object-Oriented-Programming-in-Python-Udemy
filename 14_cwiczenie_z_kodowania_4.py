'''
Ćwiczenie 4
Załóżmy, że pracujesz nad klasą o nazwie Person, która ma następujące atrybuty:

name: imię osoby
age: wiek osoby
nationality: narodowość osoby

Potrzebujesz zaimplementować metodę __bool__() tej klasy, która zwraca True, jeśli wiek osoby jest większy lub równy 18 lat, i False w przeciwnym razie.

Przykłady:
[IN]: person1 = Person('Alice', 25, 'American')
[IN] bool(person1)
[OUT]: True

[IN]: person1 = Person('Alice', 16, 'American')
[IN] bool(person1)
[OUT]: False

Następnie przetestuj swoją implementację, tworząc dwa obiekty klasy Person z poniższymi danymi i drukując ich wartości logiczne w podanej kolejności do konsoli.

Person('Alice', 25, 'American')
Person('Bob', 15, 'British')

Oczekiwany wynik:
True
False
'''

class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
 
    def __bool__(self):
        return self.age >= 18
 
 
person1 = Person('Alice', 25, 'American')
person2 = Person('Bob', 15, 'British')
 
print(bool(person1))
print(bool(person2))