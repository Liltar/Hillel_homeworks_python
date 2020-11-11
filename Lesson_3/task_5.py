# 5. Пользователь вводит число от 1 до 10, программа генерирует рандомное число от 1 до 10,
# если числа равны напечатать 'You won!' если нет - 'You lose!'.
# Дать пользователю три попытки ;)

import random
program_number = random.randint(0, 10)
attempts = 0
while attempts < 3:
    user_guess = (input('Enter a number from 1 to 10: '))
    attempts += 1
    if int(user_guess) == program_number:
        print('You won!')
        break
    else:
        print('Try again!')
    attempts += 1
else:
    print('You lose!')
print(f'The answer is {program_number}')
