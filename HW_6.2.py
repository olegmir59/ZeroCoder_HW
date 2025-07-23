import math


def square(side):
    perimeter = 4 * side              # Периметр квадрата
    area = side ** 2                  # Площадь квадрата
    diagonal = side * math.sqrt(2)    # Диагональ квадрата
    return perimeter, area, diagonal  # Возвращаем кортеж из трех значений


# Пример использования функции
side_length = float(input("Введите длину стороны квадрата: "))
perimeter, area, diagonal = square(side_length)

print(f"Периметр квадрата: {perimeter}")
print(f"Площадь квадрата: {area}")
print(f"Диагональ квадрата: {diagonal:.2f}")
