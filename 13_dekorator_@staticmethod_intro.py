'''
Dekorator @staticmethod - Intro
Dekorator @staticmethod w języku Python jest używany do tworzenia statycznych metod w klasach. 
Metody statyczne są funkcjami, które są związane z klasą, ale nie operują na instancjach ani 
nie mają dostępu do ich atrybutów. Dzięki temu dekoratorowi, metoda jest dostępna na poziomie 
klasy, a nie na poziomie instancji.

Główne cechy @staticmethod:
Nie przyjmuje automatycznie argumentu reprezentującego klasę lub instancję (brak self ani 
cls jako pierwszego argumentu).
Może być wywoływany na poziomie klasy, bez tworzenia instancji klasy.
Nie ma dostępu do atrybutów ani stanu instancji klasy.
Jest często używany do zdefiniowania funkcji, które są związane z klasą, ale nie wymagają 
dostępu do instancji ani jej atrybutów.

Przykład użycia dekoratora @staticmethod:
'''
class KlasaPrzykladowa:
    def __init__(self, nazwa):
        self.nazwa = nazwa
 
    @staticmethod
    def statyczna_metoda():
        print("To jest metoda statyczna")
 
# Tworzenie instancji klasy
obiekt = KlasaPrzykladowa("Obiekt 1")
 
# Wywołanie metody statycznej bez tworzenia instancji
KlasaPrzykladowa.statyczna_metoda()

'''
W powyższym przykładzie metoda statyczna_metoda jest dekorowana @staticmethod i może być
wywoływana bezpośrednio na klasie KlasaPrzykladowa. Metody statyczne są przydatne, gdy 
potrzebujemy funkcji związanych z klasą, ale nie potrzebujemy dostępu do jej instancji 
ani jej atrybutów.
'''