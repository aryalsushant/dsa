"""
Given an array nums of size n, use a divide and conquer approach to write a function return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority 
element always exists in the array.
"""
def majority_element(nums, left=0, right=None):
    # Set the right boundary on the first call
    if right is None:
        right = len(nums) - 1

    # Base case: if there's only one element in this segment,
    # then that element is the majority by default
    if left == right:
        return nums[left]

    # Find the middle index to split the array into two halves
    mid = (left + right) // 2

    # Recursively find the majority element in the left half
    left_major = majority_element(nums, left, mid)

    # Recursively find the majority element in the right half
    right_major = majority_element(nums, mid + 1, right)

    # If both halves agree on the majority element, return it
    if left_major == right_major:
        return left_major

    # If the two sides return different elements, we need to count
    # how many times each candidate appears in the full current segment
    left_count = sum(1 for i in range(left, right + 1) if nums[i] == left_major)
    right_count = sum(1 for i in range(left, right + 1) if nums[i] == right_major)

    # Whichever one appears more is the true majority in this segment
    return left_major if left_count > right_count else right_major
