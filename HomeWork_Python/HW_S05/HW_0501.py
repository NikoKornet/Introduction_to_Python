# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = "Накушавшись досытабв, он преспокойно убрабвся из дома, растянулся набв большом лугу под деревом и начабв засыпать"
text_find = 'абв'
index = 0

my_list = text.split(' ')
print(my_list)

my_list_result = []
for item in my_list:
    if text_find not in item:
        my_list_result.append(item)

print(my_list_result)
