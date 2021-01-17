#
# 2. Написать программу которая будет форматировать номер телефона к единому виду.
#
# На ввод программа принимает строку введенного номера телефона, например:
#
# 063-999-99-99 вывод (+38) 063 999-99-99
# 063 999-99-99 вывод (+38) 063 999-99-99
# 063-99999-99 вывод (+38) 063 999-99-99
# +3806399-999-99 вывод (+38) 063 999-99-99
# 380639999999 вывод (+38) 063 999-99-99
#
#
# Если что-то не так с номером - пишет 'Failed to recognize number'.

import re
number_to_convert = input('Enter an intended number: ')


def format_phone_number(number_to_convert):
    try:
        pattern = r'^[(]?[+]?(?:38){0,1}[)]?[- ]?([\d]{3})[- ]?([\d]{3})[- ]?([\d]{2})[- ]?([\d]{2})$'
        (d1, d2, d3, d4) = re.findall(pattern, number_to_convert)[0]
        print('(+38)' + ' ' + d1 + ' ' + d2 + '-' + d3 + '-' + d4)
    except IndexError:
        print('Failed to recognize number')

format_phone_number(number_to_convert)