#!/usr/bin/env python3
import sys
parameters = sys.argv[1:]
if len(parameters) < 2:
    print("none")
else:
    parameters.reverse()
    for param in parameters:
        print(param)