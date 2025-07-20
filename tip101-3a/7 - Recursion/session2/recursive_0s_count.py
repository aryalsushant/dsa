"""
Implement count_zeroes() recursively.
"""
def count_zeroes(lst, left = 0, right = None):
	if right == None:
		right = len(lst)-1
	if left>right:
		return len(lst)
	middle = (left+right)//2
	if lst[middle]==1:
		if middle == 0 or lst[middle-1]==0:
			return middle
		else:
			return count_zeroes(lst, left, middle-1)
	else:
		return count_zeroes(lst, middle+1, right)
	
print(count_zeroes([0, 0, 0, 1, 1]))  # Output: 3
print(count_zeroes([0, 0, 0, 0]))     # Output: 4
print(count_zeroes([1, 1, 1, 1]))     # Output: 0
print(count_zeroes([]))              # Output: 0
print(count_zeroes([0]))             # Output: 1
print(count_zeroes([1]))             # Output: 0
