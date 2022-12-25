# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def compression(text):
    compressed_data = ''
    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
        compressed_data += str(count) + text[i]
        i += 1
    return compressed_data


def decompressing(text):
    decompressing_data = ''
    i = 0
    while i < len(text):
        decompressing_data += str(text[i + 1]) * int(text[i])
        i += 2
    return decompressing_data


with open('Text1.txt', 'r') as file1:
    file1 = file1.read()

with open('Text2.txt', 'w+') as file2:
    file2.write(compression(file1))
    file2.seek(0)
    file2 = file2.read()

with open('Text3.txt', 'w') as file3:
    file3.write(decompressing(file2))
