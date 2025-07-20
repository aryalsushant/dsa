"""
Implement count_zeroes() recursively.
"""
def count_zeroes(lst, left=0, right=None):
    # This function returns the number of 0s in a sorted list of 0s and 1s using recursion.
    # It works by finding the index of the first occurrence of 1.
    # Since all 0s come before 1s in a sorted list, that index equals the number of 0s.

    # On the first call, we don't know what 'right' should be,
    # so we set it to the last index of the list
    if right is None:
        right = len(lst) - 1  # This ensures we search the entire list initially

    # Base case: If left index goes beyond the right index,
    # it means we’ve searched all possible locations and didn’t find a 1
    if left > right:
        return len(lst)  # No 1s found at all, so all values are 0s → return total length

    # Calculate the middle index of the current search window
    mid = (left + right) // 2  # Binary search always looks at the midpoint

    # If the middle element is 1, we might have found the first 1
    if lst[mid] == 1:
        # Now check if it is really the *first* 1 in the list
        # This is true if it's the first element (index 0), or the one before it is 0
        if mid == 0 or lst[mid - 1] == 0:
            return mid  # We’ve found the first 1 → index = count of 0s
        else:
            # If it's not the first 1, search the left half to find an earlier one
            return count_zeroes(lst, left, mid - 1)

    else:
        # If the middle element is 0, then we need to search the right half
        # Because the first 1 (if it exists) must be further to the right
        return count_zeroes(lst, mid + 1, right)

	
print(count_zeroes([0, 0, 0, 1, 1]))  # Output: 3
print(count_zeroes([0, 0, 0, 0]))     # Output: 4
print(count_zeroes([1, 1, 1, 1]))     # Output: 0
print(count_zeroes([]))              # Output: 0
print(count_zeroes([0]))             # Output: 1
print(count_zeroes([1]))             # Output: 0
