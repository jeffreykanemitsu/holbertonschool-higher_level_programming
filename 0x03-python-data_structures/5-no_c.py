#!/usr/bin/python3
def no_c(my_string):
    return my_string.translate({ord(x): '' for x in "cC"})
