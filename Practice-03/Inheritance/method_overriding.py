# Методты қайта жазу (override)

class Person:
    def speak(self):
        print("Мен сөйлеп жатырмын")

class Student(Person):
    def speak(self):
        print("Мен студентпін және сөйлеп жатырмын")

s = Student()
s.speak()
