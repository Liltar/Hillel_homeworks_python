# 1. Написать функцию которая посчитает количество очков футбольной команды.
#
#     Победа дает 3 очка, ничья 1 очко, поражение 0 очков.
#
#     Функция принимает три аргумента - win, draw, loss.

# var_1 classic
def win(amount):
    return 3 * amount


def draw(amount):
    return 1 * amount


def loss(amount):
    return 0 * amount


def points_calc(win, draw, loss):
    return win + draw + loss




# var_2 with lambdas
# win = lambda x: x * 3
# draw = lambda x: x * 1
# loss = lambda x: x * 0
#
#
# def points_calc_2(win, draw, loss):
#     return win + draw + loss
