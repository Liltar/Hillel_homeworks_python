# 3. Получить прогноз погоды для Одессы на следующие 5 дней
# и записать в файл с именем текущей даты,
#
# http://api.openweathermap.org/data/2.5/forecast/daily?q=city&cnt=1&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8
#
# Параметр cnt = количество дней
#   Параметр q = город
# Так мы получим и обработаем дату из ответа (ключ dt):
#
#   datetime.datetime.fromtimestamp(1600419600)
# Применив к полученному обьекту даты strftime("%d-%m-%Y") получим строковую дату для записи в файл.
# Пример имени файла: 19-09-2020-Odessa-5-days-weather-forecast.txt
# Записанный файл должен выглядеть вот так:
# Дата             Температура днем   По ощущениям
#   18-09-2020       17.86              11.18
#   19-09-2020       15.75              11.21
#   20-09-2020       20.37              17.49
#   21-09-2020       20.75              18.08
#   22-09-2020       20.96              17.47

import requests
import datetime

url = 'http://api.openweathermap.org/data/2.5/forecast/daily'
days_number = int(input('Enter a number of days: '))
city = input('Enter city: ')


def weather_forecast(days_number):
    data = {'q': city, 'units': 'metric', 'cnt': days_number, 'appid': 'f9ada9efec6a3934dad5f30068fdcbb8'}
    r = requests.get(url, data)
    return r.json()


def format_value(val):
    if val >= 0:
        result = ' {:.2f}'.format(val)
    else:
        result = '{:.2f}'.format(val)
    return result


def create_file():
    result = weather_forecast(days_number)
    with open('weather.txt', 'w') as f:
            f.writelines(['   Date   ','    Day    ', '   Night   ', '\n'])
            for day in result['list']:
                f.writelines([datetime.date.fromtimestamp(day['dt']).strftime('%d-%m-%Y') + (4 * ' '),
                          format_value(day['temp']['day']) + (4 * ' '),
                          format_value(day['temp']['night']) + (4 * ' '), '\n'])


create_file()