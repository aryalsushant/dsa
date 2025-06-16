"""
start value and stop value are given. you gotta print a sum of all numbers in the range (inclusive)
"""

def sum_range(start, stop):
    sum = 0
    for num in range(start, stop+1):
        sum = sum + num
    return sum

print(sum_range(3,9))
