"""
Merge sort is a sorting algorithm that takes in an unsorted list and returns a sorted list in O(n log n) 
time which is faster than many other sorting algorithms that have O(n²) time complexity. It uses a divide 
and conquer approach.

Merge sort works by using a divide and conquer approach: it divides the array into two halves until each
 sublist contains only a single element, then it recursively sorts each sublist, and merges the sorted 
 sublists into a sorted array.

Given the main function merge_sort() below, implement the helper function merge() below. merge() accepts 
two sorted lists left and right and returns a sorted list.
"""
def merge_sort(lst):
		# If the length of the list is 0-1, the list is already sorted. 
    if len(lst) <= 1:
        return lst
    
    # Find the middle index of the array
    mid = len(lst) // 2
    # Divide the array into two halves
    left_half = lst[:mid]
    right_half = lst[mid:]
    
    # Recursive calls to merge_sort for sorting the left and right halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted arrays
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i+=1
    while j < len(right):
        result.append(right[j])
        j+=1
    return result

print(merge_sort([5, 3, 8, 2, 1, 9]))
# Output: [1, 2, 3, 5, 8, 9]
