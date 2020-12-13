# 3. Написать функцию которая сдвинет полученный список на N элементов вправо или влево,
# принимаемые аргументы - список и натуральное число
# (если отрицательное сдвигаем влево, положительное - вправо).
some_list = ['a', 'b', 'c', 'd', 'e', 'f']
some_digit = int(input('Enter digit: '))


def move_it(some_list, some_digit):
    return some_list[some_digit:] + some_list[:some_digit]


print(move_it(some_list, some_digit))