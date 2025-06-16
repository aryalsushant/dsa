"""
take two dictionaries
return a new dictionary with items that are in both dictionaries
key-value pairs should be the same
"""

def dict_intersection(d1, d2):
    d3={}
    for key1, value1 in d1.items():
        for key2, value2 in d2.items():
            if key1==key2 and value1==value2:
                d3[key1]=value1
    return d3

#test case
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 4}

print(dict_intersection(d1, d2))