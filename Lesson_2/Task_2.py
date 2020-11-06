# 2. Напишите программу, которая считывает целое число и выводит текст,
# аналогичный приведенному в примере
#
# (пробелы важны!). Первая строка содержит следующее значение,
# а вторая строка содержит предыдущее значение введёного числа
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
try:
    val = int(some_input)
    print(f'       The next number for the number {val} is {val + 1} '
          f'\n       The previous number for the number {val} is {val - 1}')
except ValueError:
    try:
        val = float(some_input)
        print('Input is a float')
    except ValueError:
        print('Input is not an ingteger, it\'s a string')
