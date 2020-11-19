# 6. * доп. задание Написать функцию которая уберет из dict элементы с пустыми значениями:
#
#    {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
#    Должно вернуть {'first_color': 'Red', 'second_color': 'Green'} # * dict может быть произвольным

some_dict = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
new_dict = {}


def remove_empty_values_dict_var1(any_dict: dict) -> dict:
    for key, value in some_dict.items():
        if value is not None:
            new_dict[key] = value
        else:
            pass
    return new_dict


print(remove_empty_values_dict_var1(some_dict))


def remove_empty_values_dict_var2(any_dict: dict) -> dict:
    any_dict = {key: value for key, value in any_dict.items() if value is not None}
    return any_dict


print(remove_empty_values_dict_var2(some_dict))