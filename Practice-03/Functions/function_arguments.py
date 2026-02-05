# Функция аргументтері: позициялық және әдепкі (default)

def introduce(name, age=18):
    """
    Адам туралы ақпарат шығарады
    name - аты
    age - жасы (әдепкісі 18)
    """
    print(f"Аты: {name}, Жасы: {age}")

introduce("Ержан", 19)
introduce("Айдана")
