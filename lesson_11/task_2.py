# 2. Написать функцию которая будет частично скрывать e-mail, пример:
#
#   hide_email(somebody_email@gmail.com) -> em***@**il.com


def hide_email(some_string):
    index_of_at = [pos for pos, char in enumerate(some_string) if char == '@'][0]
    some_string_to_list = list(some_string)
    some_string_to_list[index_of_at - 3:index_of_at] = '***'
    some_string_to_list[index_of_at + 1:index_of_at + 3] = '**'
    new_string = ''.join(some_string_to_list)
    return new_string


print(hide_email('somebody_email@gmail.com'))


# def hide_email_1(some_string):
#     print([some_string.find('@')])
#     some_string = '@'.join([some_string.replace(some_string[some_string.find('@') - 3:], '***'),
#                             some_string.replace(some_string[:len(some_string) - some_string.find('@') + 2], '**')])
#     return some_string
#
#
# print(hide_email_1('somebody_email@gmail.com'))