# Создайте программу для игры в ""Крестики-нолики""

import os
os.system("cls")

board = list(range(1,10))

def board_draw(board):
    print ("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)

def player_turn(player):
    flag = False
    while not flag:
        player_answer = input("Choose place " + player + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Uncorrect. Choose number!")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player
                flag = True
            else:
                print ("Already taken")
        else:
            print ("Uncorrect. Choose in range from 1 to 9")

def win_conditions(board):
    win_win = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_win:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def game(board):
    counter = 0
    win = False
    while not win:
        board_draw(board)
        if counter % 2 == 0:
            player_turn("X")
        else:
            player_turn("O")
        counter += 1
        if counter > 4:
            a = win_conditions(board)
            if a:
                print(a, "win!")
                win = True
                break
        if counter == 9:
            print("Drow!")
            break
    board_draw(board)

game(board)