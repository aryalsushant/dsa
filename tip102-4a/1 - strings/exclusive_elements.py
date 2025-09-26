"""
Given two lists lst1 and lst2, write a function exclusive_elemts() that returns a new list that contains the 
elements which are in lst1 but not in lst2 and the elements that are in lst2 but not in lst1.
"""
def exclusive_elemts(lst1, lst2):
	result = []
	for item in lst1:
		if item not in lst2:
			result.append(item)
	for item in lst2:
		if item not in lst1:
			result.append(item)
	return result

#test case
lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
print(exclusive_elemts(lst1, lst2))