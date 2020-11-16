# 2. Написать программу которая вернет количество введенных пользователем слов и общее число символов.
some_str = input('Enter a string: ')


def str_words_quantity(any_str):
    words_number = 1
    for i in any_str:
        if i == ' ':
            words_number += 1
    return words_number


def str_symbol_quantity(any_str):
    symbol_quantity = 0
    for i in any_str:
        if i is not None:
            symbol_quantity += 1
    return symbol_quantity


print(str_words_quantity(some_str))
print(str_symbol_quantity(some_str))
