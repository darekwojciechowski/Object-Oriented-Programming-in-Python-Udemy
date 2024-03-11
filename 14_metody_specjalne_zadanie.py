#   14 metody specjalne zadanie
'''
Zbuduj klasę o nazwie Integer, która imitować będzie liczbę całkowitą.
Zaimplementuj poniższe:

metodę __init__(), jeżeli użytkownik nie przekaże żadnego argumentu ustaw wartość 0.
metodę __str__() będącą nieformalną reprezentacją obiektu
metodę __repr__() będącą formalną reprezentacją obiektu
metodę __add__(), która pozwala na dodawanie obiektów klasy Integer
metodę __sub__(), która pozwala na odejmowanie obiektów klasy Integer
'''
class Integer:

    def __init__(self, val=0):
        self.val = int(val)

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return f"Integer({self.val})"

    def __add__(self, other):
        if not isinstance(other, Integer):
            return NotImplemented
        return Integer(self.val + other.val)

    def __sub__(self, other):
        if not isinstance(other, Integer):
            return NotImplemented
        return Integer(self.val - other.val)    

x = Integer(3)
x

y = Integer()
y

z = Integer(-4)
z

x + z
x - z
print(x)
print(y)
print(z)