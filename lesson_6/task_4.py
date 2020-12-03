# Во вложении есть json файл. Написать программу которая прочитает его
# и посчитает общую длительность всех треков в альбоме.
#
# Базовый кейс - вернет количество секунд.
#
#    * доп. усложнение вернуть в виде строки часы:минуты:секунды,
#    прим. '0:41:39' (datetime.timedelta)


import json
import datetime

# func to count sum of seconds from list with durations of tracks as its elements
def sum_of_seconds(total_duration=list, elements=str):
    total_length = 0
    for element in range(0, len(track_durations)):
        total_length = total_length + int(track_durations[element])
    return total_length


with open('acdc.json', 'r') as f:
    json_text_file_acdc = f.read()
    acdc = json.loads(json_text_file_acdc)
    track_durations = [track['duration'] for track in acdc['album']['tracks']['track']]
    print(sum_of_seconds(track_durations))


print(datetime.timedelta(0, sum_of_seconds(track_durations)))