import random
options = ["камень", "ножницы", "бумага"]
player_score = 0
computer_score = 0
while True:
    player_choice = input("Ваша очередь (камень/ножницы/бумага)? ").lower()
    if player_choice not in options:
        print("Некорректный выбор. Попробуйте снова.")
        continue
    computer_choice = random.choice(options)
    print(f"Компьютер выбрал: {computer_choice}")
    if player_choice == computer_choice:
        print("Ничья!")
    elif (player_choice == "камень" and computer_choice == "ножницы") or \
         (player_choice == "бумага" and computer_choice == "камень") or \
         (player_choice == "ножницы" and computer_choice == "бумага"):
        print("Вы выиграли раунд!")
        player_score += 1
    else:
        print("Компьютер выиграл раунд!")
        computer_score += 1
    if player_score >= 3:
        print("Вы победили в игре!")
        break
    elif computer_score >= 3:
        print("Компьютер победил в игре!")
        break
