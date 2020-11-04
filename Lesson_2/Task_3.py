# 3. Длина маршрута велоралли "100 километров за 10 часов по Поясу Славы" - примерно 100 километров.
# Велосипедист Вася стартует с нулевого километра маршрута и едет со скоростью `v` километров в час.
# На какой отметке он остановится через `t` часов?
#
# Программа получает на вход значение `v` и `t`.
# Если `v > 0`, то Вася движется в положительном направлении по маршруту,
# если же значение `v < 0`, то в отрицательном.
#
# Программа должна вывести целое число от 0 до 100 — номер отметки, на которой остановится Вася.

# speed
import sys
v = input('Enter speed: ')
if int(v) > 0:
    pass
elif int(v) < 0:
    sys.exit('Wrong way!')
elif int(v) == 0:
    sys.exit('Keep moving!')

# time
t = input('Enter time: ')
if int(t) > 0:
    pass
elif int(t) <= 0:
    sys.exit('TIME PARADOX')

mark = int(v) * int(t)
if mark > 0 and mark <= 100:
    print('The number of the mark at which bicyclist will stop is', mark)
else:
    sys.exit('No way!')