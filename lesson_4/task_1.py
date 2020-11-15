# В первый день спортсмен пробежал `x` километров,
# а затем он каждый день увеличивал пробег на 10% от предыдущего значения.
# По данному числу `y` определите номер дня, на который пробег спортсмена составит не менее `y` километров.
#
# Программа получает на вход числа `x` и `y` и должна вывести одно число - номер дня.
first_day_dist = int(input('Enter a first day distance: '))
last_day_dist = int(input('Enter an intended distance: '))
i = 1
while first_day_dist < last_day_dist:
    first_day_dist *= 1.1
    i += 1
print(i)