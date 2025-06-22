"""
Write a function sum_of_unique_elements() that takes in two lists of integers, lst1 and lst2, 
as parameters and returns the sum of the elements that are unique in lst1.

An element is unique if:

it appears exactly once in lst1
it does not appear in lst2
ok we can use .count function to know how many times an item appears in a list
"""
def sum_of_unique_elements(lst1, lst2):
	result = []
	for i in lst1:
		if lst1.count(i)==1 and i not in lst2:
			result.append(i)
	return sum(result)
		
		

#test case
lstA = [1, 2 ,3, 4] 
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]

sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1)

sum2 = sum_of_unique_elements(lstC, lstB)
print(sum2)