#   14_operator_porownania__it__le__
'''
The lt method in Python is used to define behavior for the less than (<) operator between objects of a class.

Here are some key points about lt:

It allows you to compare two objects of the same class using <, e.g. a < b.

lt should return True if self is considered less than other, and False otherwise.

This method is part of a group of rich comparison methods that also includes gt, le, ge in addition to eq and ne.

When defining lt, it's a good idea to define the other related methods too for consistency.

lt should implement a total ordering relationship. If a < b and b < c then a < c should also be True.

The method should also satisfy symmetry and transitivity principles to avoid unexpected behavior.

If lt is not defined, the default < falls back to comparing object identities - id(self) < id(other).

So lt needs to be overridden to enable a meaningful ordering based on the contents of class instances.

Common examples are ordering objects based on a numeric field or lexicographic ordering on a string field.

So in summary, lt allows customized ordering logic for objects of a class using the < operator. It should be implemented along with the other rich comparison methods to get a consistent ordering.
'''
#   metoda __le__ less then


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

    def __lt__(self, other):
        if not isinstance(other, Doc):
            return NotImplemented
        return len(self.string) < len(other.string)

    def __le__(self, other):
        if not isinstance(other, Doc):
            return NotImplemented
        return len(self.string) <= len(other.string)


doc1 = Doc('AB')
doc2 = Doc('XYZ')
doc1, doc2
doc1 <= doc2

doc1 = Doc('ABCD')
doc2 = Doc('XYZ')
doc1, doc2
doc1 <= doc2
doc1 < doc2
doc1 <= doc2

doc1 = Doc('ABC')
doc2 = Doc('XYZ')
doc1, doc2
doc1 <= doc2
