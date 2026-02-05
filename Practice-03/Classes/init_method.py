# __init__ конструкторы

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ержан", 19)
print(s1.name, s1.age)
