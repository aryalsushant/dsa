"""
Without using the built-in sum() function, write a function sum_list() that calculates the sum of all values
in a list recursively.

What is the time complexity of this function? What is the space complexity?
"""
def sum_list(lst):
	if len(lst)==0:
		return 0
	return lst[0]+sum_list(lst[1:])