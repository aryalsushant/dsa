"""
Write a function remove_duplicates() that takes in a sorted list of integers nums as a parameter and removes 
the duplicates in-place such that each element appears only once. Do not allocate extra space for another array; 
you must do this by modifying the input list with O(1) extra memory. The function returns the new length of the list.

my idea:
two pointers next to each other
if left = right, remove item in left and move left by 1, move right by 1
if left != right, move right by 1 and keep left where it is
but nah this wont work cause second item has nothing to be compared to.
"""

def remove_duplicates(nums):
    i = 0 #this is the index of the first unique element
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i+=1
            nums[i]=nums[j]
    del nums[i+1:]
    return i+1

#test case
nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) # same list