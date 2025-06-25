#!/usr/bin/env python3
import sys
def add_one(num):
    num += 1
    return num
if len(sys.argv) != 2:
    print("none")
else:
    try:
        my_variable = int(sys.argv[1])
        print(my_variable)
        my_variable = add_one(my_variable)
        print(my_variable)
    except ValueError:
        print("none")