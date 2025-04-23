help(object.__str__)

help(str)


class Phone:

    def __init__(self, brand):
        self.brand = brand

    def __repr__(self):
        return f"Phone(brand='{self.brand}')"

    def __str__(self):
        return f'{self.brand} brand mobile phone.'


phone = Phone('Apple')
phone

repr(phone)
str(phone)
repr(phone)
phone.__repr__()
phone.__str__()


class Phone:

    def __init__(self, brand):
        self.brand = brand

    # def __repr__(self):
    #     return f"Phone(brand='{self.brand}')"

    def __str__(self):
        return f'{self.brand} brand mobile phone.'


phone = Phone('Apple')
phone

print(phone)
