# 2. Написать функцию которая будет частично скрывать e-mail, пример:
#
#   hide_email(somebody_email@gmail.com) -> em***@**il.com


def hide_email(str):
    index_of_at = [pos for pos, char in enumerate(str) if char == '@']
    return str[:3, index_of_at], str[-2:index_of_at]

print(hide_email('somebody_email@gmail.com'))