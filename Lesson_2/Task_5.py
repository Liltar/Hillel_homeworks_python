# 5. В математике функция `sign(x)` (знак числа) определена так:
#
#    ``
#
#    sign(x) = 1, если x > 0,
#
#    sign(x) = -1, если x < 0,
#
#    sign(x) = 0, если x = 0.
#
#    ``
#
#    Для данного числа x выведите значение sign(x).
#    Эту задачу желательно решить с использованием каскадных инструкций if... elif... else.

some_input = input('Enter an integer: ')
try:
    val = int(some_input)
    if val > 0:
        print('sign(x) = 1')
    elif val < 0:
        print('sign(x) = -1')
    elif val == 0:
        print('sign(x) = 0')
except ValueError:
    try:
        val = float(some_input)
        print('Input is a float')
    except ValueError:
        print('Input is a string')
