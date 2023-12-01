#!/usr/bin/python3
if __name__ == "__main__":
    """print the number of and list of argument"""
    import sys
    count = len(sys.argv) - 1
    if count == 0:
        print("0 argument")
    elif  count == 1:
        print("1 argument:")
    else:
        print("{} argument:".format(count))
    for n in range(count):
        print("{}: {}".format(n + 1, sys.argv[n + 1]))
