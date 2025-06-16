"""
majority element appears more than n/2 times where n is the size of the list
if there is no majority element, return none
"""

def find_majority_element(elements):
    hashmap = {}
    for element in elements:
        if element in hashmap:
            hashmap[element] +=1
        else:
            hashmap[element] = 1
    
    for key, value in hashmap.items():
        if value > len(elements)/2:
            return key
        else:
            return None

#test case
elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))