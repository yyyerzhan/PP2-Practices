# sorted() + lambda

students = [
    ("Ержан", 90),
    ("Айдана", 85),
    ("Мадина", 95)
]

# Балл бойынша сұрыптау
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
