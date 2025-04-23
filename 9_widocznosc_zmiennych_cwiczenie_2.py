'''
Ćwiczenie 2
Zaimplementowano klasę o nazwie Smartphone, która przy tworzeniu instancji ustawia poniższe atrybuty instancji:

    brand jako atrybut publiczny
    model jako atrybut chroniony
    price jako atrybut prywatny

Następnie utworzono instancję klasy Smartphone o nazwie smartphone o podanych parametrach:

    'Huawei'
    'Mate 20 Pro'
    1999

W odpowiedzi wydrukuj wartość dla każdego atrybutu (w osobnej linii) instancji smartphone tak jak pokazano poniżej.

Oczekiwany wynik:
    brand -> Huawei
    model -> Mate 20 Pro
    price -> 1999
'''


class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self.__price = price


smartphone = Smartphone('Huawei', 'Mate 20 Pro', 1999)
print(f'brand -> {smartphone.brand}')
print(f'model -> {smartphone._model}')
print(f'price -> {smartphone._Smartphone__price}')
