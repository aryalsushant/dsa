"""
A recursive function is a function that calls itself within the body of the function.

Step 1: Copy this code into Replit and run it.

Step 2: Then create another function countdown_iterative() that produces the same output without using recursion.

Compare your iterative (non-recursive) solution to the recursive solution provided. What is similar? What is different?
"""
def countdown(n):
	if n > 0:
		print(n)
		countdown(n - 1)
		
countdown(5)

def non_recursive(n):
	while n > 0:
		print(n)
		n-=1

non_recursive(5)