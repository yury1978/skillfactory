import numpy as np


def game_core_v2(number):
    ''' Ищем срединную точку, постепенно сдвигая границы диапозона. '''

    count = 1
    border_min = 0
    border_max = 100
    predict = border_max - (border_max - border_min) // 2

    while number != predict:
        count += 1

        if predict > number:
            border_max = predict  # сдвигаем правую границу
        elif predict < number:
            border_min = predict  # сдвигаем левую границу

        predict = border_max - (border_max - border_min) // 2

    return count


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''

    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)

    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))

    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v2)
