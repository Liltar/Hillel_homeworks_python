# 2. Написать калькулятор температур.
#
# Пользователь вводит число и тип температуры (C, F, K - Цельсий, Фарренгейт, Кельвин соответственно)
#
# Программа должна вывести температуру в трех шкалах температур - Цельсий, Фарренгейт, Кельвин

degrees = int(input('Enter a degree: '))
temper_type = input('Enter a type - C, F or K:')
exit_text = 'The temperature is {} in Celsius, {} in Fahreinheits, {} in Kelvins'


def celsius():
        fahr = int(degrees * 9/5 + 32.0)
        kelv = degrees + 273
        return exit_text.format(degrees, fahr, kelv)


def fahreinheits():
        cels = (degrees - 32) * 5/9
        kelv = cels + 273
        return exit_text.format(cels, degrees, kelv)


def kelvins():
        cels = degrees - 273
        fahr = cels * 9/5 + 32
        return exit_text.format(cels, fahr, degrees)


def temp_calc():
    if temper_type == 'C':
        print(celsius())
    if temper_type == 'F':
        print(fahreinheits())
    if temper_type == 'K':
        print(kelvins())


temp_calc()