def input_number():
    number = int(input('Введите число: '))
    return number


def input_operation():
    operation = input('Введите операцию (+, -, *, /, =): ')
    return operation


def print_result(smth):
    print(smth)


def input_string():
    calc_string = input('Введите строку: ')
    calc_string = calc_string.replace(' ', '')
    if '=' in calc_string:
        calc_string = calc_string[:calc_string.find('=')]
    calc_string = calc_string.replace('*', ' * ').replace('/', ' / ').replace('+', ' + ').replace('-', ' - ')
    return calc_string


def input_calc_type():
    answer = input('Выберите тип калькулятора:\nО - Кнопочный\n1 - Строчный\n')
    while answer not in ['0', '1']:
        answer = input('Неверный ввод!\nО - Кнопочный\n1 - Строчный\n')
    return int(answer)
