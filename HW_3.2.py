# Запрашиваем имя и возраст пользователя
name = input("Введи своё имя: ")
age = int(input("Введи свой возраст: "))

# Рассчитываем месяцы, дни и часы жизни
months = age * 12  # Месяцы = годы × 12
days = age * 365   # Приблизительно считаем 365 дней в году
hours = days * 24   # Часы = дни × 24 часа

# Выводим результат
print(f"Привет {name}! Тебе {age} лет.")
print(f"Ты прожил примерно {months} месяцев, {days} дней и {hours} часов.")
