# 2. Написать функцию которая будет частично скрывать e-mail, пример:
#
#   hide_email(somebody_email@gmail.com) -> em***@**il.com

#
def hide_email(str):
    index_of_at = [pos for pos, char in enumerate(str) if char == '@'][0]
    return str[index_of_at - 3:index_of_at], str[index_of_at + 1:index_of_at + 3]
#
#
# print(hide_email('somebody_email@gmail.com'))


# def hide_email_2(str):
#     index_of_at = [pos for pos, char in enumerate(str) if char == '@'][0]
#     str_list = list(str)
#     str_list[index_of_at - 3:index_of_at] = '*'
#     str_list_new = ''.join(str_list)
#     return str_list_new


# print(hide_email_2('somebody_email@gmail.com'))
