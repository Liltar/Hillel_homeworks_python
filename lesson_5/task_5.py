# 5. Написать функцию square,
# принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата,
# площадь квадрата
# и диагональ квадрата.
side = int(input('Enter side: '))


def square(arg: int):
    perimeter = arg * 4
    area = arg ** 2
    root_2 = 2 ** 0.5
    diagonal = round(arg * root_2, 2)
    return perimeter, area, diagonal


print(square(side))
