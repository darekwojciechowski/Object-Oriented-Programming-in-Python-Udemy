class Phone:
    """Phone class docs."""

    def __init__(self, price):
        self._price = price

    def get_price(self):
        print('getting...')
        return self._price

    def set_price(self, value):
        print('setting...')
        if isinstance(value, (int, float)):
            if value > 0:
                self._price = value
            else:
                raise ValueError('The price attribute must be positive.')
        else:
            raise TypeError('The price attribute must be an int or float value.')

    def del_price(self):
        print('deleting...')
        del self._price

    price = property(fget=get_price, fset=set_price, fdel=del_price, doc='Phone price.')

help(Phone)