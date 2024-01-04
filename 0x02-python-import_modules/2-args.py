#!/usr/bin/python3

import sys

arguments = sys.argv
if len(arguments) == 1:
    print("0 arguments.")
elif len(arguments) > 2:
    le = len(arguments) - 1
    print("{} arguments:".format(le))
    for i, arg in enumerate(arguments):
        if i == 0:
            pass
        else:
            print("{}: {}".format(i, arg))
else:  # Changed from len(arguments) == 2 to else
    print("1 argument:")
    print("1:", arguments[1])
