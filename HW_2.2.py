# Домашнее задание 2 №2  21.07.2025    выполнил Олег Мироненко
# Заданние:
# Напиши программу на Питоне для решения задачи:
# Сжатие Строки: Дана строка, состоящая из букв. Напишите программу, которая сжимает строку, используя счетчик повторяющихся символов.
# Например, строка "aabcccccaaa" должна превратиться в "a2b1c5a3".

def compress_string(s):
    result = []
    i = 0
    n = len(s)

    while i < n:
        current_char = s[i]
        count = 1

        # Подсчет подряд идущих одинаковых символов
        while i + 1 < n and s[i + 1] == current_char:
            count += 1
            i += 1

        # Добавляем символ и его количество в результирующую строку
        result.append(current_char + str(count))
        i += 1

    return ''.join(result)

# Тестирование функции
test_str = "aabcccccaaa"
compressed = compress_string(test_str)
print(compressed)  # a2b1c5a3

test_str = "aabbbbbbbbbbbbbbbbbbbbbbbbcccccaaa"
compressed = compress_string(test_str)
print(compressed)  # aabbbbbbbbbbbbbbbbbbbbbbbbcccccaaa
