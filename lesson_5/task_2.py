# 2. Написать программу которая вернет количество введенных пользователем слов и общее число символов.
some_str = input('Enter a string: ')


def str_words_quantity(some_str):
    words_number = 1
    for i in some_str:
        if i == ' ':
            words_number += 1
        else:
            pass
    return words_number


def str_symbol_quantity(some_str):
    symbol_quantity = 0
    for i in some_str:
        if i != None:
            symbol_quantity += 1
        else:
            pass
    return symbol_quantity


print(str_words_quantity(some_str))
print(str_symbol_quantity(some_str))
