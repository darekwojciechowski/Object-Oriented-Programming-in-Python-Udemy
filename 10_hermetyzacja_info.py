'''
118. Hermetyzacja - Intro

Hermetyzacja w języku Python odnosi się do mechanizmu kontroli dostępu do atrybutów i 
metod obiektów. Głównym celem hermetyzacji jest ukrycie pewnych elementów obiektu 
przed bezpośrednim dostępem z zewnątrz. W Pythonie hermetyzacja jest często osiągana 
poprzez stosowanie zakresów nazw (ang. name mangling) i konwencji nazewniczych.

Aby zaimplementować hermetyzację, można użyć dwóch podstawowych mechanizmów:

Prywatność za pomocą podkreślenia: Atrybuty i metody, których nazwy zaczynają się 
od pojedynczego podkreślenia (np. _zmienna lub _metoda()), są uważane za prywatne. 
Choć technicznie można do nich uzyskać dostęp z zewnątrz, zgodnie z konwencją 
programistyczną, są one traktowane jako elementy przeznaczone do użytku wewnątrz klasy.

Zakres nazw (Name Mangling): Python umożliwia hermetyzację poprzez dodawanie przedrostka 
podwójnego podkreślenia i nazwy klasy do atrybutu lub metody (np. self.__zmienna lub 
self.__metoda()). To sprawia, że atrybuty stają się trudniejsze do dostępu z zewnątrz 
klasy, ponieważ ich nazwy są zmieniane w sposób, który zależy od nazwy klasy.

Przykład:
'''

class MojaKlasa:
    def __init__(self):
        self.__prywatna_zmienna = 42
 
    def publiczna_metoda(self):
        print("To jest publiczna metoda")
 
    def __prywatna_metoda(self):
        print("To jest prywatna metoda")
 
obiekt = MojaKlasa()
print(obiekt.__prywatna_zmienna)  # To spowoduje błąd
obiekt.publiczna_metoda()         # To jest poprawne
obiekt.__prywatna_metoda()        # To spowoduje błąd

'''
Jednak ważne jest, aby pamiętać, że hermetyzacja w Pythonie jest bardziej kwestią konwencji 
niż ścisłego ograniczenia dostępu, ponieważ można do atrybutów prywatnych uzyskać dostęp z 
zewnątrz, ale nie jest to zalecane ze względów bezpieczeństwa i utrzymania.
'''