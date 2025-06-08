"""
take an int and return a list of its divisors

if an integer is one, we iterate through num in range 0 - n+1 
if num % given_int == 0

"""

def find_divisors(n):

    divisors = []
    for num in range(1, n+1):
        
        if n % num == 0:
            divisors.append(num)
    return divisors

lst = find_divisors(6)
print(lst)


