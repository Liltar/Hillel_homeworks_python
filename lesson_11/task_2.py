# 2. Написать функцию которая будет частично скрывать e-mail, пример:
#
#   hide_email(somebody_email@gmail.com) -> em***@**il.com


def hide_email(str => some string):
    index_of_at = [pos for pos, char in enumerate(str) if char == '@'][0]
    return str[index_of_at - 3:index_of_at], str[index_of_at + 1:index_of_at + 3]


print(hide_email('somebody_email@gmail.com'))

# some_str = 'somebody_email@gmail.com'
# print(some_str[3:5])

# old_string = "aba"
# string_list = list(old_string)
# string_list[2] = "c"
#
# Replace 3rd element
# new_string = "".join(string_list)
# print(new_string)
#
# Output
#
# abc