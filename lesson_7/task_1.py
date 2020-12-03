# 1. Написать функцию которая вернет строку введенную пользователем.
#
#   Обернуть функцию в декоратор чтобы функция вместо строки целиком вернула список слов.

any_input = input('Enter something: ')


def input_to_list(any_input):
    return any_input.split()


print(input_to_list(any_input))
