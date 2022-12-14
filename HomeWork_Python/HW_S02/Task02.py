# 02. Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывести в консоль сам список и сумму его элементов.

number = int(input("Введите число: "))
sum_res = 0
my_list = []

for i in range(1, number + 1):
    my_list.append(round(((1 + 1 / i) ** i), 2))

for j in my_list:
    sum_res += j

print(my_list)
print(f"Сумма элементов списка -> {sum_res}")
