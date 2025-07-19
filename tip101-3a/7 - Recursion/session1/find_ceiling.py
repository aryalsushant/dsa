"""
Given a sorted list of integers and a value x, return the index of the ceiling of x.
 The ceiling of x is the smallest element in the array larger than or equal to x. If 
 there is no ceiling of x, return -1.

Evaluate the time and space complexity of your function.
"""
def find_ceiling(lst, x):
	left = 0
	right = len(lst)-1
	result = -1
	while left <= right:
		middle = (left+right)//2
		if lst[middle]==x:
			return middle
		elif lst[middle]<=x:
			left = middle +1
		else:
			result = middle
			right = middle -1
	return result

lst = [1, 2, 8, 10, 11, 12, 19]
x = 5
print(find_ceiling(lst, x))