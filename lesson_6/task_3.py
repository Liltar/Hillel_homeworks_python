   # 3. Дан список значений. Вернуть словарь где каждый ключ - это индекс листа,
   #
   #    а значение листа - это значение ключа:
   #
   #    Input:
   #
   # ['a', 'b', 'c', 'd', 'e']
   #
   #    Output
   #
   # {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}

some_list = ['a', 'b', 'c', 'd', 'e']
some_list_en = enumerate(some_list)
new_dict = {key: value for key, value in some_list_en}
print(new_dict)

#var 2
# почему ключи начинаются с 1?
def dict_from_list(some_list):
   some_list_en = enumerate(some_list)
   locals()
   for key, value in some_list_en:
      new_dict = {key: value for key, value in some_list_en}
      return new_dict

print(dict_from_list(some_list))