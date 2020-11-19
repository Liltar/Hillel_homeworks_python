# 3. Написать функцию которая вернет площадь фигуры:
# по-умолчанию треугольника, опционально квадрата.
# На входе 2 величины и параметр типа фигуры.
first_side = int(input('Enter a size of first side: '))
second_side = int(input('Enter a size of second side: '))


def area(any_side, any_side_2, *triangle):
