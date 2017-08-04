#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    if num == 1:
        print("{}".format("0 argument."))
    if num == 2:
        print("{}".format("1 argument:"))
    if num > 2:
        print("{:d} arguments:".format(num - 1))
    for x in range(1, num):
        print("{:d}: {:s}".format(x, sys.argv[x]))
