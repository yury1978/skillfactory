area_x0 = [['-', '-', '-'],
           ['-', '-', '-'],
           ['-', '-', '-']
           ]


def display_x0():
    """ Вывод игрового области """
    print('       0       1       2')
    print('---------------------------')
    for i, value in enumerate(area_x0):
        print(f'{i}  |   {"   |   ".join(value)}')
        print('---------------------------')


def next_move():
    """ ВВод очередного хода игрока и компьютера """
    while True:
        if player == 'X':
            n_str = int(input('Введите номер строки - '))
            n_col = int(input('Введите номер столбца - '))
            if area_x0[n_str][n_col] != '-':
                print('Неверный ход')
                continue
            else:
                return n_str, n_col
        else:
            n_str = random.randint(0, 2)
            n_col = random.randint(0, 2)
            if area_x0[n_str][n_col] != '-':
                continue
            else:
                return n_str, n_col


def win_x0():
    """ Поиск выйгрышной комбинации """
    win_str = []
    win_col = []
    win_dg1 = []
    win_dg2 = []

    for i in range(3):
        for j in range(3):
            win_str.append(area_x0[i][j])
            win_col.append(area_x0[j][i])
            if win_str == ['X', 'X', 'X'] or win_col == ['X', 'X', 'X']:
                print('Игрок_1 победил')
                return True
            elif win_str == ['O', 'O', 'O'] or win_col == ['O', 'O', 'O']:
                print('PC победил')
                return True
        win_str = []
        win_col = []

        win_dg1.append(area_x0[i][i])
        win_dg2.append(area_x0[2 - i][i])
        if win_dg1 == ['X', 'X', 'X'] or win_dg2 == ['X', 'X', 'X']:
            print('Игрок_1 победил')
            return True
        elif win_dg1 == ['O', 'O', 'O'] or win_dg2 == ['O', 'O', 'O']:
            print('PC победил')
            return True


player = 'X'  # Маркер очереди хода
move_count = 0
import random

while True:
    move_count += 1
    display_x0()

    if player == 'X':
        print('Игрок_1 - ваш ход')
        n_str, n_col = next_move()
        area_x0[n_str][n_col] = 'X'
        player = 'O'
    else:
        print('Ход PC')
        n_str, n_col = next_move()
        area_x0[n_str][n_col] = 'O'
        player = 'X'

    if win_x0():
        display_x0()
        break

    if move_count == 9:
        print(' Ничья ')
        display_x0()
        break
