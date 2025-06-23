#!/usr/bin/env python3
import math

x = input("Give me a number: ")
try:
    num = float(x)
    rounded_num = math.ceil(num)
    print(rounded_num)
except ValueError:
    print("That's not a valid number.")