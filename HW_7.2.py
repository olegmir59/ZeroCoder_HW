while True:
    user_input = input("Введите целое число: ")
    try:
        integer_value = int(user_input)
        print(f"Вы ввели корректное целое число: {integer_value}")
        break

    except ValueError:
        print("Невозможно преобразовать введенное значение в целое число. Попробуйте еще раз.")
#    except TypeError:
#        print("Введено значение неподходящего типа")