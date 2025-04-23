'''
Ćwiczenie 1
Zdefiniuj klasę Container, która będzie posiadać metodę statyczną (wykorzystaj dekorator
@staticmethod) o nazwie get_current_time() zwracającą aktualny czas w 
formacie '%H:%M:%S', 
np. '09:45:10'.
'''

import time


class Container:
    @staticmethod
    def get_current_time():
        return time.strftime('%H:%M:%S', time.localtime())


info = Container.get_current_time()
print(info)
print(info)
time.sleep(2)
print(info)
