#!/usr/bin/env python3
x = int(input("Enter a number less than 25: "))
if x > 25:
    print("Error")
else:
    for y in range(x, 26):
        print("Inside the loop, my variable is", y)