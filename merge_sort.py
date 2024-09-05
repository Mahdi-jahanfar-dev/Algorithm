from random import shuffle as shfl
def merge(list_1,list_2):
    list_3 = []

    len_list_1 = len(list_1)
    len_list_2 = len(list_2)

    i = j = 0

    while i<len_list_1 and j<len_list_2:
        if list_1[i]<list_2[j]:
            list_3.append(list_1[i])
            i+=1
        else:
            list_3.append(list_2[j])
            j+=1

    list_3 += list_1[i:]
    list_3 += list_2[j:]

    return list_3


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    else:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)

length = 10

_list = [i for i in range(length)]

shfl(_list)

print(merge_sort(_list))