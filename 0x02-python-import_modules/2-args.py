#!/usr/bin/python3
if __name__ == "__main__":
    import sys

arguments = sys.argv
length = len(arguments) - 1

if length == 0:
    print("{} arguments.".format(length))

elif length > 1:
    print("{} arguments:".format(length))
    for i, arg in enumerate(arguments):
        if i == 0:
            pass
        else:
            print("{}: {}".format(i, arg))
else:
    print("{} argument:".format(length))
    print("{}: {}".format(length, arguments[1]))
