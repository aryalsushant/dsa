def find_middle(lst):
    slow=fast=0
    while fast < len(lst) and fast+1 <len(lst):
        slow+=1
        fast+=2
    return lst[slow]
#example
lst = [1,2,3,4,5,6]
print(find_middle(lst))

#the error is that for a list with even number of elements, this function returns the element one position after the middle
        