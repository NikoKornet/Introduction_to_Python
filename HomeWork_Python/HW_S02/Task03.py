# 03. Реализуйте алгоритм перемешивания списка.
# Встроенный алгоритм SHUFFLE не использовать!
# Реализовать свой метод.

from random import randint

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(my_list) - 1):
    elem = my_list[i]
    my_list.pop(i)
    my_list.insert(randint(0, len(my_list)), elem)

print(my_list)
