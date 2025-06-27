"""
Problem 2: Two-Pointer Reverse List
Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order.
 The list should be reversed in-place without using list slicing (e.g. lst[::-1]).

Instead, use the two-pointer approach, which is a common technique in which we initialize two variables 
(also called a pointer in this context) to track different indices or places in a list or string, then moves the
 pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, 
 we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list.
   We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the 
   pointers reach the opposite ends of the list.

1. make the pointers left = 0 and right = len(lst)-1

2. while left < right:
3.      flip the right and left
    keep moving
"""

def reverse_list(lst):
    left = 0
    right = len(lst)-1
    while left < right:
        replace_left = lst[left]
        lst[left] = lst[right]
        lst[right] = replace_left

        left+=1
        right-=1

    return lst


#test case
lst = [1,2,3,4,5]
print(reverse_list(lst))
