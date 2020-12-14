# 2. Написать функцию которая будет частично скрывать e-mail, пример:
#
#   hide_email(somebody_email@gmail.com) -> em***@**il.com
#
def hide_email(some_string):
    index_of_at = [pos for pos, char in enumerate(some_string) if char == '@'][0]
    some_string = list(some_string)
    some_string[index_of_at - 3:index_of_at] = '*'
    some_string[index_of_at + 1:index_of_at + 3] = '*'
    return some_string


print(hide_email('somebody_email@gmail.com'))


# def hide_email_2(some_string):
#     index_of_at = [pos for pos, char in enumerate(some_string) if char == '@'][0]
#     some_string_list = list(some_string)
#     some_string_list[index_of_at - 3:index_of_at] = '*'
#     some_string_list_new = ''.join(some_string_list)
#     return some_string_list_new


# print(hide_email_2('somebody_email@gmail.com'))
