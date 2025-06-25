#!/usr/bin/env python3
def array_of_names(persons_dict):
    full_names = []
    for first, last in persons_dict.items():
        full_names.append(f"{first.capitalize()} {last.capitalize()}")
    return full_names
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
print(array_of_names(persons))