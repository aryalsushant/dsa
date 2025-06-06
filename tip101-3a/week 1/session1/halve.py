"""
write a function that divides each value in a list by 2
"""
def halve_lst(lst):
    result = []
    
    for num in lst:
        halved = num/2
        result.append(halved)
    return result

print(halve_lst([2,4,6,8]))
