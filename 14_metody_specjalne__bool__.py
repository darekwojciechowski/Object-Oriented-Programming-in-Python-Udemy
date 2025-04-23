#   161. Metoda __bool__()
#   14_metody_specjalne__bool__

class Point:

    def __init__(self, *coords):
        for value in coords:
            if not isinstance(value, (int, float)):
                raise ValueError('Coordinates must be of type int or float.')
        self._coords = coords

    def __repr__(self):
        return f"Point(coords={self._coords})"

    def __len__(self):
        return len(self._coords)

    @property
    def coords(self):
        return self._coords


p = Point()
q = Point(4, 2)
bool(p), bool(q)  # (False, True)


class Point:

    def __init__(self, *coords):
        for value in coords:
            if not isinstance(value, (int, float)):
                raise ValueError('Coordinates must be of type int or float.')
        self._coords = coords

    def __repr__(self):
        return f"Point(coords={self._coords})"

    def __len__(self):
        return len(self._coords)

    def __bool__(self):
        return sum(self._coords) != 0

    @property
    def coords(self):
        return self._coords


p = Point(1, 2)
bool(p)
p = Point(1, 2, -3)
bool(p)
p = Point()
bool(p)
