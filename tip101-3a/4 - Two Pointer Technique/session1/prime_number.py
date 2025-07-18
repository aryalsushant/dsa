"""
Write a function is_prime() that takes in a positive integer n and returns True if it is a prime number
and False otherwise. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
prime number can't be obtained by multiplying any other numbers than 1 and itself

1. for i in range(2,n)
2.    if n%i ==0
            return false
    
"""
def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

#test case
print(is_prime(5))
print(is_prime(12))
print(is_prime(2))