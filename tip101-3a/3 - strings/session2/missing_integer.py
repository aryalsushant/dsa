"""
Write a function find_missing_positive() that takes in a sorted list of integers nums that always starts at 1,
and returns the smallest missing positive integer.
"""
def find_missing_positive(nums):
    for i in range(1, nums[-1]):
        if i not in nums:
            return i
    return nums[-1]+1

#test case
nums1 = [1,2,3,5,6,10]
print(find_missing_positive(nums1))

nums2 = [1,2,3,4,5]
print(find_missing_positive(nums2))