#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return None
    sorted_dict = sorted(my_dict)
    return(sorted_dict[-1])
