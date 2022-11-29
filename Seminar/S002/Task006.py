# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# number = int(input("Введите число: "))
# my_list = []
# for i in range(1, number + 1):
#     my_list.append(f'{i} : {3 * i + 1}')
# print(*my_list, sep=' , ')

# for j in range(1, number + 1):
#     print(f'{j} : {3 * j + 1}', end=', ')

# Решение через словарь

number = int(input("Введите число: "))
my_dict = {}

for i in range(1, number + 1):
    my_dict[i] = 3 * i + 1

print(my_dict)
