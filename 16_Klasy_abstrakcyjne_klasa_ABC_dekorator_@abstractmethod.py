#   201. Klasy abstrakcyjne - klasa ABC oraz dekorator @abstractmethod

import abc


help(abc.ABC)

help(abc.abstractmethod)

from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def area(self):
        pass


class Square(Figure):

    def __init__(self, a=1):
        self.a = a

    def area(self):
        return self.a * self.a


figures = [Square(), Square(5), Square(10)]

for figure in figures:
    print(f'Side length: {figure.a}')
    print(f'Area: {figure.area()}\n')


#   f = Figure()