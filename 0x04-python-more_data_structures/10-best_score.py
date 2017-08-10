#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None or my_dict is 0:
        return None
    sorted_dict = sorted(my_dict)
    return(sorted_dict[-1])
