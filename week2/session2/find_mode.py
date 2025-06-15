"""
Write a function find_mode() that takes in a non-empty list of integers lst as a parameter. 
The function returns the mode (the most frequently occurring number) and if there is a tie, return 
the element which appeared first in the list.

step 1 make a hashmap
step 2 loop through list of values of the hashmap
step 3 if value at index i and index i-1 is equal, return index i-1
step 4 else: create a new variable, make it equal to the highest value, return the corresponding key
"""

def find_mode(lst):
    hashmap = {}
    for item in lst:
        if item in hashmap:
            hashmap[item] +=1
        else:
            hashmap[item] = 1
    highest = 0
    result = 0
    for key, value in hashmap.items():
        if value > highest:
            highest = value
            result = key
    return result
    #as i was coding i realized i dont need to check which key appeared first,
    #if two keys have same frequency then for the second key, value > highest will be false

#test case
lst = [1,2,3,2,3,3,3,4,4,4,4]
mode = find_mode(lst)
print(mode)



