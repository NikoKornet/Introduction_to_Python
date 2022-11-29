# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

string1 = input("Введите строку: ")
string2 = input("Введите подстроку: ")
# count = 0

# for i in range(len(string1)):
#     if string2 == string1[i:i + len(string2)]:
#         count += 1
# print(count)

count = string1.count(string2)
print(f'Подстрока {string2} встречается в строке '
      f'{string1} - {count} раз')
