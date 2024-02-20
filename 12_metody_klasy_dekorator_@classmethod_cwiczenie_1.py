'''
Ćwiczenie 1
Zaimplementuj klasę o nazwie Worker, która będzie posiadać atrybut klasy o
nazwie instances będący pustą listą. Następnie przy każdym utworzeniu instancji 
klasy Worker dodawaj ją do listy Worker.instances (wykorzystaj do 
tego metodę __init__()).

Zaimplementuj także metodę klasy o nazwie count_instances() pozwalającą zwrócić
liczbę utworzonych obiektów klasy Worker (liczbę elementów listy
Worker.instances).

Utwórz w dowolny sposób trzy instancje klasy Worker, następnie wydrukuj do
konsoli wywołanie metody count_instances().

Oczekiwany wynik:
3
'''
class Worker:
    instances = []
 
    def __init__(self):
        Worker.instances.append(self)
    
    @classmethod
    def count_instances(cls):
        return len(Worker.instances)
 
 
p1 = Worker()
p2 = Worker()
p3 = Worker()
print(Worker.count_instances())

