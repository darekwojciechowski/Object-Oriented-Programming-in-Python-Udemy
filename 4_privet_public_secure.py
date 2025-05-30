'''
Ćwiczenie z kodowania 27: Ćwiczenie 1 
116. Rozwiązanie 1

Ćwiczenie 1
Zaimplementuj klasę o nazwie Smartphone, która przy tworzeniu instancji ustawi poniższe atrybuty instancji:

    brand jako atrybut publiczny
    model jako atrybut chroniony
    price jako atrybut prywatny

Następnie utwórz instancję klasy Smartphone o nazwie smartphone o podanych parametrach:

    'Huawei'
    'Mate 20 Pro'
    1999

W odpowiedzi wydrukuj wartość atrybutu __dict__ obiektu smartphone.

Oczekiwany wynik:
{'brand': 'Huawei', '_model': 'Mate 20 Pro', '_Smartphone__price': 1999}
'''


class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand  # atrybut publiczny
        self._model = model  # atrybut chroniony
        self.__price = price  # atrybut prywatny


smartphone = Smartphone('Huawei', 'Mate 20 Pro', 1999)
print(smartphone.__dict__)


''' Cwiczenie 2  (111. Rozwiązanie 4)

Oczekiwany wynik:

    brand -> Huawei
    model -> Mate 20 Pro
    price -> 1999
'''


class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand  # atrybut publiczny
        self._model = model  # atrybut chroniony
        self.__price = price  # atrybut prywatny


smartphone = Smartphone('Huawei', 'Mate 20 Pro', 1999)
print(f'brand -> {smartphone.brand}')  # atrybut publiczny
print(f'model -> {smartphone._model}')  # atrybut chroniony
print(f'price -> {smartphone._Smartphone__price}')  # atrybut prywatny
