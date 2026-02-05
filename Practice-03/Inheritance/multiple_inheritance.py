# Көптік мұрагерлік

class Athlete:
    def train(self):
        print("Жаттығу жасап жатыр")

class Student:
    def study(self):
        print("Сабақ оқып жатыр")

class SportsStudent(Athlete, Student):
    pass

ss = SportsStudent()
ss.train()
ss.study()
