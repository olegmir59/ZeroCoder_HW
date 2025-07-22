# Домашнее задание 3 №1  22.07.2025    выполнил Олег Мироненко
# Заданние:
# Напиши программу на Питоне для решения задачи:
# Создать калькулятор — программу, в которой мы вводим 2 числа,
# и с ними производятся сразу все математические действия


num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Выполняем различные арифметические операции
addition = num1 + num2           # сложение
subtraction = num1 - num2        # вычитание
multiplication = num1 * num2     # умножение
division = num1 / num2           # деление (обычное)
integer_division = num1 // num2  # целочисленное деление
remainder = num1 % num2          # остаток от деления

# Выводим результаты операций
print(f"Сложение: {num1} + {num2} = {addition:.2f}")
print(f"Вычитание: {num1} - {num2} = {subtraction:.2f}")
print(f"Умножение: {num1} * {num2} = {multiplication:.2f}")
print(f"Деление: {num1} / {num2} = {division:.2f}")
print(f"Целочисленное деление: {num1} // {num2} = {integer_division:.2f}")
print(f"Остаток от деления: {num1} % {num2} = {remainder:.2f}")