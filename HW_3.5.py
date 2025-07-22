# Запрашиваем у пользователя сумму, которую он хочет конвертировать
amount = float(input("Введите сумму для конвертации: "))

# Ввод целевой валюты (в какую валюту хотим перевести)
target_currency = input("Введите целевую валюту (например, EUR): ").strip().upper()

# Ручной ввод курса обмена (однократно)
exchange_rate = float(input(f"Введите курс обмена {target_currency}/валюта введенной суммы: "))

# Расчёт суммы в новой валюте
converted_amount = amount / exchange_rate

# Вывод результата
print(f"{amount}  эквивалентно {converted_amount:.2f} {target_currency}")
