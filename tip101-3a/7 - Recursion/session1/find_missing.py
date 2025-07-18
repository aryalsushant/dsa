"""
Given a sorted list of integers nums containing n distinct numbers in the range [0, n], return the only
 number in the range that is missing from the list.

Your solution must have O(log n) time complexity.
"""
def find_missing(nums):
	left = 0
	right = len(nums)-1
	while left<=right:
		middle = (left+right)//2
		if nums[middle]==middle:
			left = middle +1
		else:
			right = middle -1
	return left


# Test cases
print(find_missing([0, 1, 2, 3, 4, 6]))      # Expected: 5
print(find_missing([0, 1, 2, 3, 5]))         # Expected: 4
print(find_missing([1, 2, 3, 4, 5]))         # Expected: 0
print(find_missing([0, 1, 2, 3, 4]))         # Expected: 5
print(find_missing([0, 2, 3, 4, 5, 6, 7]))   # Expected: 1