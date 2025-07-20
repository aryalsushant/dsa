"""
Merge sort is a sorting algorithm that takes in an unsorted list and returns a sorted list in O(n log n) time 
which is faster than many other sorting algorithms that have O(n²) time complexity. It uses a divide and conquer approach.

Merge sort works by using a divide and conquer approach: it divides the array into two halves until each sublist 
contains only a single element, then it recursively sorts each sublist, and merges the sorted sublists into a sorted array.

Given the pseudo-code below, implement the merge_sort() function.
"""
def merge(left, right):
	
	# Initialize an empty list to store the merged result
	result = []
	# Initialize a pointer to iterate over the left input list
	i = 0
	# Initialize a pointer to iterate over the right input list
	j = 0
	
	# Iterate over left & right lists simultaneously
	while i<len(left) and j<len(right) :
		# Compare elements at same indices of left and right halves of the list 
		if left[i]<=right[j]:
			result.append(left[i])
			i+=1
		# Add them to the result list in the correct order
		else:
			result.append(right[j])
			j+=1
  # Add any remaining elements from the left half to the result list
	while i < len(left):
		result.append(left[i])
		i+=1

  # Add any remaining elements from the right half to the result list
	while j < len(right):
		result.append(right[j])
		j += 1
	return result

def merge_sort(lst):
	if len(lst)<=1:
		return lst
	mid = len(lst)//2
	left = merge_sort(lst[:mid])
	right = merge_sort(lst[mid:])
	return merge(left, right)

print(merge_sort([5, 3, 8, 1, 2, 7]))
# Output: [1, 2, 3, 5, 7, 8]

