def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


# Демонстрация работы функции
print(safe_divide(10, 2))      # Нормальное деление, результат: 5.0
print(safe_divide(10, 0))      # Деление на ноль, результат: None
print(safe_divide(10, -5))       # Нормальное деление, результат: -2.0
print(safe_divide(0, 10))      # Деление нуля, результат: 0.0