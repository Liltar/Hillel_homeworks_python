# 1. Написать функцию которая вернет строку введенную пользователем.
#
#   Обернуть функцию в декоратор чтобы функция вместо строки целиком вернула список слов.
#


def input_to_list_decorator(func):
    return func().split


@input_to_list_decorator
def input_return():
    return input('Enter something: ')


print(input_return())
