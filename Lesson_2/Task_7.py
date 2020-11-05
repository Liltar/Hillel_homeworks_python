# 7. ** Написать программу "Показать звезды". На вход принимает обычное целое число,
# должно напечатать количество звезд:
#
#      Пример:
#
#      Input number of stars: 8
#      ********

some_input = input('Input number of stars: ')
try:
    stars_number = int(some_input)
    print('*' * stars_number)
except ValueError:
    try:
        stars_number = float(some_input)
        print('Input is a float!')
    except ValueError:
        print('Input is a string!')