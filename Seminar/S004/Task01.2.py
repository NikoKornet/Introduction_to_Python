from decimal import Decimal

number = Decimal(input("Введите число: "))
original = number


def sum_digits(num: int): # Решение без строковых методов
    summa = 0
    while num > 0:
        summa += num % 10
        num //= 10
    return summa


while (number != int(number)):
    number *= 10

result = sum_digits(number)
print(number)
print(f"Сумма цифр в числе {original} равна {int(result)}")
