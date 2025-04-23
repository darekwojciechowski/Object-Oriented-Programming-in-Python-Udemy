'''
Metody specjalne -> “dunder” (double-underscore) methods
__new__
__init__
__del__
__str__
__repr__
__len__
__bool__
'''

print(dir(object))


class Company:
    'The Company class docs.'

    def __init__(self, name):
        self.name = name


company = Company('Microsoft')
company.__dict__

company2 = Company.__new__(Company)
company2.__init__('Microsoft')
company2.__dict__
