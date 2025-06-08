"""
function name is self explanatory

nahh this is the best problem i have done so far. i thought this would be harder

step 1, iterate through a range of numbers
start: length of list -1, stop before -1, step -1
append every item to new list
return the new list
easy peasy
"""

def reverse_list(lst):
    new_lst=[]
    for i in range(len(lst)-1, -1, -1):
        new_lst.append(i)
    return new_lst

lst = [1,2,3,4,5]
rev_lst = reverse_list(lst)
print(rev_lst)

