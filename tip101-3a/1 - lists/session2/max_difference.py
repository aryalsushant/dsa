"""
take in a list of integer and return the difference between the largest and smallest value
"""
#Step 1: create new variables for max and min values =0
#Step 2: finding the minimum, 


#daniel's soln
#current min = lst [] and current_max = lst[0]
#start iterating, if num < current_min, current_min=num
#if num < current_max, current_max = num
#return current_max - current_min
def max_difference(lst):
    current_max=lst[0]
    current_min=lst[0]

    for num in lst:
        if current_max < num:
            current_max = num
        elif current_min > num:
            current_min = num
    return(current_max - current_min)

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)
            
        
    



