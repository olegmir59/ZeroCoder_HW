start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

for num in range(start, end + 1):
    if num % 2 == 0:
        print(num)
