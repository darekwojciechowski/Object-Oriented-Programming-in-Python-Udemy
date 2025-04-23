"""
Demonstrates using the __len__() special method to define custom length 
behavior for a class, allowing len() to be called on instances.

Defines a Point class with coords stored in self._coords. 
Implements __len__() to return length of coords.

Creates Point instances and shows accessing .coords property, 
calling len() on instances, etc.
"""
"""
Demonstrates using the __len__ magic method to allow the len() 
function to be called on custom classes, returning the length of 
the _coords attribute.

Also shows using __repr__ to customize the string representation.
"""

help(len)


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


p = Point(3, 4)
p.__dict__
p.coords
p
repr(p)

p = Point(3, 4, -4)
p.__dict__

''' error
p = Point(3, 4, 'var2')
p.__dict__
'''

q = Point(4, 2, 5)
q.coords
len(q)
q.__len__()
q = Point()
q.coords
len(q)
