# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

num = int(input("Введите число обозначающее день недели: "))

if num == 6 or num == 7:
    print("Да, выходной!")
elif num > 7:
    print("Введите корректное число!")
else:
    print("Нет, это не выходной((")