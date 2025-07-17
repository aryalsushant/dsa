"""
Binary search is a searching algorithm that allows us to efficiently find the index of a given value within a 
sorted list. Given the pseudo code for binary search below, implement an iterative (non-recursive) implementation
 of binary search. There is also a recursive alternative that we’ll cover in the session 2 problem set!

Evaluate the time and space complexity of your implementation.
"""
def binary_search(lst, target):
	# Initialize a left pointer to the 0th index in the list
    left = 0
	# Initialize a right pointer to the last index in the list
    right = len(lst)-1
	
	# While left pointer is less than right pointer:
    while left<right:
		# Find the middle index of the array
        middle = (left+right)//2
		
		# If the value at the middle index is the target value:
        if lst[middle] == target:
			# Return the middle index
            return middle
		# Else if the value at the middle index is less than our target value:
        elif lst[middle] < target:
			# Update pointer(s) to only search right half of the list in next loop iteration
            left = middle +1
		# Else
        else:
			# Update pointer(s) to only search left half of the list in next loop iteration
            right = middle -1
	
	# If we search whole list and haven't found target value, return -1
    return -1
