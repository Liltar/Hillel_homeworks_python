# 4. Вывести на консоль своё имя, нарисованное 'звёздочками'
getName = input('Enter your name: ')
for letter in getName:
   getName = getName.replace(letter, "*")
print('\nResult is: ', getName)

# python -m pip install -U pip
# установка менеджера пакетов
#
# pip install art
# установка модуля art
#
#from art import *
#print('taras', font='asterisk')

