"""
a function that returns the sum of all even values in a dictionary
assume the values are all integers
"""

def sum_even_values(dictionary):
    sum = 0
    for value in dictionary.values():
        if value%2==0:
            sum += value
    return sum

#test case
dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
print(sum_even_values(dictionary))