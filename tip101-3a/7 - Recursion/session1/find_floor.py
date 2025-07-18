"""
Given a sorted list of integers and a value x, return the index of the floor of x. The floor of x is the 
largest element in the array smaller than or equal to x. If there is no floor of x, return -1.

Evaluate the time and space complexity of your function.
"""
def find_floor(lst, x):
    left = 0
    right = len(lst)-1
    result = -1
    while left<=right:
        middle = (left+right)//2
        if lst[middle] == x:
            return middle
        elif lst[middle]<x:
            result = middle
            left = middle +1
        else:
            right = middle -1
    return result
			
    

lst = [0,1,2,3,4,5,6,7,8]
x = 5
print(find_floor(lst, x))
