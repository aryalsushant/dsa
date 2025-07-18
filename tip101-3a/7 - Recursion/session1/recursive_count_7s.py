"""
Given a non-negative integer n, write a recursive function count_sevens() that returns the count of the
 occurrences of 7 as a digit.

Evaluate the time and space complexity of your solution.
"""
def count_sevens(n):
	if n==0:
		return 0
	if n%10 ==7:
		return 1+ count_sevens(n//10)
	else:
		return count_sevens(n//10)
	
print(count_sevens(727))
