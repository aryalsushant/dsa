"""
Given the base case and recursive case, write a recursive function string_length() that returns the 
length of a string s without using the built-in len() function.

Base Case: An empty string should have size 0.

Recursive Case: We can restate the problem to say that the string length is 1 + the length of s[1:].
"""
def string_length(s):
	if s == "":
		return 0
	else:
		return 1 + string_length(s[1:])

print(string_length("abcs"))
		
	