def input_int(text: str, error: str) -> int:  # проверка ввода числа.
    while True:
        try:
            number = int(input(text))
            devide = 100 / number
            return number
        except:
            print(error)


number = input_int("Введите целое число: ", "Ошибка! Введите целое число!")
print(number)
