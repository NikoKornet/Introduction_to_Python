# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

my_list = input("Введите числа через пробел: ").split(" ")
print(min(my_list))
print(max(my_list))