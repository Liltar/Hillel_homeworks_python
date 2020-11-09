# 6. *доп.задание
#
# Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении
# и на одну клетку по горизонтали,
#
# или наоборот. Даны две различные клетки шахматной доски, определите,
# может ли конь попасть с первой клетки на вторую одним ходом.

vertical_first = int(input('vertical_first: '))
horizontal_first = int(input('horizontal first: '))
vertical_second = int(input('vertical second: '))
horizontal_second = int(input('horizontal second: '))
dx = abs(vertical_first - vertical_second)
dy = abs(horizontal_first - horizontal_second)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')