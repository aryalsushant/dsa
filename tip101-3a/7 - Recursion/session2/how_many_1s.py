"""
Given a sorted list of integers containing only 0s and 1s, count the total number of 1’s in the array in O(log n) time.
"""
"""
def count_ones(lst):
	left = 0
	right = len(lst)-1
	result = 0
	while left <= right:
		middle = (left+right)//2
		if lst[middle]<1:
			left = middle + 1
		else:
			left +=1
			result +=1
	return result
#this solution is O(n) not O(logn)
"""
def count_ones(lst):
    left = 0
    right = len(lst)-1
    first_occurence = -1
    while left <= right:
        middle = (left+right)//2
        if lst[middle]==1:
            first_occurence = middle
            right = middle -1
        else:
            left = middle + 1
    if first_occurence == -1:
        return 0
    else:
        return len(lst)-first_occurence



print(count_ones([0, 0, 0, 0, 1, 1, 1]))