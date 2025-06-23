#!/usr/bin/env python3
x = int(input("What's your first number?: "))
y = int(input("What's your second number?: "))
z = x * y
print(x, "x", y, "=", z)
v = int(z)
if v < 0:
    print("This number is negative.")
elif v > 0:
    print("This number is positive.")
elif v == 0:
    print("This number is both positive and negative.")