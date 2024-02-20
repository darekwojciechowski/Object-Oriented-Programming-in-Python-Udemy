'''
Dekorator @classmethod - Intro
Dekorator @classmethod w języku Python jest specjalnym rodzajem dekoratora, 
który jest używany do tworzenia metod klasy. Metody klasy są metodami, 
które nie operują na instancjach klasy, ale na samej klasie. Głównym celem 
dekoratora @classmethod jest umożliwienie dostępu do metody bez konieczności
tworzenia instancji klasy.



Główne cechy @classmethod:

Przyjmuje pierwszy argument nazwany cls, który reprezentuje klasę, a nie instancję.

Może być wywoływany na poziomie klasy, bez tworzenia obiektu danej klasy.

Jest często używany do tworzenia alternatywnych konstruktorów lub operacji, 
które są powiązane z klasą jako całością, a nie z konkretnymi instancjami.



Przykład użycia dekoratora @classmethod:

class KlasaPrzykladowa:
    licznik_instancji = 0
 
    def __init__(self, nazwa):
        self.nazwa = nazwa
        KlasaPrzykladowa.licznik_instancji += 1
 
    @classmethod
    def wyswietl_licznik(cls):
        print(f"Liczba instancji klasy: {cls.licznik_instancji}")
 
# Tworzenie instancji klasy
obiekt1 = KlasaPrzykladowa("Obiekt 1")
obiekt2 = KlasaPrzykladowa("Obiekt 2")
 
# Wywołanie metody klasy bez tworzenia instancji
KlasaPrzykladowa.wyswietl_licznik()


W powyższym przykładzie metoda wyswietl_licznik jest dekorowana @classmethod i może 
być wywoływana bezpośrednio na klasie KlasaPrzykladowa, co umożliwia dostęp do zmiennej
licznik_instancji bez konieczności tworzenia instancji klasy. Jest to przydatne w sytuacjach,
gdy potrzebujemy działań związanych z klasą, a nie z konkretnymi obiektami tej klasy.
'''