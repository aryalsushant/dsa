"""
Example Input: nums = [1, 2, 2, 3, 3, 3, 4]
Example Output: {1: 1, 2: 2, 3: 3, 4: 1}
"""

def count_occurrences(nums):
    hashmap = {}
    
    for i in nums:
        if i in hashmap:
            hashmap[i] +=1
        else:
            hashmap[i] = 1
    return hashmap

#test case
nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums))
