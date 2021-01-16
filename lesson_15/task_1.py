# Во вложении файл csv с данными про аэропорты мира, написать программу которая сможет
#
# вернуть данные по таким параметрам:
#
# --iata_code - код аэропорта, должно вернуть 1 запись по коду аэропорта(всю строку) или вернуть ошибку AirportNotFoundError
# --country - страна, должно вернуть все записи по аэропортам или
# CountryNotFoundError
# --name - значение имени аэропорта, допустимо вхождение строки хотябы
# минимально, т.е. liman должен вернуть строки с такими названиями:
# Ilimanaq Heliport
# Sidi Slimane Airport
# Kilimanjaro International Airport
# West Kilimanjaro Airport
# Limanske Airfield
# Liman Airfield
# ...
# или AirportNotFoundError
#
#
# Только один параметр обязателен, если выбрано несколько - вернуть
# ошибку:
# MultipleOptionsError, если ни одного - NoOptionsFoundError
#
# ** доп. ошибки принимают два аргумента, текст ошибки и входные данные,
#
#    пример:
#
# AirportNotFoundError: ('Airport not found', 'OESD')
# CountryNotFoundError: ('Country not found', 'UGUGU')
#
#   IATA код может быть только 3х буквенным в верхнем регистре, сделать валидацию на него
#
#   или вернуть IATACodeError

class AirportFounder:
    def __init__(self, arguments):
        self.args = self.check_arguments(arguments)
    def check_argument(self):
        if len(arg_dict) == 1:
            return arg_dict
        elif len(arg_dict) > 1:
            raise Exception('MultipleErrorsFound')

import csv


def print_first_element_from_csv():
    with open('airport-codes_csv.csv', 'r', encoding='utf-8') as airport_codes:
        csv_reader = csv.DictReader(airport_codes)
        result = []
        for row in csv_reader:
            if row['iata_code'] == args_dict['iata_code']:
                result.append(row)
        first_element = result[0]
        print(first_element)
        # for key, value in first_element.items():
        #     print(key, value)


print_first_element_from_csv()