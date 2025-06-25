#!/usr/bin/env python3
import sys
if len(sys.argv) != 2:
    print("none")
else:
    input_string = sys.argv[1]
    
    found_zs = []
    
    for char in input_string:
        if char == 'z':
            found_zs.append('z')
    
    if found_zs:
        print("".join(found_zs))
    else:
        print("none")