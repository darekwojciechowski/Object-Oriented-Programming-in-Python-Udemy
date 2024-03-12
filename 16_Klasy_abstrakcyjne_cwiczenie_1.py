'''
Ćwiczenie 1
Zdefiniuj klasę abstrakcyjną o nazwie TaxPayer. Klasa TaxPayer ma posiadać jeden atrybut salary,
który określa pensję podatnika. Klasa ta posiada również jedną abstrakcyjną metodę calculate_tax(),
która będzie musiała być zaimplementowana w klasach dziedziczących. Metoda ta ma za zadanie obliczenie
wysokości podatku, który musi zapłacić podatnik.
'''

from abc import ABC, abstractmethod
 
 
class TaxPayer(ABC):
    def __init__(self, salary):
        self.salary = salary
 
    @abstractmethod
    def calculate_tax(self):
        pass