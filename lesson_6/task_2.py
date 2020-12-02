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


def countdown(func):
    def seconds(*args):
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
        func(*args)
    return seconds()


@countdown
def time_now():
    print(time.strftime('%H:%M'))