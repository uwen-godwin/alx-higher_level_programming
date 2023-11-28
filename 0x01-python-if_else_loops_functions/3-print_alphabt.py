#!/usr/bin/python3
for n in range(97, 123):
    if n in [101, 113]:
        continue
    print("{}".format(chr(n)), end='')
