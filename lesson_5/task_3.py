# 3. Написать функцию которая вернет площадь фигуры:
# по-умолчанию треугольника, опционально квадрата.
# На входе 2 величины и параметр типа фигуры.

side = int(input('Enter the size of the side: '))
height = int(input('Enter the size of height: '))


def area(*args: float, parameter='triangle'):
    s = None
    if parameter == 'triangle':
        s = 0.5 * side * height
    else:
        s = side ** 2
    return s


parameter = input('Enter the type of figure: triangle or square: ')
print(area(side, height, parameter))