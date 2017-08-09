#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    max = my_list[0]
    length = len(my_list)
    for x in range(length):
        if max < my_list[x]:
          max = my_list[x]
    return max
