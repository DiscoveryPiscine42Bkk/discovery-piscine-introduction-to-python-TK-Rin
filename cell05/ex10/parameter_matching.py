#!/usr/bin/env python3
import sys
if len(sys.argv) != 2:
    print("none")
else:
    x = sys.argv[1]
    print("What was the parameter? ", end='')
    y = input()
    
    if y == x:
        print("Good job!")
    else:
        print("Nope, sorry...")