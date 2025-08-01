import random

# Список учеников
students = [
    "Олег",
    "Вера",
    "Александра",
    "Ярослав",
    "Иван",
    "Марина",
    "Сергей",
    "Анна",
    "Ольга",
    "Максим",
    "Светлана"
]

# Выбираем 5 уникальных учеников случайным образом
selected_students = random.sample(students, k=5)

print("Сегодня отвечают следующие ученики:")
for student in selected_students:
    print(student)
