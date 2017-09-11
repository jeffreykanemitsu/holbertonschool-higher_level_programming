#!/usr/bin/python3


import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
my_list = []

fn = "add_item.json"

try:
    my_list = load_from_json_file(fn)
except:
    my_list = []

for i in argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, fn)
