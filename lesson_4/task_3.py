# 3. Даны два целых числа `A` и `В`.
# Выведите все числа от `A` до `B` включительно, в порядке возрастания, если `A < B`,
# или в порядке убывания в противном случае.

first_number = int(input('Enter a first number: '))
second_number = int(input('Enter a second number: '))


def number_list_2(*args):
    step = 1
    if first_number > second_number:
        step = -1
    for i in range(first_number, second_number + step, step):
        print(i)


number_list_2(first_number, second_number)

# var 2
# if first_number < second_number:
#     for i in range(first_number, second_number + 1):
#         print(i)
# elif first_number > second_number:
#     for i in range(first_number, second_number - 1, - 1):
#         print(i)
# else:
#     print('No way!')

# var 3
# def number_list_1():
#     if first_number < second_number:
#         for i in range(first_number, second_number + 1):
#             print(i)
#     elif first_number > second_number:
#         for i in range(first_number, second_number - 1, - 1):
#             print(i)
#     else:
#         print('No way')
