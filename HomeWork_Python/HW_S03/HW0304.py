# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроенных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

number = int(input("Введите десятичное число: "))
binary_number = " "

while number > 0:
    binary_number = str(number % 2) + binary_number
    number //= 2

print(binary_number)


