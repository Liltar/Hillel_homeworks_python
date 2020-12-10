# 2. Написать функцию которая определит является ли введенная строка палиндромом
# (та которая читается одинаково с любой стороны), пример:
#
# ШАЛАШ, КАЗАК, ДЕД, ДОХОД, 13231 и т.д.
#
word_to_check = input('Enter a word for palindrome check: ')


def is_palindrome(arg):
    if word_to_check == word_to_check[::-1]:
        print(f'{word_to_check} is palindrome')
    else:
        print(f'{word_to_check} is not a palindrome')


is_palindrome(word_to_check)
