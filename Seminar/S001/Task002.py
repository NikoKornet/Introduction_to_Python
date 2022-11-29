# 2. Напишите программу, которая на вход принимает 5 чисел и
# находит максимальное из них.
#
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

numbers = []
for i in range(1, 6):
    numbers.append(int(input(f'Введите {i} число: ')))

max = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
print(numbers)
print(max)
