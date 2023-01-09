# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import os
os.system("cls")

from random import randint as rd

sweety = 2021 # Если ты ходишь первым нужно взять 5 конфет чтобы выиграть, далее добираешь конфеты до 28 или берешь тоже по 28.

flag = int(rd(0, 1))
if flag == 1:
    print('Bot first')
else:
    print('Player first')

while sweety > 0:
    if flag == 1:
        b = int(rd(1, 29))
        if sweety - 28 <= 28:
            b = sweety - 29
        if sweety <= 28:
            b = sweety
        print(f'Bot choose: ', b, ' sweety')
        sweety = sweety - b
        flag = 0
    else:
        a = int(input('Playes choose. Enter number: '))
        while a < 1 or a > 28:
            print('wrong numb, choose another one!')
            a = int(input('Playes choose. Enter number: '))
        sweety = sweety - a
        flag = 1
    if sweety > 0:
        print(f'Sweety left: ', sweety)
    else:
        print('No sweety more!')

if flag == 1:
    print('Player win!')
else:
    print('Bot win!')
