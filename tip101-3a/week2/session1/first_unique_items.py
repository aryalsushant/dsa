"""
Write a function find_unique_items() that takes two lists list_a and list_b as parameters.
 The function identifies unique items from the lists and returns a dictionary with the items as keys
 and a boolean value as the value indicating whether the item is unique to the first list (True) or not (False).
"""

def find_unique_items(list_a, list_b):
    dict = {}

    for item1 in list_a:
        if item1 not in list_b:
            dict[item1] = True
    for item2 in list_b:
        if item2 not in list_a:
            dict[item2] = False
    return dict
#test case
list_a = ["apple", "banana", "carrot"]
list_b = ["apple", "banana", "date"]

print(find_unique_items(list_a, list_b))