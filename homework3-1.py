# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# восттановление

import os
os.system("cls")

with open('2.txt', 'r') as f:
    string = f.read()

decode = str()
count = str()

print(string)

for i in string:
    if i.isdigit():
            count += i
    else:
            decode += i * int(count)
            count = ''

print(decode)

with open('3.txt', 'w') as z:
    z.write(decode)
