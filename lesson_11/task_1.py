# 1. Написать функцию которая посчитает количество очков футбольной команды.
#
#     Победа дает 3 очка, ничья 1 очко, поражение 0 очков.
#
#     Функция принимает три аргумента - win, draw, loss.


def calc_points(win_amount, draw_amount, loss_amount):
    win = win_amount * 3
    draw = draw_amount * 1
    loss = loss_amount * 0
    return win + draw + loss


print(calc_points(2, 1, 0))