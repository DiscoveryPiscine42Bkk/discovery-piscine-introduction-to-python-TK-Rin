#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
    print("none")
else:
    num_parameters = len(sys.argv) - 1
    print(f"parameters: {num_parameters}")
    for param in sys.argv[1:]:
        print(f"{param}: {len(param)}")