#   14 rozszerzone przypisanie__iadd__
'''
operator	metoda
+=	object.__iadd__(self, other)
-=	object.__isub__(self, other)
*=	object.__imul__(self, other)
/=	object.__itruediv__(self, other)
'''


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

    def __iadd__(self, other):
        if not isinstance(other, Doc):
            return NotImplemented
        return Doc(self.string + '-' + other.string)


Doc.__dict__

doc1 = Doc('Object')
doc2 = Doc('Oriented')
doc3 = Doc('Programming')
doc1
doc1 += doc2
doc1
