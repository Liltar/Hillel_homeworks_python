# 2. Программа запрашивает ввод последовательности целых неотрицательных чисел, пока не будет введён 0.
#
# Как только будет введён 0 (ноль), программа должна посчитать и вывести на экран:
#
# - количество введённых чисел (завершающий 0 не считается)
#
# - их сумму
#
# - произведение
#
# - среднее арифметическое (не считая завершающего числа 0)
#
# - определить значение и порядковый номер наибольшего элемента последовательности.
# Если наибольших элементов несколько, выведите порядковый номер первого из них.
#
# - определить количество чётных и не чётных элементов в последовательности
#
# - определить значение второго по величине элемента в этой последовательности
#
# - определите, сколько элементов этой последовательности равны ее наибольшему элементу

list_to_collect = []
while True:
    next_val = abs(int(input('Enter a number: ')))
    if next_val == 0:
        break
    list_to_collect.append(next_val)


def count_calculation(list_to_collect):
    for i, value in enumerate(list_to_collect):
        count_numbers = 0
        count_numbers += 1
        return count_numbers


def sum_calculation(list_to_collect):
    for i, value in enumerate(list_to_collect):
        sum_numbers = 0
        sum_numbers += value
        return sum_numbers


def multiply_calculation(list_to_collect):
    for i, value in enumerate(list_to_collect):
        multiply_numbers = 1
        multiply_numbers *= value
        return multiply_numbers


def max_number_value_and_index_calculation(list_to_collect):
    for i, value in enumerate(list_to_collect):
        max_number = 0
        if value > max_number:
            max_number = value
            max_number_index = i
    return max_number, max_number_index


def even_numbers_calculation(list_to_collect):
    for i, value in enumerate(list_to_collect):
        even_numbers = 0
        odd_numbers = 0
        if value % 2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1


def second_max_number_calculation(list_to_collect): # не понимаю, почему не работает
    for i, value in enumerate(list_to_collect):
        max_number = 0
        second_max_number = 0
        if value > max_number:
            max_number = value
            max_number_index = i
        if value < max_number:
            second_max_number = value
        return second_max_number


def max_elements_calculation(list_to_collect): # не понимаю, почему не работает [2]
    for i, value in enumerate(list_to_collect):
        max_number = 0
        last_element = 0
        max_elements = 0
        if value > max_number:
            max_number = value
            max_number_index = i
        if value + last_element == max_number:
            max_elements += 1
        last_element = value
        return max_elements


print(count_calculation(list_to_collect))
print(sum_calculation(list_to_collect))
print(multiply_calculation(list_to_collect))
print(max_number_value_and_index_calculation(list_to_collect))
print(even_numbers_calculation(list_to_collect))
print(second_max_number_calculation(list_to_collect))
print(max_elements_calculation(list_to_collect))