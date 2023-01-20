# Задача 1:
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

# import random

# name1 = input('Введите имя первого игрока: ')
# name2 = input('Введите имя второго игрока: ')
# gamer = random.randrange(1, 3)
# a = int(input('Введите колличество конфет: '))
# if gamer == 1:
#     print('Первый ход делает ', name1)
# else:
#     print('Первый ход делает ', name2)
# while a > 0:
#     if a > 28:
#         gamer1 = int(input('Ты можешь взять не более 28 конфет, сколько ты взял? '))
#         a = a - gamer1
#         if a > 28:
#             gamer2 = int(input('Ты можешь взять не более 28 конфет, сколько ты взял? '))
#             a = a - gamer2
#             if a <= 28:
#                 if gamer == 1:
#                     print('Осталось ', a, 'шт, их забирает', name1,'а значит ПОБЕДИЛ ', name1)
#                 else:
#                     print('Осталось ', a, 'шт, их забирает', name2, 'а значит ПОБЕДИЛ', name2)
#     else:
#         if gamer ==1:
#             print('Осталось ', a, 'шт, их забирает', name2, 'а значит ПОБЕДИЛ(A)', name2)
#         else:
#             print('Осталось ',a, 'шт, их забирает', name1, 'а значит ПОБЕДИЛ(A)', name1) 
 
import random
from random import randint, choice

messages = ['Ваш ход брать конфеты', 'Возьмите конфеты', 'Сколько конфет берём?', 'берите ещё', 'Ваш ход']
max_number_move = 0

def introduce_players():
    player1 = input('Первый игрок, представтесь\n')
    player2 = 'SmartBOT'
    print(f'Очень приятно, сегодня Вы играете с искусственным {player2}')
    return [player1, player2]

def sweets_game(players):
    global max_number_move
    total_sweets = int(input('Введите сколько всего у нас конфет:\n'))
    max_number_move = int(input('Введите колличество конфет, которое можно забрать за один ход:\n'))
    first = int(input(f'[players[0], если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
    if first != 1:
        first = 0
    return[total_sweets, max_number_move, int(first)]

max_move = max_number_move

def game_player_vs_smart_bot(sweets, players, massages):
    global max_number_move
    count = sweets[2]
    
    while sweets[0] > 0:
        if sweets[0] == (max_number_move and sweets[0] < max_number_move and sweets[0] > 1):
            move = sweets[0] - 1
            print(f'Я забираю {move}')
        elif not count % 2:
            move = random.randint(1, sweets[1])
            print(f'Я забираю {move}')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > sweets[0] or move > sweets[1]:
                print(f'Можно взять не более {sweets[1]} конфет, у нас всего {sweets[0]} конфет')
                chance = 2
                while chance > 0:
                    if sweets[0] >= move <= sweets[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {chance} попытки')
                    move = int(input())
                    chance -= 1
                else:
                    return print(f'Попыток не осталось. Game over!')
        sweets[0] = sweets[0] - move
        if sweets[0] > 0:
                print(f'Осталось {sweets[0]} конфет')
        else:
                print(f'Все конфеты разобраны.')
        count += 1
    return players[not count % 2]
    
players = introduce_players()
sweets = sweets_game(players)

winer = game_player_vs_smart_bot(sweets, players, messages)
if not winer:
    print('У нас нет победителя.')
else:
    print(f'Поздравляю! В Этот раз победил {winer}! Ему достаются все конфеты!')
    
                        
                
        
           