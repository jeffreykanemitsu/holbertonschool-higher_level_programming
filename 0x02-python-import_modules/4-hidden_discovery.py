#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    LOL = dir(hidden_4)
    for x in LOL:
        if x[:0} != "_":
            print("{}".format(x), end="\n")
