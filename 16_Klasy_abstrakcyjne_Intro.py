'''
Klasy abstrakcyjne - Intro

Klasy abstrakcyjne w języku Python to klasy, które nie mogą być bezpośrednio instancjonowane, ale stanowią szkic lub szablon do tworzenia innych klas. Klasy abstrakcyjne służą do definiowania ogólnych interfejsów i metod, które muszą być zaimplementowane w klasach potomnych. Głównym celem klasy abstrakcyjnej jest narzucanie określonych wymagań dla klas dziedziczących, zapewniając pewien poziom spójności w hierarchii klas.
Klasy abstrakcyjne w Pythonie są często tworzone przy użyciu modułu abc (Abstract Base Classes), który udostępnia mechanizmy do definiowania abstrakcyjnych klas bazowych.

Główne cechy klas abstrakcyjnych w Pythonie:
    Nie można tworzyć instancji klasy abstrakcyjnej.
    Klasy abstrakcyjne zawierają abstrakcyjne metody, czyli metody, które są deklarowane, ale nie posiadają konkretnej implementacji.
    Klasy dziedziczące po klasie abstrakcyjnej muszą zaimplementować wszystkie jej abstrakcyjne metody, w przeciwnym razie będą to klasy abstrakcyjne.
    Klasy abstrakcyjne mogą zawierać także konkretne metody (metody z implementacją), które mogą być dziedziczone przez klasy potomne.

Przykład klasy abstrakcyjnej w Pythonie za pomocą modułu abc:
'''
from abc import ABC, abstractmethod

# Base class (or parent class)


class Animal(ABC):
    def __init__(self, species):
        self.species = species

    @abstractmethod
    def eat(self):
        pass

# Derived class (or child class) inheriting from Animal


class Bird(Animal):
    def eat(self):
        print(f"{self.species} eats insects")


# Creating an instance of the derived class
eagle = Bird("Eagle")

# Calling the inherited method from the abstract base class
eagle.eat()  # Output: "Eagle eats insects"

'''
W tym przykładzie klasa Animal jest klasą abstrakcyjną, ponieważ zawiera abstrakcyjną metodę eat(). Klasa Bird dziedziczy po klasie Animal i musi zaimplementować tę abstrakcyjną metodę, co jest realizowane w jej definicji. Klasy abstrakcyjne pomagają narzucać pewne standardy i interfejsy dla klas potomnych.
'''
