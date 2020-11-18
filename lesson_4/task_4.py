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


enter_number = input('Enter a number: ')
for i in range(int(enter_number) + 1):
    list_1 = ''.join([str(num) for num in range(1, int(enter_number)+ 1)])
    print(list_1[0:i])
