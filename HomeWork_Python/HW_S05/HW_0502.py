# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import shuffle, randint

candies = 150
remaining_sweets = 28


def bot_run(candi: int) -> int:
    result = candi % 29
    if not result:
        result = randint(1, 28)
    return result


def alternation_moves(pl_act):
    first, second = players
    return second if pl_act == first else first


players = ["'Мешок с костями'", "'Бот'"]
shuffle(players)

active_player = players[0]
print(f'1 игрок - {players[0]}, 2 игрок - {players[1]}')

while candies > 0:
    print(f'\nНа столе лежит {candies} конфет, можно взять [1 .. {remaining_sweets}]')
    print(f"Ходит - {active_player}")

    if active_player == "'Бот'":
        get_candies = bot_run(candies)
        print(f'Бот взял {get_candies} конфет.')
    else:
        get_candies = int(input(f'Сколько конфет возьмешь {active_player}: '))

    if get_candies not in range(1, remaining_sweets + 1):
        print('Не верный ход!')
    else:
        candies -= get_candies
        if candies > 0:
            active_player = alternation_moves(active_player)
        else:
            if active_player == "'Бот'":
                print(f'ХааХа {active_player} выиграл! \n"Поцелуй мой блестящий металлический зад !!"')
