"""
Write a function is_perfect_number() that takes in a positive integer n and returns True if it is a perfect number and 
False otherwise. A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.

For example, 6 is a perfect number because its divisors or 1, 2, and 3 and 1 + 2 + 3 = 6.
"""
def is_perfect_number(n):
    divisors = [1]
    for i in range(2, n):
        if n%i==0:
            divisors.append(i)
    
    return sum(divisors)==n


print(is_perfect_number(6))
print(is_perfect_number(28))
print(is_perfect_number(9))