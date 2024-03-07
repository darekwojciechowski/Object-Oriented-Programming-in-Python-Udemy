'''
Dziedziczenie - Intro
Dziedziczenie w języku Python jest mechanizmem programowania obiektowego, który umożliwia tworzenie nowych klas (klasa potomna lub pochodna) na podstawie istniejących klas (klasa bazowa lub nadrzędna). Dziedziczenie pozwala na ponowne wykorzystanie kodu i tworzenie hierarchii klas, gdzie nowe klasy mogą dziedziczyć atrybuty i metody swoich klas nadrzędnych.

Główne cechy dziedziczenia w Pythonie:

Klasa potomna dziedziczy atrybuty (zmienne) i metody z klasy nadrzędnej.

Klasy potomne mogą rozszerzać (dodawać nowe atrybuty i metody) lub nadpisywać (zmieniać zachowanie istniejących metod) dziedziczone elementy.

Dziedziczenie pozwala na tworzenie hierarchii klas, gdzie klasy nadrzędne reprezentują bardziej ogólne koncepcje, a klasy potomne bardziej szczegółowe.

Python obsługuje dziedziczenie wielokrotne, co oznacza, że klasa potomna może dziedziczyć z kilku klas nadrzędnych.

Przykład dziedziczenia w Pythonie:
'''
# Base class (or parent class)
class Animal:
    def __init__(self, name):
        self.name = name
 
    def speak(self):
        pass
 
# Derived class (or child class) inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
 
# Another derived class inheriting from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
 
# Creating instances of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
 
# Calling the speak method on instances
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!