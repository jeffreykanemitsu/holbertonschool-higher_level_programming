#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value))
        return True
    except TypeError as t:
        print("Exception: {}".format(t), file=stderr)
        return False
    except ValueError as v:
        print("Exception: {}".format(v), file=stderr)
        return False
