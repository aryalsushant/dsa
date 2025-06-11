"""
given a list of numbers, move zeroes to the end of the list
"""

def move_zeroes(lst):
    zeroes = 0
    new_list = []
    for i in lst:
        if i != 0:
            new_list.append(i)
        else:
            zeroes += 1
    new_list += [0]*zeroes
    return new_list

nums = [1,0,2,3,0,0,4]
new_nums = move_zeroes(nums)
print(new_nums)