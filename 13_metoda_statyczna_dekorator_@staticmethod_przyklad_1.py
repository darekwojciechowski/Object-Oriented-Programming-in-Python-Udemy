"""Demonstrates using the @staticmethod decorator to define a static method 
get_current_time() on the Phone class. This allows getting the current time 
without having to instantiate a Phone instance. 

Instances of Phone are created, passing self to __init__ which calls the static
get_current_time() to set creation_time. 

Phone.instances is used to keep a list of all Phone instances.

The instances are printed out along with their creation times to show that 
they were created at different times.
"""
import time

class Phone:

    instances = []

    def __init__(self):
        self.creation_time = Phone.get_current_time()
        Phone.instances.append(self)

    @staticmethod
    def get_current_time():
        return time.strftime('%H:%M:%S', time.localtime())

Phone.__dict__

phone1 = Phone()
time.sleep(1)
phone2 = Phone()
time.sleep(2)
phone3 = Phone()

Phone.instances
for instance in Phone.instances:
    print(instance.creation_time, instance)