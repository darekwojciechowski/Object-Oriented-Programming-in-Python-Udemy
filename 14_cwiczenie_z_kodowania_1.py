'''
Ćwiczenie 1
Zdefiniuj klasę Worker przyjmującą dwa atrybuty publiczne fname 
(first name) oraz lname (last name). Następnie zaimplementuj metodę 
specjalną __repr__() pozwalającą wyświetlić formalną reprezentację 
obiektu klasy Worker tak jak pokazano poniżej:

[IN]: worker = Worker('John', 'Doe')
[IN]: print(worker)
[OUT]: Worker(fname='John', lname='Doe')

Utwórz instancję klasy Worker z podanymi atrybutami i przypisz do
zmiennej worker.

fname = 'Mike'
lname = 'Smith'

W odpowiedzi wydrukuj instancję worker do konsoli.

Oczekiwany wynik:
Worker(fname='Mike', lname='Smith')
'''


class Worker:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f"Worker(fname='{self.fname}', lname='{self.lname}')"


worker = Worker('Mike', 'Smith')
print(worker)
