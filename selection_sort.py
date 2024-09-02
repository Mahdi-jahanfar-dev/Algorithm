from random import randint as rand

length = 10
_list = [rand(0,length) for i in range(length)]

for i in range(length-1):
    _min = i
    for j in range(i+1, length):
        if _list[_min] > _list[j] :
            _min = j
    _list[i], _list[_min] = _list[_min], _list[i]




print(_list)