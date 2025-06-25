#!/usr/bin/env python3
def find_the_redheads(family_dict):
    redheads = []
    for name, hair_color in family_dict.items():
        if hair_color == "red":
            redheads.append(name)
    return redheads
dupont_family = {
    "florian": "red",
    "marie": "blond",
    "david": "red",
    "amelia": "brunette",
    "franck": "red"
}
print(find_the_redheads(dupont_family))