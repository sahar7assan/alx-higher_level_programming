#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg = sys.argv
    sum_of_arg = 0

if len(arg) > 1:
    for i in arg:
        if i != arg[0]:
            sum_of_arg += int(i)
print("{}".format(sum_of_arg))
