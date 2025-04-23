'''
Ćwiczenie 1
Zaimplementuj klasę o nazwie Smartphone, która w metodzie __init__() ustawi wartość atrybutu chronionego _price przechowującego cenę smartfonu (bez żadnej walidacji). Następnie zaimplementuj metodę do odczytywania tego atrybutu o nazwie get_price() oraz metodę do modyfikacji tego atrybutu o nazwie set_price() również bez walidacji.

Kolejno utwórz instancję klasy Smartphone z ceną 3499 i wykonaj następujące kroki:
    wykorzystując metodę get_price() wydrukuj wartość atrybutu chronionego _price do konsoli
    wykorzystując metodę set_price() ustaw wartość atrybutu chronionego _price  na 3999
    wykorzystując metodę get_price() ponownie wydrukuj wartość atrybutu chronionego _price do konsoli

Oczekiwany wynik:
    3499
    3999
'''


class Smartphone:
    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, value):
        self._price = value


smartphone = Smartphone(3499)
print(smartphone.get_price())
smartphone.set_price(3999)
print(smartphone.get_price())
