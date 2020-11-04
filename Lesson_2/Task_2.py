# 2. Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере
#
# (пробелы важны!). Первая строка содержит следующее значение, а вторая строка содержит предыдущее значение введёного
#
# числа
#
#
#    ```
#
#        Please enter an integer number: 1234
#        The next number for the number 1234 is 1235.
#        The previous number for the number 1234 is 1233.
#
#     or
#
#        Please enter an integer number: 0
#        The next number for the number 0 is 1.
#        The previous number for the number 0 is -1.

some_input = input('       Please enter an integer number: ')
#some_int = int(some_input)
# if type(some_input) != int:
#       raise ValueError(some_input, 'is not an integer')
# else:
#       pass
print('       The next number for the number', int(some_input),'is', (int(some_input) + 1), '\n',\
      '      The previous number for the number', int(some_input), 'is', (int(some_input) - 1))
print(type(some_input))
# print(type(some_int))