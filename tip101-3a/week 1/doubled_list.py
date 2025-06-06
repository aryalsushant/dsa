#step 1, iterate through the list
# print 2 times each item


def doubled(lst):
    new_list=[]
    for num in lst:
        

        #new_list.append(num*(-1))
        new_list.append(num*2)
    return new_list

lst = [1,2,3]
print(doubled(lst))


#edge cases: empty list, letters(basically any non-numeric value), negatve numbers
#if there's any non-numeric value, skip it
