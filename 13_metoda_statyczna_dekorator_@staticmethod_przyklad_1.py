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