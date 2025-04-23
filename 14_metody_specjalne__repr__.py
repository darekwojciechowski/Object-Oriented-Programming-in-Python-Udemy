# The selected code demonstrates the __repr__ method in Python.
# __repr__ returns a string representation of the object, meant to be unambiguous.
# A Phone class is defined, with a __repr__ method that returns a representation of the Phone instance.
# The __repr__ of Phone instances is shown, as well as constructing a new Phone instance from the __repr__ string.
help(object.__repr__)

#   __repr__ -> zwraca formalną reprezentacje obiektu
repr(object)


class Phone:

    def __init__(self, brand):
        self.brand = brand


Phone.__dict__

Phone
repr(Phone)
print(Phone)
# No code was selected, so no documentation can be generated.
phone = Phone('Apple')

phone
repr(phone)
print(phone)


class Phone:

    def __init__(self, brand):
        self.brand = brand

    def __repr__(self):
        return f"Phone(brand='{self.brand}')"


Phone.__dict__

phone = Phone('Apple')
phone

repr(phone)
eval(repr(phone))
phone2 = eval(repr(phone))
phone2.brand
