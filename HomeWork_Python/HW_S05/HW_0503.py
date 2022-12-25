# Создайте программу для игры в ""Крестики-нолики""

def draw_field(field):
    print('------------------')
    print(f'  {field[0]}  |  {field[1]}   |  {field[2]}')
    print('------------------')
    print(f'  {field[3]}  |  {field[4]}   |  {field[5]}')
    print('------------------')
    print(f'  {field[6]}  |  {field[7]}   |  {field[8]}')
    print('------------------')


def take_input(player_name):
    valid = False
    while not valid:
        player_answer = input(f'Ход игрока {player_name}: ')
        try:
            player_answer = int(player_answer)
        except ValueError:
            print('Введите число от 1 до 9')
            continue
        if 1 <= player_answer <= 9:
            if str(field[player_answer - 1]) not in 'X0':
                field[player_answer - 1] = player_name
                valid = True
            else:
                print('Эта клетка уже занята! ')
        else:
            print('Введите число от 1 до 9')


def check_win(field):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False


def main(field):
    counter = 0
    win = False
    while not win:
        draw_field(field)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('0')
        counter += 1
        if counter > 4:
            tmp = check_win(field)
            if tmp:
                draw_field(field)
                print(f'{tmp}, победили!')
                win = True
                break
            if counter == 9:
                draw_field(field)
                print('Friendship!')
                break
            draw_field(field)


print('Да начнется битва!')
field = list(range(1, 10))
main(field)
