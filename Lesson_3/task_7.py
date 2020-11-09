# 7. ** доп.задание
#
# Написать программу которая найдет факториал введенного пользователем числа.
#
# Например, факториал числа 5 равен произведению 1 * 2 * 3 * 4 * 5 = 120.
#
# Формула нахождения факториала:
#
#  n! = 1 * 2 * … * n, где n - введенное пользователем число
some_input = (input('Enter a number: '))
factorial = 1
for i in range(1, int(some_input) + 1):
    factorial = factorial * i
print(f'Factorial for {some_input} is {factorial}')
