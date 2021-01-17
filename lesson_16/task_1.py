# 1. Формат украинских номеров:
#
#    ВН1010НС или АА1010АА
#
#
# На ввод программа получает строку, в ответ должна вернуть является строка автомобильным номером или нет.
#
#     * доп. Должна вернуть регион (должна знать регионы 2004 и 2013 гг.)
#
# Должна одинаково воспринимать AI - англ и АІ - украинский варианты.
#
# (для BI, AI, IA и т.д.)
import csv

argument = 'ВН1010НС'

def validate_number(argument):
    if len(argument) != 8 or type(argument[:2]) != str or type(argument[-2:]) != str:
        print(f'{argument} is not a number')
    else:
        with open('ua_auto.csv', 'r', encoding='utf-8') as auto_numbers:
            reader = csv.DictReader(auto_numbers)
            for row in reader:
                if row['Код 2004'] == argument[:2] or row['Код 2013'] == argument[:2]:
                    print(f'The {argument} is valid auto number and '
                          f'its region is {row["Регіон"]}')

validate_number(argument)