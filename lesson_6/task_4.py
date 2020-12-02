# Во вложении есть json файл. Написать программу которая прочитает его
# и посчитает общую длительность всех треков в альбоме.
#
# Базовый кейс - вернет количество секунд.
#
#    * доп. усложнение вернуть в виде строки часы:минуты:секунды,
#    прим. '0:41:39' (datetime.timedelta)


import json
with open('acdc.json', 'r') as f:
    json_text_file_acdc = f.read()
    acdc = json.loads(json_text_file_acdc)
    i = 0
    track_duration_1 = (acdc['album']['tracks']['track'][i]['duration'])
    track_durations = [value for value in acdc['album']['tracks']['track'][i]['duration']]
    print(track_duration_1)



