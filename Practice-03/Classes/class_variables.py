# Class variable vs Instance variable

class Student:
    school = "AITU"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

s1 = Student("Ержан")
s2 = Student("Айдана")

print(s1.school)
print(s2.school)
