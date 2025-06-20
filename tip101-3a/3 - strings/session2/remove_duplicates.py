"""
Write a function remove_duplicates() that takes in a sorted list of 
integers nums as a parameter and removes all duplicates in the list. 
The function returns the modified list.

Example Input: nums = [1,1,1,2,3,4,4,5,6,6]
Example Output: no_dups = [1,2,3,4,5,6]
"""
def remove_duplicates(nums):
    result = []
    for num in nums:
        if num not in result:
            result.append(num)
    return result

#test case
nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))