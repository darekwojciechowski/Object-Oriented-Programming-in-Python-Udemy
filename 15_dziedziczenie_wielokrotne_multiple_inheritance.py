#   Dziedziczenie wielokrotne - Multiple Inheritance

class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Department:

    def __init__(self, dept_name):
        self.dept_name = dept_name


class Worker(Person, Department):

    def __init__(self, first_name, last_name, age, dept_name, hours_per_day=8):
        Person.__init__(self, first_name, last_name, age)
        Department.__init__(self, dept_name)
        self.hours_per_day = hours_per_day


class Menager(Person, Department):

    def __init__(self, first_name, last_name, age, dept_name, is_founder=False):
        Person.__init__(self, first_name, last_name, age)
        Department.__init__(self, dept_name)
        self.is_founder = is_founder


worker = Worker('John', 'Smith', 40, 'IT')
worker.__dict__

m = Menager('Mark', 'Smith', 35, 'IT', True)
m.__dict__

m = Menager('Mark', 'Smith', 35, 'IT')
m.__dict__
