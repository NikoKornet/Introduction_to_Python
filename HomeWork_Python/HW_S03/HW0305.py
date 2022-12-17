# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input("Введите число: "))

fib = [0, 1]
for i in range(2, number + 1):
    fib.append(fib[-1] + fib[-2])

for i in range(number):
    fib = [fib[1] - fib[0]] + fib

print(f"Для числа {number} список будет таким: {fib}")