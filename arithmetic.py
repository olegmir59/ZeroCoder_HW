def add(x, y):
    """Функция сложения"""
    return x + y

def subtract(x, y):
    """Функция вычитания"""
    return x - y

def multiply(x, y):
    """Функция умножения"""
    return x * y

def divide(x, y):
    """Функция деления"""
    if y == 0:
        print("Делить на ноль нельзя!")
        return None
    else:
        return x / y
