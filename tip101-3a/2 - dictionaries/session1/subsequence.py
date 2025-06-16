"""
a function is_subsequence() takes in lst and sequence and determines whether sequence is a subsequence of lst
create an empty list
step 1. iterate through main list
step 2. if item in main list = item in sequence, append to new list
.. check if lists are same size 
step 3. check if new list = sequence
step 4. return true or false

"""

def is_subsequence(lst, sequence):
    new_list = []
    for item in lst:
        for i in sequence:
            if i == item:
                new_list.append(item)
    print(new_list)
    return new_list == sequence





#example test case
lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))