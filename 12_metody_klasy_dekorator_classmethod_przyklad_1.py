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