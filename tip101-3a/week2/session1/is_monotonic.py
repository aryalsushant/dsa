"""

"""

def is_monotonic(nums):
    is_decreasing = True
    is_increasing = True
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            is_decreasing = False
        if nums[i] < nums[i-1]:
            is_increasing = False
    return is_decreasing or is_increasing
    
#example test case
nums1 = [1,2,2,3,10]
print(is_monotonic(nums1))

nums2 = [12,9,8,3,1]
print(is_monotonic(nums2))

nums3 = [1,1,1]
print(is_monotonic(nums3))

nums4 = [1,9,8,3,5]
print(is_monotonic(nums4))