'''
Podstawowe operatory:

+	object.__add__(self, other)
-	object.__sub__(self, other)
*	object.__mul__(self, other)
//	object.__floordiv__(self, other)
/	object.__truediv__(self, other)
%	object.__mod__(self, other[, modulo])
**	object.__pow__(self, other)

Przykładowo, przy wywołaniu:

a + b
zostanie wywołana metoda

a.__add__(b)
'''

print('hello world!')

class Point:

    def __init__(self, *coords):
        for value in coords:
            if not isinstance(value, (int, float)):
                raise ValueError('Coordinates must be of type int or float.')
        self._coords = coords

    def __repr__(self):
        return f"Point(coords={self._coords})"

    @property
    def coords(self):
        return self._coords

p1 = Point(4, 2)
p2 = Point(5, 2)
p1 + p2