"""
Given a non-negative integer n, write a function sum_digits() that calculates and returns the sum of its digits 
recursively.

Evaluate the time and space complexity of your solution.
"""
'''
def sum_digits(n):
	digits = str(n)
	if digits == "0" or digits =="":
		return 0
	else:
		return int(digits[0]) + int(sum_digits(digits[1:]))
'''


#ok so this function works but is inconsistent bc I'm passing strings instead of integers
#more mathematical solution according to chatgpt:

def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_digits(n//10)
	
print(sum_digits(523))