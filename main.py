import numpy as np


def game_core_v1(number):
    """Просто угадываем на random ни как не используя информацию о больше или меньше.
       Функция Принимает загаданное число и возвращает число попыток"""
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            break
    return count  # выход из цикла, если угадали


def game_core_v2(number):
    """Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его
       в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 0
    predict = np.random.randint(1, 100)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count  # выход из цикла, если угадали

def game_core_v3(number):
    """Сначала устанавливаем число по середине интервала, а затем сдвигаем левую границу на predict+1
    если искомое число больше, либо правую на predict-1 если меньше. И так до тех пор пока не отгадаем.
    Суть заключается в том, что мы всегда берем середину интервала. Так оптимальней всего."""
    count = 0
    l = 1
    r = 100
    while True:
        predict = (l + r) // 2
        if number > predict:
            l = predict + 1
            count += 1
        elif number < predict:
            r = predict - 1
            count += 1
        else:
            count += 1
            break
    return count


def score_game(algo):
    """Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(algo(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# запускаем
score_game(game_core_v1)
score_game(game_core_v2)
score_game(game_core_v3)