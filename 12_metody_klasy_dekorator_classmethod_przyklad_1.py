"""
The selected code demonstrates using the @classmethod decorator to define a class method 
called show() on the Phone class. 

The show() method prints out all instances of the Phone class that have been created. It 
accesses the instances class attribute to get the list of Phone instances.

Two Phone instances (phone1 and phone2) are created to demonstrate the show() class method 
printing out those instances.
"""
class Phone:

    instances = []

    def __init__(self):
        Phone.instances.append(self)

    @classmethod
    def show(cls):
        if len(Phone.instances) > 0:
            print(f'List of instances of the {Phone.__name__} class:')
            for instance in Phone.instances:
                print(f'\t{instance}')
        else:
            print(f'There is no instance of the {Phone.__name__} class.')

Phone.__dict__
Phone.show()
phone1 = Phone()
phone2 = Phone()
Phone.show()

class Phone:

    instances = []

    def __init__(self):
        Phone.instances.append(self)

    @classmethod
    def show(cls):
        if len(cls.instances) > 0:
            print(f'List of instances of the {cls.__name__} class:')
            for instance in cls.instances:
                print(f'\t{instance}')
        else:
            print(f'There is no instance of the {cls.__name__} class.')

Phone.__dict__
Phone.show()
phone1 = Phone()
phone2 = Phone()

Phone.show()