# 4. Дан список случайных целых чисел.
# Замените все нечетные числа списка нулями.
# И выведете их количество.
some_list = list(range(0, 10))


def odd_numbers_count_and_replace(arg: list):
    odd_numbers_count = 0
    for index, item in enumerate(arg):
        if item % 2 != 0:
            odd_numbers_count += 1
            arg[index] = 0
        else:
            pass
    return arg, odd_numbers_count


print(odd_numbers_count_and_replace(some_list))
