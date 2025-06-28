"""
The two-pointer approach can also be used with two pointers that iterate forward through a list or string at
 different rates. Use two pointers to solve the following problem:

Write a function removeElement() that takes in a list nums and a value val as parameters and removes all 
instances of that value in-place. The function returns the new length of nums.
"""
def removeElement(nums, val):
    write = 0
    for read in range(len(nums)):
        if nums[read]!=val:
            nums[write]=nums[read]
            write += 1
    
    del nums[write:]
    return write


#test case
nums = [5, 4, 4, 3, 4, 1]
nums_len = removeElement(nums, 4)
print(nums) # same list
print(nums_len)

"""
outputs:
[5, 3, 1]
3
"""