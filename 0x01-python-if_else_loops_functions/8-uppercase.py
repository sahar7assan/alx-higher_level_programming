#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        upper = ord(i)
        if upper in range(97, 123):
            upper = upper - 32
        print("{:c}".format(upper), end="")
    print()
