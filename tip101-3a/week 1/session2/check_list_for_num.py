"""
check if a number is in a list. return true if yes and false if not
"""

def check_num(lst, num):
    for i in lst:
        if i == num:
            return True
    return False

lst = [5,2,3,9,10]
flag1 = check_num(lst,9)
flag2 = check_num(lst,4)

print(flag1, flag2)