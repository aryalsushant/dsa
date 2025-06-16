"""
go thru a list of integers and print the index of each item
"""


def print_indices(lst):
    for num in range(len(lst)):
        print(num)

print_indices([3,4,5,6,2,4,5])