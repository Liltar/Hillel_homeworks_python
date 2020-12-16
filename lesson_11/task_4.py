# 4. Написать функцию которая заменит в тексте слово на другое.
#
#   Функция принимает 4 аргумента, изначальная строка, заменяемое слово, новое слово, количество замен, пример:
#
#  fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 1) ->
#  'Marvel makes good movies, DC makes good comics'

#  fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 2) ->
#  'Marvel makes good movies, Marvel makes good comics'


def replacement(some_string, old_word, new_word, times_of_replacement):
    return some_string.replace(old_word, new_word, times_of_replacement)


print(replacement('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 1))
