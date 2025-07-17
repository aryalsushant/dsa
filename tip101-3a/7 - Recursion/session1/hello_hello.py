"""
A recursive function is a function that calls itself within the body of the function.

Step 1: Copy the recursive function repeat_hello() into Replit and run it.

Step 2: Then create another function repeat_hello_iterative() that produces the same output without using recursion.

Compare your iterative (non-recursive) solution to the recursive solution provided. What is similar? What is different?
"""
def repeat_hello(n):
	if n > 0:
		print("Hello")
		repeat_hello(n - 1)
		
repeat_hello(5)

def repeat_hello_again(n):
	while n>0:
		print("Hello")
		n-=1

repeat_hello_again(5)