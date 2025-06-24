#!/usr/bin/env python3
array = [2, 8, 9, 48, 8, 22, -12, 2]
p_array = []
for number in array:
    p_array.append(number + 2)
a_array = [number for number in p_array if number >= 5]
new_array = list(set(a_array))
print(array)
print(new_array)