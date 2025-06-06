"""
a function fizzbuzz() that takes an integer n as parameter, prints number from 1 to n 
for multiples of 3, prints fizz instead
for multiples of 5, prints buzz instead
"""

def fizzbuzz(n):
    for num in range(1,n):
        if num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)

fizzbuzz(13)