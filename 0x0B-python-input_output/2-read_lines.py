#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, 'r', encoding='utf-8') as my_file:
        for i in range(nb_lines):
            if nb_lines <= 0:
                print(my_file.read(), end='')
            else:
                print(my_file.readline(), end='')
