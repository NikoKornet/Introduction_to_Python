# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from HW0401 import *

first_data = open('first_polynomial.txt', 'r')
first_string = str(first_data.readline())
first_data.close()

second_data = open('second_polynomial.txt', 'r')
second_string = str(second_data.readline())
second_data.close()


def getting_polynomial_dict(polynomial: str):
    polynomial_list = []
    polynomial = polynomial.replace(' = 0', '').replace(' + ', ' ').split(' ')
    for item in polynomial:
        if not 'x' in item:
            polynomial_list.append([item, 0])
        else:
            if item.endswith('x'):
                if item == 'x':
                    polynomial_list.append(['1', '1'])
                else:
                    polynomial_list.append((item + '1').split('*x'))
            else:
                if item.startswith('x'):
                    polynomial_list.append(('1' + item).split('x**'))
                else:
                    polynomial_list.append(item.split('*x**'))
    polynomial_dict = {}
    for item in polynomial_list:
        polynomial_dict[int(item[1])] = int(item[0])
    return polynomial_dict


def addition_polynomials(first, second):
    generalized = {}
    generalized.update(first)
    generalized.update(second)
    for key in generalized:
        if first.get(key) and second.get(key):
            generalized[key] = first.get(key) + second.get(key)
        elif first.get(key):
            generalized[key] = first.get(key)
        else:
            generalized[key] = second.get(key)
    return dict(sorted(generalized.items())[::-1])


first_polynomial_dict = getting_polynomial_dict(first_string)
second_polynomial_dict = getting_polynomial_dict(second_string)
addition_dict = addition_polynomials(first_polynomial_dict, second_polynomial_dict)
result_polynomial = getting_polynomial(addition_dict)

with open('result_polynomial.txt', 'w') as data:
    data.write(result_polynomial)

print(result_polynomial)