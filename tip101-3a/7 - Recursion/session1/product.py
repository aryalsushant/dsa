"""
Write a function list_product() that calculates the product of all values in a list recursively.

What is the time complexity of this function? What is the space complexity?
"""
def list_product(lst):
	if lst == []:
		return 1
	else:
		return lst[0] * list_product(lst[1:])
	
print(list_product([1,2,3,4,5]))
print(list_product([]))