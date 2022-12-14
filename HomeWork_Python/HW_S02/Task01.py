# 01. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def func_sum_digits(num):
    sum_digits = 0
    for i in num:
        if i.isdigit():
            sum_digits += int(i)
    return sum_digits


number = input("Введите число: ")
print(f"{number} -> {func_sum_digits(number)}")

