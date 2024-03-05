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

class Point:

    def __init__(self, *coords):
        for value in coords:
            if not isinstance(value, (int, float)):
                raise ValueError('Coordinates must be of type int or float.')
        self._coords = coords

    def __repr__(self):
        return f"Point(coords={self._coords})"

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        coords = tuple(x + y for x, y in zip(self.coords, other.coords))
        return Point(*coords)

    @property
    def coords(self):
        return self._coords

p1 = Point(4, 2)
p2 = Point(5, 2)
p1 + p2
p1.__add__(p2)
p1 + 5

#p1 + 'var1'
#p1 + False