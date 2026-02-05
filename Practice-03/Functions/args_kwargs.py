# *args және **kwargs қолдану

def show_scores(*scores):
    """Кез келген сандағы балдарды қабылдайды"""
    print("Бағалар:", scores)

def student_info(**info):
    """Аты-жөні, жасы сияқты мәліметтерді қабылдайды"""
    for key, value in info.items():
        print(f"{key}: {value}")

show_scores(90, 85, 88)
student_info(name="Ержан", age=19, city="Алматы")
