'''
Ćwiczenie 2
Załóżmy, że pracujesz nad klasą o nazwie Student, która ma następujące atrybuty:

name: imię i nazwisko ucznia
age: wiek ucznia
gpa: średnia ocen ucznia

Zaimplementuj metodę na poziomie klasy Student o nazwie from_csv(cls, csv_string),
która tworzy nowy obiekt ucznia przy użyciu ciągu wartości oddzielonych przecinkami
(csv_string), gdzie wartości są w następującej kolejności: imię, wiek, średnia ocen.

Kolejno utwórz instancję klasy Student z poniższego ciągu wykorzystując zaimplementowaną
metodę from_csv()):
'Alice,22,3.5'

W odpowiedzi wydrukuj atrybut __dict__ tak utworzonej instancji.
'''

class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
 
    @classmethod
    def from_csv(cls, csv_string):
        values = csv_string.split(',')
        name = values[0]
        age = int(values[1])
        gpa = float(values[2])
        return cls(name, age, gpa)
 
 
csv_string = 'Alice,22,3.5'
student = Student.from_csv(csv_string)
print(student.__dict__)