def sum_range(start, end):
    """
    Суммирует все целые числа от start до end включительно.
    :param start: Начальное число диапазона
    :param end: Конечное число диапазона
    :return: Сумма всех целых чисел от start до end включительно
    """
    total = 0
    for num in range(start, end + 1):
        total += num
    return total


# Пример использования функции
result = sum_range(5, 25)
print("Сумма чисел от 1 до 5:", result)
