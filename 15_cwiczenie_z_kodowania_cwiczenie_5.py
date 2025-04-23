'''
Ćwiczenie 5
Załóżmy, że pracujesz nad programem, który modeluje system szkolny. Masz klasę bazową o nazwie Person, która ma następujące atrybuty:

    name: imię osoby
    age: wiek osoby
    gender: płeć osoby

Potrzebujesz utworzyć dwie podklasy klasy Person o nazwie Student oraz Teacher.

    Klasa Student powinna mieć następujące dodatkowe atrybuty:
    grade: poziom oceny ucznia (liczba całkowita z przedziału od 1 do 12)
    gpa: średnia ocen ucznia (liczba zmiennoprzecinkowa między 0,0 a 4,0)

Klasa Teacher powinna mieć następujące dodatkowe atrybuty:
    subject: przedmiot, którego uczy nauczyciel (ciąg znaków)
    years_of_experience: liczba lat doświadczenia w nauczaniu nauczyciela (liczba całkowita)

Zdefiniuj podane klasy z wymaganymi atrybutami i przetestuj swoją implementację, tworząc trzy poniższe obiekty:

    person = Person('Alice', 25, 'female')
    student = Student('Bob', 17, 'male', 11, 3.5)
    teacher = Teacher('Carol', 35, 'female', 'Math', 10)

Wystarczy zaimplementować klasy Student oraz Teacher i utworzyć podane obiekty. Zaimplementowane testy jednostkowe sprawdzają poprawność rozwiązania.
'''


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):
    def __init__(self, name, age, gender, grade, gpa):
        super().__init__(name, age, gender)
        self.grade = grade
        self.gpa = gpa


class Teacher(Person):
    def __init__(self, name, age, gender, subject, years_of_experience):
        super().__init__(name, age, gender)
        self.subject = subject
        self.years_of_experience = years_of_experience


person = Person('Alice', 25, 'female')
student = Student('Bob', 17, 'male', 11, 3.5)
teacher = Teacher('Carol', 35, 'female', 'Math', 10)
