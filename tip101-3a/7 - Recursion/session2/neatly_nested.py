"""
Given a string, return True if it is a nesting of zero or more pairs of parentheses. 
Return False otherwise. A valid pair of parentheses is defined as (). The input string will only
 contain the characters ( or ). Your solution must be recursive.

Evaluate the time and space complexity of your solution.
"""
def is_nested(paren_s):
	if paren_s == "":
		return True
	if paren_s[0] == "(" and paren_s[-1]==")":
		return is_nested(paren_s[1:-1])
	return False

print(is_nested("(((())))"))