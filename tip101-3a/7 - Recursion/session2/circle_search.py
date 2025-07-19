"""
Given a circularly sorted list of integers, return the index of a given target. 
Assume there are no duplicates in the list.
"""
def search_circular_list(nums, target):
    # Start by setting the left and right pointers to the beginning and end of the list
    left = 0
    right = len(nums) - 1

    # Keep looping as long as the search window is valid (left doesn't pass right)
    while left <= right:
        # Find the middle index between left and right
        # This is the element we will check in this round
        mid = (left + right) // 2

        # If the element at the middle index is the target, we're done
        # Return the index where we found it
        if nums[mid] == target:
            return mid

        # Now we need to decide which half of the list to search next
        # Check if the left half (from left to mid) is sorted
        # In a rotated sorted array, one of the two halves will always be sorted
        if nums[left] <= nums[mid]:
            # The left half is sorted

            # Check if the target lies within the sorted left half
            # If it does, we can safely ignore the right half
            if nums[left] <= target < nums[mid]:
                # Target is somewhere between left and mid (not including mid)
                # So we move the right pointer just before mid
                right = mid - 1
            else:
                # Target is not in the sorted left half
                # So we search the right half by moving the left pointer after mid
                left = mid + 1
        else:
            # If the left half isn't sorted, then the right half must be sorted

            # Check if the target is within the sorted right half
            if nums[mid] < target <= nums[right]:
                # Target is between mid and right (inclusive of right)
                # So we move the left pointer just after mid to search the right half
                left = mid + 1
            else:
                # Target is not in the sorted right half
                # So we search the left half by moving the right pointer before mid
                right = mid - 1

    # If we've searched the entire list and didn't find the target
    # Return -1 to indicate it's not present
    return -1

# Test case
nums = [15, 18, 2, 3, 6, 12]
target = 3

# Run the function and print the result
print("Index of", target, "is:", search_circular_list(nums, target))
				
			