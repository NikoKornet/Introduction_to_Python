# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# real_number_list = [1.1, 1.2, 3.1, 5, 10.01]

real_number_list = [1.1, 1.2, 3.1, 5, 10.01, 6.5, 2.3]
print(real_number_list)

result_list = []
for i in real_number_list:
    elem = i - int(i)
    if elem != 0:
        result_list.append(round(elem, 2))
print(f"Разница между максимальным и минимальным значением дробной части => {max(result_list) - min(result_list)}")
