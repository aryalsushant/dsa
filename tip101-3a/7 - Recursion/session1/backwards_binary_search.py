"""
Generally binary search returns the index of the first occurrence of the target in the list. Write an updated 
version of binary search find_last() that, given a list that may contain duplicates, returns the index of the last 
occurrence of target.

Evaluate the time and space complexity of your function.
"""

def find_last(lst, target):
	# Initialize a left pointer to the 0th index in the list
    left = 0
	# Initialize a right pointer to the last index in the list
    right = len(lst)-1
    result = -1
	
	# While left pointer is less than right pointer:
    while left<=right:
		# Find the middle index of the array
        middle = (left+right)//2
		
		# If the value at the middle index is the target value:
        if lst[middle] == target:
			# Return the middle index
            result = middle
            left = middle +1
		# Else if the value at the middle index is less than our target value:
        elif lst[middle] < target:
			# Update pointer(s) to only search right half of the list in next loop iteration
            left = middle +1
		# Else
        else:
			# Update pointer(s) to only search left half of the list in next loop iteration
            right = middle -1
	
	# If we search whole list and haven't found target value, return -1
    return result