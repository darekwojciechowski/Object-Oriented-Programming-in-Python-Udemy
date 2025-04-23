'''
Operatory porównania
operator	metoda
<	object.__lt__(self, other)
<=	object.__le__(self, other)
>	object.__gt__(self, other)
>=	object.__ge__(self, other)
==	object.__eq__(self, other)
!=	object.__ne__(self, other)
'''
'''
The eq method in Python is used to define behavior for the equality operator == between objects of a class.
Here are a few key points about eq:

*It is one of the "dunder" or double underscore special methods in Python. These methods allow you to define custom behavior for built-in operators and functions.
eq is called when you use the == operator to compare two objects of the same class, e.g. a == b.

*The eq method should return True if the objects are considered equal, and False otherwise.

*The default eq implementation compares object identities - two objects are considered equal only if they are the exact same object in memory.

*To make a meaningful equality comparison for a class, eq needs to be overridden to compare the actual contents of the objects.

*When overriding eq, it's important to also override ne (not equal) for consistency.

*eq and other rich comparison methods should follow certain conventions like symmetry and transitivity to avoid confusing behavior.

So in summary, eq allows you to customize equality comparison behavior for classes in Python. Overriding it is necessary to get meaningful identity-based comparison rather than default object identity comparison.'''

help(object.__eq__)


class Doc:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        if not isinstance(other, Doc):
            return NotImplemented
        return Doc(self.string + ' ' + other.string)

    def __eq__(self, other):
        if not isinstance(other, Doc):
            return False
        return len(self.string) == len(other.string)


doc1 = Doc('ABC')
doc2 = Doc('XYZ')
doc1, doc2
doc1 == doc2
doc1 != doc2
id(doc1), id(doc2)

doc1 = Doc('ABCD')
doc2 = Doc('XYZ')
doc1, doc2
doc1 == doc2
doc1 != doc2
id(doc1), id(doc2)
