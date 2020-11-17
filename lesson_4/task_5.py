# 5. Дана строка.
#
#    a. выведите третий символ этой строки.
#
#    b. выведите предпоследний символ этой строки.
#
#    c. выведите первые пять символов этой строки.
#
#    d. выведите всю строку, кроме последних двух символов.
#
#    e. выведите все символы с четными индексами
#    (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
#
#    f. выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
#
#    g. выведите все символы в обратном порядке.
#
#    h. выведите все символы строки через один в обратном порядке, начиная с последнего.
#
#    i. выведите длину данной строки.

some_string = input('Enter a string: ')


def third_symbol(some_string):
    return some_string[2]


def penultimate_symbol(some_string):
    return some_string[-2]


def first_five_symbols(some_string):
    return some_string[0:5]


def string_without_two_last_symbols(some_string):
    return some_string[:-2]


def even_symbols(some_string):
    return some_string[1::2]


def odd_symbols(some_string):
    return some_string[2::2]


def reversed_string(some_string):
    return ''.join(reversed(some_string))


#    h. выведите все символы строки через один в обратном порядке, начиная с последнего.
def reversed_next_nearest_symbol(some_string):
    return some_string[::-1][::2]


def length_of_the_string(some_string):
    return len(some_string)
