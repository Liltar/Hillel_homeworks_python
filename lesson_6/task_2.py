# 2. Написать функцию которая возвращает текущее время. И обернуть ее в декоратор @countdown
#    который отсчитает 3 секунды.
#    Пример:
#    >>> what_time_is_it_now()
#
#    3
#
#    2
#
#    1
#
#    '16:21'
#
# time.sleep() поможет программе уснуть на первый аргумент секунду =)
#
#    Вернуть время поможет метод time.strftime, с аргументом '%H:%M'
import time


def countdown(*args):
    for i in range(3, 0, -1):
        time.sleep(1)
        print(i)
    return args

print(countdown())

# def time_now():
#     print(time_now)