class Student:

    students = []
    limit = 3

    def __new__(cls):
        if len(cls.students) >= cls.limit:
            raise RuntimeError(f'Instance limit reached: {cls.limit}')
        instance = object.__new__(cls)
        cls.students.append(instance)
        return instance
    

s1 = Student()
s2 = Student()
s3 = Student()

Student.__dict__
Student.students


#s4 = Student() error