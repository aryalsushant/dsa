"""
You are given a circularly sorted list of integers. A circularly sorted list of integers is a sorted list whose 
elements have then been rotated some number of times such that the last element of the array becomes the first 
element of the array. Write a function count_rotations() that returns the total number of times the array is rotated.
Assume there are no duplicates in the array.
"""
def count_rotations(nums):
	
    #this is the same as finding the index of the smallest element
    left = 0
    right = len(nums)-1
    while left<right:
        middle = (left+right)//2

        if nums[middle]>nums[right]:
            left = middle+1
        else:
            right = middle
        
    return left
        
		

# Example Input: [8, 9, 10, 2, 5, 6]
# Expected Output: 3
# Explanation: Array is rotated 3 times:
	# Sorted Array: [2, 5, 6, 8, 9, 10]
	# First Rotation: [10, 2, 5, 6, 8, 9]
	# Second Rotation: [9, 10, 2, 5, 6, 8]
	# Third Rotation: [8, 9, 10, 2, 5, 6]

print(count_rotations([8, 9, 10, 2, 5, 6]))  # Output: 3
