"""
take in a list of integers nums containing n unique elements in the range [0, n]. print the missing number from that range
hint: use sort()

step 1: sort the array
step 2: iterate through i in range(length of array)
step 4" if item in range != array[i], return that number
"""

def find_missing(nums):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] != i:
            return(i)

nums = [2,4,1,0,5]
missing_num = find_missing(nums)
print(missing_num)