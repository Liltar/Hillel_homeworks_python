_list = [1, 2, 3]
another_list = _list.copy()
for element in _list:
    _list.append(element)
print(_list)