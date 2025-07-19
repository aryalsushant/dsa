"""
Given the base case and recursive case, write a function fibonacci() that returns the nth number in the
 fibonacci sequence. The Fibonacci sequence is a mathematical sequence of numbers where each number is the 
 sum of the two preceding numbers.

Base Cases: Because Fibonacci numbers are defined by adding the two previous numbers in the sequence, the
 first two Fibonacci numbers are pre-defined. By definition, the 0th Fibonacci number is 0, and the 1st
   Fibonacci number is 1.

Recursive Case: The nth Fibonacci number is the n-1th Fibonacci number + the n-2th Fibonacci number.
"""
def fibonacci(n):
	if n == 0 or n==1:
		return n
	return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(6))