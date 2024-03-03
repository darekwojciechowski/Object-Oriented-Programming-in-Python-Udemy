"""
Demonstrates using a classmethod to keep track of all 
instances of a class.

The Phone class keeps a list of all Phone instances in the
Phone.instances class attribute. 

The show() classmethod prints information about the 
instances.

Two Phone instances are created, and the show() method is
called to print information about them.
"""
class Phone:

    instances = []

    def __init__(self, brand):
        self.brand = brand
        Phone.instances.append(self)

    @classmethod
    def show(cls):
        if len(cls.instances) > 0:
            print(f'List of instances of the {cls.__name__} class:')
            for instance in cls.instances:
                print(f'\t{instance}')
        else:
            print(f'There is no instance of the {cls.__name__} class.')

    def show_brand(self):
        print(f'Brand: {self.brand}')
    
phone1 = Phone('Apple')
phone2 = Phone('Samsung')

Phone.show()

for instance in Phone.instances:
    instance.show_brand()