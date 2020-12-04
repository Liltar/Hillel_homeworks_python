# 1. Написать функцию которая вернет строку введенную пользователем.
#
#   Обернуть функцию в декоратор чтобы функция вместо строки целиком вернула список слов.
#
any_input = input('Enter something: ')


def input_to_list(input_return):
    return input_return.split()


def input_return():
        return any_input


print(input_to_list(any_input))
