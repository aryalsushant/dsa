"""
return the sum of numbers from 1 to a given STOP value (inclusive)
"""
def sum_positive_range(stop):
    sum = 0
    for num in range(1, stop+1):
        sum = sum + num
    return sum



print(sum_positive_range(6))