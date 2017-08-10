#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) is 0:
        return 0
    return (sum([x*y for x, y in my_list]) / sum([y for x, y in my_list]))
