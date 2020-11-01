# 4. Вывести на консоль своё имя, нарисованное 'звёздочками'
t = '*********\n    *\n    *\n    *\n    *\n    *\n    *\n    *\n    *\n'
a = '       *\n*              *\n*              *\n*              *\n*              *\n****************/' \
    '\n*              *\n*              *\n*              *'
r = ''

s = ''

# python -m pip install -U pip
# установка менеджера пакетов
#
# pip install art
# установка модуля art
#
from art import *
tprint('taras', font='asterisk')