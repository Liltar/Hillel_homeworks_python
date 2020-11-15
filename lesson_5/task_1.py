# 1. Написать функцию `is_prime`, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую `True`, если оно простое, и `False` - иначе.
#
# (Простые числа - те которые делятся без остатка только на само себя или 1,
# например 2, 3, 5, 7, 11...)
input_number = int(input('Enter a number: '))
def is_prime(input_number):
    for i in range(input_number + 1):
        if input_number % i:
            return True
        else:
            return False
is_prime(input_number)