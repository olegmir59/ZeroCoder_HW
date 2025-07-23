def bank(a, years):
    rate = 0.1     # Годовой процент доходности (10%)
    future_value = a * (1 + rate)**years
    return round(future_value, 2)  # Округляем до 2 знаков после запятой


# Пример использования функции
initial_deposit = float(input("Введите сумму первоначального вклада: "))
deposit_years = int(input("Введите срок вклада в годах: "))
final_amount = bank(initial_deposit, deposit_years)

print(f"Через {deposit_years} лет сумма на вашем счете составит: {final_amount} руб.")