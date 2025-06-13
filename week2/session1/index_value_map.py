"""
take in a list
return a dictionary with the index of each item as key and item as value
"""
def index_to_value_map(lst):
    dictionary = {}
    for i in range(len(lst)):
        dictionary[i] = lst[i]
    return dictionary

#example test case
lst = ["apple", "banana", "cherry"]
print(index_to_value_map(lst))

#no way i did this by myself lol
    