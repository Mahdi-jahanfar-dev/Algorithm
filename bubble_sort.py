from random import randint as rnd

length = 10

_list = [rnd(0,length) for i in range(length)]


for i in range(length-1):
    for j in range(length-i-1):
        if _list[j+1]<_list[j]:
            _list[j], _list[j+1] = _list[j+1], _list[j]



print(_list)