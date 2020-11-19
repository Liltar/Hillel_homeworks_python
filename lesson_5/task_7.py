# 7. ** доп. задание Написать функцию `is_date`, принимающую 3 аргумента — день, месяц и год.
#
# Вернуть `True`, если дата корректная
# (надо учитывать число месяца. Например 30.02 - дата не корректная, так же 31.06 или 32.07 и т.д.),
# и `False` иначе.
#
# (можно использовать модуль calendar или datetime)
import datetime
day = int(input('Enter the day: '))
month = int(input('Enter the month: '))
year = int(input('Enter the year: '))


def is_date(*args):
    try:
        date = datetime.date(year, month, day)
        return True
    except:
        ValueError(print('Incorrect date'))


print(is_date())