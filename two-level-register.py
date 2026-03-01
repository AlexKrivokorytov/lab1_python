# two_level_register.py
# Вхідні дані для завдання "Дворівневий реєстр"

exam_results = [
    ("Shevchenko", "Data Bases", 95),
    ("Shevchenko", "Operating Systems", 88),
    ("Shevchenko", "Computer Networks", 91),

    ("Petrenko", "Data Bases", 87),
    ("Petrenko", "Operating Systems", 88),
    ("Petrenko", "Algorithms", 90),

    ("Ivanenko", "Data Bases", 78),
    ("Ivanenko", "Algorithms", 85),
    ("Ivanenko", "Discrete Math", 82),

    ("Koval", "Operating Systems", 91),
    ("Koval", "Computer Networks", 89),
    ("Koval", "Databases Security", 86),

    ("Bondarenko", "Algorithms", 92),
    ("Bondarenko", "Data Bases", 90),
    ("Bondarenko", "Discrete Math", 88),

    ("Tkachenko", "Operating Systems", 84),
    ("Tkachenko", "Computer Networks", 87),
    ("Tkachenko", "Data Bases", 80),

    ("Moroz", "Algorithms", 76),
    ("Moroz", "Discrete Math", 79),
    ("Moroz", "Data Bases", 75),

    ("Lysenko", "Computer Networks", 93),
    ("Lysenko", "Operating Systems", 90),
    ("Lysenko", "Databases Security", 88),

    ("Hrytsenko", "Algorithms", 89),
    ("Hrytsenko", "Discrete Math", 91),
    ("Hrytsenko", "Data Bases", 92),

    ("Romanenko", "Operating Systems", 85),
    ("Romanenko", "Computer Networks", 83),
    ("Romanenko", "Data Bases", 88),

    ("Savchenko", "Algorithms", 94),
    ("Savchenko", "Data Bases", 93),
    ("Savchenko", "Discrete Math", 90),

    ("Kravchenko", "Operating Systems", 82),
    ("Kravchenko", "Computer Networks", 80),
    ("Kravchenko", "Algorithms", 78),
]

register = {}

for student, subject, grade in exam_results:
    if student not in register:
        register[student] = {}
    register[student][subject] = grade

print(register["Shevchenko"]["Data Bases"])