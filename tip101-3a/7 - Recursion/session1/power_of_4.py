"""
Given an integer n, return True if n is a power of four. Otherwise, return False.

An integer n is a power of four if there exists an integer x such that n == 4ˣ.

Solve the problem recursively. What is the time complexity of this function? What is the space complexity?
"""
def is_power_of_four(n):
	if n==1:
		return True
	if n%4 != 0 or n==0:
		return False
	else:
		return is_power_of_four(n/4)
	
print(is_power_of_four(64))