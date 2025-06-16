"""
given a number, return its factorial
"""

def calculate_factorial(num):

    factorial =1
    for i in range(1, num+1):
        factorial = factorial*i
    return factorial

print(calculate_factorial(3))

