number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))
number3 = float(input("Введите третье число: "))
minimum_number = min(number1, number2, number3)
print("Наименьшее число:", minimum_number)

print(" используя условый оператор if, elif, else   По теме урока!")
if number1 <= number2 and number1 <= number3:
    minimum_number = number1
elif number2 <= number1 and number2 <= number3:
    minimum_number = number2
else:
    minimum_number = number3
print("Наименьшее число:", minimum_number)