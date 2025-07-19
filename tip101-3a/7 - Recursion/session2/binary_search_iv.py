"""
Thus far, we’ve mostly been using an iterative implementation of the binary search algorithm. 
Recursive implementations of binary search are also very common. 
Implement binary_search() recursively.
"""
def binary_search(nums, target, left = 0, right = None):
    if right is None:
        right = len(nums)-1
    if left>right:
        return -1
    
    #binary search starts here
    middle = (left+right)//2
    if nums[middle]==target:
        return middle
    elif nums[middle]< target:
        return binary_search(nums, target, middle+1, right)
    else:
        return binary_search(nums, target, left, middle-1)


nums = [1, 3, 5, 7, 9, 11, 13, 15] 
target = 11
print(binary_search(nums, target))
