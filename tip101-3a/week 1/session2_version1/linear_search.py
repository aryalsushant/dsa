"""
a function linear_search() takes two parameters: lst and target
if target if found in lst, return index of target
else, return -1

1. loop through the list of numbers between 0 and total length of lst, so all indexes
2. if a value in the index is equal to index, return that index
3. if not return -1, but you cannot put -1 inside the for loop in an else condition
because as soonn as it doesn't find target in first iteration, it will print -1
"""

def linear_search(lst, target):
    for num in range(len(lst)):
        if lst[num] == target:
            return num
    return -1

lst = [1,4,5,2,8]
position = linear_search(lst,5)
print(position)
