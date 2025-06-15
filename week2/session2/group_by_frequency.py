"""
Example Usage:

lst = ['a', 'b', 'c', 'd', 'd', 'c', 'e', 'e', 'e']
print(group_by_frequency(lst))
Example Output:

{ 1 : ['a', 'b'], 2: ['c', 'd'], 3: ['e']}
"""

def group_by_frequency(lst):
    hashmap = {}
    for item in lst:
        if item in hashmap:
            hashmap[item]+=1
        else:
            hashmap[item]=1
    result = {}
    for key, value in hashmap.items():
        if value not in result:
            result[value]=[key]
        else:
            result[value].append(key)
    return result

#test case
lst = ['a', 'b', 'c', 'd', 'd', 'c', 'e', 'e', 'e']
print(group_by_frequency(lst))