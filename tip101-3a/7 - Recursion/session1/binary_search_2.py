"""
Binary search is a searching algorithm that allows us to efficiently find the index of a given value within a 
sorted list. Given the pseudo code for binary search below, implement an iterative (non-recursive) implementation 
of binary search that returns True if the given target is in the list and False otherwise. There is also a recursive 
alternative that we’ll cover in the session 2 problem set!

Evaluate the time and space complexity of your implementation.
"""
def binary_search(lst, target):
    # Initialize a left pointer to the 0th index in the list
    left = 0
    # Initialize a right pointer to the last index in the list
    right = len(lst) - 1
    # While left pointer is less than right pointer:
    while left < right:
        # Find the middle index of the array
        middle = (left + right) // 2

        # If the middle value is the target value, return True
        if middle == target:
            return True
        # If the middle value is smaller than the target value, search the right half of the list
        elif middle < target:
            left = middle + 1
        # If the middle value is greater than the target value, search the left half of the list
        else:
            right = middle - 1

    # Return False if the target element has not been found
    return False

#test case
# Sample sorted list
lst = [1, 3, 5, 7, 9, 11, 13, 15]

# Test cases
print(binary_search(lst, 7))   # Expected output: True
print(binary_search(lst, 2))   # Expected output: False
print(binary_search(lst, 15))  # Expected output: True
print(binary_search(lst, 1))   # Expected output: True
print(binary_search(lst, 20))  # Expected output: False

