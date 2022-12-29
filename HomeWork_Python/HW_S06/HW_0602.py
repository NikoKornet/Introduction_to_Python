# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];

my_list = [2, 3, 4, 5, 6]


def multiplication(new_list):
    result_list = []
    for (i, j) in zip(new_list[0: int(len(new_list) / 2 + 1): 1],
                      new_list[-1: int(len(new_list) / 2 - 1): -1]):
        result_list.append(i * j)
    return result_list


print(f"Произведения пар чисел списка -> {multiplication(my_list)}")
