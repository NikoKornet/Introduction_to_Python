# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

my_list = ['qwerty345678oiuye4r5t6y7', '65r75r75e7f7d6f78d6gf8', 'n5mn6m54nm8nm99']
number = input("Введите искомое число: ")

# trigger = True
#
# for item in my_list:
#     for char in item:
#         if char == number:
#             print(f'Число {number} есть в строке {item}')
#             trigger = False
#             break
# if trigger == True:
#     print(f'Числа {number} нет в заданном списке')

for item in my_list:
    for char in item:
        if char == number:
            print(f"Символ {number} есть в строке {item}")
            break
    else:
        print(f"Символа {number} нет в строке {item}")