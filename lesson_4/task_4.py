# 4. По данному натуральному `n ≤ 9` выведите лесенку из `n` ступенек, `
# i`-я ступенька состоит из чисел от 1 до `i` без пробелов.
#
#    ```
#
#    1
#
#    12
#
#    123
#
#    1234
#
#    12345
enter_number = int(input('Enter a number: '))
for i in range(1, enter_number + 1):
    for element in range(1, i + 1):
        print(element, sep='', end='')
    print()