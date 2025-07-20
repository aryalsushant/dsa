"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order. You must write an algorithm with O(log n) 
runtime complexity.
"""
def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if the middle element is the target
        if nums[mid] == target:
            return mid
        
        # If the target is less than the middle element, search in the left half
        if target < nums[mid]:
            right = mid - 1
        # Otherwise, search in the right half
        else:
            left = mid + 1
    
    # If the target is not found, 'left' will be the index where it can be inserted.
    return left

def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr)-1
    mid = (left+right)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binary_search_recursive(arr, target, left, mid-1)
    else:
        return binary_search_recursive(arr, target, mid+1, right)