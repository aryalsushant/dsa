"""
Given a sorted list of integers containing only 0s and 1s, count the total number of 0’s in the array in O(log n) time.
"""
def count_zeroes(lst):
	#number of 0s is just the index of the first 1?
    left = 0
    right = len(lst)-1
    first_occurence = len(lst)
    while left <= right:
        middle = (left+right)//2
        if lst[middle] == 1:
            first_occurence = middle
            right = middle -1
        else:
            left = middle +1
    return first_occurence

print(count_zeroes([0, 0, 0, 1, 1]))  # Output: 3
print(count_zeroes([0, 0, 0, 0]))     # Output: 4
print(count_zeroes([1, 1, 1]))        # Output: 0
print(count_zeroes([]))              # Output: 0
