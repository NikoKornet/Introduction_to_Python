# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


def getting_dict(degree, min, max):
    polynom_dict = {}
    for key in range(degree, -1, -1):
        value = randint(min, max)
        polynom_dict[key] = value
    return polynom_dict

def getting_polynomial(polynom_dict):
    polynom = ''
    first = True
    for (key, value) in polynom_dict.items():
        if value != 0:
            if first:
                if value > 0:
                    polynom += f'{value}*x**{key} '
                first = False
            else:
                if value == 1:
                    if key == 1:
                        polynom += f'+ x '
                    elif key == 0:
                        polynom += f'+ 1 '
                    else:
                        polynom += f'+ x**{key} '
                elif value > 1:
                    if key == 1:
                        polynom += f'+ {value}*x '
                    elif key == 0:
                        polynom += f'+ {value} '
                    else:
                        polynom += f'+ {value}*x**{key} '
    return polynom + '= 0'

k1 = int(input("Введите натуральную степень k1: "))
first_polynomial_dict = getting_dict(k1, 0, 100)
first_polynomial = getting_polynomial(first_polynomial_dict)
with open('first_polynomial.txt', 'w') as data:
    data.write(first_polynomial)

k2 = int(input("Введите натуральную степень k2: "))
second_polynomial_dict = getting_dict(k2, 0, 100)
second_polynomial = getting_polynomial(second_polynomial_dict)
with open('second_polynomial.txt', 'w') as data:
    data.write(second_polynomial)

print(first_polynomial)
print(second_polynomial)
