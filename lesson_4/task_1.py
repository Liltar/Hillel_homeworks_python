# some_input = sum([int(i) for i in input('Enter a 3-digit number: ')])
# print(some_input)

# 5. Пользователь вводит число от 1 до 10, программа генерирует рандомное число от 1 до 10,
# если числа равны напечатать 'You won!' если нет - 'You lose!'.
# Дать пользователю три попытки ;)

# import random
# programm_number = random.randint(0, 10)
# attempts = 0
# while attempts < 3:
#     user_guess = random.randint(0, 10)
#     attempts += 1
#     if int(user_guess) == programm_number:
#         print('You won!')
#         break
#     else:
#         print('Try again!')
#     attempts += 1
# else:
#     print('You lose!')
# print(f'The answer is {programm_number}')
#
# print(globals())
#
first_day_dist = int(input('Enter a first day distance: '))
last_day_dist = int(input('Enter an intended distance: '))
i = 1
while first_day_dist < last_day_dist:
    first_day_dist *= 1.1
    i += 1
