"""
Write a function interleave_lists() that accepts two lists as parameters. The function should return a new list that
 combines the given lists by alternating which list it takes its next element from. It will take elements in order, and 
 if one list is longer it will append the remaining elements to the end of the interleaved list.
"""
def interleave_lists(lst1, lst2):
    result = []
    if len(lst1)>=len(lst2):
        for i in range(len(lst2)):
            result.append(lst1[i])
            result.append(lst2[i])
        for i in range(len(lst2), len(lst1)):
            result.append(lst1[i])
    else:
        for i in range(len(lst1)):
            result.append(lst1[i])
            result.append(lst2[i])
        for i in range(len(lst1), len(lst2)):
            result.append(lst2[i])
    return result

            

#test case
lst1 = [1, 2, 3, 4]
lst2 = [10, 20]
inter_lst = interleave_lists(lst1, lst2)
print(inter_lst)