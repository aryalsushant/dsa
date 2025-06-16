"""
we're given two dictionaries
we return a list of common keys

create an empty list
you create a new list
loop thru list of keys in dict 1
if key in dict2, append key to list
return list
return list

"""

def common_keys(dict1, dict2):
    lst = []
    for key in dict1.keys():
        if(key in dict2):
            lst.append(key)
    return lst

#example test case
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)
