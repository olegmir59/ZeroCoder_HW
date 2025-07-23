num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

operation = input("Введите операцию (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Ошибка: деление на ноль!"
    case _:
        result = "Неправильная операция."

print("Результат:", result)
