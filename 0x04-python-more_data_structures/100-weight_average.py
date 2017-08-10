#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    den = 0 #dividen
    sor = 0 #divisor
    for (x, y) in my_list:
        den += (x * y)
        sor += y
    return den / sor
