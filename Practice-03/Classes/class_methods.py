# Instance method және self

class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Сәлем, менің атым {self.name}")

student = Student("Айдана")
student.greet()
