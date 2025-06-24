#!/usr/bin/env python3
import sys
import re
parameters = sys.argv[1:]
if len(parameters) == 2:
    keyword = parameters[0]
    text_to_search = parameters[1]
    matches = re.findall(keyword, text_to_search)
    print(len(matches))
else:
    print("none")