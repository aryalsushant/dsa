"""
Write a function numIdenticalPairs() that takes in a list of integers nums and returns the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.

eg:
nums = [1,2,3,1,1,3]
ans = numIdenticalPairs(nums)
# ans == 4
"""

def numIdenticalPairs(nums):
    counter = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
        #using i+1 to make sure j is greater than i
            if nums[i]==nums[j]:
                counter+=1
    return counter

#test case
nums = [1,2,3,1,1,3]
ans = numIdenticalPairs(nums)
print(ans)