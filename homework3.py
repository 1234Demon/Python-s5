# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Сжатие

import os
os.system("cls")

with open('1.txt', 'r') as f:
    string = f.read()

encode = str()
print(string)

count = 1
for i in range(len(string)-1):
    if string[i] == string[i + 1]:
        count += 1
    else:
        encode += str(count) + string[i]
        # print(cout, string[i])
        count = 1
encode += str(count) + string[len(string) - 1]

print(encode)

with open('2.txt', 'w') as z:
    z.write(encode)