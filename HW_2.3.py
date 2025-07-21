# Домашнее задание 2 №3  21.07.2025    выполнил Олег Мироненко
# Заданние:
# Напиши программу на Питоне для решения задачи:
# Шифр Цезаря:
# Реализуйте функцию шифрования и дешифрования текста с помощью шифра Цезаря, где сдвиг задается пользователем.

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Проверка, является ли символ буквой
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Применяем сдвиг с учётом цикличности алфавита
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += shifted_char
        else:
            encrypted_text += char  # Оставляем остальные символы неизменными
    return encrypted_text


def caesar_decrypt(ciphered_text, shift):
    decrypted_text = ""
    for char in ciphered_text:
        if char.isalpha():  # Проверка, является ли символ буквой
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Применяем обратный сдвиг
            original_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += original_char
        else:
            decrypted_text += char  # Оставляем остальные символы неизменными
    return decrypted_text


# Примеры использования
shift_value = int(input("Введите величину сдвига: "))
original_message = input("Введите сообщение для шифрования: ")
encrypted_message = caesar_encrypt(original_message, shift_value)
decrypted_message = caesar_decrypt(encrypted_message, shift_value)

print("Оригинальное сообщение:", original_message)
print("Зашифрованное сообщение:", encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)