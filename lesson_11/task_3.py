# 3. Написать функцию которая вернет самое длинное слово в строке:
#
# longest_word("What makes a good man") -> makes


def longest_word(string):
    new_string = string.split()
    return max(new_string, key=len)


print(longest_word('Tongue tied and twisted just an earth bound misfit I'))