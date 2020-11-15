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


def calculate(list_to_collect):
    count_numbers = 0
    sum_numbers = 0
    multiply_numbers = 1
    max_number = 0
    max_number_index = 0
    even_numbers = 0
    odd_numbers = 0
    second_max_number = 0
    last_element = 0
    max_elements = 0
    for i, value in enumerate(list_to_collect):
        count_numbers += 1
        sum_numbers += value
        multiply_numbers *= value
        if value > max_number:
            max_number = value
            max_number_index = i
        if value < max_number:
            second_max_number = value
        if value % 2 == 0:
            even_numbers += 1
        if value + last_element == max_number:
            max_elements += 1
        else:
            odd_numbers += 1
        last_element = value
    numbers_avg = multiply_numbers / count_numbers
    return (count_numbers, sum_numbers, multiply_numbers, numbers_avg,
            max_number, max_number_index, even_numbers, odd_numbers,
            second_max_number, max_elements)

print(calculate(list_to_collect))

# # - определить значение и порядковый номер наибольшего элемента последовательности
# for value in list_to_collect:
#     if

