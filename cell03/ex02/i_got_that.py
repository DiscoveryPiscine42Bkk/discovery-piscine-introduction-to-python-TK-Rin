#!/usr/bin/env python3
x = False
while True:
    if not x:
        y = input("What you gotta say? : ")
        x = True
    else:
        y = input("I got that! Anything else? : ")

    if y == "STOP":
        break