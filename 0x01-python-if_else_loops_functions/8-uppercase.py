#!/usr/bin/pyton3
def uppercase(s):
    for i in s:
        tmp = i
        if ord(tmp) >= 97 and ord(tmp) <= 122:
            temp = chr(ord(i) - 32)
        print("{}".format(tmp), end='')
    print()
