'''
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
        self.brand = brand
        self._model = model
        self.__price = price


smartphone = Smartphone('Huawei', 'Mate 20 Pro', 1999)
print(smartphone.__dict__)
