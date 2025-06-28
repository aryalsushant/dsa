"""
Write a function find_highest_exponent() that takes in an integer base and an integer limit as parameters. 
The function returns the highest exponent for which a given base raised to that exponent is less than or equal to limit.
"""
def find_highest_exponent(base, limit):
    max = 1
    for i in range(1,limit):
        if base ** i <= limit:
            max =i
            i+=1
    return max

            


#test case
exp = find_highest_exponent(2, 100)
print(exp)

exp2 = find_highest_exponent(3, 5)
print(exp2)