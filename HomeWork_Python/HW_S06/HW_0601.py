# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# - 6782 -> 23
# - 0,56 -> 11

number = input('Введите вещественное число: ')
number = float(number)
number = abs(number)
sum_digits = sum(map(int, str(number).replace('.', '')))
print(f"Сумма цифр числа -> {sum_digits}")