"""
Pooh is eating all of his hunny jars in order of smallest to largest. Given a list of integers hunny_jar_sizes, 
write a function delete_minimum_elements() that continuously removes the minimum element until the list is empty. 
Return a new list of the elements of hunny_jar_sizes in the order in which they were removed.
"""
def delete_minimum_elements(hunny_jar_sizes):
	result = []
	while hunny_jar_sizes != []:
		min_number = min(hunny_jar_sizes)
		hunny_jar_sizes.remove(min_number)
		result.append(min_number)
	return result

#test cases

hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))
		